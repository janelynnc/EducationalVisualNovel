## The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

init python in definitions:
    nominal = "a type of data that is used to label variables without providing any quantitative value."
    ratio = "defined as a quantitative data, having the same properties as {color=#259ce6}interval{/color} data, with an equal and definitive ratio between each data and absolute zero"
    interval = "when we have a variable that contains numeric values that are ordered and where we know the exact differences between the values"
    binary = "a type of data where there can only be two values."
    ordinal = "when the values follow a natural order."
label partnerMinigame:
    scene outside
    player "Hey, [Friend]!"
    "I have decided to help [Friend] prepare for the field study."
    show LI with easeinright
    Friend "(*Pointing at [LI]. *) What's he doing here?"

    player "He's here to help."
    LI "There's not much else to do here."
    player "Right. Let's get started."
    show Friend at left with moveinleft
    show LI at right with move

    label NominalDef:
        player "{color=#259ce6}Nominal{/color} data is..."
        menu:
            "[definitions.nominal]":
                LI "An easy way to remember is {color=#259ce6}Nominal{/color} kind of sounds like name."
            "[definitions.ratio]":
                "Wait, this doesn't sound quite right. This sounds more like the definition of {color=#259ce6}ratio{/color} data."
                jump NominalDef
            "[definitions.interval]":
                LI "This sounds more like {color=#259ce6}interval{/color} to me."
                jump NominalDef
            "[definitions.binary]":
                "This doesn't seem quite right."
                jump NominalDef
            "[definitions.ordinal]":
                Friend "If there's one thing I know, it's that this is the definition of {color=#259ce6}Ordinal{/color}. {color=#259ce6}Ordinal{/color} sounds like order!"
                Friend "...at least, that is how I remember it."
                jump NominalDef
        "You point to [LI]."
        hide Friend with moveoutleft
        show LI at center with move
    label NominalExample:
    player "For Example, "
    menu:
        "[LI]'s height":
            Friend "That doesn't really make sense. Isn't height a number you can measure?"
            jump NominalExample
        "[LI]'s relationship status":
            LI "This works as an example. I’m single *blush* but I could be in other categories such as engaged or married (one day)"
        "[LI] His temperature":
            LI "I'd say this would be {color=#259ce6}ratio{/color} data"
            jump NominalExample


    show LI at right with move
    show Friend at left with moveinleft
    Friend "Well, that one makes sense."
    Friend "What I really have trouble with is Ratio and {color=#259ce6}interval{/color}. Aren't they like the same thing? Like, they both got numbers right?"
    player "Not quite. There is a difference between the two."
    player "Let's start with {color=#259ce6}interval{/color} data."

    label intervalDef:
        player "{color=#259ce6}interval{/color} data is..."
        menu:
            "[definitions.ratio]":
                LI "This sounds like {color=#259ce6}ratio{/color}."
                jump IntervalDef
            "[definitions.interval]":
                pass
            "[definitions.binary]":
                LI "I'm pretty sure this is {color=#259ce6}binary{/color}."
                jump IntervalDef
            "[definitions.ordinal]":
                Friend "Oh, oh! I remember this one! This is ordinary data. I mean {color=#259ce6}Ordinal{/color}."
                jump IntervalDef
    label IntervalExample:
        "Looking around the room"
        menu:
            "The time on a broken clock":
                player "The time on a clock could be considered a {color=#259ce6}interval{/color}"
                player "You can subtract two different times from each other. But unlike a {color=#259ce6}ratio{/color}, it doesn't make sense to perform division.
                Dividing 2pm by 12am doesn't make any sense."
                LI "*nods* There's also no true 0 or starting point."
            "The color of the chair":
                player "For example, the color of this chair..."
                Friend "Is considered {color=#259ce6}Nominal{/color} data right?"
                player "Right."
                jump IntervalExample
            "The weight of this bottle cap":
                player "Wait, this isn't quite right."
                jump IntervalExample
            "Measuring Cups":
                LI "Remember, intervals don't have a true zero and can't form ratios."
                LI "So 1/4 cup would not be part of an {color=#259ce6}interval{/color}. Since there is a 0 cup and you can form ratios. Like 1/4 cup is exactly half of a half cup."
                jump IntervalExample
        Friend "So what about {color=#259ce6}ratio{/color}"

    label RatioDef:
        player "{color=#259ce6}ratio{/color} data is ..."

        menu:
            "[definitions.ratio]":
                pass
            "[definitions.interval]":
                Friend "Wasn't this {color=#259ce6}interval{/color}?"
                jump RatioDef
            "[definitions.binary]":
                "This doesn't seem right"
                jump RatioDef
            "[definitions.ordinal]":
                "This doesn't seem right"
                jump RatioDef

    label ratioExample:
        "Looking around the room..."
        menu:
            "The time on a broken clock":
                "I already said this was an {color=#259ce6}interval{/color}"
                jump ratioExample
            "The color of the chair":
                player "For example, the color of this chair..."
                Friend "Is considered {color=#259ce6}Nominal{/color} data right?"
                player "right"
                jump ratioExample
            "The weight of this bottle cap":
                player "Weight is an example of {color=#259ce6}ratio{/color} data. There's an absolute 0 and we can multiply, divide and form ratios from weight."
            "Grade level in school":
                player "Nope. I can't form ratios out of grade levels. 9th grade over 12th grade makes no sense, and the zero point is arbitrary. Some people start counting from kindergarten, other start at first grade."
                jump ratioExample

    hide Friend with moveoutleft
    show LI at center with move
    LI "Then there were two"

    player "You're making a lame joke about {color=#259ce6}binary{/color} data right?"

    LI "It's not lame. And yes"

    show LI at right with move
    show Friend at left with moveinleft

    label binaryDef:
        player "{color=#259ce6}binary{/color} data is..."

        menu:
            "[definitions.nominal]":
                Friend "Sounds exactly like {color=#259ce6}Nominal{/color} to me"
                jump binaryDef
            "[definitions.ratio]":
                Friend "Sounds exactly like {color=#259ce6}ratio{/color} to me"
                jump binaryDef
            "[definitions.interval]":
                Friend "Sounds exactly like {color=#259ce6}interval{/color} to me"
                jump binaryDef
            "[definitions.binary]":
                pass
            "[definitions.ordinal]":
                player "Hold on. Let me start from the top"
                jump binaryDef

    player "To demonstrate I'll ask [LI] a question"

    player "Do you have an ulterior motive?"

    hide Friend with moveoutleft
    show LI at center with move
    LI "I'm 90 percent sure I don't"

    Friend "Was that a {color=#259ce6}binary{/color} response?"

    menu:
        "Yes":
            LI "Well it wasn't but .. "
        "No":
            player "I'm looking for a yes or no. All or nothing answer"

    LI "Fine, maybe I do have an ulterior motive"
    show Friend at left with moveinleft
    show LI at right with move
    Friend "Oooh this is getting spicy"
    LI "I don't know what {color=#259ce6}Ordinal{/color} data is and I'm hoping you'd define it for me"
    LI "I know we're competing for the same position but ..."
    player "I don't see an issue with helping you."
    LI "Really?"
    Friend "Here's a {color=#259ce6}binary{/color} answer they(p) means yes"
    label ordinalDef:
        player "{color=#259ce6}Ordinal{/color} data is"
        menu:
            "a classification of categorical variables that do not have any quantitative value":
                Friend "Sounds exactly like {color=#259ce6}Nominal{/color} to me"
                jump ordinalDef
            "[definitions.ratio]":
                Friend "Sounds exactly like {color=#259ce6}ratio{/color} to me"
                jump ordinalDef
            "[definitions.interval]":
                Friend "Sounds exactly like {color=#259ce6}interval{/color} to me"
                jump ordinalDef
            "[definitions.binary]":
                player "Hold on. Let me start from the top"
                jump ordinalDef
            "categorical data where order matters":
                pass

    label ordinalExample:
        player "[Friend] pull out the"

        menu:
            "Ruler":
                player "Wait let me try again"
                jump ordinalExample
            "Measuring Scale":
                player "Hold on. That works better for {color=#259ce6}ratio{/color}"
                jump ordinalExample
            "Colored Markers":
                player "we can't really assign an order to these"
                jump ordinalExample
            "Lab Satisfaction Survey Poster":
                player "You stole from [Scientist] and kept it this long?"
                Friend "Back on topic please?"
                player "Do you see the scale that goes from unsatisfied 1 to very satisfied 5"
                Friend "It's an {color=#259ce6}Ordinal{/color} scale because you can assign an order, but if I rated you at a 3."
                player "You wouldn't know exactly how much more I was satisfied then if I say rated you at 1. All you can say is that I'm somewhere between very satisfied and unsatisfied with you."
                LI "So, I can't add or subtract these ratings?"
                player "Right."

    hide Friend
    show LI at center with move
    LI "Well, I give your explanation a 5. Thanks for helping me"
    player "I think I'll be seeing you soon"
    hide LI

    return
