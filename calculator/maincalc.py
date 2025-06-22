import math
import random
import time

def quickMaths(choice):
    match choice:
        case 0:
           number = float(input(">>> "))
           number1 = float(input(">>> "))
           print(number + number1)
        case 1:
           number = float(input(">>> "))
           number1 = float(input(">>> "))
           print(number - number1)
        case 2:
           number = float(input(">>> "))
           number1 = float(input(">>> "))
           print(number / number1)
        case 3:
           number = float(input(">>> "))
           number1 = float(input(">>> "))
           print(number * number1)
        case 4:
           number = float(input(">>> "))
           print(math.sqrt(number))
        case 5:
           print(math.pi)
        case 6:
           question = input("Type GBP to do pounds to dollars or type USD to do dollars to pounds\n >>> ")
           if question == "gbp":
                  number = float(input(">>> "))
                  print(number * 1.35)
           elif question == "usd":
                  number = float(input(">>> "))
                  print(number * 0.74)
           else:
                  print("OOPS! Looks like you made a type error or typed something that doesn't exist. Mabye you spelt it wrong (Capital letters matter to!).")
        case 7:
           number = int(input("Please type the starting point for your random number generator\n >>> "))
           number1 = int(input("Please type the ending point for your random number generator \n >>> "))
           r = random.randint(number, number1)
           print(r)
        case 8:
           r = random.choice(["Heads", "Tails"])
           question = input("Which do you think you will get? Heads or Tails?\n >>> ")
           if r == "Heads" and question == "Heads":
                  print(r, "\n You won!")
           elif r == "Tails" and question == "Tails":
                  print(r, "\n You won!")
           elif r == "Heads" and question == "Tails":
                  print("You lost . . .")
           elif r == "Tails" and question == "Heads":
                  print("You lost . . .")
           else:
                  print("You lost . . .")
        case 9:
           question = input("Type bits if you want to do bits to bytes or type bytes if you want to do bytes to bits")
           if question == "bits":
                  number = int(input(">>> "))
                  print(number / 8)
           elif question == "bytes":
                  number = int(input(">>> "))
                  print(number * 8)
           else:
                print("OOPS! Looks like you made a type error or typed something that doesn't exist. Mabye you spelt it wrong (Capital letters matter to!).")
        case 10:
              question = input("Type miles for miles to kilometers or type kilometers for kilometers to miles.")
              if question == "miles":
                   number = float(input(">>> "))
                   print(number * 1.60934)
              elif question == "kilometers":
                   number = float(input(">>> "))
                   print(number * 0.621371)
              else:
                   print("OOPS! Looks like you made a type error or typed something that doesn't exist. Mabye you spelt it wrong (Capital letters matter to!).")

def main():
    print("0- addition,\n" \
        "1- subtraction," \
        "\n2- division," \
        "\n3- multiplication," \
        "\n4- square_root," \
        "\n5- pi," \
        "\n6- currency_conversion," \
        "\n7- number_generator," \
        "\n8- coin_flip, " \
        "\n9- bits_bytes_conversion " \
        "\n10- miles to kilometers")
    
    choice = int(input("What would you like to do in this calculator? From the list above.\n >>> "))
    quickMaths(choice)

if __name__ == "__main__":
    main()

time.sleep(5)
print("If you want to use this again then run the .exe again.")
time.sleep(2)
print("I hope you enjoyed the calculator! If you want to say what I can improve or add to the calculator on github I will apreaciate it!")
time.sleep(1.25)
print("I hope you use me again as I can't wait!")
time.sleep(1)
print("Exiting calculator. . .")
time.sleep(1.5)
quit()