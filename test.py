class Tv:
    def __init__(self, vol1, vol2):
        self.vol1=vol1
        self.vol2=vol2
    def num(self,chanel):
        if a<=100:
            print('сейчас стоит канал:',chanel)
        elif a>100:
            print('Нету каналов выше цыфры 100')
    def v1(self,u):
        u=self.vol1-self.vol2
        print('Громкость увеличилась на',u)


    def v2(self,y):
        y=self.vol2-self.vol1
        print('Громкость уменьшилась на',y)
def main():
    crit = Tv()
    chanel=int(input('Поставьте номер канала:'))
    vol1=int(input('Увеличить громкость на:'))
    vol2=int(input('Уменьшить громкость на:'))
    choice = None  
    while choice != "0":
        print \
        ("""
        Мой Телевизор
    
        0 - Выйти
        1 - Номер канала
        2 - Увеличить громкость 
        3 - Уменьшить громкость
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            crit.num(chanel)
        
        # кормление зверюшки
        elif choice == "2":
            crit.v1()
         
        # игра со зверюшкой
        elif choice == "3":
            crit.v2()

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
main()