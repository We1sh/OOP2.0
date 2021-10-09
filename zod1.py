class Soda: 
    def __init__(self, add = None): 
        self.add = add 
    def show_my_drink(self): 
        print(f"Газировка и {self.add}")
    def show_my_drink_2(self):
        print("Обычная газировка")
def main():    
    soda1 = Soda()     
    soda = Soda(add = "Банан") 
    choice = None  
    while choice != "0":
        print \
        ("""
        Мой Телевизор
    
        0 - Выйти
        1 - Показать соду с наполнителем
        2 - Показать соду без наполнителя
        """)
    if choice=="1":
        soda.show_my_drink()
    elif choice=="2": 
        soda1.show_my_drink_2()