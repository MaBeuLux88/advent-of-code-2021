def read_hex_from_file():
    f = open('inputs/input1.txt', 'r')
    return f.readline().strip()


def hex_to_binary(hexa):
    nb_bits = len(hexa) * 4
    return bin(int(hexa, 16))[2:].zfill(nb_bits)


def read_payload(payload):
    # print(payload)
    typ = payload.get('t')
    literal = payload.get('is_literal')
    p = payload.get('p')
    if literal:
        return p
    if typ == 0:
        res = 0
        for i in p:
            res += read_payload(i)
        return res
    if typ == 1:
        res = 1
        for i in p:
            res *= read_payload(i)
        return res
    if typ == 2:
        res = []
        for i in p:
            res.append(read_payload(i))
        return min(res)
    if typ == 3:
        res = []
        for i in p:
            res.append(read_payload(i))
        return max(res)
    if typ == 5:
        res = []
        for i in p:
            res.append(read_payload(i))
        return 1 if res[0] > res[1] else 0
    if typ == 6:
        res = []
        for i in p:
            res.append(read_payload(i))
        return 1 if res[0] < res[1] else 0
    if typ == 7:
        res = []
        for i in p:
            res.append(read_payload(i))
        return 1 if res[0] == res[1] else 0
    else:
        print('TYPE NOT SUPPORTED')


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
    bs = [[hex_to_binary(read_hex_from_file()), 1673210814091],
          ['110100101111111000101000', 2021],
          ['00111000000000000110111101000101001010010001001000000000', 1],
          ['11101110000000001101010000001100100000100011000001100000', 3],
          [hex_to_binary('C200B40A82'), 3],
          [hex_to_binary('04005AC33890'), 54],
          [hex_to_binary('880086C3E88112'), 7],
          [hex_to_binary('CE00C43D881120'), 9],
          [hex_to_binary('D8005AC2A8F0'), 1],
          [hex_to_binary('F600BC2D8F'), 0],
          [hex_to_binary('9C005AC2F8F0'), 0],
          [hex_to_binary('9C0141080250320F1802104A08'), 1]]
    for b, expected_value in bs:
        payload, b = read_bloc(b)
        value = read_payload(payload)
        print(value == expected_value, 'Found', value, 'Expected', expected_value)


if __name__ == '__main__':
    main()
