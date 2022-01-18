state = {'A':[], 'B':[], 'C':[] }
count = 0

def hanoi(src,dest,rest, n):
    global count

    if n==1:
        count += 1
        print("원판 %d : %s --> %s"%(state[src][0],src,dest))
        state[dest].append(state[src].pop())
    else:
        hanoi(src,rest,dest,n-1)
        hanoi(src,dest,rest,1)
        hanoi(rest,dest,src,n-1)


def main():
    while True:
        user_input = int(input("원판의 수를 입력하세요 : "))

        if user_input == 0:
            break

        for i in range(user_input):
            state['A'].append(i+1)

        hanoi('A','C','B',user_input)

        print("이동 횟수 :",count)

main()