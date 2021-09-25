class Tv:
    def num(self,chanel):
        if chanel<=100:
            print('сейчас стоит канал:',chanel)
        elif chanel>100:
            print('Нету каналов выше цыфры 100')
    def v1(self,vol1):
        if vol1<=30:
            print('Вы успешно изменили громкость на:',vol1)
        elif vol1>30:
            print('Это слишком громко')
        elif vol1<=0:
            print('Вы же ничего не')
        
def main():
    crit = Tv()
    chanel=int(input('Поставьте номер канала:'))
    vol1=int(input('Ввести громкость:'))
    choice = None  
    while choice != "0":
        print \
        ("""
        Мой Телевизор
    
        0 - Выйти
        1 - Номер канала
        2 - Изменить громкость 
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
            crit.v1(vol1)
         
        # игра со зверюшкой


        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
main()