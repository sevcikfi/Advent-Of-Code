class Tree:
    def __init__(self, name, data=0, children=None):
        self.name = name
        self.children = []
        self.data = data
    def __repr__(self):
        return self.name
    def addChild(self, node):
        #assert isinstance(node, Tree)
        self.children.append(node)


def searchDict(what: str, where: dict):
    for key in where:
        if key in what:
            return where[key]
