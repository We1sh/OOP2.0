import random
class Farm:
    """Ферма"""
    total = 3

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)
        
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 16)
        self.boredom = random.randint(0, 16)
     
    def __str__(self):
        rep = 'Имя: ' + self.name + '\n' + 'Голод: ' + str(self.hunger) + '\n' + 'Щастье: ' + str(self.boredom)
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            f = "Прекрасно"
        elif 5 <= unhappiness <= 10:
            f = "Нормально"
        elif 11 <= unhappiness <= 15:
            f = "Плоховато"
        else:
            f = "Ужасно"
        return f

    def talk(self):
        print("Я", self.name, "и я чуствую себя", self.mood)
        self.__pass_time()

    @staticmethod 
    def number(number=None, x=0, f=0):
        while x==0:
          number=input('Сколько?')
          try:
           f=int(number)
           x=1
          except:
            print('Повторите снова')
       
        if int(number)<0:
          number=0
        else:
          number=f
        return number
         
    def eat(self, food):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Как хотите назвать первую зверушку? ")
    p1 = Farm(crit_name)
    crit_name = input("Как хотите назвать вторую зверушку? ")
    p2 = Farm(crit_name)
    crit_name = input("Как хотите назвать третюю зверушку? ")
    p3 = Farm(crit_name)

    choice = None
    numb=None
    while choice != "0":
        print \
        ("""
        Farm Caretaker
 
        0 - Выйти
        1 - Самочуствие питомцев
        2 - Покормить
        3 - Поиграть
        """)
 
        choice = input("Choice: ")
        print()

        if choice == "0":
            print("Пока.")

        elif choice == "1":
            p1.talk()
            print('Виииииии \n')
            p2.talk()
            print('Вуууууу \n')
            p3.talk()
            print('Хииииииииии \n')
     
        elif choice == "2":
            numb=Farm.number()
            p1.eat(numb)
            print("Вау,Спасибо тебе")
            p2.eat(numb)
            print("Спасибо тебе")
            p3.eat(numb)
            print("Мммм,Спасибо тебе")

        elif choice == "3":
            numb=Farm.number()
            p1.play(numb)
            p2.play(numb)
            p3.play(numb)
            print('Увиииииииии!!!!')

        elif choice =="4":
            print(p1)
            print(p2)
            print(p3)
            
        else:
            print("\nПростите, но пункта", choice, "не существует")

main()
