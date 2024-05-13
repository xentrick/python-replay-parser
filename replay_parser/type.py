import os
from typing import TypeAlias, TypeVar

PathLike = TypeVar("PathLike", str, bytes, os.PathLike)


# Generic

Bool_1: TypeAlias = bool
Bool_8: TypeAlias = bool
UInt_8: TypeAlias = int
UInt_32: TypeAlias = int
UInt_64: TypeAlias = int

Bit_1: TypeAlias = int

Vector3f: TypeAlias = list
