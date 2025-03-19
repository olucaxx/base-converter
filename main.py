def decimal_to_another(number, new_base):
    # decimal para outra base -> divisões sucessivas pela base que desejamos
    new_number = str()
    
    while 1:

        quotient = number // new_base
        remainder = number % new_base
        number = quotient

        new_number = str(remainder) + new_number
        
        if quotient < new_base:
            new_number = str(quotient) + new_number
            break

    return new_number
        

def another_to_decimal(original_base, number):
    # outra base para decimal -> multiplicação do valor pela base elevada a posição
    number = str(number)
    decimal_num = 0

    for i, number in enumerate(reversed(number)):
        decimal_num += int(number) * original_base ** i

    return decimal_num


def slice_binary(binary_digits, base):
    # binário para outra base (além da decimal) -> 2ⁿ = base, onde n será a quantidade de bits de cada grupo
    group_by = 0
    while base != 1:
        base /= 2
        group_by += 1
    
    binary_digits = [int(x) for x in binary_digits]
    if len(binary_digits) % group_by != 0:
        for _ in range(group_by - (len(binary_digits) % group_by)):
            binary_digits.insert(0, 0)
    
    grouped_bits = list()
    for i in range(0, len(binary_digits), group_by):
        grouped_bits.append(binary_digits[i:(i+group_by)])

    return grouped_bits


def binary_to_another(binary_digits, base):
    
    binary_digits = [binary_digits[i] for i in range(len(binary_digits) - 1, 0 , -1)]
    


print(binary_to_another("111111110", 8))

"""
binary -> quat
binary -> octa
binary -> decimal
binary -> hexa

quat -> binary
quat -> octa
quat -> decimal
quat -> hexa

octa -> binary
octa -> quat
octa -> decimal
octa -> hexa

decimal -> binary
decimal -> quat
decimal -> octa
decimal -> hexa

hexa -> binary
hexa -> quat
hexa -> octa
hexa -> decimal
"""