from Date import Date

def main():
    with open("input3.txt","r") as f:
        for line in f:
            data = [int(x) for x in line.split()]
            date1 = Date(data[0],data[1],data[2])
            date2 = Date(data[3],data[4],data[5])

            count = 0
            if date1 > date2:
                while date1.notEqual(date2):
                    date2.increment()
                    count += 1
                count *= -1
            else:
                while date1.notEqual(date2):
                    date1.increment()
                    count += 1

            print("%d일 경과"%(count))

main()