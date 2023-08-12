def example1():
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
        except ValueError:
            print("please enter a number")
            continue
        try:
            print(x, "/", y, "=", x / y)
        except ZeroDivisionError as e:
            print("Error: ", e)


def example2(L):
    print("Example 2")
    sum = 0
    sumOfPairs = []
    try:
        for i in range(len(L)):
            sumOfPairs.append(L[i] + L[i + 1])
    except TypeError as e:
        print("Error: ", e)
    except IndexError as e:
        print("Error: ", e)
    else:
        print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError as e:
        print("provide valid path", e)
        return
    for line in file:
        print(line.upper())
    file.close()


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    try:
        example3([10, 3, 5, 6])
    except NameError as e:
        print("function does not exist", e)

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")


try:
    if __name__ == `__main__`:
        main()
except SyntaxError as e:
    print("SyntaxError: ", e)
