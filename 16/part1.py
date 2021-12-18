def read_hex_from_file():
    f = open('inputs/input1.txt', 'r')
    return f.readline().strip()


def hex_to_binary(hexa):
    nb_bits = len(hexa) * 4
    return bin(int(hexa, 16))[2:].zfill(nb_bits)


def read_payload(payload):
    versions = []
    for k, v in payload.items():
        if k == 'v':
            versions.append(v)
        elif k == 'p':
            if type(v) == list:
                for i in v:
                    versions += read_payload(i)
    return versions


def read_version(b):
    return int(b[:3], 2), b[3:]


def read_type(b):
    return int(b[:3], 2), b[3:]


def get_next_5_bits(b):
    return b[:1], b[1:5], b[5:]


def read_bloc(b):
    version, b = read_version(b)
    typ, b = read_type(b)
    literal = typ == 4
    if literal:
        payload, b = read_literal(b)
    else:
        payload, b = read_operator(b)
    # print('\nVersion', version, '\nType', typ, '\nLiteral', literal, '\nPayload', payload)
    return {'v': version, 't': typ, 'is_literal': literal, 'p': payload}, b


def read_literal(b):
    v = ''
    start, value, b = get_next_5_bits(b)
    v += value
    while start == '1':
        start, value, b = get_next_5_bits(b)
        v += value
    return int(v, 2), b


def read_operator(b):
    i = b[:1]
    b = b[1:]

    read_length = 15 if i == '0' else 11
    length = int(b[:read_length], 2)
    b = b[read_length:]
    payloads = []
    if i == '0':
        size_bin_init = len(b)
        size_bin = len(b)
        while size_bin_init != size_bin + length:
            payload, b = read_bloc(b)
            payloads.append(payload)
            size_bin = len(b)
    else:
        while length > 0:
            payload, b = read_bloc(b)
            payloads.append(payload)
            length -= 1
    return payloads, b


def main():
    bs = ['110100101111111000101000',
          '00111000000000000110111101000101001010010001001000000000',
          '11101110000000001101010000001100100000100011000001100000',
          hex_to_binary(read_hex_from_file())]
    for b in bs:
        payload, b = read_bloc(b)
        # print(payload)
        versions = read_payload(payload)
        print('Versions', sum(versions))


if __name__ == '__main__':
    main()
