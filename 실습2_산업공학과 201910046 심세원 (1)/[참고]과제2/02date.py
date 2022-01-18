from Date import Date


def findMinMax(lst):
    min = lst[0]
    max = lst[0]

    for el in lst:
        if el < min:
            min = el
        if el > max:
            max = el

    return min,max

def main():
    inFile = open("input.txt","r")
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()]
        lst.append(Date(date[0], date[1], date[2]))
    for i in range(len(lst)):
        print(lst[i])
    min,max = findMinMax(lst)
    print()
    print("earlist date:",min)
    print("latest date:",max)
    inFile.close()

main()