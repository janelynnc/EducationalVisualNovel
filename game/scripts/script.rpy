# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Scientist = Character("Scientist")
define LI = Character("LOVE_INTEREST")
define Rival = Character("Rival")
define Friend = Character("Cutiepie")
define playerName = "Me"
define player = DynamicCharacter("playerName")

define Teacher = Character("Teacher")
define male_pronouns = ['he','him','his','his','himself']
define female_pronouns = ['she','her','her','hers','herself']
define nonbinary_pronouns = ['they','them','their','theirs','themself']
define player_keys = ['they(p)','them(p)','their(p)','theirs(p)','themself(p)']
define love_interest_keys = ['(they(li)','them(li)','their(li)','theirs(li)','themself(li)']
define gender_lookup = {}
# The game starts here.

init python:
    def replace_text(what):
        for key, value in gender_lookup.items():
            what = what.replace( "{0}".format(key), value)
            what = what.replace( "{0}".format(key.capitalize()), value.capitalize())
        return what
    config.replace_text = replace_text
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    jump introSceneChapter


    # This ends the game.

    return
