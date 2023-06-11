import random

class Game:
    def __init__(self):
        self._number = None
        self._guess = None

    def generate_number(self):
        self._number = random.randint(1, 100)

    def get_guess(self):
        return self._guess

    def set_guess(self, guess):
        try:
            self._guess = int(guess)
        except ValueError:
            print("Niepoprawne dane. Podaj liczbę.")

    def check_guess(self):
        if self._guess is None:
            print("Nie podano liczby.")
        elif self._guess < self._number:
            print("Za mało. Spróbuj ponownie.")
        elif self._guess > self._number:
            print("Za dużo. Spróbuj ponownie.")
        else:
            print("Brawo! Zgadłeś liczbę.")

class GuessingGame(Game):
    def check_guess(self):
        if self.get_guess() is None:
            print("Nie podano liczby.")
        elif self.get_guess() < self._number:
            print("Za mało. Spróbuj ponownie.")
        elif self.get_guess() > self._number:
            print("Za dużo. Spróbuj ponownie.")
        else:
            print("Brawo! Zgadłeś liczbę.")

game = GuessingGame()

print("Witaj w grze Zgadnij Liczbę.")
print("Komputer wylosuje liczbę z zakresu 1-100, a Twoim zadaniem będzie ją odgadnąć.")

game.generate_number()

while True:
    guess = input("Podaj swoją liczbę: ")
    game.set_guess(guess)

    game.check_guess()

    play_again = input("Czy chcesz zagrać ponownie? (tak/nie): ")
    if play_again.lower() != "tak":
        break