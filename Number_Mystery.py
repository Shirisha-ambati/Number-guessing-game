# Number Mystery

import random

secret_num=random.randint(1,200)

name=input("May i know who is playing:-")

while True:
    ur_choice=input("Assume a Number or Quit:")
    if ur_choice=="Quit":
        break

    ur_choice=int(ur_choice)
    if (secret_num==ur_choice):
        print("Yoo your quite good!,your guess is correct",name)
        break
    elif (secret_num>ur_choice):
        print("Way too smaller",name," guess a bigger one..")
    else:
        print("Way too Bigger",name ,"guess a smaller one.. ")

print("<<<<<___GAME OVER___>>>>>")
    