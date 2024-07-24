def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("select an operation:")
print("1.add")
print("2.mul")
print("3.sub")
print("4.div")
print("5.exit")
choice = int(input("enter ur choice('1','2','3','4','5'):"))
while 1:
    if choice == 5:
        print("tata......")
        break
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))
    if choice == 1:
        print(add(num1,num2))
        break
    elif choice == 2:
            print(sub(num1,num2))
            break

    elif choice == 3:
            print(mul(num1,num2))
            break
    elif choice == 4:
            print(div(num1,num2))
            break
    else:
        print("invlid input")
        break


