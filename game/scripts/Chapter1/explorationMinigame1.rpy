# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bgLab = "Backgrounds/LabNoItems.png"
image vignette = "backgrounds/vignette.png"

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
    global obj5Clicked
    obj5Clicked = False

init:
    transform showChemical:
        #replace x and y pos here
        pos (446, 290)
        zoom .13

    transform showComputer:
        #replace x and y pos here
        pos (0,150)
        zoom .98

    transform showPoster:
        #replace x and y pos here
         xpos 1152
         ypos 61
         zoom .0725

    transform showTemperature:
        #replace x and y pos here
        pos (974, 133)
        zoom .06

    transform showFolders:
        align (0.5,0.5)
        pos (1027, 644)
        zoom .33

    transform customZoomQuarter :
        zoom 0.25

    transform customZoomThird :
        zoom 0.33


# Clickable objects
screen objects():
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
        imagebutton:
             auto "ConfirmedAndUnconfirmedFolders_%s.png"
             focus_mask True
             at showFolders
             action [SetVariable("obj5Clicked",True),Call("describeFolders"),Return()]

screen objOverlay():
    fixed:
        add "computer_idle.png" at showComputer
        add "chemicals_idle.png" at showChemical
        add "poster_idle.png" at showPoster
        add "temperature_idle.png" at showTemperature
        add "ConfirmedAndUnconfirmedFolders_idle.png" at showFolders

screen showObj(obj):
    fixed:
        window id "window"
        add "computer_idle.png" at showComputer
        add "chemicals_idle.png" at showChemical
        add "poster_idle.png" at showPoster
        add "temperature_idle.png" at showTemperature

        showif(obj == "computer"):
            add "gui/textbox.png" xcenter 640 ycenter 250 size(360,360)
            add "computer_idle.png" xcenter 640 ycenter 250 zoom.5
        elif(obj == "chemicals"):
            add "gui/textbox.png" xcenter 640 ycenter 250 size(360,360)
            add "chemicals_idle.png" xcenter 640 ycenter 250 zoom.25
        elif(obj == "folders"):
            add "gui/textbox.png" xcenter 640 ycenter 250 size(360,360)
            add "ConfirmedAndUnconfirmedFolders_idle.png" xcenter 640 ycenter 250 zoom.5
        else:
            add "gui/textbox.png" xcenter 640 ycenter 250 size(360,360)
            add "temperature_idle.png" xcenter 640 ycenter 250 zoom.25

screen poster:
    modal False
    zorder 99
    fixed:
        imagemap:
            ground At("Poster_filled.png",zoom(.2))
            idle At("Poster.png",zoom(.2))
            hover At("Poster_highlighted.png",zoom(.2))
            xcenter 640 ycenter 250
            showif(not selectedOpt1):
                hotspot (175/5, 1644/5, 187/5, 35) action Jump("one")
            showif(not selectedOpt2):
                hotspot (400/5, 1644/5, 187/5, 35) action Jump("two")
            showif(not selectedOpt3):
                hotspot (650/5, 1644/5, 187/5, 35) action Jump("three")
            showif(not selectedOpt4):
                hotspot (875/5, 1644/5, 187/5, 35) action Jump("four")
            showif(not selectedOpt5):
                hotspot (1125/5, 1644/5, 187/5, 35) action Jump("five")

style example:
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

label describeComputer:
    play sound "audio/SFX/typing.wav"
    show screen showObj("computer")
    player "There's a computer with a weird graph on it."
    player "It looks like on one axis, it shows days, and on the the other axis, I see the words 'confirmed cases.'"
    Scientist  "I see you’ve found an example of some of our ratio data."
    Scientist "As you can see, unlike interval data for ratio data zero means there are no cases."
    hide screen showObj
    if (not (obj1Clicked and obj2Clicked and obj3Clicked and obj4Clicked and obj5Clicked)):
        show screen objOverlay
        jump pick
    return

label describeChemical:
    play sound "audio/SFX/bubble.wav"
    show screen showObj("chemicals")
    player "Woah! Pretty colors! 'Toxic', 'Poison', 'Explosive'?"
    Scientist "Oh, the names on those jars are nominal data and describe what type of content they hold."
    Scientist "For instance, one of these jars contains POISON."
    Scientist "Don’t touch it by the way."
    player "Sorry..."
    hide screen showObj
    if (not (obj1Clicked and obj2Clicked and obj3Clicked and obj4Clicked and obj5Clicked)):
        show screen objOverlay
        jump pick
    return

label describePoster:
    show screen objOverlay
    Friend "[player]! Look! That sign is so cuuuuute!"
    "I turned around to see what she was pointing at and was in awe."
    $selectedOpt1 = False
    $selectedOpt2 = False
    $selectedOpt3 = False
    $selectedOpt4 = False
    $selectedOpt5 = False
    $interacting = True
    show screen poster
    Friend "'On a scale from 1 to 5, how satisfied are you with your visit to the lab...'"
    if (not (obj1Clicked and obj2Clicked and obj3Clicked and obj4Clicked and obj5Clicked)):
        show screen objOverlay
        jump pick
    return

label one:
        $selectedOpt1 = True
        $selectedOpt2 = False
        $selectedOpt3 = False
        $selectedOpt4 = False
        $selectedOpt5 = False
        $interacting = False
        show screen poster
        jump done

label two:
        $selectedOpt1 = False
        $selectedOpt2 = True
        $selectedOpt3 = False
        $selectedOpt4 = False
        $selectedOpt5 = False
        $interacting = False
        show screen poster
        jump done

label three:
        $selectedOpt1 = False
        $selectedOpt2 = False
        $selectedOpt3 = True
        $selectedOpt4 = False
        $selectedOpt5 = False
        $interacting = False
        show screen poster
        jump done

label four:
        $selectedOpt1 = False
        $selectedOpt2 = False
        $selectedOpt3 = False
        $selectedOpt4 = True
        $selectedOpt5 = False
        $interacting = False
        show screen poster
        jump done

label five:
        $selectedOpt1 = False
        $selectedOpt2 = False
        $selectedOpt3 = False
        $selectedOpt4 = False
        $selectedOpt5 = True
        $interacting = False
        show screen poster
        jump done

label done:
    Friend "Oh Oh! I know what this is. Its ordinary data is right."
    Scientist "Close. It's ordinal data."
    Friend "Dang it."
    hide screen poster
    if (not (obj1Clicked and obj2Clicked and obj3Clicked and obj4Clicked and obj5Clicked)):
        show screen objOverlay
        jump pick

label describeThermometer:
    show screen showObj("thermometer")
    Friend "Oooooh! What is this?"
    Scientist "That, my child, is a thermometer."
    Scientist "It is a device that measures degrees of Farenheit and Celsius. This is a fine example of interval data. "
    Scientist "Unlike ratio data, the zero here doesn't mean no temperature."
    hide screen showObj
    if (not (obj1Clicked and obj2Clicked and obj3Clicked and obj4Clicked and obj5Clicked)):
        show screen objOverlay
        jump pick
    return

label describeFolders:
    show screen showObj("folders")
    player "'confirmed' and 'unconfirmed?'"
    Scientist "This is an example of binary data."
    Scientist "Here we sort patient reports, into two possibilities, a confirmed case or an unconfirmed case."
    Scientist "We either have enough facts to say that a case is confirmed otherwise it's unconfirmed. There are no maybes. "
    hide screen showObj
    if (not (obj1Clicked and obj2Clicked and obj3Clicked and obj4Clicked and obj5Clicked)):
        show screen objOverlay
        jump pick
    return

label flashbackMinigame:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #swap background below
    scene bgLab
    show screen objOverlay
    $renpy.music.set_volume(0.05, delay=0, channel='music')
    $renpy.music.set_volume(0.5, delay=0, channel='ambient')
    play ambient "audio/SFX/kids.mp3" fadein 3.0

    player "Wow! Look at all of this! It’s amazing!"
    Friend "I know! Isn’t this cool?!"

    Teacher "{size=+10}Settle down, children!{/size}"

    stop ambient fadeout 2.0
    Teacher "I know science is intriguing, but be careful you don’t touch anything."

    "A mysterious man in white lab coat steps in from the back of the room."
    show Scientist Shadow onlayer screens
    Scientist "Now, now. It’s fine."
    Scientist "I’m just so happy to see a bunch of future scientists right before my eyes."
    Teacher "As you wish, Sir."

    Teacher "{size=+10}Ahem.{/size}"
    Teacher "Everyone, let’s sit down for our lesson."
    play music "audio/Music/Out of my dreams Nes.ogg"

    Scientist "Data is how we describe things."
    Scientist "It can be as simple as binary data like, are you guys in a lab right now? This type of data only has two possible responses."
    Scientist "Other data can have multiple possibilities. For instance..."
    "I see him pointing at me."
    Scientist "What's your name?"

    python:
        playerName = renpy.input("Enter name here:")
        player_name = playerName.strip()
        if player_name == "":
            playerName = "Riley"


    player "My name is [player]."
    Scientist "Nice to meet you, [player]. Your name is an example of nominal data."
    Scientist "Nominal means name. Nominal data are usually categories or descriptions. "

    Scientist "Other types of data include ratio and interval data. Both of these data types involve numbers."
    Scientist "For interval data, zero can be set to mean whatever we want. While in ratio data, zero always means none."
    Scientist "How many girls are there in the room?"

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

    Scientist "The number of boys and girls in this room is an example of ratio data."
    Scientist "There could be zero boys in the room, which would mean there are no boys in the room."

    Scientist "Interval data, on the other hand, would be the temperature in the room. If we are measuring temperature in celsius 0 is set to temperature that water freezes."
    Scientist "Finally there's ordinal data, or things we can put in order and rank..."

    Friend "{size=12}This is so boring. So [player] I heard you had crush on someone in clase.{/size}"

    Scientist "..."

    Scientist "And for Ordinal Data 1 could be you are totally bored by my lecture, and 5 could mean you’re excited to listen."

    Friend "{size=12} That was oddly specific do you think he heard us? {/size}"

    menu:
        "Not now, [Friend].":
            "{size=12}Not now, [Friend]. I'm trying to learn.{/size}"
        "I don't think so?":
            "{size=12}Nah. I think we're in the clear.{/size}"
        "I think he did.":
            "{size=12}I think he did.{/size}"

    Scientist "Here's an example. On a scale from 1 to 3 on how well I heard you with being I didn’t hear you well and three I heard everything you said."
    Scientist "If I replied to this scale with a two, you would know that I heard more than nothing and less than everything."
    Scientist "But you wouldn’t be able to tell exactly how much more than nothing, I heard. (*wink*)"

    define Class = Character("The Class")
    stop music
    play sound "audio/SFX/oooh.wav"
    Class "{size=+10} Haha! You're in trouuuuuuuble! {/size}"
    Friend "He totally heard us."
    player "(*blush*) {size=+10}Duh!{/size}"
    Scientist "Thank you, feel free to look at things and ask questions"
    hide Scientist Shadow onlayer screens

    play music "audio/Music/Welcome.mp3"
    $firstTime = True
    label pick:
        hide screen objOverlay
        call screen objects
    show screen objOverlay

    if (firstTime is True):
        stop music
        "[Friend] dashes around the room. She bumps into a shelf with various chemicals, and a labelled jar tumbles off the shelf and is about to hit you."
        Teacher "{size=+10}Watch out [player]! {/size}"
        play sound "audio/SFX/glass_smash.wav"
        $firstTime = False
    return
