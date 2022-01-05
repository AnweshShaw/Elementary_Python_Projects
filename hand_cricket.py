import random
import os
print("\n                                                 ........Hand Cricket Game.......")
print("Instructions:-")
print("This game is like a real cricket match played between you and the computer.")
print("You score runs when you choose any number from 1 to 10.")
print("Simultaneously,the computer will also choose any number from 1 to 10.")
print("If both the numbers are same,you are out.")
print("If both numbers are different your chosen number will be added in your score.\n\n")
print("                                               Toss")
print("1)Heads")
print("2)Tails")
num = int(input("Press the option number you want to toss the coin: "))
toss = random.randint(0,1)
if toss==1:
    print("\nYou have won the toss.")
    print("What would you like to choose?")
    print("1)Batting.")
    print("2)Bowling.")
    choice = input("Enter the option number that you would like to choose: ")
    if choice=="1":
        print("You bat first.")
        print("                                            1st Innings")
        user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
        os.system("cls")
        computer_number = random.randint(1,10)
        print(f"The computer chooses the number: {computer_number}")
        total=0;
        if(user_number==computer_number):
            print("You are out.")
            print("Your score is = 0")
        else:
            total += user_number
            print(f"Your score is = {total}")
            while not(user_number == computer_number):
                user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
                os.system("cls")
                computer_number = random.randint(1, 10)
                print(f"The computer chooses the number: {computer_number}")
                if (user_number == computer_number):
                    print("You are out.")
                    print(f"Your score is ={total}")
                    total += 1
                    print(f"The target is ={total}")
                else:
                    total += user_number
                    print(f"Your score is = {total}")
        print("\n\n\n                                            2nd Innings")
        print("The Computer will bat now.You have to bowl now")
        user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
        os.system("cls")
        computer_number = random.randint(1, 10)
        print(f"The computer chooses the number: {computer_number}")
        total2=0;count=0
        if (user_number == computer_number):
            print("Computer is out.")
            print("Computer's score is = 0")
            print("                        Congratulations!!!You have won the game.")
        else:
            total2 += computer_number
            print(f"Computer's score is: {total2}")
            while not (user_number == computer_number):
                user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
                os.system("cls")
                computer_number = random.randint(1, 10)
                print(f"The computer chooses the number: {computer_number}")
                if (user_number == computer_number):
                    print("Computer is out.")
                    print(f"Computer's score is = {total2}")
                    if (total2 >= total):
                        count += 1
                        break
                else:
                    total2 += computer_number
                    print(f"Computer's score is = {total2}")
                    if(total2 >= total):
                        count += 1
                        break
        if(count == 1):
            print("                        Sorry ☹,The computer has won the game.")
        else:
            print("                        Congratulations!!!You have won the game.")
    else:
        print("\n\n                                 1st Innings")
        print("\nComputer bats first.You have to bowl now")
        user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
        os.system("cls")
        computer_number = random.randint(1, 10)
        print(f"The computer chooses the number: {computer_number}")
        total2 = 0;count = 0
        if (user_number == computer_number):
            print("Computer is out.")
            print("Computer's score is = 0")
        else:
            total2 += computer_number
            print(f"Computer's score is: {total2}")
            while not (user_number == computer_number):
                user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
                os.system("cls")
                computer_number = random.randint(1, 10)
                print(f"The computer chooses the number: {computer_number}")
                if (user_number == computer_number):
                    print("Computer is out.")
                    print(f"Computer's score is = {total2}")
                    total2 += 1
                    print(f"The target is ={total2}")
                else:
                    total2 += computer_number
                    print(f"Computer's score is = {total2}")
        print("                                 2nd Innings")
        print("You will bat now.")
        user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
        os.system("cls")
        computer_number = random.randint(1, 10)
        print(f"The computer chooses the number: {computer_number}")
        total = 0;
        if (user_number == computer_number):
            print("You are out.")
            print("Your score is = 0")
        else:
            total += user_number
            print(f"Your score is = {total}")
            while not (user_number == computer_number):
                user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
                os.system("cls")
                computer_number = random.randint(1, 10)
                print(f"The computer chooses the number: {computer_number}")
                if (user_number == computer_number):
                    print("You are out.")
                    print(f"Your score is ={total}")
                    if(total2 > total):
                        count += 1
                        break
                else:
                    total += user_number
                    print(f"Your score is = {total}")
                    if(total>=total2):
                        print("                        Congratulations!!!You have won the game.")
                        break
        if(count==1):
            print("                        Sorry ☹,The computer has won the game.")
else:
    print("\n\n                                 1st Innings")
    print("The Computer has won the toss.")
    print("Computer bats first.You have to bowl now")
    user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
    os.system("cls")
    computer_number = random.randint(1, 10)
    print(f"The computer chooses the number: {computer_number}")
    total2 = 0;
    count = 0
    if (user_number == computer_number):
        print("Computer is out.")
        print("Computer's score is = 0")
    else:
        total2 += computer_number
        print(f"Computer's score is: {total2}")
        while not (user_number == computer_number):
            user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
            os.system("cls")
            computer_number = random.randint(1, 10)
            print(f"The computer chooses the number: {computer_number}")
            if (user_number == computer_number):
                print("Computer is out.")
                print(f"Computer's score is = {total2}")
                total2 += 1
                print(f"The target is ={total2}")
            else:
                total2 += computer_number
                print(f"Computer's score is = {total2}")
    print("                                 2nd Innings")
    print("You will bat now.")
    user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
    os.system("cls")
    computer_number = random.randint(1, 10)
    print(f"The computer chooses the number: {computer_number}")
    total = 0;
    if (user_number == computer_number):
        print("You are out.")
        print("Your score is = 0")
    else:
        total += user_number
        print(f"Your score is = {total}")
        while not (user_number == computer_number):
            user_number = int(input("Enter the number from 1 to 10 that you want to chose: "))
            os.system("cls")
            computer_number = random.randint(1, 10)
            print(f"The computer chooses the number: {computer_number}")
            if (user_number == computer_number):
                print("You are out.")
                print(f"Your score is ={total}")
                if (total2 > total):
                    count += 1
                    break
            else:
                total += user_number
                print(f"Your score is = {total}")
                if (total >= total2):
                    print("                        Congratulations!!!You have won the game.")
                    break
    if (count == 1):
        print("                        Sorry ☹,The computer has won the game.")