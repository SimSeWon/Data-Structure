from Date import Date


def main():
    with open("input2.txt","r") as f:
        for line in f:
            data = [int(x) for x in line.split()]
            date = Date(data[0], data[1], data[2])
            
            for i in range(data[3]):
                date.increment()

            print(date)

main()