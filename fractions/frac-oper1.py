import random

import random


def FatFraction(x):
    a = random.randint(1, 9) * x
    b = random.randint(1, 9) * x
    if a > b:
        print(str(b) + "/" + str(a), end="=")
    else:
        print(str(a) + "/" + str(b), end="=")


def FatMultiplication():
    k = random.randint(2, 100)
    x = random.randint(2, 9)
    y = random.randint(2, 9)

    print(k, "*", end=" ")
    FatFraction(x)

    print()
    print()

    FatFraction(x)
    print("* ", end="")
    FatFraction(y)
    print("=")


def FatAddition():

    x = random.randint(2, 9)
    a = random.randint(2, 9) * x
    a1 = random.randint(2, 9) * x

    b = random.randint(2, 9) * x

    print(str(a) + "/" + str(b), "+", str(a1) + "/" + str(b), "=")


def FatSubtraction():

    x = random.randint(2, 9)
    a = random.randint(2, 9) * x
    a1 = random.randint(2, 9) * x

    b = random.randint(2, 9) * x

    print(str(a) + "/" + str(b), "-", str(a1) + "/" + str(b), "=")


def FatAdditionDenominatorDifferent():

    i = random.randint(1, 9)
    i1 = random.randint(1, 9)
    j = random.randint(1, 9)
    k = random.randint(1, 9)
    print("{}/{} + {}/{}".format(i*j, i*k, i1*j, i1*k))


def FatSubtractionDenominatorDifferent():
    i = random.randint(1, 9)
    i1 = random.randint(1, 9)
    j = random.randint(1, 9)
    k = random.randint(1, 9)

    print("{}/{} - {}/{}".format(i*j, i*k, i1*j, i1*k))


def FatDivisionDenominatorDifferent():
    i = random.randint(1, 9)
    i1 = random.randint(1, 9)
    j = random.randint(1, 9)
    k = random.randint(1, 9)
    print("{}/{} \u00F7 {}/{}".format(i*j, i*k, i1*j, i1*k))


def FatRandom():
    random_val = random.randint(1, 7)

    if random_val == 1:
        x = random.randint(2, 9)
        FatFraction(x)
        print()
    elif random_val == 2:
        FatMultiplication()
    elif random_val == 3:
        FatAddition()
    elif random_val == 4:
        FatSubtraction()
    elif random_val == 5:
        FatAdditionDenominatorDifferent()
    elif random_val == 6:
        FatSubtractionDenominatorDifferent()
    elif random_val == 7:
        FatDivisionDenominatorDifferent()


def main():

    print()
    print("Please select a fraction method")
    print("1. Fat Fraction")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Multiplication")
    print("5. Addition Denominator Different")
    print("6. Subtraction Denominator Different")
    print("7. Division Denominator Different")
    print("8. Random")

    user_choice = input("Enter choice <1/2/3/4/5/6/7/8>: ")
    samples = int(input("Please enter number of samples you wish to generate: "))

    if user_choice == "1":
        print()
        print("-" * 25, "FAT FRACTION", "-" * 25)

    elif user_choice == "2":
        print()
        print("-" * 24, "MATRIX ADDITION (DENOMINATOR SAME)", "-" * 23)

    elif user_choice == "3":
        print()
        print("-" * 22, "MATRIX SUBTRACTION (DENOMINATOR SAME)", "-" * 22)

    elif user_choice == "4":
        print()
        print("-" * 21, "MATRIX MULTIPLICATION (DENOMINATOR SAME)", "-" * 20)

    elif user_choice == "5":
        print()
        print("-" * 21, "ADDITION (DENOMINATOR DIFFERENT)", "-" * 20)

    elif user_choice == "6":
        print()
        print("-" * 21, "SUBTRACTION (DENOMINATOR DIFFERENT)", "-" * 20)

    elif user_choice == "7":
        print()
        print("-" * 21, "DIVISION (DENOMINATOR DIFFERENT)", "-" * 20)

    elif user_choice == "8":
        print()
        print("-" * 21, "RANDOM", "-" * 20)

    for i in range(samples):
        print()
        if user_choice == "1":
            x = random.randint(2, 9)
            FatFraction(x)
            print()

        elif user_choice == "2":
            FatAddition()

        elif user_choice == "3":
            FatSubtraction()

        elif user_choice == "4":
            FatMultiplication()

        elif user_choice == "5":
            FatAdditionDenominatorDifferent()

        elif user_choice == "6":
            FatSubtractionDenominatorDifferent()

        elif user_choice == "7":
            FatDivisionDenominatorDifferent()

        elif user_choice == "8":
            FatRandom()


main()
