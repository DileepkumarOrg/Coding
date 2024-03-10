def generate_table():
    #print("{:<5} {:<5} {:<5} {:<5}".format("Decimal", "Binary", "Octal", "Hexadecimal"))
    length=len(bin(n+1))
    for i in range(1, 18):
        binary_str = bin(i)[2:]
        octal_str = oct(i)[2:]
        hex_str = hex(i)[2:]
        print("{:<5} {:<5} {:<5} {:<5}".format(i, octal_str, hex_str, binary_str))


# Call the function to generate and print the table
generate_table()
