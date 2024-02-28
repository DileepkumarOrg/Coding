if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        l = []
        command = input().split()

        if command[0] == 'insert':
            i = int(command[1])
            e = int(command[2])
            l.insert(i, e)
            print(l)
        elif command[0] == 'remove':
            l.remove(int(command[1]))
            print(l)
        elif command[0] == 'append':
            l.append(int(command[1]))
            print(l)
        elif command[0] == 'sort':
            l.sort()
            print(l)
        elif command[0] == 'pop':
            l.pop()
            print(l)
        elif command[0] == 'reverse':
            l.reverse()
            print(l)
        elif command[0] == 'print':
            print(l)
        else:
            print('invalid command')


