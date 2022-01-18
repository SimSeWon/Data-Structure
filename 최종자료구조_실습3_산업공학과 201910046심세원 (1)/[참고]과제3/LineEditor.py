from ArrayList import ArrayList

def printTXT(arraylist):
    length = arraylist.size()
    for i in range(length):
        print("%d>%s" % (i+1, arraylist.getEntry(i)),end='')
    print()

def main():
    lines =  ArrayList()

    with open("input.txt","r") as f:
        for line in f:
            lines.add(line)

    printTXT(lines)
    
    while True:
        print("> ", end="")
        user_input = input().split()
        arglist = [int(i) for i in user_input[1:]]
        cmd = user_input[0]

        if cmd == 'i':
            newinput = input()
            while newinput!="*":
                lines.insert(arglist[0], newinput+"\n")
                arglist[0] += 1
                newinput = input()
        elif cmd =='d':
            begin = arglist[0]
            end = arglist[1]

            for i in range(end-begin+1):
                lines.delete(begin-1)
            
        elif cmd =='r':
            newinput = input()
            lines.replace(arglist[0]-1,newinput+"\n")
        elif cmd=='p':
            printTXT(lines)
        elif cmd=='q':
            break
        else:
            print("Unknown command",cmd)

if __name__ == '__main__':
    main()