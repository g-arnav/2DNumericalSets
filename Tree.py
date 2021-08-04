from Node import Node
from Ordering import OrderedPair

class Tree:
    def __init__(self, depth):
        root_gen = [OrderedPair(0, 1), OrderedPair(1, 0)]
        root_gaps = [OrderedPair(-1, -1)]
        self.root = Node(root_gen, root_gaps, 0)
        self.depth = depth
        self.size = [0] * (depth + 1)
        self.build_tree(self.root)

    def build_tree(self, node):
        self.size[node.depth] += 1
        if node.depth != self.depth:
            node.next_layer()
            for n in node.children:
                self.build_tree(n)

    def size_at(self, d):
        if d > self.depth:
            print("Tree is not calculated at that depth")
        return self.size[d]

    def size(self):
        return self.size[-1]

    def print_depth(self, d):
        if d > self.depth:
            print("Tree is not calculated at that depth")
        string = ""
        queue = [self.root]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.depth == d:
                string += " " + str(current) + ","
            else:
                for n in current.children:
                    queue.append(n)
        print(string)

    def __repr__(self):
        string = "Level 0 [1]: "
        i = 0
        queue = [self.root]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.depth > i:
                i += 1
                string = string[:-1]
                string += "\nLevel {} [{}]: ".format(i, self.size_at(i))
            string += " " + str(current) + ","
            for n in current.children:
                queue.append(n)
        return string
