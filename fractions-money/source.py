import random


def FatFraction(x):
    a = random.randint(1, 9) * x
    b = random.randint(1, 9) * x
    if a > b:
        print(str(b) + "/" + str(a), end=" ")
    else:
        print(str(a) + "/" + str(b), end=" ")


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


def main():

    print()
    print("Please select a fraction method")
    print("1. Fat Fraction")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Multiplication")

    user_choice = input("Enter choice <1/2/3/4>: ")

    samples = int(input("Please enter number of samples you wish to generate: "))

    if user_choice == "1":
        print()
        print("-" * 25, "FAT FRACTION", "-" * 25)

    elif user_choice == "2":
        print()
        print("-" * 24, "MATRIX ADDITION", "-" * 23)

    elif user_choice == "3":
        print()
        print("-" * 22, "MATRIX SUBTRACTION", "-" * 22)

    elif user_choice == "4":
        print()
        print("-" * 21, "MATRIX MULTIPLICATION", "-" * 20)

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


main()
