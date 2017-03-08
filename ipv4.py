# 08.03.2017
# CodeWars Kata IPv4 to int32
# passed all tests


def ip_to_int32(ip):
    # your code here
    ip = ip.split('.')
    binary = []
    for number in ip:
        binary += int_to_binary(int(number))
    return binary_to_int(binary)


def int_to_binary(number):
    binary = []
    i = 7
    while i >= 0:
        if number >= 2**i:
            binary.append(1)
            number -= 2**i
        else:
            binary.append(0)
        i -= 1
    return binary


def binary_to_int(binary):
    result = 0
    expo = 31
    for bit in binary:
        if bit:
            result += 2**expo
        expo -= 1
    return result


print(ip_to_int32('128.114.17.104'))
