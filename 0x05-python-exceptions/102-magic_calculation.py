#!/usr/bin/python3


def special_calculation(base, exponent):
    result = 0
    for i in range(1, 3):
        try:
            if i > base:
                raise Exception('Too far')
            else:
                result += base ** exponent / i
        except:
            result = base + exponent
            break
    return (result)
