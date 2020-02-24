# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label sortingGame1:
    init python in sortingGame1:
        player_targets = ["chemicals_idle.png","chemicals_idle.png","chemicals_idle.png","chemicals_idle.png","chemicals_idle.png"]
        nominal = {"chemicals_idle.png"}
        interval = {}
        ratio = {}
        binary = {}
        ordinal = {}
        categories = {'nominal':nominal,'interval':interval,'ratio':ratio,'binary':binary,'ordinal':ordinal}
        player_correct = {'nominal':'Yep looks like it could be category','interval': 'good job!', 'ratio': 'looks good to me', 'binary': " Between correct and incorrect. I'd say correct", 'ordinal': "I see you got everything in order. Get it order and ordinal?"}
        objNum = 0
        def shouldReset(drop_obj,drag_obj):
            if len(drag_obj) == 0:
                return

            matching = drag_obj[0].drag_name in categories[drop_obj.drag_name]
            if(matching):
                response = player_correct[drop_obj.drag_name]
                renpy.show_screen("bubbleSay", response,True)
            else:
                response = "Hm something seems a little off"
                renpy.show_screen("bubbleSay", response,False);

            renpy.restart_interaction()

    screen bubbleSay(what,ctc):
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
                textbutton "Disagree" action [Hide("bubbleSay"),Return(True)]


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
                #xpos 0 ypos 0

            # what you wanna drog item to
            drag:
                drag_name "nominal"
                child "SortingObjects/nominalfolder.png"
                draggable False
                dropped sortingGame1.shouldReset
                xpos 100 ypos 100
                #xpos 0 ypos 0

            drag:
                drag_name "binary"
                child "SortingObjects/binaryfolder.png"
                draggable False
                dropped sortingGame1.shouldReset
                xpos 300 ypos 100
                #xpos 0 ypos 0

            drag:
                drag_name "ordinal"
                child "SortingObjects/ordinalfolder.png"
                draggable False
                dropped sortingGame1.shouldReset
                xpos 500 ypos 100
                #xpos 0 ypos 0

            drag:
                drag_name "ratio"
                child "SortingObjects/ratiofolder.png"
                draggable False
                dropped sortingGame1.shouldReset
                xpos 700 ypos 100
                #xpos 0 ypos 0

            drag:
                drag_name "interval"
                child "SortingObjects/intervalfolder.png"
                draggable False
                dropped sortingGame1.shouldReset
                xpos 900 ypos 100
                #xpos 0 ypos 0



    label player_sorting:
        call screen sortingScreen(sortingGame1.objNum)
        if(_return and sortingGame1.objNum < len(sortingGame1.player_targets)-1):
           $sortingGame1.objNum = sortingGame1.objNum + 1
           $_return = False
           jump player_sorting
        "Done"

label npc_sorting:
