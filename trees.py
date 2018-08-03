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

    def level(self):
        stack = []
        queue = Queue()
        level = 0
        if self.root is None:
            return queue
        else:
            queue.put((self.root,0))
            while not queue.empty():
                temp = queue.get()
                # print(temp[0].data)
                stack.append((temp[0].data, temp[1]))
                level = temp[1] + 1
                if temp[0].left:
                    queue.put((temp[0].left, level))
                if temp[0].right:
                    queue.put((temp[0].right, level))
        return stack

    def get_nodes_at_level(self, level):
        levels_list = self.level()
        if levels_list:
            result = [i[0] for i in levels_list if i[1] == level]
        return result

    def get_max_level_of_tree(self):
        tree_list = self.level()
        return max([i[1] for i in tree_list])

    def deepest_node(self):
        tree_list = self.level()
        max_level = self.get_max_level_of_tree()
        if tree_list:
            return [i[0] for i in tree_list if i[1] == max_level][0]

    def find_all_leaf_nodes(self):
        leaf_nodes_list = []
        if self.root is None:
            return
        elif self.root.left is None and self.root.right is None:
            leaf_nodes_list.append(self.root.data)
            return leaf_nodes_list
        else:
            left_tree = self._leaf_nodes(self.root.left, leaf_nodes_list)
            right_tree = self._leaf_nodes(self.root.right, leaf_nodes_list)
        leaf_nodes_list = left_tree
        return  leaf_nodes_list

    def _leaf_nodes(self,root, leaf_list):
        if root is None:
            return
        else:
            self._leaf_nodes(root.left, leaf_list)
            if root.left is None and root.right is None:
                leaf_list.append(root.data)
            self._leaf_nodes(root.right, leaf_list)
        return leaf_list

    def leaf_nodes_iteratively(self):
        queue = Queue()
        stack = []
        queue.put(self.root)
        while not queue.empty():
            temp = queue.get()
            if temp.left is None and temp.right is None:
                stack.append(temp.data)

            if temp.left:
                queue.put(temp.left)
            if temp.right:
                queue.put(temp.right)
        return stack




tree = Tree()
tree.insert_node(50)
tree.insert_node(60)
tree.insert_node(40)
tree.insert_node(55)
tree.insert_node(35)
tree.insert_node(75)
tree.insert_node(63)
tree.insert_node(77)
tree.insert_node(150)
# a, b = tree.get_node_with_parent(63)
# print(a.data, b.data)
# tree.remove_node(60)
# print(tree.maximum_value())
# print(tree.level_order_travesal())
# print(tree.level())
# print(tree.get_nodes_at_level(3))
# print(tree.get_max_level_of_tree())
# print(tree.deepest_node())
print(tree.find_all_leaf_nodes())
print(tree.leaf_nodes_iteratively())