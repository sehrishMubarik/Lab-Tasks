import re

class Calculator:
    def __init__(self):
        self.result = 0

    def menu(self):
        while True:
            print("1. for addition")
            print("2. for subtraction")
            print("3. for multiplication")
            print("4. for division")
            print("5. for expression")
            try:
                option = int(input("Choose an operation: "))

                if option in [1, 2, 3, 4]:
                    x = float(input("Enter the first number: "))
                    y = float(input("Enter the second number: "))

                    if option == 1:
                        self.result = x + y
                    elif option == 2:
                        self.result = x - y
                    elif option == 3:
                        self.result = x * y
                    elif option == 4:
                        if y != 0:
                            self.result = x / y
                        else:
                            print("Error: Division by zero")
                            continue  
                elif option == 5:
                    self.result = self.complex_number()
                else:
                    print("Invalid operation")
                    continue
                print(f"The result of the operation is: {self.result}")
            except ValueError:
                print("Invalid input! Please enter a valid option.")
                continue
            
            choice = input("Do you want to perform another operation?").strip().lower()
            if choice != 'yes':
                print("Exiting the calculator")
                break

    def complex_number(self):
        try:
            e = input("Enter the expression: ")
            e = self.fix_implicit(e)  
            result = eval(e)
            return result
        except ZeroDivisionError:
            print("Error: Division by zero")
        except Exception as e:
            print("Error:", str(e))
            return None

    def fix_implicit(self, e):
        fixed_expression = re.sub(r'(\d)\s*\(', r'\1*(', e) 
        fixed_expression = re.sub(r'\)(\d)', r')*\1', fixed_expression)
        return fixed_expression
    
y = Calculator()
y.menu()
