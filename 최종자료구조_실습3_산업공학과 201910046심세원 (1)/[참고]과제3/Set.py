class Set:
    def __init__(self):
        self.items = []

    def __eq__(self, setB):
        A = sorted(self.items)
        B = sorted(setB.items)

        if A==B:
            return True
        else:
            return False
    
    def insert(self,elem):
        if elem not in self.items:
            self.items.append(elem)

    def delete(self,elem):
        self.items.remove(elem)

    def union(self, setB):
        newset = Set()
        for el in self.items:
            newset.insert(el)
        for el in setB.items:
            newset.insert(el)
        return newset

    def intersect(self, setB):
        newSet = Set()
        for el in self.items:
            if el in setB.items:
                newSet.insert(el)
        return newSet

    def difference(self, setB):
        newSet = Set()
        for el in self.items:
            if el not in setB.items:
                newSet.insert(el)
        return newSet

    def isSubset(self,setB):
        for el in self.items:
            if el not in setB.items:
                return False
        return True

    def isProperSubset(self,setB):
        if self.isSubset(setB) and not self==setB:
            return True
        return False 

    def size(self):
        return len(self.items)

    def print(self,msg):
        print(msg,":",self)

    def __str__(self):
        return str(self.items)

def test(setA,setB):
    print("SetA: ",setA)
    print("SetB: ",setB)
    if setA == setB:
        print("A equal B: True")
    else:
        print("A equal B: False")
    print("A subset B :",setA.isSubset(setB))
    print("A proper subset B: ",setA.isProperSubset(setB))
    print("A union B :",setA.union(setB))
    print("A intersect B :",setA.intersect(setB))
    print("A difference B :",setA.difference(setB))
    print()

def main():
    setA = Set()
    setA.insert(2)
    setA.insert(3)
    setA.insert(4)

    setB = Set()
    setB.insert(2)
    setB.insert(3)
    setB.insert(4)

    setC = Set()
    setC.insert(2)
    setC.insert(3)
    setC.insert(4)
    setC.delete(4)

    test(setA,setB)
    test(setA, setC)
    test(setC, setA)

if __name__ == '__main__':
    main()