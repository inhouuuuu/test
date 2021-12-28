import random

input_num = input()
receive_num = (random.randint(1, 100))
num_list = list(range(1,100))
value = 0

#플레이어가 input 함수를 통해서 1~100 중 임의의 수(P)를 입력한다. (1~100 이외의 수를 입력할 경우, 다시 입력하도록 할 것)
while True:{


}

while True:

    print(receive_num/2)
    input_hint = input("업 or 다운")

    if input_hint == "업":
        print(receive_num)
        value > receive_num

    elif input_hint == "다운":
        print(receive_num)
        value = receive_num
    else:
        input_num == receive_num
        print('성공')
        break

# start = 0
# end = 100
# while True:
#     middle = int((start+end)/2)
#     print(middle)
#     answer =input("값보다 up? down? answer?")
#
#     if(answer == "up"):
#         start=middle
#     elif(answer == "down"):
#         end = middle
#     elif(answer == "answer"):
#         print("정답입니다")
#         break
# print("게임이 끝났습니다")
