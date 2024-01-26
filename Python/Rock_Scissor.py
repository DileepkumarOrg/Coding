def Rock_Paper_Scissor(num1,num2,bit1,bit2):




player_one={0:'Rock',1:'Scissor',2:'Paper'}
player_two={0:'Scissor',1:'Paper',2:'Rock'}
while(1):
    num1 = input("player 1 ,Enter your choice: ")
    num2 = input("player 2 ,Enter your choice: ")
    bit1 = int(input("Enter your seret bit posion: "))
    bit2 = int(input("Enter your seret bit posion: "))
    ch=input("Do you want to continue or not? y/n")
    if (ch=='n'):
        break