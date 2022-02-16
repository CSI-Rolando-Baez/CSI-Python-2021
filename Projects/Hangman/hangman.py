import random

def get_word():
  possibleWords = ['ponce', 'guaynabo', 'fajardo', 'bayamon', 'carolina', 'cabo rojo', 'san juan', 'aguadilla', 'moca', 'lajas', 'arecibo', 'orocovis', 'cayey', 'corozal', 'salinas', 'arroyo', 'yabucoa', 'humacao', 'ceiba', 'luquillo']
  hangmanWord = random.choice(possibleWords)

get_word()

def pick_letter():
  while True:
    chosenLetter = input("Insert a letter... ")
    # [chosenLetter.lower] will automatically turn the response given into lower case
    if chosenLetter.lower() not in ( 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'):
      print ("not a valid answer")
    #unfinshed statement
      pick_letter()

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
