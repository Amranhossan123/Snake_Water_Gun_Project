'''
-1 for Water

0 for Gun

1 for Snake

'''
import random
computer=random.choice([-1,0,1])
you_choice=input("Enter your choice S,W,G :")
you_choice_dict={"W":-1,"G":0,"S":1}
reverse_your_dict={-1:"Water",0:"Snake",1:"Gun"}
you=you_choice_dict[you_choice]
print(f"You Choice {reverse_your_dict[you]}\nComputer Choice {reverse_your_dict[computer]}")
if(computer==you):
    print("It's Draw")
else:
    if(computer==-1 and you==0):
        print("You Win")
    elif(computer==0 and you==-1):
        print("Computer Win")
    elif(computer==0 and you==1):
        print("You Win")
    elif(computer==1 and you==0):
        print("Computer win")
    elif(computer==-1 and you==1):
        print("Computer Win")
    else:
        print("You Win")



