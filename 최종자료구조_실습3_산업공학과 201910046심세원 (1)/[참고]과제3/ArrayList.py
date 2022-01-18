class ArrayList:
    def __init__(self):
        self.items = []

    def add(self, elem):
        self.items.append(elem)

    def remove(self,elem):
        try:
            self.items.remove(elem)
            return elem
        except ValueError:
            return -1

    def insert(self,pos,elem):
        self.items.insert(pos, elem)

    def delete(self,pos):
        del self.items[pos]

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def getEntry(self,pos):
        return self.items[pos]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def find(self,item):
        try:
            return self.items.index(item)
        except ValueError:
            return -1

    def replace(self,pos,elem):
        self.items[pos] = elem

    def sort(self):
        self.items.sort()

    def merge(self, lst):
        self.items += lst

    def removeDuplicates(self):
        copied = self.items[:]
        copied.sort()
        
        for i in range(len(copied)-1):
            if copied[i]==copied[i+1]:
                self.remove(copied[i])

    def print(self, msg = "ArrayList"):
        print(msg,self.size(),self.items)

def main():
    print("Enter a command : i(nsert), d(elete), e(mpty), g(etEntry), c(lear), a(dd),"\
        " dup, remove, serach, f(ind), r(eplace), s(ort), m(erge), p(rint)")

    lst = ArrayList()

    while True:
        print("> ",end='')
        user_input = input().split()

        command = user_input[0]
        arglist = user_input[1:]

        if command == 'i':
            lst.insert(int(arglist[0]), arglist[1])  
        elif command== 'd':
            lst.delete(int(arglist[0]))
        elif command== 'e':
            print(lst.isEmpty())
        elif command == 'g':
            print(lst.getEntry(int(arglist[0])))
        elif command == 'c':
            lst.clear()
        elif command == 'a':
            lst.add(arglist[0])
        elif command == 'dup':
            lst.removeDuplicates()
        elif command == 'remove':
            result = lst.remove(arglist[0])
            if result==-1:
                print("No such element")
            else:
                print(result,"removed")
        elif command == 'search':
            result = lst.find(arglist[0])
            if result==-1:
                print("No such element")
            else:
                print(lst.getEntry(result),"found")
        elif command == 'f':
            result = lst.find(arglist[0])
            if result==-1:
                print("No such element")
            else:
                print("found at index",result)
        elif command == 'r':
            lst.replace(int(arglist[0]),arglist[1])
        elif command == 's':
            lst.sort()
        elif command == 'm':
            lst.merge(arglist)
        elif command == 'p':
            lst.print()
        elif command == 'q':
            break
        else:
            print("Unknown command", command)


if __name__ == "__main__":
    main()