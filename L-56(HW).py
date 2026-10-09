def binary_to_decimal_loop(binary_string):
    """
    Converts a binary string to a decimal integer using manual math logic.
    Multiplies each bit by its corresponding power of 2 from right to left.
    """
    decimal_value = 0
    # Reverse string to easily match positions with indices as powers of 2
    reversed_binary = binary_string[::-1]

    for index, bit in enumerate(reversed_binary):
        if bit == "1":
            decimal_value += 2**index
        elif bit != "0":
            raise ValueError("Invalid binary digit detected. Only 0 and 1 are allowed.")

    return decimal_value


def binary_to_decimal_builtin(binary_string):
    """
    Converts a binary string to a decimal integer using Python's built-in int function.
    """
    return int(binary_string, 2)


# --- Sample Test Execution ---
if __name__ == "__main__":
    sample_binary = "101010"  # (1*32) + (0*16) + (1*8) + (0*4) + (1*2) + (0*1) = 42

    print("Execution Results:")
    print("-" * 30)
    print(f"Binary Input: {sample_binary}")
    print(
        f"Manual Loop Method Result:    {binary_to_decimal_loop(sample_binary)}"
    )
    print(
        f"Built-in Function Result:     {binary_to_decimal_builtin(sample_binary)}"
    )
