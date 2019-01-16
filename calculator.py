# =======================================
# This is the calculator app
# =======================================

class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """

    def add(self, firstOperand, secondOperand):
        """Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """

        return firstOperand + secondOperand
        
    def subtract(self, firstOperand, secondOperand):
        """subtracts two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """

        return firstOperand - secondOperand

    def multiply(self, firstOperand, secondOperand):
        """multiplies two numbers together
        
        Arguments:
            firstOperand -- any number
            secondOperand -- any number
        """
        return firstOperand * secondOperand

    def divide(self, firstOperand, secondOperand):
        """divides two numbers
        
        Arguments:
            firstOperand -- any number
            secondOperand -- any number
        """
        return firstOperand / secondOperand

