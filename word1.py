import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250

class WOFPlayer():
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney = self.prizeMoney + amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)
  
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)


class WOFHumanPlayer(WOFPlayer):
    def __init__(self, name):
        WOFPlayer.__init__(self, name)
        
    def getMove(self, category, obscuredPhrase, guessed):
        print(self.__str__(), '\n')
        print("Category: {}\nPhrase: {}\nGuessed: {}\n".format(category, obscuredPhrase, ", ".join(sorted(guessed))))
        move = input("Guess a letter, phrase, or type 'exit' or 'pass':")
        return move


class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFLip(self):
        rand_number = random.randint(1, 10)
        if rand_number > self.difficulty:
            return False
        elif rand_number <= self.difficulty:
            return True
  
    def getPossibleLetters(self, guessed):
        possibleLetters = []
        if self.prizeMoney <= VOWEL_COST:
            for i in LETTERS:
                if i in VOWELS:
                    continue
                elif i not in guessed:
                    possibleLetters.append(i)
        else:
            for i in LETTERS:
                if i in guessed:
                    continue
                else:
                    possibleLetters.append(i)
        return possibleLetters
  
    def getMove(self, category, obscuredPhrase, guessed):
        print(self.__str__(), '\n')
        print("Category: {}\nPhrase: {}\nGuessed: {}\n".format(category, obscuredPhrase, ", ".join(sorted(guessed))))
        possibleLetters = self.getPossibleLetters(guessed)
        move = self.smartCoinFLip()
        if possibleLetters == []:
            return 'pass'
        if move == True:
            index = 0
            for i in possibleLetters:
                if (index > self.SORTED_FREQUENCIES.index(i)):
                    continue
                else:
                    index = self.SORTED_FREQUENCIES.index(i)
            return self.SORTED_FREQUENCIES[index]
        elif move == False:
            return random.choice(possibleLetters)


def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        userinp = input('{}\n{}'.format(errmessage, prompt))


def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)


def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())


def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv


def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))


print('='*15)
print('WHEEL OF PYTHON')
print('='*15)
print('')

num_human = getNumberBetween('How many human players?', 0, 10)

human_players = [WOFHumanPlayer(input('Enter the name for human player #{}'.format(i+1))) for i in range(num_human)]

num_computer = getNumberBetween('How many computer players?', 0, 10)

if num_computer >= 1:
    difficulty = getNumberBetween('What difficulty for the computers? (1-10)', 1, 10)

computer_players = [WOFComputerPlayer('Computer {}'.format(i+1), difficulty) for i in range(num_computer)]

players = human_players + computer_players

if len(players) == 0:
    print('We need players to play!')
    raise Exception('Not enough players')

category, phrase = getRandomCategoryAndPhrase()
guessed = []

playerIndex = 0

winner = False

def requestPlayerMove(player, category, guessed):
    attempts = 0
    while attempts < 5:
        time.sleep(0.1)

        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        if len(move) == 1:
            move = move.upper()
        if move == 'EXIT' or move == 'PASS':
            return move
        elif len(move) == 1: 
            if move not in LETTERS: 
                print('Guesses should be letters. Try again.')
                attempts += 1
                continue
            elif move in guessed: 
                print('{} has already been guessed. Try again.'.format(move))
                attempts += 1
                continue
            elif move in VOWELS and player.prizeMoney < VOWEL_COST:
                print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                attempts += 1
                continue
            else:
                return move
        else:
            return move
    return 'PASS'


while True:
    player = players[playerIndex]
    wheelPrize = spinWheel()

    print('')
    print('-'*15)
    print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
    print('')
    print('{} spins...'.format(player.name))
    time.sleep(2)
    print('{}!'.format(wheelPrize['text']))
    time.sleep(1)

    if wheelPrize['type'] == 'bankrupt':
        player.goBankrupt()
    elif wheelPrize['type'] == 'loseturn':
        pass
    elif wheelPrize['type'] == 'cash':
        move = requestPlayerMove(player, category, guessed)
        if move == 'EXIT': 
            print('Until next time!')
            break
        elif move == 'PASS': 
            print('{} passes'.format(player.name))
        elif len(move) == 1:
            guessed.append(move)

            print('{} guesses "{}"'.format(player.name, move))

            if move in VOWELS:
                player.prizeMoney -= VOWEL_COST

            count = phrase.count(move)
            if count > 0:
                if count == 1:
                    print("There is one {}".format(move))
                else:
                    print("There are {} {}'s".format(count, move))

                player.addMoney(count * wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                if obscurePhrase(phrase, guessed) == phrase:
                    winner = player
                    break

                continue 

            elif count == 0:
                print("There is no {}".format(move))
        else:
            if move == phrase:
                winner = player

                player.addMoney(wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                break
            else:
                print('{} was not the phrase'.format(move))

    playerIndex = (playerIndex + 1) % len(players)

if winner:
    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.prizes:
            print('    - {}'.format(prize))
else:
    print('Nobody won. The phrase was {}'.format(phrase))
