print("*********** Command ************")
print("+<c> : AddQ, - : DeleteQ,\nS : Show, Q : Quit")
print("********************************")

# 큐 초기화
queue = []

def queue_func(command):
    # AddQ
    if command[0] == "+":
        queue.append(command[1])
    
    # DeleteQ
    elif command == "-":
        if len(queue) == 0:
            print("Queue is empty !!!")
            return True
        print(queue[0])
        queue.pop(0)
    
    # Show
    elif command == "S" or command == "s":
        for item in queue:
            print(item, end=" ")
        print()
    
    # Quit
    elif command == "Q" or command == "q":
        print("Quit")
        return False
    
    return True


# 실행 루프
while True:
    command = input("Command> ")
    if not queue_func(command):
        break
