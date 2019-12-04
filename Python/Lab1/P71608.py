from functools import reduce

class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ith_child(self, i):
        return self.child[i]

    def num_children(self):
        return len(self.child)

class Pre (Tree):
    def preorder(self):
        return reduce(lambda acc, x: acc + x.preorder(), self.child, [self.rt])