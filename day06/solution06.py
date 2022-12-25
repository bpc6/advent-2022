def has_repeat(s: str) -> bool:
    return len(set(s)) != len(s)


def find_index(s: str, buffer_len: int) -> int:
    buffer = ''
    for idx, c in enumerate(s):
        if len(buffer) < buffer_len:
            buffer += c
        elif has_repeat(buffer):
            buffer = buffer[1:] + c
        else:
            return idx
    return 0


if __name__ == '__main__':
    filename = 'input.txt'
    with open(filename, 'r') as f:
        input_str = f.read().strip()

    print(find_index(input_str, 4))
    print(find_index(input_str, 14))


