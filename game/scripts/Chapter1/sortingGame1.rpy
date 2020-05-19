# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.




# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image backgroundImg = "Backgrounds/abandoned_lab.png"
image nominal = At("SortingObjects/nominalfolder.png",zoom(.8))
image binary = At("SortingObjects/binaryfolder.png",zoom(.8))
image ordinal = At("SortingObjects/ordinalFolder.png",zoom(.8))
image ratio = At("SortingObjects/ratioFolder.png",zoom(.8))
image interval = At("SortingObjects/intervalFolder.png",zoom(.8))

#npc objects to sort
image placeholder = "computer_idle.png"
image petriDish = At("SortingObjects/PertiDish.png",zoom(.5),pivotCenter(0.5,.85))
image microscopeSlides = At("SortingObjects/MicroscopeSlidesDeck2.png",zoom(.5),pivotCenter(0.5,0.5))
image beakers = At("SortingObjects/beakers.png",zoom(.25),pivotCenter(0.5,0))
label question(obj,category):
    scene backgroundImg
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
    LI "I do not think [obj] belongs in [category]"
    menu:
        "Agree":
            "Let me try again"
            $sortingGame1.retry = True
        "Disagree":
            LI "Hm, I think you might be on to something"
            $sortingGame1.retry = False
    return

label wrongAnswer(category):
    scene backgroundImg
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
    show backgroundImg
    show Scientist
    Scientist "Hold on this does not belong in [category]"
    return

init python in sortingGame1:
    player_targets = [
    "age groups",
    "stop watch",
    "red blood cells"]
    player_imgs = [
    "SortingObjects/Torn Page.png",
    "SortingObjects/DirtyTimer.png",
    "SortingObjects/RedBloodCellsPage.png"]
    descriptions = [
    "A torn page of a lab report with death rates categorized by age ranges",
    "A broken stop watch. Looks like what ever they were timing only to 3 seconds",
    "Looks like a test report on a patient's red blood cell concentration"]
    img_sizes = [.5,.40,.20,.20,.20]
    nominal = {}
    interval = {"stop watch"}
    ratio = {"red blood cells"}
    binary = {}
    ordinal = {"age groups"}
    categories = {'nominal':nominal,'interval':interval,'ratio':ratio,'binary':binary,'ordinal':ordinal}
    player_correct = {'nominal':'Yep looks {color=#259ce6}nominal{/color} to me','interval': 'good job!', 'ratio': 'looks good to me', 'binary': " Between correct and incorrect. I would say correct", 'ordinal': "I see you got everything in order. Get it order and ordinal?"}
    objNum = 0
    score = 0
    matching = False;

    def shouldReset(drop_obj,drag_obj):
        if len(drag_obj) == 0:
            return
        renpy.hide_screen("description")
        matching = drag_obj[0].drag_name in categories[drop_obj.drag_name]
        category = drop_obj.drag_name
        if(renpy.random.randint(1,3)<2):
            if(matching):
                response = player_correct[drop_obj.drag_name]
                renpy.show_screen("bubbleSay", response,True,drop_obj.drag_name,matching)
            else:
                renpy.call_in_new_context("wrongAnswer",drop_obj.drag_name)
                renpy.jump("next_try")
        else:
            renpy.call_in_new_context("question",drag_obj[0].drag_name,drop_obj.drag_name)
            if(not retry and not matching):
                renpy.call_in_new_context("wrongAnswer",drop_obj.drag_name)
                renpy.jump("next_try")
            elif(retry):
                return
            else:
                renpy.jump("next_try")

        renpy.restart_interaction()
    def shrink(dragged_objs):
        if len(dragged_objs) == 0:
            return
        dragged_objs[0].w = dragged_objs[0].w/2
        dragged_objs[0].h = dragged_objs[0].h/2
        renpy.force_full_redraw()

screen bubbleSay(what,ctc,category,matching):
    modal True
    $clickToContinue = ctc
    window:
        id "window"
        text what:
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

    showif clickToContinue:
        button:
            xfill True
            yfill True
            action [Hide("bubbleSay"),Return(True)]
    else:
        vbox:
            xpos 600 ypos 600
            textbutton "Let me try again." action [Hide("bubbleSay")]
            textbutton "Disagree" action[Hide("bubbleSay"),If(matching,false=Function(renpy.call_in_new_context,"wrongAnswer",category)),Return(True)]

screen description(what):
    zorder 10
    window:
        id "window"
        text what:
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos


screen sortingScreen(n):

    modal True
    draggroup:
        # what you wanna drag
        drag:
            as target
            drag_name sortingGame1.player_targets[n]
            idle_child At(sortingGame1.player_imgs[n],zoom(sortingGame1.img_sizes[n]))
            hover_child At(sortingGame1.player_imgs[n],zoom(sortingGame1.img_sizes[n]))
            selected_hover_child At(sortingGame1.player_imgs[n],zoom(sortingGame1.img_sizes[n]/2))
            dragged
            droppable False
            xcenter 640 ycenter 400
        # what you wanna drog item to
        drag:
            drag_name "nominal"
            child "SortingObjects/nominalfolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 50 ypos 30

        drag:
            drag_name "binary"
            child "SortingObjects/binaryfolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 300 ypos 30

        drag:
            drag_name "ordinal"
            child "SortingObjects/ordinalfolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 550 ypos 30

        drag:
            drag_name "ratio"
            child "SortingObjects/ratiofolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 750 ypos 30

        drag:
            drag_name "interval"
            child "SortingObjects/intervalfolder.png"
            draggable False
            dropped sortingGame1.shouldReset
            xpos 1000 ypos 30

transform nominalFolder(timing = 0):
    xpos 50 ypos 100
transform binaryFolder(timing = 0):
    xpos 300 ypos 100
transform ordinalFolder(timing = 0):
    xpos 550 ypos 100
transform ratioFolder(timing = 0):
    xpos 800 ypos 100
transform intervalFolder(timing = 0):
    xpos 1050 ypos 100



label sortingGame1:
    scene outside
    play music "audio/Music/The-Secret-Lab.mp3"
    "Our little group decided to take a trip to an abandoned lab. There are signs scattered everywhere that literally tell us not to enter. "
    player "{size=+10}'DANGER?' 'MANDATORY QUARANTINE ZONE?' {/size}"

    LI "[Scientist], you sure this is safe? What are we doing here anyways? "

    show Friend
    Friend "{size=12}*whispers* Do you think he’s here to murder us and harvest our organs?{/size}"

    player "{size=12}Yeah [Friend], he’s totally going to do that.{/size}"

    show LI at right with moveinright
    show Friend at left with move
    LI "{size=12}Afterwards, he is gonna turn them into soup and serve them to the local children.{/size}"

    Friend "{size=12}Ew. I swear, you two can be so messed up sometimes.{/size}"

    hide Friend with moveoutleft

    show Scientist at left with moveinleft
    Scientist "Are you wearing a mask and eye protection?"

    LI "Yeah"

    Scientist "Then it should be fine. We’re here to collect some evidence and data."
    Scientist "They used to conduct animal studies here and observe the subjects for reactions. We might be able to find something useful."

    player "And how do you know about this place?"

    Scientist "I'm afraid that's classified"
    Scientist "Anyways, we’re here. Everyone pair up and make sure you’re wearing gloves. All of you are going to be sifting through items and placing them in the correct category."
    scene lab
    hide Scientist
    show LI at center with move
    "I will choose to partner with [LI]."

    player "Hey [LI]! Are you ready to do this?"

    LI "Only if you’re there to help guide me."

    player "If I didn’t know any better, I’d assume you were trying to impress me again."

    hide LI
    show Scientist at left
    Scientist "Kids get to work! This data isn’t going to collect itself."
    hide Scientist
    show Friend Wink at right
    Friend "Enjoy your date [player]!"
    player "It's not a date!"
    hide Friend

    show LI
    LI "I guess I’ll go first."
    hide LI

    label npc_sorting:
        show nominal at nominalFolder
        show binary at binaryFolder
        show ratio at ratioFolder
        show ordinal at ordinalFolder
        show interval at intervalFolder
        show petriDish at center

        LI "Hm... I think this is {color=#259ce6}nominal{/color} data. There is words on these dishes, and from what I remember, words mean {color=#259ce6}nominal{/color}."

        menu:
            "I agree. {color=#259ce6}nominal{/color} data usually involves qualitative data.":
                player "Yeah I agree {color=#259ce6}nominal{/color} data usually involves qualitative data like names or categories"
                show petriDish at nominalFolder with MoveTransition(3.0)
                pause(3.0)
            "It could also be ordinal":
                LI "Why ordinal?"
                player "I am glad you asked."
                player "Well, the notebook said "
                menu:
                    "Ordinal data can be put in order":
                        player "Ordinal data is data that has a an order. Like the rating you gave on how great [Friend] and my explantion of ordinal was."
                        LI "I was not sucking up, I really thought you did a good job explaining it. But did not that rating have a number. I am not seeing a number here."
                        menu:
                            "You are right, there should be a number":
                                player "You are right there should be a number for ordinal data."
                                LI "I will go with my hunch then."
                                show petriDish at nominalFolder with MoveTransition(3.0)
                                pause(3.0)
                            "Ordinal data does not always need a number":
                                player "Ordinal data does not always need a number"
                                player "For example, I can construct a scale with three values: hate, indifferent, and like."
                                LI "So you are measuring how much you like a certain person?"
                                player "Exactly. I would put you in the like category by the way."
                                player "For these dishes I would categorize it as no growth, some growth, and a lot of growth."
                                LI "But could't we get an exact measurement of how much growth is in the petri dish"
                                menu:
                                    "We don't have the equipment":
                                        player "We don't have the equipment"
                                        LI "So ordinal is the best we can do"
                                        show petriDish at ordinalFolder with MoveTransition(3.0)
                                        pause(3.0)
                                    "I guess we can count individual spots it":
                                        LI "What type of data is a count then?"
                                        menu:
                                            "Ratio":
                                                show petriDish at ratioFolder with MoveTransition(3.0)
                                                pause(3.0)
                                            "Interval":
                                                show petriDish at intervalFolder with MoveTransition(3.0)
                                                pause(3.0)
                                            "Binary":
                                                show petriDish at binaryFolder with MoveTransition(3.0)
                                                pause(3.0)
                            "For ordinal data, we assign the numbers ourselves":
                                player "For example, l."
                                LI "Well, what numbers would we assign here"
                                player "Well, we can assign a scale 1 to 5. 1 being no growth and 5 being the petri dish is completely filled."
                                LI "But could't we get an exact measurement of how much growth is in the petri dish?"
                                menu:
                                    "We don't have the equipment":
                                        player "We don't have the equipment."
                                        LI "So ordinal is the best we can do"
                                        show petriDish at ordinalFolder with MoveTransition(3.0)
                                        pause(3.0)
                                    "I guess we can count individual spots it":
                                        LI "What type of data is a count then?"
                                        menu:
                                            "Ratio":
                                                show petriDish at ratioFolder with MoveTransition(3.0)
                                                pause(3.0)
                                            "Interval":
                                                show petriDish at intervalFolder with MoveTransition(3.0)
                                                pause(3.0)
                                            "Binary":
                                                show petriDish at binaryFolder with MoveTransition(3.0)
                                                pause(3.0)
                    "There is a true zero":
                        LI "I am not sure what you mean"
                        player "Well, zero here means theres nothing in the petri dish"
                        LI "I do not think that has anything to do with ordinal data"
                        show petriDish at nominalFolder with MoveTransition(3.0)
                        pause(3.0)
                    "You can calculate an average":
                        player "We could measure the weight of each sample and get an average"
                        LI "That seems like something other than ordinal data if we do that."
                        menu:
                            "Disagree":
                                player "You should be able to calculate the average of ordinal data"
                                show petriDish at ordinalFolder with MoveTransition(3.0)
                                pause(3.0)
                                Scientist "Sorry to interrupt, but that was not true"
                            "Agree":
                                LI "I am going with my original answer then"
                                show petriDish at nominalFolder with MoveTransition(3.0)
                                pause(3.0)
            "It could also be ratio data":
                LI "How so?"
                menu:
                    "We can compare their weights":
                        LI "What about measuring weights makes it a ratio"
                        menu:
                            "Well, we can add or subtract the weights":
                                player "We could subtract two weights to find their difference"
                                LI "I think that applies to interval data too. I think I will go with my initial category"
                                show petriDish at nominalFolder with MoveTransition(3.0)
                                pause(3.0)
                            "We can multiply or divide the weights":
                                player "We could form a ratio by dividing two weights. For example one sample maybe 5 grams and another might be 10 grams."
                                LI "In that case the first sample would be half the weight of the other sample"
                                player "Yeah"
                                show petriDish at ratioFolder with MoveTransition(3.0)
                                pause(3.0)
                            "We can put the samples in order by weight":
                                LI "I think we could do that with ordinal data"
                                show petriDish at ordinalFolder with MoveTransition(3.0)
                                pause(3.0)

        hide petriDish
        LI "Hm looks like a slide deck. I found it near some microscopes looks like these samples are labeled by whether or not they recieved treatment"
        LI "This probably falls under {color=#259ce6}nominal{/color} data"

        show microscopeSlides at center

        menu:
            "What are we measuring?":
                player "What exactly are we measuring that makes it nominal?"
                LI "Well I think we can split it up the samples into two main categories treatment and non-treatment"
                menu:
                    "Then it should be {color=#259ce6}binary{/color}":
                        player "If theres only two categories then should not it fall under {color=#259ce6}binary{/color}?"
                        label slide_deck_binary:
                            LI "I suppose it could be. The one thing that bothers me is that the samples all look completely different."
                            player "What do you mean?"
                            LI "In {color=#259ce6}binary{/color} data should not all the samples in one category look the same."
                            LI "For example, when you flip a coin the result is {color=#259ce6}binary{/color}."
                            LI "You either get heads or tails. And everytime you flip the coin heads and tails look the same"
                            menu:
                                "The samples do not always have look the same":
                                    player "Not always. For example do you like working together as team?"
                                    LI "I do. What about you?"
                                    menu:
                                        "Yes":
                                            player "I think its fun to work with you."
                                        "I do not hate it":
                                            player "Well I do not hate working with you"
                                    player "So we have a sample size of two, and the answers don not quite sound the same."
                                    player "You could still say, they both fall under the yes category"
                                    LI "In that case yeah this should go into {color=#259ce6}binary{/color}"
                                    show microscopeSlides at binaryFolder  with MoveTransition(3.0)
                                    pause(3.0)

                                "I agree but it could be something else":
                                    Scientist "Hold on you two."
                                    Scientist "Even if the samples do not look the exact same, we can still collect {color=#259ce6}binary{/color} data."
                                    player "Do you have an example?"
                                    Scientist "Do you think those two *pointing at [Friend] and [Rival] arguing* are getting along?"
                                    player "Nope"
                                    LI "No"
                                    Scientist "So I have a sample size of two. And my two participants are two very different people."
                                    Scientist "The exact answers are slightly different too. However I can still split the the answers into
                                    two unique categories yes and no."
                                    LI "So are these slide decks {color=#259ce6}binary{/color} data?"
                                    Scientist "What do you two think?"
                                    menu:
                                        "Yes":
                                            show microscopeSlides at binaryFolder  with MoveTransition(3.0)
                                            pause(3.0)
                                        "No it is {color=#259ce6}nominal{/color}":
                                            show microscopeSlides at nominalFolder  with MoveTransition(3.0)
                                            pause(3.0)
                    "I see":
                        label slide_deck_nominal:
                            player "I see how this could be {color=#259ce6}nominal{/color}.."
                            player "The data is qualitative and has no order"
                            player "The categories names are not numbers like in ratio and interval."
                            player "They also cannot be put into a natural order like ordinal data"
                            player "What about {color=#259ce6}binary{/color} then?"
                            jump slide_deck_binary

            "I agree":
                jump slide_deck_nominal


        hide microscopeSlides
        "A set of beakers. They come in different sizes. I am not sure how to categorize this one."

        show beakers at center

        menu:
            "Are there any labels?":
                player "Do you see and markings on them or labels"
                LI "Yeah I think under the rust I see ticks and the letters ml."
            "I think these measure volume":
                player "I see some markings on here. It looks like it measure the amount of liquid inside by mk"
                player "I remember when I was little, we used to have measuring cups that had similiar measurement labels"

        LI "So we know that these beakers measured something with numbers"

        LI "Do you think the data is ratio?"

        default pickedRatio = False
        default pickedInterval = False
        default pickedOrdinal = False

        menu beaker_ops:
            "Can we multiply and divide the numbers?":
                player "Remember when we talked about measuring cups being ratios."
                LI "Yeah"
                player "I think it is similiar to the measuring cups. Here, we can divide to voumes to get a ratio"
                player "For example, 200ml divided by 100ml. We get the number 2 which tells us 200ml is exactly double of 100ml"
                LI "So that means the data is ratio"
                show beakers at ratioFolder  with MoveTransition(3.0)
                pause(3.0)
                hide beakers
            "Can we add and subtract the numbers?" if not pickedInterval:
                $pickedInterval = True
                player "I think we can add and subtract these numbers from each other"
                player "So that narrows it down to interval and"
                menu:
                    "ratio":
                        LI "So we are down to interval and ratio"
                    "ordinal":
                        LI "I think you mean ratio"
                jump beaker_ops
            "We can put the number in order" if not pickedOrdinal:
                $pickedOrdinal = True
                player "We can put the beakers in order from highst to lowest amount"
                player "So it could be ordinal data"
                LI "We could also order the numbers for ratio and interval data too."
                jump beaker_ops


        $sortingGame1.objNum = 0

    #call npc_sorting

    label player_sorting:
        show screen description(sortingGame1.descriptions[sortingGame1.objNum])
        call screen sortingScreen(sortingGame1.objNum)
        label next_try:
            hide Scientist
            $sortingGame1.objNum = sortingGame1.objNum + 1
            if(sortingGame1.matching):
                $score = score + 1
            $_return = False
            if(sortingGame1.objNum < len(sortingGame1.player_targets)):
                jump player_sorting

        hide screen sortingScreen

    label doneSorting:
        scene backgroundImg
        show Scientist
        Scientist "Alright! Everyone got what they needed? Let’s head back to the lab. I’ll debrief you on why data is important."
        hide Scientist
        play music "audio/Music/Blue-Ridge_Looping.mp3"
        show LI
        "Glancing at [LI],  I pull [LI] aside."
        player "I am sorry if I was a little pushy today. I hope I did not scare you"
        LI "There is nothing wrong with a little back and forth. Plus, I think its kinda cute"
        "It must be the all the lifting I did, but I am starting to feeling my heart beat faster than usual."
        hide LI
        scene
        show Friend
        Friend "So what does the data show?"
        player "Oh right the data."
        player "Let's take a look."
        player "..."
        Friend "What is it?"
        player "I think you're right. I think I might be in love."
        return
