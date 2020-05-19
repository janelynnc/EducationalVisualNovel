# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Scientist = Character("Dr. Dan")
define LI = Character("Toby")
define Rival = Character("Brianna")
define Friend = Character("Molly")
define playerName = "Me"
define player = DynamicCharacter("playerName")
define os = Character("Other Student")

define Teacher = Character("Teacher")
define male_pronouns = ['he','him','his','his','himself']
define female_pronouns = ['she','her','her','hers','herself']
define nonbinary_pronouns = ['they','them','their','theirs','themself']
define player_keys = ['they(p)','them(p)','their(p)','theirs(p)','themself(p)']
define love_interest_keys = ['they(li)','them(li)','their(li)','theirs(li)','themself(li)']
define gender_lookup = {}
define li_gender = 'male'
# The game starts here.
init:
    transform zoom(size):
        zoom size
    transform pivotCenter(x,y):
        anchor(x,y)
    transform pos(x,y):
        xcenter x
        ycenter y

    image LI = At(ConditionSwitch("li_gender == 'male' ", "Characters/TobyMale.png","li_gender == 'female' ", "Characters/TobyFemale.png"),zoom(.65))

    image Friend = At("Characters/BestFriend.png",zoom(.65))
    image Friend Shocked = At("Characters/BestFriendShocked.png",zoom(.65))
    image Friend Sad = At("Characters/BestFriendSad.png",zoom(.65))
    image Friend Wink = At("Characters/BestFriendWink.png",zoom(.65))
    image Scientist = At("Characters/Mentor.png",zoom(.65))
    image Scientist Shadow = At("Characters/MentorShadow.png",zoom(.65))
    image Rival = At("Characters/Rival.png",zoom(.65))
    image Map = At("Map.png")
    image Notebook = At("Notebook.png")
init python:
    def replace_text(what):
        for key, value in gender_lookup.items():
            what = what.replace( "{0}".format(key), value)
            what = what.replace( "{0}".format(key.capitalize()), value.capitalize())
        return what
    config.replace_text = replace_text
    interacting = False
    renpy.music.register_channel("ambient","sfx",True)
    config.debug_sound = True
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    jump introSceneChapter


    # This ends the game.

    return
