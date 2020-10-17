
try:
    a = int(input("Please enter first Digit."))
    b = int(input("Please enter Second Digit."))
    c = input("Please enter interprator.")
except:
    print("Please enter an valid Chracter.")



if __name__ == "__main__":
        
    if c == '+':
        print(a+b)

    if c == '-':
            print(a-b)

    if c == '*':
            print(a*b)

    if c == '/':
            print(a/b)
    else:
        print("Please fill data properly")        