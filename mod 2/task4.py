a = int(input())

def convert_to(number, base):
    result = ''
    while number > 0:
        result = str(number % base) + result
        number //= base
    return result


print(convert_to(100,2),convert_to(100,8),convert_to(100,16))


