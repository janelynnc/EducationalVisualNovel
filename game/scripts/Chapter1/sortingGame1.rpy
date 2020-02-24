# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label sortingGame1:
    $player_targets = ["chemicals_idle.png", ]
    $selected = ""
    init python:
        nominal = {"chemicals_idle.png"}
        interval = {}
        ratio = {}
        binary = {}
        ordinal = {}
        categories = {'nominal':nominal,'interval':interval,'ratio':ratio,'binary':binary,'ordinal':ordinal}
        player_correct = {'nominal':'Yep looks like it could be category','interval': 'good job!', 'ratio': 'looks good to me', 'binary': " Between correct and incorrect. I'd say correct", 'ordinal': "I see you got everything in order. Get it order and ordinal?"}
        def blah_dragged(drop_obj,drag_obj):
            if len(drag_obj) == 0:
                return

            store.selected = drag_obj[0].drag_name
            store.matching = drag_obj[0].drag_name in categories[drop_obj.drag_name]
            if(store.matching):
                store.response = player_correct[drop_obj.drag_name]
            else:
                store.response = "Hm something seems a little off" + store.selected
            return True
    screen sorting_screen:
        modal True
        add "backgroundFiller.png"
        draggroup:
            # what you wanna drag
            drag:
                as target
                drag_name "[selected]"
                child "UFO.png"
                droppable False
                xpos 350 ypos 100
                #xpos 0 ypos 0

            # what you wanna drog item to
            drag:
                drag_name "nominal"
                child "LaserCannon.png"
                draggable False
                dropped blah_dragged
                xpos 150 ypos 100
                #xpos 0 ypos 0


    

    label player_sorting:
        call screen sorting_screen
        if(matching):
            "[response]"
        else:
            show screen sorting_screen
            "[response]"
            menu:
                "Let me try again":
                    pass
                "Disagree":
                    "I think I'm right on this one"

        jump player_sorting

    label npc_sorting:
