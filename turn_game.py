# 1. Object 클래스는 '이름', 'HP', '공격력'이라는 속성과 '공격'이라는 메소드를 가지고 있습니다.
class Object:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

# (공격이라는 함수는 '공격하고자 하는 대상'을 인자로 받으며, 실행할 경우, 공격하고자 하는 대상의 HP를 자신의 공격력만큼 감소시킵니다. 공격할 때에는 ~~가 ~~를 공격했고, 그에 따라 공격받은 대상의 체력이 얼마 남았는지가 print 문으로 출력됩니다.)
    def attack(self, enemy):
        print(f"{self.name}이(가) {enemy.name}를(을) 공격!")
        print(f"{enemy.name}에게 {self.dmg}만큼의 데미지!")
        enemy.hp = enemy.hp - self.dmg

        if (enemy.hp <= 0):
            print(f"{enemy.name}")
        else:
            print(f"{enemy.name}의 체력이 {enemy.hp}가 됐습니다.")

# 1. Player 클래스는 Object 클래스를 상속받으며, '마법'이라는 메소드를 가지고 있습니다.
# (마법이라는 함수는 '공격하고자 하는 대상'을 인자로 받으며, 실행할 경우, 공격하고자 하는 대상의 HP를 50만큼 감소시킵니다. 공격할 때에는 ~~가 ~~를 공격했고, 그에 따라 공격받은 대상의 체력이 얼마 남았는지가 print 문으로 출력됩니다.)
class Player(Object):
    def magic(self,enemy):
        print(f"{self.name}이가 {enemy.name}에게 마법을 사용!")
        print(f"{enemy.name}에게 50데미지 공격!")
        enemy.hp = enemy.hp - 50
        if (enemy.hp <= 0):
            print(f"{enemy.name}을(를) 죽였습니다!")
        else:
            print(f"{enemy.name}의 체력이 {enemy.hp}가 됐습니다")

# 1. Monster 클래스는 Object 클래스를 상속받으며, '대기'와 '치료'라는 메소드를 가지고 있습니다.
class Monster(Object):
    # (대기라는 함수는 self 외에는 다른 인자를 받지 않으며, 그냥 "~~가 대기했습니다" 만 출력됩니다.)
    def wait(self):
        print(f"{self.name}(이)가 대기했습니다")

    # (치료라는 함수는 self 외에는 다른 인자를 받지 않으며, 자기 자신의 HP를 10 증가시키는 기능을 가지고 있습니다. 증가시킬 때는 "~~가 자신의 체력을 10만큼 회복했다" 가 출력됩니다.)
    def heal(self):
        print(f"{self.name}(이)가 자신의 체력을 10만큼 회복했다")
        self.hp = self.hp + 10

warrior = Player('전사', 100, 10)
mini_goblin, goblin, super_goblin = Monster('')

while True:

    print("전사 체력 :", warrior.hp)

    if warrior.hp <= 0:  # 전사 체력이 0 이하라면 반복문 탈출.
        break

    print("")

    print("미니 고블린 체력 :", min_goblin.hp)
    #print("고블린 체력 :", goblin.hp)
    #print("슈퍼 고블린 체력 :", super_goblin.hp)

    Monster.hp = warrior.attack_dmg(Monster.hp)
    print("미니 고블린 체력 :", min_goblin.hp)
    #print("고블린 체력 :", goblin.hp)
    #print("슈퍼 고블린 체력 :", super_goblin.hp)

    if Monster.hp() <= 0:  # 슬라임 체력이 0 이하라면 반복문 탈출.
        break

print("게임을 종료합니다.")

while True:

    print("고블린의 공격")
    print("1. 일반공격")
    print("2. 몸통박치기")

    slime_input = input('사용할 스킬의 번호를 입력세요. ')

    print("전사 체력 :", warrior.hp)
    if slime_input == "1":
        warrior.hp = Monster.attack(warrior.hp)
    elif slime_input == "2":
        warrior.hp = Monster.body_attack(warrior.hp)

    print("전사 체력 :", warrior.hp)

    if warrior.hp <= 0:  # 전사 체력이 0 이하라면 반복문 탈출.
        break

    print("")

    print("전사가 공격합니다.")
    print("1. 일반공격")
    print("2. 파워스트라이크")
    print("3. 포션사용")

    warrior_input = input("사용할 스킬의 번호를 입력하세요. ")

    print("슬라임 체력 :", Monster.hp)

    if warrior_input == "공격":
        Monster.hp = warrior.attack(Monster.hp)
    elif warrior_input == "마법":
        Monster.hp = warrior.power_strike(Monster.hp)
    elif warrior_input == "3":
        warrior.drink_potion()
        print("전사 체력 :", warrior.hp)

    print("슬라임 체력 :", Monster.hp)

    if Monster.hp() <= 0:  # 슬라임 체력이 0 이하라면 반복문 탈출.
        break

print("게임을 종료합니다.")
