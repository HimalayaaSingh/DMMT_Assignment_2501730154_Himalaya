# BST stuff

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # inserting a node (prof showed this in class)
    def insert(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # helper for delete - finds smallest node in right subtree
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # no children (leaf node)
            if root.left is None and root.right is None:
                return None

            # only one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # two children - replace with inorder successor
            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


# graph using adjacency list

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))  # storing as (neighbor, weight)

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

    # BFS using a queue (just using a list here)
    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor, _ in self.graph.get(node, []):
                    queue.append(neighbor)

    # DFS using recursion
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        if start not in visited:
            print(start, end=" ")
            visited.add(start)
            for neighbor, _ in self.graph.get(start, []):
                self.dfs(neighbor, visited)


# hash table with chaining (separate chaining method)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of lists

    def hash_function(self, key):
        return key % self.size  # simple mod hashing

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # not found

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, "->", bucket)


# testing everything

if __name__ == "__main__":

    print("===== BST =====")
    bst = BST()
    root = None

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        root = bst.insert(root, v)

    print("Inorder traversal:")
    bst.inorder(root)
    print()

    print("Searching 20:", bst.search(root, 20))
    print("Searching 90:", bst.search(root, 90))

    root = bst.delete(root, 20)  # deleting leaf node
    print("After deleting 20:")
    bst.inorder(root)
    print()

    root = bst.insert(root, 65)
    root = bst.delete(root, 60)  # node with one child
    print("After deleting 60:")
    bst.inorder(root)
    print()

    root = bst.delete(root, 30)  # node with two children
    print("After deleting 30:")
    bst.inorder(root)
    print()


    print("\n===== GRAPH =====")
    g = Graph()

    edges = [
        ('A','B',2), ('A','C',4), ('B','D',7), ('B','E',3),
        ('C','E',1), ('D','F',5), ('E','D',2), ('E','F',6),
        ('C','F',8)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("Adjacency List:")
    g.print_graph()

    print("BFS starting from A:")
    g.bfs('A')
    print()

    print("DFS starting from A:")
    g.dfs('A')
    print()


    print("\n===== HASH TABLE =====")
    ht = HashTable(5)

    keys = [10, 15, 20, 7, 12]
    for k in keys:
        ht.insert(k, f"Value{k}")

    print("Hash Table:")
    ht.display()

    print("Getting 15:", ht.get(15))
    print("Getting 7:", ht.get(7))

    ht.delete(15)
    print("After deleting 15:")
    ht.display()