print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower() + name2.lower()

T = name.count('t')
R = name.count('r')
U = name.count('u')
E = name.count('e')
L = name.count('l')
O = name.count('o')
V = name.count('v')
E = name.count('e')
H = str(T+R+U+E)
E = str(L+O+V+E)
love_score = H + E
n = int(love_score)

if n <10 or n>90:
    print(f"Your sorce is {love_score}, you go together like coke and mentos.")
elif n >=40 and n<=50:         
    print(f"Your sorce is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")