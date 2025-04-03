from typing import Tuple, List

def number_to_hexa(digits: List[int]) -> List[str]: 
    hexa_dict= {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    
    for i in range(0, len(digits)):
        if digits[i] in hexa_dict.keys():
            digits[i] = hexa_dict.get(digits[i])
            
    return [i for i in digits]

def hexa_to_number(digits: str) -> List[int]:
    digits = list(digits)
    hexa_dict = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

    for i in range(0, len(digits)):
        if digits[i] in hexa_dict.keys():
            digits[i] = hexa_dict.get(digits[i])
            
    return digits

def get_correct_length(digits: str) -> Tuple[int, List[int]]:
    splitted_digits = digits.replace(",", ".").split(".") # tentamos separar os dígitos em duas listas, uma para a parte inteira e outra para fracionária
    
    if len(splitted_digits) == 2: # isso quer dizer que nossos dígitos possuem parte fracionária
        length = len(splitted_digits[0]) # pega o tamanho da parte inteira, para saber quantos números terão potência positiva
        digits = splitted_digits[0] + splitted_digits[1] 
        digits = hexa_to_number(digits)
        return length, [int(i) for i in digits] # passamos quantos dígitos são da parte inteira e convertemos todos os dígitos para int
        
    if len(splitted_digits) == 1: # isso quer dizer que nossos dígitos não possuem parte fracionária
        digits = hexa_to_number(digits)
        return len(splitted_digits[0]), [int(i) for i in digits]
    
    raise ValueError("Invalid binary number") # foi indicado mais de um ponto/vírgula, resultando em três ou mais listas


def another_to_decimal(digits: str, original_base: int) -> str:
    length, digits = get_correct_length(digits) # converte os dígitos para valores inteiros e calcula o tamanho da parte inteira do valor
    
    power = original_base**(length - 1) # define o valor da primeira potência
    number = float(0)
    
    # vai multiplicando o digito pela base elevada a posição -> 101.1 -> 1x2² + 0x2¹ + 0x2⁰ + 1x2⁻¹ = 5.5
    for digit in digits:
        number += digit * power
        power /= original_base

    if number - int(number) == 0: # verifica se o número é inteiro, evitando de passar valores fracionários
        return f"{number:.0f}"
        
    return f"{number:.{len(str(number - int(number))) - 2}f}" # especifica a quantidade das casas decimais para passar corretamente
    

def decimal_to_another(decimal: int, new_base: int) -> str:
    integer, fractional = int(decimal), decimal - int(decimal) # separa a parte inteira da parte fracionária
    
    integer_half = list()
    
    while 1:
        # divisão pela base até que o quociente seja zero, armazenando o restante das divisões
        quotient = integer // new_base
        remainder = integer % new_base
        integer = quotient

        integer_half.insert(0, remainder) # adiciona os números pela esquerda
        
        if quotient == 0:
            break

    fractional_half = list()
    
    while 1:
        # multiplicação pela base até que tenhamos um valor inteiro, armazenando os inteiros e passandos os fracionários (1.5 -> armazena o 1 e passa o 0.5)
        quotient = fractional * new_base
        fractional = quotient - int(quotient)
        
        fractional_half.append(int(quotient)) # adiciona os números pela direita
        
        if fractional == int(fractional):
            break
    
    
    if len(fractional_half) == 1 and fractional_half[0] == 0:     
        if new_base == 16:                    
            integer_half = number_to_hexa(integer_half) 
            
        return "".join([str(i) for i in integer_half])
                    
    if new_base == 16: 
        integer_half = number_to_hexa(integer_half)
        fractional_half = number_to_hexa(fractional_half)
        
    return "".join([str(i) for i in integer_half]) + "." + "".join([str(i) for i in fractional_half])
    
print(another_to_decimal("5A1D,F1", 16))