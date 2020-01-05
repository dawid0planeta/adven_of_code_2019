class Node():
    def __init__(self, name):
        self.name = name
        self.siblings = []
        self.depth = 0


    def give_parent(self, parent):
        self.parent = parent
        self.update_depth(parent.depth)

    
    def add_sibling(self, sibling):
        self.siblings.append(sibling)


    def update_depth(self, parent_depth):
        self.depth += parent_depth + 1
        for each in self.siblings:
            each.update_depth(parent_depth)
        
    
    def get_dist_to(self, goal):
        if self == goal:
            return 0
        else:
            return self.parent.get_dist_to(goal)
    
    