import random

print(random.randint(2,6))      #2,3,4,5,6  2<=x<=6
print(random.randrange(2,6))    #2,3,4,5    2<=x<6
print((random.randrange(3)))    #0,1,2      0>=x>3
print(random.random())          #0.1 -- 0.9 0.1<=x<1.0
print(random.uniform(1,3))
l = ["Dileep",0,1,2,3,"Sandeep"]
print(random.choice(l))         #"Dileep",0,1,2,3,"Sandeep"
print(random.choices(l))        #["Dileep"],[0],[1],[2],[3],["Sandeep"]
random.shuffle(l)
print(l)                        #[0, 'Dileep', 2, 1, 3, 'Sandeep']