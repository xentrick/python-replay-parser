import logging
import re
import struct

log = logging.getLogger(__name__)

SERVER_REGEX = re.compile(r"((EU|USE|USW|OCE|SAM)\d+(-[A-Z][a-z]+)?)")

##################
# Header functions
##################

##################
# Footer functions
##################


def read_property_tree(replay_file, objects, classes):
    branches = []

    property_tree_length = read_integer(replay_file)

    for _ in range(property_tree_length):
        data = {
            "class": read_integer(replay_file),
            "parent_id": read_integer(replay_file),
            "id": read_integer(replay_file),
            "properties": {},
        }

        if data["id"] == data["parent_id"]:
            data["id"] = 0

        length = read_integer(replay_file)

        for _ in range(length):
            index = read_integer(replay_file)
            value = read_integer(replay_file)

            data["properties"][index] = value

        branches.append(data)

    # Map the property keys against the class list.
    classed = {}

    def map_properties(id):
        for branch in branches:
            if branch["id"] == id:
                props = {}

                if branch["parent_id"] > 0:
                    props = map_properties(branch["parent_id"])

                for k, v in enumerate(branch["properties"]):
                    props[v] = objects[k]

                return props

        return {}

    for branch in branches:
        # {'parent_id': 36, 'properties': {42: 36}, 'class': 43, 'id': 37}
        classed[branch["class"]] = {
            "class": classes[branch["class"]],
            "properties": map_properties(
                branch["id"] if branch["id"] > 0 else branch["parent_id"]
            ),
        }

    return branches


# Temporary method while we learn the replay format.
def manual_parse(self, results, replay_file, filename):
    replay_file.seek(0)

    search = SERVER_REGEX.search(replay_file.read().decode("utf-8", "ignore"))
    if search:
        results["header"]["ServerName"] = search.group()

    return results


##################
# Helper functions
##################


def debug_bits(replay_file, labels=None):
    byte = replay_file.read(1)
    output = ()

    for index in range(8):
        i, j = divmod(index, 8)

        if ord(byte[i]) & (1 << j):
            value = "1"
        else:
            value = "0"

        formatted = value.rjust(index + 1, ".").ljust(8, ".")
        output = output + (int(value),)

        if labels and len(labels) == 8:
            print(
                "{} = {}: {}".format(
                    formatted,
                    labels[index],
                    "Set" if formatted == "1" else "Not set",
                )
            )
        else:
            print(value.rjust(index + 1, ".").ljust(8, "."))

    return output


def read_bit(string, index):
    i, j = divmod(index, 8)

    if ord(string[i]) & (1 << j):
        return 1
    else:
        return 0


def pretty_byte_string(bytes_read):
    return " ".join("{:02x}".format(ord(x)) for x in bytes_read)


def pretty_bytes(bytes_read):
    return " ".join([f"{x:02x}" for x in bytes_read])


def read_integer(replay_file, length=4):
    number_format = {
        1: "<b",
        2: "<h",
        4: "<i",
        8: "<q",
    }[length]

    bytes_read = replay_file.read(length)
    value = struct.unpack(number_format, bytes_read)[0]

    return value


def read_float(replay_file, length):
    number_format = {4: "<f", 8: "<d"}[length]

    bytes_read = replay_file.read(length)
    value = struct.unpack(number_format, bytes_read)[0]

    return value


def read_unknown(replay_file, num_bytes):
    bytes_read = replay_file.read(num_bytes)
    return bytes_read


def read_string(replay_file, length=None) -> str:
    if not length:
        length = read_integer(replay_file)
    bytes_read = replay_file.read(length)[0:-1]
    return bytes_read


def read_string8(replay_file) -> str:
    len = read_integer(replay_file, 4)
    raw = replay_file.read(len)[:-1]
    return raw.decode("utf-8")


def read_string16(replay_file) -> str:
    len = read_integer(replay_file, 4)
    if len == 0:
        return ""
    elif len > 0:
        raw = replay_file.read(len)[:-1]
        return raw.decode("cp1252")
    else:
        raw = replay_file.read(len * -2)[:-2]
        return raw.decode("utf-16le")


def sniff_bytes(replay_file, size):
    b = read_unknown(replay_file, size)

    print("**** BYTES ****")
    print("Bytes: {}".format(pretty_bytes(b)))
    print("Size:", size)

    if size == 2:
        print(
            "Short: Signed: {} Unsigned: {}".format(
                struct.unpack("<h", b), struct.unpack("<H", b)
            )
        )
    else:
        if size == 4:
            print(
                "Integer: Signed: {}, Unsigned: {}".format(
                    struct.unpack("<i", b), struct.unpack("<I", b)
                )
            )
            print("Float: {}".format(struct.unpack("<f", b)))
        print(f"String: {b}")
