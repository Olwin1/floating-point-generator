import random

# Default settings for mantissa and exponent bit lengths
mantissa_bits = 7
exponent_bits = 4

# Prompt the user to select a format for the floating-point number
selection = input("Please Enter What Format You Would Like Your Numbers To Be In:\n"
                  "1: 7-bit Mant, 4-bit Exp (Default)\n"
                  "2: 5-bit Mant, 3-bit Exp\n"
                  "3: 11-bit Mant, 5-bit Exp (Half) (Just for Fun, You'll never be asked to give this much precision)\n"
                  "4: 24-bit Mant, 8-bit Exp (Single) (... Why) \n"
                  " :")

# Match the user's selection to set the appropriate mantissa and exponent bit lengths
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
    case _:
        pass  # If no valid selection is made, default to 7-bit mantissa and 4-bit exponent

def twos_complement(value, bits):
    """Compute the two's complement of int value."""
    if value & (1 << (bits - 1)):  # If the sign bit is set
        value -= 1 << bits  # Subtract the value to get the two's complement
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
    # Generate a random floating point value based on the current mantissa and exponent bit lengths
    mantissa_binary, exponent_binary, mantissa_twos_complement, exponent_twos_complement, floating_point_value = generateValue(mantissa_bits, exponent_bits)
    
    # Output the values
    print(f"Two's Compliment Binary ({mantissa_bits}-bit Mantissa, {exponent_bits}-bit Exponent): {mantissa_binary} {exponent_binary}")
    print(f"Base-10 Value: {floating_point_value * 10**exponent_twos_complement}")
    
    # Wait for user input to generate another value
    input("Press Any Key for Another Value")
