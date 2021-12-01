# ------------------------------------------------- #
# Title: Error Handling Test
# Description: Show examples of error handling
# ChangeLog: (Who, When, What)
# DEsporma,11.29.2021,Created Script
# ------------------------------------------------- #


# Data -------------------------------------------- #
# Define variables
userdata = ""
repeat = ""
menurepeat = ""


# Processing -------------------------------------- #
# Define functions for error code display.
class ErrorDisp:
    @staticmethod
    def errorcodemsg(e):
        """Standard format in this script for error readout when showing examples."""
        ErrorDisp.spacer(0)
        print("Error:")
        print("Type: " + str(type(e)))
        print("Object: ",e)
        print("Message: ",e.__doc__)

    @staticmethod
    def ZeroDiv():
        """Zero Division Error example to show user"""
        print("*** ZeroDivisionError: Attempt to divide a value by zero. ***")
        ErrorDisp.spacer(0)
        try:
            print(1 / 0)
        except Exception as e:
            print("Attempted code:"
                  "\nprint(1/0)")
            ErrorDisp.errorcodemsg(e)
            ErrorDisp.spacer(2)

    @staticmethod
    def IndexErr():
        """Index Error example to show user"""
        print("*** IndexError: Indexed reference does not exist. ***")
        ErrorDisp.spacer(0)
        try:
            hello = [1, 2]
            print(hello[3])
        except Exception as e:
            print("Attempted code: \n"
                  "hello = [1, 2]\n"
                  "print(hello[3])"
                  )
            ErrorDisp.errorcodemsg(e)
            ErrorDisp.spacer(2)

    @staticmethod
    def NameErr():
        """NameError to show user"""
        print("*** NameError: Reference is not defined. ***")
        ErrorDisp.spacer(0)
        try:
            for row in fakefile:
                print(row)
        except Exception as e:
            print("Attempted code: \n"
                  "for row in fakefile:\n"
                  "\tprint(row)")
            ErrorDisp.errorcodemsg(e)
            ErrorDisp.spacer(2)

    @staticmethod
    def spacer(reps):
        """Easy function for author to add newlines. Makes much easier when using laptop keys instead of external keyboard."""
        print("\n"*reps)

# Define functions for menu
class Menu:
    @staticmethod
    def userselect():
        print("-"*15,
        "\nMenu of Options:"
        "\n1. See Example Errors"
        "\n2. Divide by Configurable Divisor"
        "\n3. Exit program."
        "\n")
        selection = int((input("Please select a menu item: ")).strip())
        return selection

    @staticmethod
    def simplediv():
        repeat = False
        while(repeat == False):
            try:
                divisor = input("Equation = 1 / [divisor]\n"
                            "Please enter an value as the divisor in the equation above. Entering a zero or non-numeric character will result in an error: ").strip()
                quotient = 1 / float(divisor)
                print("Quotient = ", quotient)
            except ZeroDivisionError as e:
                print("Zero Division Error: Please do not enter zero. Please try again.\n")
            except ValueError as e:
                print("Value Error: Please do not enter non-numeric values. Please try again.\n")
            else:
                repeat = True

# Define custom error classes for menu system
#class MenuError(Exception):
#    def __str__(self):
#        return "Please enter an integer value between 1 and 3"

#class DivisionOptionError(Exception):
#    def __str__(self):
#        return "Please enter a numeric non-zero value."

# Presentation ------------------------------------ #
while (True):
    userdata = str(Menu.userselect()).strip()
    menurepeat = True
    if userdata == "1":   # Show user examples of errors
        # ZeroDivisionError
        ErrorDisp.ZeroDiv()

        # IndexError
        ErrorDisp.IndexErr()

        # NameError
        ErrorDisp.NameErr()

    elif userdata == "2":   # Give user interactive option to test error handling.
        Menu.simplediv()

    elif userdata == "3":   # Exit program
        print("Program successfully exited.")
        break
    else:
        print("\nValue must be an integer between 1 and 3. Please try again.\n")
        menurepeat = False

    continue