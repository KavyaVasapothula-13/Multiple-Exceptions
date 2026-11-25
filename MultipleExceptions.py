def exception_demo(): 
    try: 
        # Taking inputs from user 
        a = int(input("Enter first number: ")) 
        b = int(input("Enter second number: ")) 
  
        # Performing division 
        quotient = a / b 
  
        # Working with a list 
        data = [100, 200, 300] 
        pos = int(input("Enter index (0-2): ")) 
        print("Value at index:", data[pos]) 
        print("Result of division:", quotient) 
  
    except ZeroDivisionError: 
        print("Error: Division by zero is not allowed.") 
  
    except ValueError: 
        print("Error: Please enter valid numeric input.") 
  
    except IndexError: 
        print("Error: Invalid index. Please choose between 0 and 2.") 
  
    except Exception as err: 
        print("Unexpected error:", err) 
  
    else: 
        print("All tasks executed without any error.") 
  
    finally: 
        print("Program has ended.") 
  
# Call the function 
exception_demo() 
