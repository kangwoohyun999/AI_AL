print("*********** Command ************")
print("+<c> : Insert c, -<c> : Delete c")
print("?<c> : Search c, S : Show, Q : Quit")
print("********************************")

stack_list = []

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

    def __str__(self):
        return f"Node address = {hex(id(self))}, data = {self.data}, link = {hex(id(self.link)) if self.link else 'None'}"

def list_func(command):
    # AddQ
    if command[0] == "+":
        c = command[1:]
        new_node = Node(c)
        if stack_list:
            new_node.link = stack_list[-1]  # Link to previous top
        stack_list.append(new_node)
    
    # DeleteQ
    elif command[0] == "-":
        c = command[1:]
        for i in range(len(stack_list) - 1, -1, -1):
            if stack_list[i].data == c:
                del stack_list[i]
                break
        else:
            print(f"{c} not found in stack.")
    
    elif command[0] == "?":
        c = command[1:]
        for node in reversed(stack_list):
            if node.data == c:
                print("{c} is in the list.")
                print(node)
                break
        else:
            print(f"{c} not found.")

    # Show
    elif command == "S" or command == "s":
        if len(stack_list) == 0:
            print("List is Empty")
        else:
            for i in range(len(stack_list) - 1, -1, -1):
                    print(stack_list[i].data, end = " ")  # 노드의 data 값만 출력
            print()
    
    # Quit
    elif command == "Q" or command == "q":
        print("Quit")
        return False
    
    return True


# 실행 루프
while True:
    command = input("Command> ")
    if not list_func(command):
        break