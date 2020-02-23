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


    "I think I'm going to be late. I better hurry I hope I make it in time"
    "I run frantically down the street."
    "In front of me I see a strange man in a lab coat staring out into the distance. "

    menu:
        "No time to stop. I got an interview to catch":
            "I keep runninng"
            "*Crash* the strange man drops his folders and papers scatter everywhere"
            player "Ouch. Sorry Mister no time to stop I got an interview to catch"
            "You look down and see some interesting notes. You recognize the labels on the folder
            as the categories of data you learned as a kid"
            player "On second thought, mister do you need some help?"
            Scientist "*smirks* Always"

            jump player_sorting

        "Stop and observe":
            "It wouldn't hurt to take a little break"
            "The wind blows and you see papers come flying out"
            "You catch one"
            Scientist "Hey kid, mind helping me out"


    menu:
        "ignore":
            Scientist "I guess I could keep all this classified top secret scientific info all to myself"
            "I'm most definetly not falling for this."
            Player "Oh yeah? What's so important about a few pieces of paper?"
            Scientist "Why don't you help me and find out"

        "sure":
            "I'm already late anyways"

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
