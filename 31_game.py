# 1. 컴퓨터가 먼저 숫자를 말할지, 플레이어가 먼저 숫자를 말할지는 랜덤으로 정한다.
import random

print("베스킨라빈스 31 게임 시작")

print("랜덤 순서 배정")
first_order = random.randrange(1,3)
order = int()
call = 0
count = 1

# 2. 컴퓨터 혹은 플레이어는 1 혹은 1, 2 혹은 1, 2, 3을 말하면서 게임을 시작한다. (단, 컴퓨터가 숫자를 1개 부를지, 2개 부를지, 3개 부를지는 random 패키지를 이용해서 랜덤으로 정한다. 플레이어는 input 함수를 통해서 연속해서 부르고 싶은 숫자 개수를 입력한다.)
while call < 31:
    if count % 2 == order:
        print('사용자 차례')
        size_of_call = input("숫자 갯수를 입력: ")
        size_of_call = int(size_of_call)

        for i in range(size_of_call):
            call += 1
            print("사용자: '{0}'".format(call))

# 3. 컴퓨터 혹은 플레이어는 앞 사람이 부른 숫자에 이어서, 1개~3개까지의 연속된 숫자를 말한다.
    else:
        print('컴퓨터의 차례')
        size_of_call = random.randint(1, 3)

        for i in range(size_of_call):
            call += 1
            print("컴퓨터: '{0}'".format(call))

    count += 1
# 4. 2\~3번을 31을 말하는 사람이 나올 때까지 반복한다. (즉, 2\~3번을 for문 혹은 while문으로 작성할 것. 단, 컴퓨터와 플레이어 모두 31을 초과해서 숫자를 부를 수는 없다.)

# 5. 31을 말하는 사람이 컴퓨터라면 '플레이어 승'을, 31을 말하는 사람이 플레이어라면 '컴퓨터 승'을 출력한다.
if count % 2 == order:
    print("사용자의 승리!!")
else:
    print("컴퓨터의 승리!!")

# (가능하다면, 컴퓨터가 숫자를 뽑는 코드와 플레이어가 숫자를 뽑는 코드는 함수화를 해보세요!)