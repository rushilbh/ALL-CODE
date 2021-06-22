random=(1,5)
print("Number Guessing Game")
print("select a number between 1-10")
numberString=input("Enter your guess:-")
number = int(numberString)
if (number==random):
    print("congratulation you won")
    numberString=input("Enter your guess")
else:
    print("try again")
    numberString=input("Enter your guess:-")
if(numberString==random):
    print("congratulation you won")
    numberString=input("Enter your guess")
else:
        print("try again")
        numberString=input("Enter your guess:-")
        print("you lost")
