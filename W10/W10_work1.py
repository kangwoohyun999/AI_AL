class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_simple_tree():
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(30)

    root.left.left = TreeNode(40)
    root.left.right = TreeNode(50)

    root.right.left = TreeNode(60)
    root.right.right = TreeNode(70)

    return root


def bt_count(node):
    if node is None:
        return 0
    return 1 + bt_count(node.left) + bt_count(node.right)


def bt_add(node):
    if node is None:
        return 0
    return node.data + bt_add(node.left) + bt_add(node.right)


def bt_height(node):
    if node is None:
        return 0
    return 1 + max(bt_height(node.left), bt_height(node.right))


def bt_show_preorder(node):
    if node:
        print(node.data, end=" ")
        bt_show_preorder(node.left)
        bt_show_preorder(node.right)


def bt_free(node):
    if node is None:
        return
    bt_free(node.left)
    bt_free(node.right)
    print(f"free node with item {node.data} ...")

if __name__ == "__main__":
    t = build_simple_tree()

    print("************* Command ************")
    print("C: Count tree, A: Add tree data")
    print("H: Height of tree, S: Show preorder")
    print("F: Free tree, Q: Quit")
    print("**********************************")

    while True:
        cmd = input("\nCommand> ").upper()

        if cmd == "C":
            print(f"Total number of node = {bt_count(t)}")

        elif cmd == "A":
            print(f"Sum of tree data = {bt_add(t)}")

        elif cmd == "H":
            print(f"Height of tree = {bt_height(t)}")

        elif cmd == "S":
            bt_show_preorder(t)
            print()

        elif cmd == "F":
            bt_free(t)
            t = None

        elif cmd == "Q":
            print("Quit Program")
            break

        else:
            print("Invalid command!")
