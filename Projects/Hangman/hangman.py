import random

steps = ["""
 
      ___________
     [          []
     ]          []
                []
                []
                []
                []
                []
    ==============
""",
"""

      ___________
     [          []
     ]          []           
    / \         []
    \_/         []
                []
                []
                []
                []
    ==============

""",
"""
      ___________
     [          []
     ]          []           
    / \         []
    \_/         []
    | |         []
    |_|         []
                []
                []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
    \_/ /       []
    | |/        []
    |_|         []
                []
                []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
  \ \_/ /       []
   \| |/        []
    |_|         []
                []
                []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
  \ \_/ /       []
   \| |/        []
    |_|         []
      \         []
       \        []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
  \ \_/ /       []
   \| |/        []
    |_|         []
    / \         []
   /   \        []
    ==============

"""
]
def get_word():
  possibleWords = ['ponce', 'guaynabo', 'fajardo', 'bayamon', 'carolina', 'cabo rojo', 'san juan', 'aguadilla', 'moca', 'lajas', 'arecibo', 'orocovis', 'cayey', 'corozal', 'salinas', 'arroyo', 'yabucoa', 'humacao', 'ceiba', 'luquillo']
  hangmanWord = random.choice(possibleWords)
  return hangmanWord

def used_letters():
  lettersList = []
  maxTries = 15
  while len(lettersList) < maxTries:
    lettersList.append

def print_word(hangmanWord):
  blank_word = len(hangmanWord) * '_'
  word = print(blank_word)
  return word

def get_input():
  while True:
    letter = input("Choose letter")
    if letter.isalpha():
      print("Choose a valid character (A letter from a to z)")
      continue
      
    return letter
 
def word_check(letter, hangmanWord, lettersList):
      if letter not in hangmanWord:
        print('Incorrect guess...')
        lettersList.append(letter)
        print (steps[0])
        print(lettersList)
      if letter in hangmanWord:
        print('Correct Guess!')
        lettersList.append(letter)
        print(lettersList)

def fill_blanks(letter, hangmanWord, lettersList):
  temp = ""
  for letter in hangmanWord:
    if(letter in lettersList):
      temp = temp + letter
    else:
      temp = temp + '_'

get_word()

print_word('hangmanWord')

get_input()

used_letters()

word_check()

fill_blanks()


    
