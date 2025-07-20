# Практическая работа №1. Системы контроля версий. Работа с Flask
# На этом практическом занятии создаём консольную игру «Камень-Ножницы-Бумага»
import random
import json

class RockPaperScissors:
    def __init__(self):
        """Инициализация игры: задаем начальные очки, варианты и список для записи счёта"""
        self.random_variants = ('камень', 'ножницы', 'бумага')
        self.count_user = 0
        self.count_comp = 0
        self.score = []

    def computer_variant(self):
        """Возвращает случайный выбор компьютера"""
        return random.choice(self.random_variants)

    def user_variant(self):
        """Получает выбор пользователя"""
        while True:
            choice = input('Выберите один из трёх вариантов: ').lower()
            if choice in self.random_variants or choice == 'выход':
                return choice
            else:
                print('❌ Неверный ввод: попробуйте снова...')

    def play_round(self):
        """Логика одного раунда игры"""
        comp = self.computer_variant()
        user = self.user_variant()
        if user == 'выход':
            print('Спасибо за игру! Приходите к нам снова')
            self.save_score_json()
            return False # Сигнал для выхода из игры
        print(f'Я выкинул {comp}')
        if comp == user:
            print('Ничья :)')
        elif (comp == 'камень' and user == 'бумага') or \
             (comp == 'бумага' and user == 'ножницы') or \
             (comp == 'ножницы' and user == 'камень'):
            self.count_user += 1
            print('Вы победили! Вам очко')
        else:
            self.count_comp += 1
            print('Я выиграл. Очко мне :) ')
        print(f'Счёт: Я - {self.count_comp}, Вы - {self.count_user}')
        self.score.append(f'Счёт: Я - {self.count_comp}, Вы - {self.count_user}') # добавление счёта в список
        return True # Сигнал для продолжения игры
    
    def save_score_json(self, filename='score.json'):
        '''Сохранение счёта в формате json'''
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.score, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f'Ошибка при сохранении файла: {e}')

    def start_game(self):
        """Запуск игры"""
        print('Давайте сыграем в игру "Камень, ножницы, бумага"')
        print('Если устанете, напишите: "Выход"')
        while self.play_round():
            pass

# Запуск игры
if __name__ == '__main__':
    game = RockPaperScissors()
    game.start_game()
