# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label introSceneChapter:

    call flashbackMinigame

    call discoverTheLab

    # jump applyingForTheLab

    call partnerMinigame

    call sortingGame1
    # This ends the game.


    # return

label discoverTheLab:
    player "Molly? Molly?!"
    player "AHHHHHH"
    "You wake up, faceplanted on the dusty floor. "
    player "Molly? Are you okay?"
    Friend "Yeah."
    Friend "Was it about that again?"
    player "Huh? Oh. No."
    Friend "Then what?"
    player "Remember the field trip we took to SC**NCE LAB in the third grade?"
    Friend "I just remember that the teacher was HOT"
    player "OMIGOD [Friend]"
    player "...and that was the day you decided to pursue SCIENCE for the rest of your life."
    player "Yeah."
    Friend "It’s a shame you didn’t get to finish your degree in SCIENCE"
    "What a dream. It’s been five years since modern science has been erased from our lives."
    "Extra! Extra! Read all about it!"
    "Oh, it’s the paperboy."
    player "Hey, Molly. Can you get the newspaper? I’m gonna make food."
    Friend "Sure"
    "You open the door to find the local paperboy throwing newpapers at people’s doorsteps."
    "A new lab is opening up, and they wanna create medicine!"
    "Medicine?"
    "Yup! I hear they’re looking the best of the best!"
    player "Oh"
    "I hear that if you get in, you get the best benefits."
    "best benefits, huh?"

    return
label applyingForTheLab:
