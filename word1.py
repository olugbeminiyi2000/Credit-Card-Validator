import sys
import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
VOWEL_COST = 250

class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return f"{self.name} (${self.prizeMoney})"


class WOFHumanPlayer(WOFPlayer):
    def __init__(self, name):
        super().__init__(name)

    def getMove(self, category, obscuredPhrase, guessed):
        print(self.__str__(), '\n')
        print(f"Category: {category}\nPhrase: {obscuredPhrase}\nGuessed: {', '.join(sorted(guessed))}\n")
        move = input("Guess a letter, phrase, or type 'exit' or 'pass':")
        return move


class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        return random.randint(1, 10) <= self.difficulty

    def getPossibleLetters(self, guessed):
        possibleLetters = []
        for letter in LETTERS:
            if letter in VOWELS and self.prizeMoney < VOWEL_COST:
                continue
            elif letter not in guessed:
                possibleLetters.append(letter)
        return possibleLetters

    def getMove(self, category, obscuredPhrase, guessed):
        print(self.__str__(), '\n')
        print(f"Category: {category}\nPhrase: {obscuredPhrase}\nGuessed: {', '.join(sorted(guessed))}\n")
        possibleLetters = self.getPossibleLetters(guessed)
        if not possibleLetters:
            return 'pass'
        if self.smartCoinFlip():
            for letter in self.SORTED_FREQUENCIES:
                if letter in possibleLetters:
                    return letter
        return random.choice(possibleLetters)


def getNumberBetween(prompt, min, max):
    while True:
        try:
            n = int(input(prompt))
            if n < min:
                print(f"Must be at least {min}")
            elif n > max:
                print(f"Must be at most {max}")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a number.")


def spinWheel():
    try:
        with open("wheel.json", 'r') as f:
            wheel = json.loads(f.read())
            return random.choice(wheel)
    except FileNotFoundError:
        print("Error: wheel.json file not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: wheel.json file is not in the correct format.")
        sys.exit(1)


def getRandomCategoryAndPhrase():
    try:
        with open("phrases.json", 'r') as f:
            phrases = json.loads(f.read())
            category = random.choice(list(phrases.keys()))
            phrase = random.choice(phrases[category])
            return category, phrase.upper()
    except FileNotFoundError:
        print("Error: phrases.json file not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: phrases.json file is not in the correct format.")
        sys.exit(1)


def obscurePhrase(phrase, guessed):
    return ''.join([letter if letter in guessed or letter not in LETTERS else '_' for letter in phrase])


def showBoard(category, obscuredPhrase, guessed):
    return f"""
Category: {category}
Phrase:   {obscuredPhrase}
Guessed:  {', '.join(sorted(guessed))}
"""


def requestPlayerMove(player, category, guessed, phrase):
    while True:
        time.sleep(0.1)
        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        if move.upper() == 'EXIT' or move.upper() == 'PASS':
            return move.upper()
        elif len(move) == 1 and move.isalpha():
            if move.upper() not in LETTERS:
                print("Guesses should be letters. Try again.")
                continue
            elif move.upper() in guessed:
                print(f"{move.upper()} has already been guessed. Try again.")
                continue
            elif move.upper() in VOWELS and player.prizeMoney < VOWEL_COST:
                print(f"Need ${VOWEL_COST} to guess a vowel. Try again.")
                continue
            else:
                return move.upper()
        else:
            return move


def main():
    print('=' * 15)
    print('WHEEL OF PYTHON')
    print('=' * 15)
    print('')

    numHuman = getNumberBetween('How many human players?', 0, 10)
    humanPlayers = [WOFHumanPlayer(input(f'Enter the name for human player #{i + 1}')) for i in range(numHuman)]

    numComputer = getNumberBetween('How many computer players?', 0, 10)
    if numComputer >= 1:
        difficulty = getNumberBetween('What difficulty for the computers? (1-10)', 1, 10)
    computerPlayers = [WOFComputerPlayer(f'Computer {i + 1}', difficulty) for i in range(numComputer)]

    players = humanPlayers + computerPlayers

    if not players:
        print('We need players to play!')
        return

    category, phrase = getRandomCategoryAndPhrase()
    guessed = []
    playerIndex = 0

    while True:
        player = players[playerIndex]
        wheelPrize = spinWheel()

        print('')
        print('-' * 15)
        print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
        print('')
        print(f'{player.name} spins...')
        time.sleep(2)
        print(f'{wheelPrize["text"]}!')
        time.sleep(1)

        if wheelPrize['type'] == 'bankrupt':
            player.goBankrupt()
        elif wheelPrize['type'] == 'loseturn':
            pass
        elif wheelPrize['type'] == 'cash':
            move = requestPlayerMove(player, category, guessed, phrase)
            if move == 'EXIT':
                print('Until next time!')
                break
            elif move == 'PASS':
                print(f'{player.name} passes')
            elif len(move) == 1:
                guessed.append(move)

                print(f'{player.name} guesses "{move}"')

                if move in VOWELS:
                    player.prizeMoney -= VOWEL_COST

                count = phrase.count(move)
                if count > 0:
                    if count == 1:
                        print(f"There is one {move}")
                    else:
                        print(f"There are {count} {move}'s")

                    player.addMoney(count * wheelPrize['value'])
                    if wheelPrize['prize']:
                        player.addPrize(wheelPrize['prize'])

                    if obscurePhrase(phrase, guessed) == phrase:
                        print(f"{player.name} wins! The phrase was {phrase}")
                        print(f"{player.name} won ${player.prizeMoney}")
                        if player.prizes:
                            print(f"{player.name} also won:")
                            for prize in player.prizes:
                                print(f"    - {prize}")
                        return

                    continue

                elif count == 0:
                    print(f"There is no {move}")
            else:
                if move == phrase:
                    print(f"{player.name} wins! The phrase was {phrase}")
                    print(f"{player.name} won ${player.prizeMoney + wheelPrize['value']}")
                    if wheelPrize['prize']:
                        player.addPrize(wheelPrize['prize'])
                    if player.prizes:
                        print(f"{player.name} also won:")
                        for prize in player.prizes:
                            print(f"    - {prize}")
                    return
                else:
                    print(f'{move} was not the phrase')

        playerIndex = (playerIndex + 1) % len(players)

    print(f"Nobody won. The phrase was {phrase}")


if __name__ == "__main__":
    main()
