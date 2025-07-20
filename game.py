# Практическая работа №1. Системы контроля версий. Работа с Flask
# На этом практическом занятии создаём консольную игру «Камень-Ножницы-Бумага»
import random

random_variants = ('камень', 'ножницы', 'бумага')

def computer_variant():
    '''Возвращает случайный выбор из random_variants'''
    return random.choice(random_variants)

def user_variant():
    '''Пользовательский ввод'''
    while True:
        choice = input('Выберите один из трёх вариантов: ').lower()
        if choice in random_variants:
            return choice
        elif choice == 'выход':
            return choice
        else: print('❌ Неверный ввод: попробуйте снова...')

def game():
    '''Сравнивание результатов и подсчёт очков'''
    count_comp = 0
    count_user = 0
    while True:
        comp = computer_variant()
        user = user_variant()
        if user == 'выход':
            print('Спасибо за игру! Приходите к нам снова')
            break
        print (f'Я выкинул {comp}')
        if comp == user:
            print('Ничья :)')
        elif (comp == 'камень' and user == 'бумага') or (comp == 'бумага' and user == 'ножницы') \
        or (comp == 'ножницы' and user == 'камень'):
            count_user += 1
            print('Вы победили! Вам очко')
        else:
            count_comp += 1
            print('Я выиграл. Очко мне :) ')
        print(f'Счёт: Я - {count_comp}, Вы - {count_user}')    
        
def start_game():
    print('Давайте сыграем в игру "Камень, ножницы, бумага"')
    print('Если устанете, напишите: "Выход"')
    game()

# Запуск игры
if __name__ == '__main__': 
     start_game()
