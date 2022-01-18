import os
import glob

def phone_format(n):                                                                                                                                  
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1] 

class Node:

    def __init__(self, data,info):

        self.left = None
        self.right = None
        self.data = data
        self.info = info

# Insert method to create nodes
    def insert(self, data, data1):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, data1)
                else:
                    self.left.insert(data, data1)
            elif data  > self.data:
                if self.right is None:
                    self.right = Node(data, data1)
                else:
                    self.right.insert(data, data1)
        else:
            self.data = data

# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            x = str(self.info[3])
            number = x[:3] + '-' + x[3:5] + '-' + x[5:]
            print("ID: "+str(self.data) + "\nFirst Name: " + str(self.info[0])+ "\nLast Name: " + str(self.info[1])+ "\nPhone Number: " + str(phone_format(self.info[2]))+ "\nSSN Number: " + str(number)+ "\nAddress: " + str(self.info[4]) + "\nRank: " + str(self.info[5])+ "\nSalary: " + str(self.info[6]))

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

def search(ID):
    tree = Node(1, "test")
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "EmployeeList.csv"
    abs_file_path = os.path.join(script_dir, rel_path)
    file = open(abs_file_path)
        
    for line in file:
        line = line.split(",")
        n = int(line[0])
        d = line[1:]
        tree.insert(n, d)
        
    if ID:
        result = tree.findval(int(float(ID)))
    else:
        print("Invalid Input")

def data():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "DNA"
    abs_file_path = os.path.join(script_dir, rel_path)
    os.chdir(abs_file_path)

    myFiles = glob.glob('*.txt')  #retrieves every .txt file in a dir
    spot = -1
    f=open(myFiles[75], 'r')       #child's DNA

    childDNA = f.read()
    updatedChildsDNA = childDNA.replace("GAATTC", "G/AATTC").replace("GGATCC", "G/GATCC").replace("AAGCTT", "A/AGCTT").split('/')
    child = []
    for index in range(len(updatedChildsDNA)):
            child.append(len(updatedChildsDNA[index]))
    childsSet = set(child)

    for index in range(len(myFiles)-1):
        spot += 1
        dnaSequence = open(myFiles[index], 'r')
        data = dnaSequence.read()



        parentsDNA = data.replace("GAATTC", "G/AATTC").replace("GGATCC", "G/GATCC").replace("AAGCTT", "A/AGCTT").split('/')
        parent = []
        child = []

        for index in range(len(parentsDNA)):
            parent.append(len(parentsDNA[index]))


        parentsSet = set(parent)
        inter = parentsSet.intersection(childsSet)
        if len(inter) > 5:
            g = os.path.splitext(myFiles[spot])[0]
            search(g)
            break

        
def Main():
    data()

Main()

       



