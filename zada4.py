class Critter:
    """Виртуальные питомцы"""
    total = 3

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, name2, name3, hunger = 0, boredom = 0,hunger2=1,hunger3=2,boredom2=1,boredom3=2):
        self.boredom2=boredom2
        self.boredom3=boredom3
        self.hunger2=hunger2
        self.hunger3=hunger3
        self.name3= name3
        self.name2 = name2
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 3

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
        self.hunger2 += 1
        self.hunger3 += 1
        self.boredom2 += 1
        self.boredom3 += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имена зверушек не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имена успешно изменены.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m
    @property
    def mood2(self):
        unhappiness2 = self.hunger2 + self.boredom2
        if unhappiness2 < 5:
            m1 = "прекрасно"
        elif 5 <= unhappiness2 <= 10:
            m1 = "неплохо"
        elif 11 <= unhappiness2 <= 15:
            m1 = "не сказать чтобы хорошо"
        else:
            m1 = "ужасно"
        return m1
    @property
    def mood3(self):
        unhappiness3 = self.hunger3 + self.boredom3
        if unhappiness3 < 5:
            m2 = "прекрасно"
        elif 5 <= unhappiness3 <= 10:
            m2 = "неплохо"
        elif 11 <= unhappiness3 <= 15:
           m2  = "не сказать чтобы хорошо"
        else:
            m2 = "ужасно"
        return m2


    def talk(self):
        print("Нас зовут", self.name, ",",self.name2,",", self.name3,
              ", и сейчас мы чувствуем себя:", "1я",self.mood,"2я",self.mood2,"3я",self.mood3)
        self.__pass_time()

    def eat(self, food = 4,food2=4,food3=4):
        print("Мррр...  Спасибо!")
        self.hunger -= food
        self.hunger2 -= food2
        self.hunger3 -= food3
        if self.hunger < 0:
            self.hunger = 0
        elif self.hunger2 < 0:
            self.hunger2 = 0
        elif self.hunger3 < 0:
            self.hunger3 = 0
        self.__pass_time()

    def play(self, fun = 4,fun2=4,fun3=4):
        print("Уиии!")
        self.boredom -= fun
        self.boredom2 -= fun2
        self.boredom3 -= fun3
        if self.boredom < 0:
            self.boredom = 0
        elif self.boredom2 < 0:
            self.boredom2 = 0
        elif self.boredom3 < 0:
            self.boredom3 = 0
        self.__pass_time()

def main():
    zveri=[]
    crit_name = input("Как вы назовете свою  первую зверюшку?: ")
    crit_name2 = input("Как вы назовете свою  вторую зверюшку?: ")
    crit_name3 = input("Как вы назовете свою  третюю зверюшку?: ")
    crit = Critter(crit_name,crit_name2,crit_name3)
    zveri.append(crit)
    choice = None  
    while choice != "0":
        print \
        ("""
        Моя зверюшка
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшек
        2 - Покормить зверюшек
        3 - Поиграть со зверюшками
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        
        # кормление зверюшки
        elif choice == "2":
            crit.eat()
         
        # игра со зверюшкой
        elif choice == "3":
            crit.play()

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
main()