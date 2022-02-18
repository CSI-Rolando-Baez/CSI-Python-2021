import random

def get_word():
  possibleWords = ['ponce', 'guaynabo', 'fajardo', 'bayamon', 'carolina', 'cabo rojo', 'san juan', 'aguadilla', 'moca', 'lajas', 'arecibo', 'orocovis', 'cayey', 'corozal', 'salinas', 'arroyo', 'yabucoa', 'humacao', 'ceiba', 'luquillo']
  hangmanWord = random.choice(possibleWords)

get_word()

def get_input(hangmanWord):
  while True:
    letter = input("Choose letter")
    if letter.isalpha():
      break
    print("Please choose a valid Character")
    if letter in hangmanWord:
    print('Correct Guess!')
    elif letter not in hangmanWord:
    
    
get_input()




def print_word(hangmanWord):
  blank_word = len(hangmanWord) * ['_']
  print(blank_word)

print_word()
    
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
    / \        []
   /   \       []
    ==============

"""
]
print(steps[0])