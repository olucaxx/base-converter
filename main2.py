from typing import Tuple, List

def get_correct_length(binary_digits: str) -> Tuple[int, List[int]]:
    splitted_digits = binary_digits.replace(",", ".").split(".")
    
    if len(splitted_digits) == 2:
        length = len(splitted_digits[0])
        binary_digits = splitted_digits[0] + splitted_digits[1]
        return length, [int(i) for i in binary_digits]
        
    if len(splitted_digits) == 1:
        return len(splitted_digits[0]), [int(i) for i in binary_digits]
    
    raise ValueError("Invalid binary number")
    
    
def another_to_decimal(binary_digits: str, base: int) -> float:
    length, binary_digits = get_correct_length(binary_digits)
    
    power = base**(length - 1)
    number = 0
    for digit in binary_digits:
        number += digit * power
        power /= base
    
    return number
    
    
def decimal_to_another(decimal, new_base):
    number = str()
    
    while 1:

        quotient = decimal // new_base
        remainder = decimal % new_base
        decimal = quotient

        number = str(remainder) + number
        
        if quotient < new_base:
            number = str(quotient) + number
            break

    return number
    
    
def hexa_to_binary(hexa_num: str) -> float:
    hexa_dict = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    
    numbers = list(hexa_num)
    binary_digits = ""
    
    for number in numbers:
        binary_digits += (decimal_to_another(hexa_dict.get(number), 2))
        
    return binary_digits

    
def binary_to_quat(binary_digits):
    pass

# o tamanho da lista do número inteiro para se basear no len() delattr
# somar as duas listas em uma única lista

# adicionar limitador, por exmeplo, o decimal não passar de X casas

print(hexa_to_binary("3AF")) # 0011 1010 1111 