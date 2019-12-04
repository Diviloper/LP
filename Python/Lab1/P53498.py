class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def addChild(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ithChild(self, i):
        return self.child[i]

    def numChildren(self):
        return len(self.child)

    def __iter__(self):
        yield self.rt
        trees = [] + self.child
        while trees:
            yield trees[0].rt
            trees += trees[0].child
            trees = trees[1:]
        return
