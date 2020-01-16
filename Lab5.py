import time

class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
       
    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
       
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.insert_helper(self.root, val)
           
    def insert_helper(self, current_node, val):
        if val < current_node.data:
            if current_node.left == None:
                current_node.left = Node(val)
            else:
                self.insert_helper(current_node.left, val)
        else:
            if current_node.right == None:
                current_node.right = Node(val)
            else:
                self.insert_helper(current_node.right, val)
   
    def search(self, val):
        start = time.time()
        result = self.search_helper(self.root, val)        
        
        if result:
            end = time.time()
            elapsed = end - start  
            print("Elapsed time:" , elapsed , "seconds")
            return True
        else:
            end = time.time()
            elapsed = end - start            
            print("Elapsed time:" , elapsed , "seconds")
            return False
        
        
    def search_helper(self, current_node, val):
        if current_node == None:
            return False
        elif current_node.data.rstrip() == val:
            return True
        elif val < current_node.data:
            return self.search_helper(current_node.left, val)
        else:
            return self.search_helper(current_node.right, val)
            
def constructBST(file_name):
    myfile = open(file_name, 'r')
    lines = myfile.readlines()
    bst = BinarySearchTree()
    
    for i in range(len(lines)):
        bst.insert(lines[i])
    return bst


if (__name__ == "__main__"):
    name = "websites.txt"
    bst = constructBST(name)
    print(bst.search("cnnindonesia.com"))
          
