# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image backgroundImg = "backgroundFiller.png"
image chemicals = "chemicals_idle.png"
image computer = "computer_idle.png"
image poster = "poster_idle.png"
image temperature = "temperature_idle.png"
# The game starts here.

init python:
    global obj1Clicked
    obj1Clicked = False
    global obj2Clicked
    obj2Clicked = False
    global obj3Clicked
    obj3Clicked = False
    global obj4Clicked
    obj4Clicked = False

init:
    transform showChemical:
        xcenter 400
        ycenter 320
        zoom .25

    transform showComputer:
        xcenter 500
        ycenter 120
        zoom .25
    transform showPoster:
         xcenter 1000
         ycenter 320
         zoom .25
    transform showTemperature:
        xcenter 700
        ycenter 400
        zoom .25


    transform customZoomQuarter :
        zoom 0.25

    transform customZoomThird :
        zoom 0.33

# Clickable objects
screen objects:
    fixed:
        imagebutton:
             auto "chemicals_%s.png"
             #Makes transparent parts unclickable
             focus_mask True
             at showChemical
             action [SetVariable("obj1Clicked",True),Call("describeChemical"),Return()]
        imagebutton:
             auto "computer_%s.png"
             #Makes transparent parts unclickable
             focus_mask True
             at showComputer
             action [SetVariable("obj2Clicked",True),Call("describeComputer"),Return()]
        imagebutton:
             auto "poster_%s.png"
             #Makes transparent parts unclickable
             focus_mask True
             at showPoster
             action [SetVariable("obj3Clicked",True),Call("describePoster"),Return()]
        imagebutton:
             auto "temperature_%s.png"
             #Makes transparent parts unclickable
             focus_mask True
             at showTemperature
             action [SetVariable("obj4Clicked",True),Call("describeThermometer"),Return()]

label describeComputer:
    show computer at showComputer
    "You look at the computer screen and see a graph. On one axis you see days, on the the other axis you see the word confirmed cases. "
    Scientist  "I see you’ve found an example of some of our ratio data. As you can see, with ratio data we can see how quickly the number of cases are growing."
    return

label describeChemical:
    show chemicals at showChemical
    "You look intensely at jars filled with various chemicals labeled poisonous, toxic and explosive."
    "Oh the names on those jars are nominal data and describe what type of content they hold. Don’t touch it by the way."
    return

label describePoster:
    show poster at showPoster
    "[Friend] points at a poster, and reads out a question on scale from 1 to 5 how satisfied are you with your visit to the lab."
    Friend "Oh Oh! I know what this is. Its ordinary data is right."
    Scientist "Close its ordinal data"
    return

label describeThermometer:
    show temperature at showTemperature
    Friend "Oh! What is this?"
    Scientist "That, my child, is a thermometer. It is a device that measures degrees of Farenheit and Celsius. This is a fine example of interval data. "
    return

label flashbackMinigame:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene backgroundImg

    player "Wow! Look at all of this! It’s amazing!"
    "I know! Isn’t this cool?! yelled another student."

    Teacher "Settle down, children. I know science is intriguing, but be careful you don’t touch anything."

    Scientist "Now, now. It’s fine. I’m just so happy to see a bunch of future scientists right before my eyes."

    Teacher "As you wish, Sir."

    Teacher "Ahem."
    Teacher "Everyone, let’s sit down for our lesson."

    Scientist "Data is how we describe things. It can be as simple as binary data like, are you guys in a lab right now? This type of data only has two possible responses. Other data can have multiple possibilities (he points towards you), What’s your name"

    python:
        playerName = renpy.input("Enter name here")
        player_name = playerName.strip()
        if player_name == "":
            playerName = "Riley"



    Scientist "Nice to meet you [player] . Your name is an example of nominal data. Nominal means name. Nominal data are usually categories or descriptions. "

    Scientist "Other types of data include ratio and interval data. Both of these data types involve numbers. For interval data, zero can be set to mean whatever we want. While in ratio data, zero always means none. How many girls are there in the room?"

    $male = False
    $female = False
    menu:
        "Raise your hand":
            $female = True
            pass
        "Don’t raise your hand":
            pass

    "How many boys are there in the room?"

    menu:
        "Raise your hand":
            $male = True
            pass
        "Don’t raise your hand":
            pass

    python:
        if(male is female):
            store.gender_lookup = dict(zip(player_keys,nonbinary_pronouns))
        elif(male is True):
            store.gender_lookup = dict(zip(player_keys,male_pronouns))
        else:
            store.gender_lookup = dict(zip(player_keys,female_pronouns))

    "The number of boys and girls in this room is an example of ratio data. There could be zero boys in the room which would mean there are no boys in the room."

    "Interval data on the other hand would be the temperature in the room. If we are measuring temperature in celsius 0 is set to temperature that water freezes. Finally theres ordinal data, or things we can put in order and rank"


    Friend "*whispers* This is so boring, I wish he’d stop talking and let us play with all the stuff in the room"

    "The Scientist glances at you and [Friend]"

    Scientist "And for Ordinal Data 1 could be you are totally bored by my lecture, and 5 could mean you’re excited to listen."

    Friend "That was oddly specific do you think he heard us?"

    menu:
        "Not now [Friend]":
            "Not now [Friend]"
        "Shh":
            "Shh"
        "I think he did":
            "I think he did"

    Scientist "Or a scale from 1 to 3 on how well I heard you. One being I didn’t hear you well and three I heard everything you said. If I replied to this scale with a two, you would know that I heard more than nothing and less than everything. But you wouldn’t be able to tell exactly how much more than nothing, I heard. (*wink*)"

    $Class = Character("The Class")
    Class "oooooh"

    Scientist "Thank you, feel free to look at things and ask questions"


    label pick:
        call screen objects

    if (not (obj1Clicked and obj2Clicked and obj3Clicked and obj4Clicked)):
        jump pick

    "Another student points to two piles of papers one marked confirmed and the other marked unconfirmed."

    Scientist "This is an example of binary data. Here we sort patient reports, into two possibilities,
    a confirmed case or an unconfirmed case. We either have enough facts to say that a case is
    confirmed otherwise its unconfirmed. There are no maybes. "

    "[Friend] dashes around the room. She bumps into a shelf with various chemicals, and a jar labelled tumbles off the shelf and is about to hit you."

    Teacher "Watch out [player]!"

    return
