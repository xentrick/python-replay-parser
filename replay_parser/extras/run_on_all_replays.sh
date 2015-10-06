find temp/* | xargs -I{} sh -c 'printf "%-50s" "{}"; echo; python rl_replay_parser.py {}'
