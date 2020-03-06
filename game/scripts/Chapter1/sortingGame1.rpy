# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.




# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image backgroundImg = "Backgrounds/backgroundFiller.png"
image nominal = "SortingObjects/nominalfolder.png"
image binary = "SortingObjects/binaryfolder.png"
image ordinal = "SortingObjects/ordinalFolder.png"
image ratio = "SortingObjects/ratioFolder.png"
image interval = "SortingObjects/intervalFolder.png"

#npc objects to sort
image placeholder = "computer_idle.png"

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
    player_targets = ["tape measure",
    "age groups",
    "test tubes",
    "scale",
    "stop watch"]
    player_imgs = ["SortingObjects/beakers.png",
    "chemicals_idle.png",
    "chemicals_idle.png",
    "chemicals_idle.png",
    "chemicals_idle.png"]
    descriptions = ["An old dirty tape measure. They probably used this collect data like height",
    "A torn page of a lab report with death rates categorized by age ranges",
    "Test tubes labeled with different names. The notebook saids these names refer to some sort of chemical mixture",
    "This scale was probably used to weigh different samples. Maybe we can re-use to meeasure ...",
    "A broken stop watch. Looks like what ever they were timing only to 3 seconds"]
    img_sizes = [.25,.25,.25,.25,.25]
    nominal = {"test tubes"}
    interval = {"tape measure","stop watch"}
    ratio = {"scale"}
    binary = {}
    ordinal = {"age groups"}
    categories = {'nominal':nominal,'interval':interval,'ratio':ratio,'binary':binary,'ordinal':ordinal}
    player_correct = {'nominal':'Yep looks nominal to me','interval': 'good job!', 'ratio': 'looks good to me', 'binary': " Between correct and incorrect. I'd say correct", 'ordinal': "I see you got everything in order. Get it order and ordinal?"}
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

screen description(what):
    zorder 10
    window:
        xpos 350 ypos 100
        xmaximum 600 ymaximum 100
        id "window"
        text what


screen sortingScreen(n):
    add "Backgrounds/backgroundFiller.png"
    modal True
    draggroup:
        # what you wanna drag
        drag:
            as target
            drag_name sortingGame1.player_targets[n]
            child At(sortingGame1.player_imgs[n],zoom(sortingGame1.img_sizes[n]))
            droppable False
            xpos 400 ypos 400
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

transform nominalFolder(timing = 0):
    xcenter 400 ycenter 400
    linear timing xpos 100 ypos 100

transform binaryFolder(timing = 0):
    xcenter 400 ycenter 400
    linear timing xpos 300 ypos 100

transform ordinalFolder(timing = 0):
    xcenter 400 ycenter 400
    linear timing xpos 500 ypos 100

transform ratioFolder(timing = 0):
    xcenter 400 ycenter 400
    linear timing xpos 700 ypos 100

transform intervalFolder(timing = 0):
    xcenter 400 ycenter 400
    linear timing xpos 900 ypos 100

transform zoom(size):
    zoom size

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

    label npc_sorting:
        show nominal at nominalFolder
        show binary at binaryFolder
        show ratio at ratioFolder
        show ordinal at ordinalFolder
        show interval at intervalFolder
        show placeholder at zoom(1.0)

        LI "Hm... I think this is nominal data. Theres words on these dishes and I from what I remember, words mean nominal"



        menu:
            "Yeah, I agree nominal data usually involves qualitative data":
                player "Yeah I agree nominal data usually involves qualitative data like names or category"
                show placeholder at nominalFolder(3.0)
                pause(3.0)
            "It could also be ordinal":
                LI "Why ordinal?"
                player "I'm glad you asked."
                player "Well, the notebook said "
                menu:
                    "Ordinal data can be put in order":
                        player "Ordinal data is data that has a an order. Like the rating you gave on how great [Friend] and my explantion of ordinal was."
                        LI "I wasn't sucking up, I really thought you did a good job explaining it. But didn't that rating have a number. I'm not seeing a number here."
                        menu:
                            "You're right, there should be a number":
                                player "You're right there should be a number for ordinal data"
                                LI "I'll go with my hunch then"
                                show placeholder at nominalFolder(3.0)
                                pause(3.0)
                            "Ordinal data doesn't always need a number":
                                player "Ordinal data doesn't always need a number"
                                player "For example, I can construct as scale with three values hate, indifferent, and like."
                                LI "So you're measuring how much you like a certain person"
                                player "Exactly. I'd put you in the like category by the way. For these dishes I would categorize it as no growth, some growth, and alot of growth."
                                LI "But couldn't we get an exact measurement of how much growth is in the petri dish"
                                menu:
                                    "We don't have the equipment":
                                        player "we dont have the equipment"
                                    "I guess we can weigh it":
                                        LI "What type of data is weight"
                                        menu:
                                            "Ratio":
                                                show placeholder at ratioFolder(3.0)
                                                pause(3.0)
                                            "Interval":
                                                show placeholder at intervalFolder(3.0)
                                                pause(3.0)
                                            "Binary":
                                                show placeholder at binaryFolder(3.0)
                                                pause(3.0)
                            "For ordinal data we assign the numbers ourselves":
                                player "For example, l"
                                LI "Well what numbers would we assign here"
                                player "Well we can assign a scale 1 to 5. 1 being no growth and 5 being the petri dish is completely filled."
                                LI "But couldn't we get an exact measurement of how much growth is in the petri dish"
                                menu:
                                    "We don't have the equipment":
                                        player "we dont have the equipment"
                                    "It would still be ordinal":
                                        LI "Alright I'll trust you on this one"
                                    "I guess we can weigh it":
                                        LI "What type of data is weight"
                                        menu:
                                            "Ratio":
                                                show placeholder at ratioFolder(3.0)
                                                pause(3.0)
                                            "Interval":
                                                show placeholder at intervalFolder(3.0)
                                                pause(3.0)
                                            "Binary":
                                                show placeholder at binaryFolder(3.0)
                                                pause(3.0)
                    "There is a true zero":
                        LI "I'm not sure what you mean"
                        player "Well zero here means theres nothing in the petri dish"
                        LI "I don't think that has anything to do ordinal data"
                        show placeholder at nominalFolder(3.0)
                        pause(3.0)
                    "You can calculate an average":
                        player "We could measure the weight of each sample and get an average"
                        LI "That seems like something other than ordinal data if we do that."
                        menu:
                            "Disagree":
                                player "You should be able to calculate the average of ordinal data"
                                show placeholder at ordinalFolder(3.0)
                                pause(3.0)
                                Scientist "Sorry to interrupt, but that wasn't true"
                            "Agree":
                                LI "I'm going with my original answer then"
                                show placeholder at nominalFolder(3.0)
                                pause(3.0)
            "It could also be ratio data":
                LI "How so?"
                menu:
                    "We can compare their weights":
                        LI "What about measuring weights makes it a ratio"
                        menu:
                            "Well we can add or subtract the weights":
                                player "We could subtract two weights to find their difference"
                                LI "I think that applies to interval data too. I think I'll go with my initial category"
                                show placeholder at nominalFolder(3.0)
                                pause(3.0)
                            "We can multiply or divide the weights":
                                player "We could form a ratio by dividing two weights. For example one sample maybe 5 grams and another might be 10 grams."
                                LI "In that case the first sample would be half the weight of the other sample"
                                player "Yeah"
                                show placeholder at ratioFolder(3.0)
                                pause(3.0)
                            "We can put the samples in order by weight":
                                LI "I think we could do that with ordinal data"
                                show placeholder at ordinalFolder(3.0)
                                pause(3.0)

        hide placeholder
        LI "Hm looks like a slide deck. I found it near some microscopes looks like these samples are labeled by whether or not they recieved treatment"
        LI "This probably falls under nominal data"

        show placeholder at zoom(1.0)

        menu:
            "What are we measuring?":
                player "What exactly are we measuring that makes it nominal?"
                LI "Well I think we can split it up the samples into two main categories treatment and non-treatment"
                menu:
                    "Then it should be binary":
                        player "If theres only two categories then shouldn't it fall under binary?"
                        label slide_deck_binary:
                            LI "I suppose it could be. The one thing that bothers me is that the samples all look completely different."
                            player "What do you mean?"
                            LI "In binary data shouldn't all the samples in one category look the same."
                            LI "For example, when you flip a coin the result is binary."
                            LI "You either get heads or tails. And everytime you flip the coin heads and tails look the same"
                            menu:
                                "The samples don't always have look the same":
                                    player "Not always. For example do you like working together as team?"
                                    LI "I do. What about you?"
                                    menu:
                                        "Yes":
                                            player "I think its fun to work with you."
                                        "I don't hate it":
                                            player "Well I don't hate working with you"
                                    player "So we have a sample size of two, and the answers don't quite sound the same."
                                    player "You could still say, they both fall under the yes category"
                                    LI "In that case yeah this should go into binary"
                                    show placeholder at binaryFolder(3.0)
                                    pause(3.0)

                                "I agree but it could be something else":
                                    scientist "Hold on you two."
                                    scientist "Even if the samples don't look the exact same, we can still collect binary data."
                                    player "Do you have an example?"
                                    scientist "Do you think those two *pointing at [Friend] and [Rival] arguing* are getting along?"
                                    player "Nope"
                                    LI "No"
                                    scientist "So I have a sample size of two. And my two participants are two very different people."
                                    scientist "The exact answers are slightly different too. However I can still split the the answers into
                                    two unique categories yes and no."
                                    LI "So are these slide decks binary data?"
                                    scientist "What do you two think?"
                                    menu:
                                        "Yes":
                                            show placeholder at binaryFolder(3.0)
                                            pause(3.0)
                                        "No it's nominal":
                                            show placeholder at nominalFolder(3.0)
                                            pause(3.0)
                    "I see":
                        label slide_deck_nominal:
                            player "I see how this could be nominal.."
                            player "The data is qualitative and has no order"
                            player "The categories names aren't numbers like in ratio and interval."
                            player "They also can't be put into a natural order like ordinal data"
                            player "What about binary then?"

            "I agree":
                jump slide_deck_nominal


        hide placeholder
        "A set of beakers. They come in different sizes. I'm not sure how to categorize this one."

        show placeholder at zoom(1.0)

        menu:
            "Are there any labels?":
                player "Do you see and markings on them or labels"
                LI "Yeah I think under the rust I see ticks and the letters ml."
            "I think these measure volume":
                player "I see some markings on here. It looks like it measure the amount of liquid inside by mk"
                player "I remember when I was little, we used to have measuring cups that had similiar measurement labels"

        LI "So we know that these beakers measured something with numbers"

        LI "Do you think the data is ratio."

        default pickedRatio = False
        default pickedInterval = False
        default pickedOrdinal = False

        menu beaker_op:
            "Can we multiply and divide the numbers?":
                player "Remember, when we talked about measuring cups being ratios."
                LI "Yeah"
                player "I think similiar to the measuring cups here we can divide to voumes to get a ratio"
                player "For example 200ml divided by 100ml. We get the number 2 which tells us 200ml is exactly double of 100ml"
                LI "So that means the data is ratio"
                show placeholder at ratioFolder(3.0)
                pause(3.0)
            "Can we add and subtract the numbers?" if not pickedInterval:
                $pickedInterval = True
                player "I think we can add and subtract these numbers from each other"
                player "So that narrows it down to interval and"
                menu:
                    "ratio":
                        LI "So we're down to interval and ratio"
                    "ordinal":
                        LI "I think you mean ratio"
                jump beaker_ops
            "We can put the number in order" if not pickedOrdinal:
                player "We can put the beakers in order from highst to lowest amount"
                player "So it could be ordinal data"
                LI "We could also order the numbers for ratio and interval data too."
                jump beaker_ops




    #call npc_sorting
    label player_sorting:
        show screen description(sortingGame1.descriptions[sortingGame1.objNum])
        call screen sortingScreen(sortingGame1.objNum)
        label next_try:
            $sortingGame1.objNum = sortingGame1.objNum + 1
            if(sortingGame1.matching):
                $score = score + 1
            $_return = False
            if(sortingGame1.objNum < len(sortingGame1.player_targets)):
                jump player_sorting
        "Done"
    Scientist "Alright everyone got what they needed? Let’s head back to the lab. I’ll debrief you on why data is important"

    "You pull [LI] aside"
    player "I'm sorry if I was a little pushy today. I hope I didn't scare you"
    LI "Theres nothing wrong with a little back and forth. Plus I think its kinda cute"
    "It must be the all the lifting I did, but I'm starting to feeling my heart beat faster than usual."

    return
