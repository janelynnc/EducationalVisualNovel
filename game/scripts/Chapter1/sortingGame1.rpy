# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label sortingGame1:
    $player_targets = ["chemicals_idle.png", ]
    define selected = "chemicals_idle.png"
    init python:
        nominal = {"chemicals_idle.png"}
        interval = {}
        ratio = {}
        binary = {}
        ordinal = {}
        categories = {'nominal':nominal,'interval':interval,'ratio':ratio,'binary':binary,'ordinal':ordinal}
        player_correct = {'nominal':'Yep looks like it could be category','interval': 'good job!', 'ratio': 'looks good to me', 'binary': " Between correct and incorrect. I'd say correct", 'ordinal': "I see you got everything in order. Get it order and ordinal?"}
        num_sorted = 0;
        def draggedItem(drop_obj,drag_obj):
            if len(drag_obj) == 0:
                return

            store.selected = drag_obj[0].drag_name
            store.matching = drag_obj[0].drag_name in categories[drop_obj.drag_name]
            if(store.matching):
                store.response = player_correct[drop_obj.drag_name]
                renpy.show_screen("bubbleSay", store.response,True)
            else:
                store.response = "Hm something seems a little off" + store.selected
                renpy.show_screen("bubbleSay", store.response,False);
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
                action Hide("bubbleSay")
        else:
            vbox:
                xpos 600 ypos 600
                textbutton "Let me try again" action Hide("bubbleSay")
                textbutton "Disagree" action [function(target.snap,200,600)]


    screen sortingScreen:
        add "backgroundFiller.png"
        modal True
        draggroup:
            # what you wanna drag
            drag:
                as target
                drag_name store.selected
                child "UFO.png"
                droppable False
                xpos 200 ypos 600
                #xpos 0 ypos 0

            # what you wanna drog item to
            drag:
                drag_name "nominal"
                child "SortingObjects/nominalfolder.png"
                draggable False
                dropped draggedItem
                xpos 100 ypos 100
                #xpos 0 ypos 0

            drag:
                drag_name "binary"
                child "SortingObjects/binaryfolder.png"
                draggable False
                dropped draggedItem
                xpos 300 ypos 100
                #xpos 0 ypos 0

            drag:
                drag_name "ordinal"
                child "SortingObjects/ordinalfolder.png"
                draggable False
                dropped draggedItem
                xpos 500 ypos 100
                #xpos 0 ypos 0

            drag:
                drag_name "ratio"
                child "SortingObjects/ratiofolder.png"
                draggable False
                dropped draggedItem
                xpos 700 ypos 100
                #xpos 0 ypos 0

            drag:
                drag_name "interval"
                child "SortingObjects/intervalfolder.png"
                draggable False
                dropped draggedItem
                xpos 900 ypos 100
                #xpos 0 ypos 0




    label player_sorting:
        call screen sortingScreen



label npc_sorting:
