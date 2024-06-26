def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y == 0:
        return "Error Division by Zero"
    return x/y
def calculator():
    print("Select choice:")
    print("1.Add")
    print("2.Sub")
    print("3.Multiply")
    print("4.Division")
    
    choice = input("Enter your choice(1/2/3/4): ")
    if choice in ["1","2","3","4"]:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        
        if choice == 1:
            print("The result is {}".format(add(num1,num2)))
        elif choice == 2:
            print("The result is {}".format(sub(num1,num2)))
        elif choice == 3:
            print("The result is {}".format(multiply(num1,num2)))
        elif choice == 4:
            print("The result is {}".format(division(num1,num2)))
        else:
            print("Invalid choice!")
            
if __name__ == "__main__":
    calculator()
            
