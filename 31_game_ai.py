# 1. 컴퓨터가 먼저 숫자를 말할지, 플레이어가 먼저 숫자를 말할지는 랜덤으로 정한다.
import random

def call_computer(call_status):
    if call_status % 4 == 0:
        computer_call = 2
    elif call_status % 4 == 1:
        computer_call = 1
    elif call_status% 4 == 3:
        computer_call = 3
    else:
        computer_call = random.randint(1, 3)

    return computer_call

print("베스킨라빈스 31 게임 시작")

print("랜덤 순서 배정")
first_order = random.randrange(1,3)

order = int()
call = 0
count = 1
# 2. 기존의 게임과 마찬가지로 1부터 순서대로 연속된 숫자를 말하되, 플레이어는 input 함수를 통해서 부르고 싶은 숫자까지 이어서 말한다. 컴퓨터는 나름의 방식을 가지고 숫자를 말한다.
while call < 31:

    if count % 2 == order:
        print('사용자 차례')
        size_of_call = input("숫자 갯수를 입력: ")
        size_of_call = int(size_of_call)

        for i in range(size_of_call):
            call += 1
            print("사용자: '{0}'".format(call))

# 3. 2번 과정을 31을 말하는 사람이 나올 때까지 반복한다. (즉, 2번을 for문 혹은 while문으로 작성할 것. 단, 컴퓨터와 플레이어 모두 31을 초과해서 숫자를 부를 수는 없다.)
    else:
        print('컴퓨터의 차례')
        size_of_call = random.randint(1, 3)
        size_of_call = call_computer()


        for i in range(size_of_call):
            call += 1
            print("컴퓨터: '{0}'".format(call))


    count += 1

# 4. 31을 말하는 사람이 컴퓨터라면 '플레이어 승'을, 31을 말하는 사람이 플레이어라면 '컴퓨터 승'을 출력한다. (단, 컴퓨터는 자신이 항상 이기도록 나름의 방식을 가지고 숫자를 부르기 때문에, 딱 한 가지 경우를 제외하고는 항상 컴퓨터가 이길 수 밖에 없을 것임에 유의)
if count % 2 == order:
    print("사용자의 승리!!")
else:
    print("컴퓨터의 승리!!")
# (가능하다면, 컴퓨터가 숫자를 뽑는 코드와 플레이어가 숫자를 뽑는 코드는 함수화를 해보세요!)