

print("*********** Command ************")
print("+<c> : Push c, - : Pop,\nS : Show, Q : Quit")
print("********************************")


total = []

    
def stack(command):
    if command[0] == "+":
        total.append(command[1])
    elif command == "-":
        if len(total) == 0:
            print("Stack is empty !!!")
            return False
        else:
            print(total[-1])
        total.pop(-1)
    elif command == "S" or command == "s":
        for i in range(0,len(total), 1):
            print(total[i] + " ", end="")
            print()
    elif command == "Q" or command == "q":
        print("Quit")
        return False
    return True


while True:
    command = input("Command> ")
    if not stack(command):
        break