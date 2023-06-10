import random

class GuessNumberGame:
    def init(self):
        self.number_to_guess = random.randint(1, 100)
        self.guesses_taken = 0

    def start(self):
        print("Witaj! Zgadnij liczbę z zakresu od 1 do 100.")

        while True:
            guess = int(input("Podaj swoją propozycję: "))
            self.guesses_taken += 1

            if guess < self.number_to_guess:
                print("Za mało!")
            elif guess > self.number_to_guess:
                print("Za dużo!")
            else:
                print(f"Brawo! Zgadłeś liczbę w {self.guesses_taken} próbach.")
                break

game = GuessNumberGame()
game.start()