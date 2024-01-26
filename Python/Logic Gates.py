import time
print("Enter a Gate: ")
print("1.AND       2.OR\n3.NOT       4.NAND\n5.NOR       6.Ex-OR\n7.Ex-NOR")
time.sleep(1)
choice=int(input("Enter Your Gate : "))
if(choice==1):  #And gate
    print("Which type of Information: ")
    time.sleep(1)
    print("a)IC Number\nb)Truth Table\nc)Structure of IC Input and Output pins")
    chance=input("Enter chance: ")
    choice1="a"
    choice2="b"
    choice3="c"
    if(chance in choice1):
        print("IC Number:")
        time.sleep(1)
        print("  7408  ")
    elif(chance in choice2):
        print("| A | B | A AND B |\n|---|---|---------|\n| 0 | 0 |    0    |\n| 0 | 1 |    0    |\n| 1 | 0 |    0    |\n| 1 | 1 |    1    |")
    elif(chance in choice3):
        print("           +---+--+---+\n     1A --|1  +--+ 14|-- Vcc\n     1B --|2       13|-- 4B\n     1Y --|3       12|-- 4A\n     2A --|4  7408 11|-- 4Y\n     2B --|5       10|-- 3B\n     2Y --|6        9|-- 3A\n    GRD --|7        8|-- 3Y\n           +----------+")
    else:
        print("Invalid choice")
elif(choice==2):   #Or gate
    print("Which type of Information: ")
    time.sleep(1)
    print("1)IC Number\n2)Truth Table\n3)Structure of IC Input and Output pins")
    chance = int(input("Enter chance: "))
    if (chance==1):
        print("IC Number:")
        time.sleep(1)
        print("  7432  ")
    elif (chance==2):
        print("|  i/p  |   o/p   |\n| A | B | A  +  B |\n|---|---|---------|\n| 0 | 0 |    0    |\n| 0 | 1 |    1    |\n| 1 | 0 |    1    |\n| 1 | 1 |    1    |")
    elif (chance==3):
        print("           +---+--+---+\n     1A <--|1  +--+ 14|--> Vcc\n     1B <--|2       13|--> 4B\n     1Y <--|3       12|--> 4A\n     2A <--|4  7432 11|--> 4Y\n     2B <--|5       10|--> 3B\n     2Y <--|6        9|--> 3A\n    GRD <--|7        8|--> 3Y\n          +-----------+")
    else:
        print("Invalid choice")
elif(choice==3):   #not gate
    print("Which type of Information: ")
    time.sleep(1)
    print("a)IC Number\nb)Truth Table\nc)Structure of IC Input and Output pins")
    chance = input("Enter chance: ")
    choice1 = "a"
    choice2 = "b"
    choice3 = "c"
    if(chance in choice1):
        print("  7404  ")
    elif(chance in choice2):
        print("| Input | Output |\n|-------|--------|\n|   0   |    1   |\n|   1   |    0   |")
    elif(chance in choice3):
        print("           +---+--+---+\n     1A <--|1  +--+ 14|--> Vcc\n     1Y <--|2       13|--> 6A\n     2A <--|3       12|--> 6Y\n     2Y <--|4  7404 11|--> 5A\n     3A <--|5       10|--> 5Y\n     3Y <--|6        9|--> 4A\n    GRD <--|7        8|--> 4Y\n          +-----------+")
    else:
        print("Invalid Choice")
elif(choice == 4):   #Nand gate
    print("Which type of Information: ")
    time.sleep(1)
    print("1)IC Number\n2)Truth Table\n3)Structure of IC Input and Output pins")
    chance = input("Enter chance: ")
    if(chance == 1):
        print("  7400  ")
    elif(chance == 2):
        print("| Input A | Input B | Output |\n|---------|---------|--------|\n|    0    |    0    |    1   |\n|    0    |    1    |    1   |\n|    1    |    0    |    1   |\n|    1    |    1    |    0   |")
    elif(chance == 3):
        print("           +---+--+---+\n     1A --|1  +--+ 14|-- Vcc\n     1B --|2       13|-- 4B\n     1Y --|3       12|-- 4A\n     2A --|4  7400 11|-- 4Y\n     2B --|5       10|-- 3B\n     2Y --|6        9|-- 3A\n    GRD --|7        8|-- 3Y\n           +----------+")
    else:
        print("Inavalid Choice")
elif(choice == 5):    #Nor
    print("Which type of Information: ")
    time.sleep(1)
    print("1)IC Number\n2)Truth Table\n3)Structure of IC Input and Output pins")
    chance = int(input("Enter chance: "))
    if (chance == 1):
        print("  7402  ")
    elif (chance == 2):
        print("| Input A | Input B | Output |\n|---------|---------|--------|\n|    0    |    0    |    1   |\n|    0    |    1    |    0   |\n|    1    |    0    |    0   |\n|    1    |    1    |    0   |")
    elif (chance == 3):
        print("           +---+--+---+\n     1y --|1  +--+ 14|-- Vcc\n     1A --|2       13|-- 4Y\n     1B --|3       12|-- 4A\n     2Y --|4  7402 11|-- 4B\n     2A --|5       10|-- 3Y\n     2B --|6        9|-- 3A\n    GRD --|7        8|-- 3B\n           +----------+")
    else:
        print("Invalid chance")
elif(choice==6):   #Xor gate
    print("Which type of Information: ")
    time.sleep(1)
    print("1)IC Number\n2)Truth Table\n3)Structure of IC Input and Output pins")
    chance = int(input("Enter chance: "))
    if (chance==1):
        print("IC Number:")
        time.sleep(1)
        print("  7486  ")
    elif (chance==2):
        print("|  i/p  |   o/p   |\n| A | B | A  +  B |\n|---|---|---------|\n| 0 | 0 |    0    |\n| 0 | 1 |    1    |\n| 1 | 0 |    1    |\n| 1 | 1 |    0    |")
    elif (chance==3):
        print("           +---+--+---+\n     1A <--|1  +--+ 14|--> Vcc\n     1B <--|2       13|--> 4B\n     1Y <--|3       12|--> 4A\n     2A <--|4  7486 11|--> 4Y\n     2B <--|5       10|--> 3B\n     2Y <--|6        9|--> 3A\n    GRD <--|7        8|--> 3Y\n          +-----------+")
    else:
        print("Invalid choice")
elif(choice==7):   #X=Nor gate
    print("Which type of Information: ")
    time.sleep(1)
    print("1)IC Number\n2)Truth Table\n3)Structure of IC Input and Output pins")
    chance = int(input("Enter chance: "))
    if (chance==1):
        print("IC Number:")
        time.sleep(1)
        print("  74266  ")
    elif (chance==2):
        print("|  i/p  |   o/p   |\n| A | B | A  +  B |\n|---|---|---------|\n| 0 | 0 |    1    |\n| 0 | 1 |    0    |\n| 1 | 0 |    0    |\n| 1 | 1 |    1    |")
    elif (chance==3):
        print("           +---+--+---+\n     1A <--|1  +---+ 14|--> Vcc\n     1B <--|2        13|--> 4B\n     1Y <--|3        12|--> 4A\n     2A <--|4  74266  11|--> 4Y\n     2B <--|5        10|--> 3B\n     2Y <--|6         9|--> 3A\n    GRD <--|7        8|--> 3Y\n          +-----------+")
    else:
        print("Invalid choice")
else:
    print("Invalid Choice")