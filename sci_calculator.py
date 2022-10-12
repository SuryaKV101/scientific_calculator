import math

def main():
    # Declaring variables
    result = 0.0
    RESULT = 0.0
    totalResult = 0.00
    numCalcs = -1
    num1 = 0.0
    num2 = 0.0

    fullProgramRun = True

    # Loop to print out calc. menu
    while fullProgramRun:
        # Logic behind the statistics, and the extra credit "RESULT"
        RESULT = result
        totalResult += result
        numCalcs += 1
        halfProgramrun = True

        # Print user interface
        print(f"\nCurrent Result: {result}")

        print("\nCalculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")

        while halfProgramrun:
            # Prompt for operation
            operator: int = int(input("\nEnter Menu Selection: "))

            if (1 <= operator <= 6):
                # get user input
                input1 = input("Enter first operand: ")
                input2 = input("Enter second operand: ")
                # Extra credit logic
                if input1.upper() == "RESULT":
                    num1 = RESULT
                else:
                    num1 = float(input1)

                if input2.upper() == "RESULT":
                    num2 = RESULT
                else:
                    num2 = float(input2)


            # Logic based on each operation
            if operator == 0:
                print("\nThanks for using this calculator. Goodbye!")
                fullProgramRun = False
                halfProgramrun = False
            elif operator == 1:
                result = num1 + num2
                halfProgramrun = False
            elif operator == 2:
                result = num1 - num2
                halfProgramrun = False
            elif operator == 3:
                result = num1 * num2
                halfProgramrun = False
            elif operator == 4:
                result = num1 / num2
                halfProgramrun = False
            elif operator == 5:
                result = num1 ** num2
                halfProgramrun = False
            elif operator == 6:
                result = math.log(num2, num1)
                halfProgramrun = False
            elif operator == 7:
                if numCalcs < 1:
                    print("\nError: No calculations yet to average!")
                    continue
                else:
                    print(f"Sum of calculations: {totalResult}")
                    print(f"Number of calculations: {numCalcs}")
                    print(f"Average of calculations: {round(totalResult / numCalcs, 2)}")
            else:
                print("Error: Invalid selection!")

if __name__ == "__main__":
    main()

