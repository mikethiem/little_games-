from random import randint
doubles = 0
num1 = randint(1, 6)
num2 = randint(1, 6)
print ("Do you want to roll? (Y)es or (N)o")
answer = input()
while answer.lower()[0] == "y":
    print ("You rolled a", num1, "and a", num2, ". Your total is", num1 + num2)
    while num1 == num2:
        print ("Well done you fabulous person, you rolled a double.")
    print ("Roll again? (Y)es or (N)o")
    answer = input()
print ("Okay. YOu rolled", doubles, "doulbes.")
