def generate_pattern(size):
    for i in range(size, 0, -1):
        line = ""
        for j in range(size, 0, -1):
            if j >= i:
                line += chr(ord('j') - (size - j))
            else:
                line += '-'
            if j > 1:
                line += '-'
        print(line.center(size * 4 - 3))

size = 11  # You can change this to adjust the size of the pattern
generate_pattern(size)
