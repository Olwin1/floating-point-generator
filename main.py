import random
mantissa_bits = 7
exponent_bits = 4
selection = input("Please Enter What Format You Would Like Your Numbers To Be In:\n1: 7-bit Mant, 4-bit Exp\n2: 5-bit Mant (Default), 3-bit Exp\n3: 11-bit Mant, 5-bit Exp (Half)\n4: 24-bit Mant, 8-bit Exp (Single), \n5: 53-bit Mant, 11-bit Exp (Double)\n :")
match selection:
    case "2":
        mantissa_bits = 5
        exponent_bits = 3
    case "3":
        mantissa_bits = 11
        exponent_bits = 5
    case "4":
        mantissa_bits = 24
        exponent_bits = 8
    case "5":
        mantissa_bits = 53
        exponent_bits = 11
    case _:
        pass
def twos_complement(value, bits):
    """Compute the two's complement of int value."""
    if value & (1 << (bits - 1)):
        value -= 1 << bits
    return value

def generateValue(mantissa_bits, exponent_bits):
    '''Generate a random floating point number'''
    # Generate a random x-bit two's complement number for the mantissa
    mantissa = random.randint(0, (1 << mantissa_bits) - 1)
    mantissa_twos_complement = twos_complement(mantissa, mantissa_bits)

    # Generate a random y-bit two's complement number for the exponent
    exponent = random.randint(0, (1 << exponent_bits) - 1)
    exponent_twos_complement = twos_complement(exponent, exponent_bits)

    # Calculate the floating point value
    floating_point_value = mantissa_twos_complement * (2 ** exponent_twos_complement)

    # Convert to binary string with leading zeros for proper formatting
    mantissa_binary = format(mantissa, f'{mantissa_bits:02}b')
    exponent_binary = format(exponent, f'{exponent_bits:02}b')
    return mantissa_binary, exponent_binary, mantissa_twos_complement, exponent_twos_complement, floating_point_value

# Main Loop
while True:
    mantissa_binary, exponent_binary, mantissa_twos_complement, exponent_twos_complement, floating_point_value = generateValue(mantissa_bits, exponent_bits)
    # Output the values
    print(f"Two's Compliment Binary ({mantissa_bits}-bit Mantissa, {exponent_bits}-bit Exponent): {mantissa_binary} {exponent_binary}")
    print(f"Base-10 Value: {floating_point_value * 10**exponent_twos_complement}")
    input("Press Any Key for Another Value")