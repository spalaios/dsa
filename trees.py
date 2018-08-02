from queue import Queue
from queue import LifoQueue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def find_min(self):
        current = self.root
        while current:
            current = current.left
        return current.data

    def find_max(self):
        current = self.root
        while current:
            current = current.right
        return current.data

    def insert_node(self, data):
        # if the tree is empty
        if self.root is None:
            # create a node with the data and make it root node
            root_node = Node(data)
            self.root = root_node
        else:
            self._insert_node(self.root,data)

    def _insert_node(self, root, data):
        if data < root.data:
            if root.left:
                self._insert_node(root.left, data)
            else:
                root.left = Node(data)
        elif data > root.data:
            if root.right:
                self._insert_node(root.right, data)
            else:
                root.right = Node(data)

    def get_node_with_parent(self, data):
        parent = None
        current = self.root
        if current is None:
            return parent , None
        while True:
            if current.data == data:
                return parent, current
            elif data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right

    def remove_node(self, data):
        parent, node = self.get_node_with_parent(data)
        #get the child count
        child_count = 0
        #when the tree is empty
        if parent is None and node is None:
            return False
        elif node.left is None and node.right is None:
            child_count = 0
        elif node.left and node.right:
            child_count = 2
        elif node.left or node.right:
            child_count = 1



        #case if the child count is 0
        if child_count == 0:
            if parent:
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
            else:
                #this will be the root node
                self.root = None
        elif child_count == 1:
            next_node = None
            if node.left:
                next_node = node.left
            elif node.right:
                next_node = node.right

            if parent:
                if parent.left:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                self.root = next_node
        elif child_count == 2:
            inorder_successor_node = self.get_inorder_successor(node.right)
            tempNode = inorder_successor_node
            #store the inorder_successor node data in temp and then first remove the inorder_successor node and then attach the temp data to its repesctive parent's child
            temp = inorder_successor_node.data
            self.remove_node(inorder_successor_node.data)
            if parent:
                if parent.left == node:
                    parent.left.data = tempNode.data
                elif parent.right == node:
                    parent.right.data = tempNode.data
            else:
                # print(self.root)
                # print(type(self.root))
                # print(self.root.data)
                self.root.data = tempNode.data


    def get_inorder_successor(self, node):
        current = node
        if current.left:
            current = current.left
        return current

    #find the maximum value element
    def maximum_value(self):
        max_value = -1
        if self.root is None:
            return -1
        else:
            count = []
            leftMax = self._maximum_value(self.root.left, count)
            # print(leftMax)
            count.clear()
            rightMax = self._maximum_value(self.root.right, count)
            # print(leftMax)
        return max(max(leftMax), max(rightMax))

    def _maximum_value(self, root, countList):
        if root is None:
            return 0
        self._maximum_value(root.left, countList)
        countList.append(root.data)
        self._maximum_value(root.right, countList)
        return countList

    #level order traversal
    def level_order_travesal(self):
        max_value = -1
        queue = Queue()
        stack = []
        if self.root is None:
            return queue
        else:
            queue.put(self.root)
            while not queue.empty():
                temp = queue.get()
                if temp.data > max_value:
                    max_value = temp.data
                stack.append(temp.data)
                if temp.left:
                    queue.put(temp.left)
                if temp.right:
                    queue.put(temp.right)
        return stack , max_value




tree = Tree()
tree.insert_node(50)
tree.insert_node(90005)
tree.insert_node(600154)
tree.insert_node(55)
tree.insert_node(35)
tree.insert_node(7558748)
tree.insert_node(63)
tree.insert_node(77)
# a, b = tree.get_node_with_parent(63)
# print(a.data, b.data)
# tree.remove_node(60)
print(tree.maximum_value())
print(tree.level_order_travesal())