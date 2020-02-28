# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.




# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image backgroundImg = "backgroundFiller.png"
image nominal = "SortingObjects/nominalfolder.png"
image binary = "SortingObjects/binaryfolder.png"
image ordinal = "SortingObjects/ordinalFolder.png"
image ratio = "SortingObjects/ratioFolder.png"
image interval = "SortingObjects/intervalFolder.png"

label question(obj,category):
    if(category == "nominal"):
        show nominal
    elif(category == "binary"):
        show binary
    elif(category == "ordinal"):
        show ordinal
    elif(category == "ratio"):
        show ratio
    else:
        show interval
    LI "I don't think [obj] belongs in [category]"
    LI "Insert reason here"
    menu:
        "Agree":
            "Let me try again"
            $sortingGame1.retry = True
        "Disagree":
            $renpy.input("Enter a reason")
            LI "Hm, I think you might be on to something"
            $sortingGame1.retry = False
    return

label wrongAnswer(category):
    if(category == "nominal"):
        show nominal
    elif(category == "binary"):
        show binary
    elif(category == "ordinal"):
        show ordinal
    elif(category == "ratio"):
        show ratio
    else:
        show interval
    show backgroundImgs
    Scientist "Hold on this doesn't belong in [category]"
    return

init python in sortingGame1:
    player_targets = ["chemicals_idle.png","chemicals_idle.png","chemicals_idle.png","chemicals_idle.png","chemicals_idle.png"]
    nominal = {"chemicals_idle.png"}
    interval = {}
    ratio = {}
    binary = {}
    ordinal = {}
    categories = {'nominal':nominal,'interval':interval,'ratio':ratio,'binary':binary,'ordinal':ordinal}
    player_correct = {'nominal':'Yep looks nominal to me','interval': 'good job!', 'ratio': 'looks good to me', 'binary': " Between correct and incorrect. I'd say correct", 'ordinal': "I see you got everything in order. Get it order and ordinal?"}
    objNum = 0
    score = 0

    def shouldReset(drop_obj,drag_obj):
        if len(drag_obj) == 0:
            return

        matching = drag_obj[0].drag_name in categories[drop_obj.drag_name]
        category = drop_obj.drag_name
        if(renpy.random.randint(1,3)<2):
            if(matching):
                response = player_correct[drop_obj.drag_name]
                renpy.show_screen("bubbleSay", response,True,drop_obj.drag_name,matching)
            else:
                renpy.call_in_new_context("wrongAnswer",drop_obj.drag_name)
                renpy.jump("player_sorting")
        else:
            renpy.call_in_new_context("question",drag_obj[0].drag_name,drop_obj.drag_name)
            if(not retry and not matching):
                renpy.call_in_new_context("wrongAnswer",drop_obj.drag_name)
                renpy.jump("player_sorting")
            elif(retry):
                return
            else:
                renpy.jump("player_sorting")

        renpy.restart_interaction()

screen bubbleSay(what,ctc,category,matching):
    modal True
    $clickToContinue = ctc
    window:
        xpos 350 ypos 100
        xmaximum 600 ymaximum 100
        id "window"
        text what

    showif clickToContinue:
        button:
            xfill True
            yfill True
            action [Hide("bubbleSay"),Return(True)]
    else:
        vbox:
            xpos 600 ypos 600
            textbutton "Let me try again" action [Hide("bubbleSay")]
            textbutton "Disagree" action[Hide("bubbleSay"),If(matching,false=Function(renpy.call_in_new_context,"wrongAnswer",category)),Return(True)]


screen sortingScreen(n):
    add "backgroundFiller.png"
    modal True
    draggroup:
        # what you wanna drag
        drag:
            as target
            drag_name sortingGame1.player_targets[n]
            child "UFO.png"
            droppable False
            xpos 200 ypos 600

        # what you wanna drog item to
        drag:
            drag_name "nominal"
            child "SortingObjects/nominalfolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 100 ypos 100

        drag:
            drag_name "binary"
            child "SortingObjects/binaryfolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 300 ypos 100

        drag:
            drag_name "ordinal"
            child "SortingObjects/ordinalfolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 500 ypos 100

        drag:
            drag_name "ratio"
            child "SortingObjects/ratiofolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 700 ypos 100

        drag:
            drag_name "interval"
            child "SortingObjects/intervalfolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 900 ypos 100

label sortingGame1:
    "Your group takes a trip to an abandoned lab. The signs do not enter, danger. Mandatory quarantine zone. "

    LI "So [Scientist], you sure this is safe? What are we doing here anyways? "

    Friend "*whispers* Do you think he’s here to murder us and harvest our organs?"

    menu:
        "Yes":
            "Yeah [Friend],he’s totally going to do that."
        "Maybe":
            "It’s possible"
        "No":
            "Stop being silly [Friend]. What would he even do with our organs"
            Friend "I don’t know, study them?"

    Scientist "Are you wearing a mask and eye protection?"

    LI "Yeah"

    Scientist "Then it should be fine. We’re here to collect some evidence and data. They used to conduct animal studies here and observe the subjects for reactions. We might be able to find something useful"

    player "And how do you know about this place?"

    Scientist "That’s a secret. Anyways we’re here, everyone pair up and make sure you’re wearing gloves. All of you are going to be sifting through items and placing them in the correct folder"

    "You choose to partner with [LI]"

    player "Hey [LI] are you ready to do this?"

    LI "Only if you’re there to help guide me."

    player "If I didn’t know any better, I’d assume you were sucking up to me."

    Scientist "Kids get to work! This data isn’t going to collect itself"

    Friend "And what will you be doing?"

    Scientist "Observing of course."

    LI "I guess I’ll go first."
    #call npc_sorting
    label player_sorting:
        call screen sortingScreen(sortingGame1.objNum)
        if(sortingGame1.objNum < len(sortingGame1.player_targets)-1):
           if(sortingGame1.matching):
               $score = score + 1
           $sortingGame1.objNum = sortingGame1.objNum + 1
           $_return = False
           jump player_sorting
        "Done"
    Scientist "Alright everyone got what they needed? Let’s head back to the lab. I’ll debrief you on why data is important"
