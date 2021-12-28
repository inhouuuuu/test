# # # ########### 1. 업다운
#
# from random import randrange
#
# # # # #1. 컴퓨터가 1~100 중에서 임의의 수(C)를 랜덤으로 정한다. (random 패키지에 있는 randrange 함수를 사용할 것)
# # # # c = randrange(1, 101)
# # # #
# # # # success = 0
# # # #
# # # # #4. 2\~3번을 4번 더 반복한다. (즉, 2\~3번을 for문으로 작성할 것)
# # # # for i in range(0, 5):
# # # #     #2. 플레이어가 input 함수를 통해서 임의의 수(P)를 입력한다.
# # # #     #3. 컴퓨터는 C와 P를 비교하여, 업 / 다운 중 하나를 출력한다. (비교할 때는 if문을 사용할 것, '업' 혹은 '다운'은 print 문을 통해서 출력할 것)
# # # #     p = int(input())
# # # #     if c > p:
# # # #         print('업')
# # # #     elif c < p:
# # # #         print('다운')
# # # #     else:
# # # #         success = 1
# # # #         break
# # # #
# # # # #5. 플레이어가 총 5회 안에 컴퓨터가 정한 수를 맞히면 '성공', 맞히지 못하면 '실패' 를 출력한다.
# # # # if success == 1:
# # # #     print('성공')
# # # # else:
# # # #     print('실패')
# # #
# # # ####### 업다운 인공지능
# # # from math import floor
# # #
# # # num_list = range(1, 101)
# # #
# # # #플레이어가 input 함수를 통해서 1~100 중 임의의 수(P)를 입력한다. (1~100 이외의 수를 입력할 경우, 다시 입력하도록 할 것)
# # # p = int(input())
# # # while p not in num_list: # p < 1 or p > 100
# # #     print('1~100 사이의 수를 입력해주세요.')
# # #     p = int(input())
# # #
# # # #컴퓨터는 플레이어가 정한 수(P)를 가장 빨리 맞힐 수 있도록 수(C)를 말한다. (randrange는 사용하지 말 것)
# # # #플레이어는 C와 P를 비교하여, 업 / 다운 중 하나를 입력한다. (비교할 때는 if문을 사용할 것)
# # # #컴퓨터는 플레이어가 말하는 업 / 다운에 따라서, 해당될 수 없는 수들을 제거해나간다.
# # # while True:
# # #     c = num_list[floor(len(num_list)/2)]
# # #     print('컴퓨터 :', c)
# # #
# # #     if c == p:
# # #         print('성공')
# # #         break
# # #
# # #     p_ud = input('업? 다운? ')
# # #     if p > c and p_ud == '업':
# # #         num_list = num_list[num_list.index(c)+1:]
# # #     elif p < c and p_ud == '다운':
# # #         num_list = num_list[:num_list.index(c)]
# # #     else:
# # #         print('거짓말하지 마세요!')
# #
# # ############## 베스킨라빈스 31
# # from random import randrange
# #
# # the_last_number = 0
# #
# # # 3. 컴퓨터 혹은 플레이어는 앞 사람이 부른 숫자에 이어서, 1개~3개까지의 연속된 숫자를 말한다.
# # def computer_pick(the_last_number):
# #     c = randrange(1, 4)
# #     # 31 초과는 부를 수 없고, 31 초과를 부르려고 한다면 그냥 컴퓨터가 31까지 부르려 한다고 생각
# #     if the_last_number + c > 31:
# #         c = 31 - the_last_number
# #     for i in range(1, 1+c):
# #         print('컴퓨터: ', the_last_number + i)
# #     return the_last_number + c
# #
# # def player_pick(the_last_number):
# #     p = int(input())
# #     # 31 초과는 부를 수 없음
# #     # 해당 예외처리는 플레이어가 숫자를 입력한다는 전제하에 작성된 것이고, 정확한 예외처리는 try, except 를 사용하는 것이 맞습니다!
# #     while (p not in [1, 2, 3]) or (the_last_number + p > 31):
# #         print('다시 입력하세요!')
# #         p = int(input())
# #     for i in range(1, 1+p):
# #         print('플레이어: ', the_last_number + i)
# #     return the_last_number + p
# #
# # # 1. 컴퓨터가 먼저 숫자를 말할지, 플레이어가 먼저 숫자를 말할지는 랜덤으로 정한다.
# # whos_first = randrange(0, 2)
# #
# # # 2. 컴퓨터 혹은 플레이어는 1 혹은 1, 2 혹은 1, 2, 3을 말하면서 게임을 시작한다. (단, 컴퓨터가 숫자를 1개 부를지, 2개 부를지, 3개 부를지는 random 패키지를 이용해서 랜덤으로 정한다. 플레이어는 input 함수를 통해서 부르고 싶은 숫자까지 이어서 말한다.)
# # # 컴퓨터가 먼저 할 경우
# # if whos_first == 1:
# #     the_last_number = computer_pick(the_last_number)
# #
# # # 4. 2~3번을 31을 말하는 사람이 나올 때까지 반복한다. (즉, 2~3번을 while문으로 작성할 것. 단, 컴퓨터와 플레이어 모두 31을 초과해서 숫자를 부를 수는 없다.)
# # # 5. 31을 말하는 사람이 컴퓨터라면 '플레이어 승'을, 31을 말하는 사람이 플레이어라면 '컴퓨터 승'을 출력한다.
# # while True:
# #     the_last_number = player_pick(the_last_number)
# #     if the_last_number == 31:
# #         print('컴퓨터 승!')
# #         break
# #     the_last_number = computer_pick(the_last_number)
# #     if the_last_number == 31:
# #         print('플레이어 승!')
# #         break
#
# ##############베스킨라빈스 인공지능
# from random import randrange
#
# the_last_number = 0
#
# # 3. 컴퓨터 혹은 플레이어는 앞 사람이 부른 숫자에 이어서, 1개~3개까지의 연속된 숫자를 말한다.
# def computer_pick(the_last_number):
#     if (the_last_number + 3) % 4 == 0:
#         c = 1 # 플레이어가 1까지 불렀다면 컴퓨터는 2까지만 부르면 됨 -> 즉, 1개만 더 부르면됨
#     elif (the_last_number + 4) % 4 == 0:
#         c = 2 # 플레이어가 4까지 불렀다면 컴퓨터는 6까지 부르면 됨 -> 즉, 2개만 더 부르면됨
#     elif (the_last_number + 5) % 4 == 0:
#         c = 3
#     else:
#         c = randrange(1, 4)
#     # 예외처리 - 31 초과는 부를 수 없고, 31 초과를 부르려고 한다면 그냥 컴퓨터가 31까지 부르려 한다고 생각
#     if the_last_number + c > 31:
#         c = 31 - the_last_number
#     for i in range(1, 1+c):
#         print('컴퓨터: ', the_last_number + i)
#     return the_last_number + c
#
# def player_pick(the_last_number):
#     p = int(input())
#     # 31 초과는 부를 수 없음
#     # 해당 예외처리는 플레이어가 숫자를 입력한다는 전제하에 작성된 것이고, 정확한 예외처리는 try, except 를 사용하는 것이 맞습니다!
#     while (p not in [1, 2, 3]) or (the_last_number + p > 31):
#         print('다시 입력하세요!')
#         p = int(input())
#     for i in range(1, 1+p):
#         print('플레이어: ', the_last_number + i)
#     return the_last_number + p
#
# # 1. 컴퓨터가 먼저 숫자를 말할지, 플레이어가 먼저 숫자를 말할지는 랜덤으로 정한다.
# whos_first = randrange(0, 2)
#
# # 2. 컴퓨터 혹은 플레이어는 1 혹은 1, 2 혹은 1, 2, 3을 말하면서 게임을 시작한다. (단, 컴퓨터가 숫자를 1개 부를지, 2개 부를지, 3개 부를지는 random 패키지를 이용해서 랜덤으로 정한다. 플레이어는 input 함수를 통해서 부르고 싶은 숫자까지 이어서 말한다.)
# # 컴퓨터가 먼저 할 경우
# if whos_first == 1:
#     the_last_number = computer_pick(the_last_number)
#
# # 4. 2~3번을 31을 말하는 사람이 나올 때까지 반복한다. (즉, 2~3번을 while문으로 작성할 것. 단, 컴퓨터와 플레이어 모두 31을 초과해서 숫자를 부를 수는 없다.)
# # 5. 31을 말하는 사람이 컴퓨터라면 '플레이어 승'을, 31을 말하는 사람이 플레이어라면 '컴퓨터 승'을 출력한다.
# while True:
#     the_last_number = player_pick(the_last_number)
#     if the_last_number == 31:
#         print('컴퓨터 승!')
#         break
#     the_last_number = computer_pick(the_last_number)
#     if the_last_number == 31:
#         print('플레이어 승!')
#         break
#######################턴제 게임 및 기본 클래스 문제

# #@title
# #클래스 1번 해답
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return (self.width + self.height) * 2
#
# rec = Rectangle(2, 3)
# print(rec.area())
#
# #클래스 2번 해답
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
# class Dog(Animal):
#     def bark(self):
#         return f'{self.name}은 왈왈'
#
# class Cat(Animal):
#     def meow(self):
#         return f'{self.name}은 야옹'
#
# dog1 = Dog('강아지')
# print(dog1.bark())

#####################턴제 게임 해설
#@title
class Object:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")
        print(f"{target.name}에게 {self.power}만큼의 데미지!")
        target.hp = target.hp - self.power
        # 심화 개념: 사실은 여기서 target.hp 를 할당한다고 해서 실제로 해당 target 의 hp 값이 바뀌면 안되는 것이 원칙.
        # 그러므로 함수 마지막에서 return target.hp 를 해서 해당 target 의 값에 재할당해주는 것이 맞음.
        # 그러나 파이썬의 경우 자동으로 target 이 가진 속성의 주소를 변경해주기에, 굳이 재할당해주지 않아도, 해당 target 의 hp 값이 바뀜.
        # (위 개념은 굳이 이해하지 않아도 괜찮습니다!)
        if (target.hp <= 0):
            print(f"{target.name}을(를) 죽였습니다!")
        else:
            print(f"{target.name}의 HP가 {target.hp}이 되었습니다")

class Player(Object):
    def magic(self, target):
        print(f"{self.name}이(가) {target.name}에게 마법을 사용!")
        print(f"{target.name}에게 50만큼의 데미지!")
        target.hp = target.hp - 50
        if (target.hp <= 0):
            print(f"{target.name}을(를) 죽였습니다!")
        else:
            print(f"{target.name}의 HP가 {target.hp}이 되었습니다")

class Monster(Object):
    def cure(self):
        self.hp = self.hp + 10
        print(f"{self.name}이 체력을 10 회복했습니다!")
    def stay(self):
        print(f"{self.name}이 대기했습니다!")

#@title
from random import choice
from time import sleep # sleep 은 게임을 진행할 때 텍스트를 보기 편하게 하기 위함.

def createobjects():
    Warrior = Player('전사', 100, 10)
    # 이름으로 해당 몬스터 인스턴스를 찾을 수 있도록, 딕셔너리 형태로 Monsters 를 묶어놓음
    Monsters = {}
    Monsters['미니고블린'] = Monster('미니고블린', 10, 10)
    Monsters['고블린'] = Monster('고블린', 30, 30)
    Monsters['슈퍼고블린'] = Monster('슈퍼고블린', 50, 50)
    return Warrior, Monsters

def showinfo(Player, Monsters):
    print("\n--------------턴 시작---------------")
    print(f"{Player.name}의 체력 : {Player.hp}")
    for key, value in Monsters.items():
        print(f"{value.name}의 체력 : {value.hp}")

def playerturn(Player, Monsters):
    print("\n--------------플레이어 턴--------------")
    # 예외처리는 각자 해보시는 것을 추천드리겠습니다!
    # 예외처리는 try except 를 쓰는 것이 정확한 방법이긴 합니다!
    command = input('공격? 마법? : ')
    target = input('누구를 공격? : ')
    if command == '공격':
        Player.attack(Monsters[target])
    elif command == '마법':
        Player.magic(Monsters[target])
    return Monsters

def check_mdead(Monsters):
    # 이번 턴에서 죽은 몬스터가 있는지 확인
    dead_monsters = []
    for key, value in Monsters.items():
        if value.hp <= 0:
            dead_monsters.append(key)
    # 죽은 몬스터는 몬스터 명단에서 삭제
    for i in dead_monsters:
        del Monsters[i]
    # 남은 몬스터가 없다면 승리 출력, 있다면 몬스터 그대로 리턴해주기
    if len(Monsters) <= 0:
        return Monsters, True
    else:
        return Monsters, False

def monsterturn(Player, Monsters):
    print("\n------------몬스터 턴-----------")
    sleep(3)
    for key, value in Monsters.items():
        commands = ['cure', 'attack', 'stay']
        command = choice(commands)
        if command == 'cure':
            value.cure()
        elif command == 'attack':
            value.attack(Player)
        elif command == 'stay':
            value.stay()
    return Player

def check_pdead(Player):
    if Player.hp <= 0:
        return True
    else:
        return False

#@title
Warrior, Monsters = createobjects()

while True:
    showinfo(Warrior, Monsters)
    Monsters = playerturn(Warrior, Monsters)
    sleep(1)
    Monsters, ismdead = check_mdead(Monsters)
    if ismdead:
        print('\n승리!!!')
        break
    Warrior = monsterturn(Warrior, Monsters)
    ispdead = check_pdead(Warrior)
    if ispdead:
        print("\n패배!!!")
        break
    sleep(1)