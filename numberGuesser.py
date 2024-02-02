# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:46:57 2024

@author: Christopher Davis and Alexis Evans
"""

import random
correct = random.randrange(101)
attempts = 0
print(f"""    After all this time...through the countless battles and tribulations, you the mighty warrior that you are make your down the suffocating, stone staircase to the base of the dungeon.
      With a feeling of exhaustion and fatigue flooding your being, your spirits are lifted upon seeing the final treasure awaiting you at the end of these treacherous trials.
      It was a fairly modest chest, make no mistake, but something about it being the object lieing in wait after all this time and the contents within being yours fills you with such pride and bravado that you continue steping forward
      Your steps upon the cobblestone floor radiate such steadfast confidence as nothing...absolutely nothing at all could ruin the moment of opening a chest and taking the plethora of valuable items within.
      You finally reach the chest and place your hands on it with fated breath...only for a magical barrier to emanante resulting in a nasty shock to your hand that stung as if you briefly made contace with the scorching sun.
      Recoiling from the burn, it takes a moment for you to gather yourself. As you wince through the pain it slowly subsides and on the barrier that surrounds that arises the number 7 floating in air.
      A piercing pain rushes to the front of your head as if insanity itself has whispered directly into your ear. With this pain comes a voice with a gravely tone that says 'You who tresspassed and seek to ravage this tomb of mine...I will grant you the treasures that lie here...on one condition...
      If you can guess the number I'm thinking of then I will dispel the barrier and the valuables you seek will be yours! However, if you fail to guess the number within 8 attempts than your soul will be mine...or something. So no pressure.'""")
keepGoing = True
while(keepGoing):
    attempts += 1
    lives = 8
    print(f"The voice in your head ravages your mind as it says 'You have {lives - attempts} guesses remaining.'")
    guess = input("Please guess a number between 0 - 100: ")
    if guess.isdigit():
        intguess = int(guess)

        if attempts >= 7:
            print(f"Dang dude the answer was actually {correct}...It doesn't help you now of course but better luck next time I guess or not as you kinda have to die now...sorry *The whispers of insanity begin to become too much for your feeble mind and just as it feels like the pain has subsided...your head explodes in a beautifully groteque boquet of crimson.*")
            keepGoing = False
        elif intguess > correct:
            print(f"The answer is less than {guess}")
        elif intguess < correct:
            print(f"The answer is more than {guess}")
        elif intguess == correct:
            print(f"Nice job the answer was indeed {correct}! *You feel a wave of relief wash upon your very soul now that the curse has been dispelled from the chest and now with renewed vigor you reach out and opening the lid as a bright light overwhelms your eyes. The brilliant luster dims down until you can finally see the inside of the chest clearly. All there is just a cookie. A cookie long rotten from the corrosion of time, but a cookie that is true to form. Congratulations I guess?")
            keepGoing = False
    else:
        print("What....just so you know that actually counts as a guess.")
        if attempts >= 7:
            print(f"Dang dude the answer was actually {correct}...It doesn't help you now of course but better luck next time I guess or not as you kinda have to die now...sorry *The whispers of insanity begin to become too much for your feeble mind and just as it feels like the pain has subsided...your head explodes in a beautifully groteque boquet of crimson.*")
            keepGoing = False
