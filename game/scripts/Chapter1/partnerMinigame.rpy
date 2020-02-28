# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label partnerMinigame:
    scene backgroundFiller

    "You decide to help [Friend] prepare for the field study"

    Friend "Pointing at [LI] what's he doing here"
    player "He's here to help"
    LI "Theres not much else to do here"
    player "Right let's get started"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    label NominalDef:
        Friend "Nominal data is..."
        menu:
            "Definition of Nominal":
                LI "A easy way to remember is nominal kind of sounds like name"
            "Definition Of Ratio":
                jump wrongAnswer1
            "Definition of Interval":
                jump wrongAnswer1
            "Definition of Binary":
                jump wrongAnswer1
            "Definition of Ordinal":
                jump wrongAnswer1

        "You point to [LI]"

    label NominalExample:
    player "For Example, "
    menu:
        "[LI]'s height":
            Friend "That doesn't really make sense. Isn't height a number you can measure"
            jump NominalExample
        "[LI]'s relationship status":
            LI "This works as an example. I’m single *blush* but I could be in other categories such as engaged or married (one day)"
        "[LI] His temperature":
            LI "I'd say this would be Ratio data"
            jump NominalExample

    label IntervalDef:
        Friend "Well that one makes sense"
        Friend "What I really have trouble with is Ratio and Itererval. Aren't they like the same thing. Like, they both got numbers right?"
        player "Not quite. There is a difference between the two."
        player "Let's start with interval data."
        player "Interval data is..."

        menu:
            "Definition Of Ratio":
                LI "Maybe this one is ratio?"
                jump IntervalDef
            "Definition of Interval":
                pass
            "Definition of Binary":
                LI "I'm pretty sure this is binary."
                jump IntervalDef
            "Definition of Ordinal":
                Friend "Oh, oh! I remember this one! This is ordinary data. I mean ordinal."
                jump IntervalDef
    label IntervalExample:
        "Looking around the room"
        menu:
            "The time on a broken clock":
                player "The time on a clock could be consider a interaval"
                player "You can subtract two diffrent times from each other. But unlike a ratio it doesn't make sense to perform division.
                Dividing 2pm by 12am doesn't make any sense."
                LI "*nods* Theres also no true 0 or starting point."
            "The color of the chair":
                player "For example, the color of this chair"
                Friend "Is considered nominal data right?"
                player "right"
                jump IntervalExample
            "The weight of this bottle cap":
                player "Wait this isn't quite right"
                jump IntervalExample
            "Measuring Cups":
                LI "Remember intervals don't have a true zero and can't form ratios."
                LI "So 1/4 cup would not be part of a interval. Since there is a 0 cup and you can form ratios. Like 1/4 cup is exactly half of a half cup"
                jump IntervalExample

    label RatioDef:
        Friend "So what about ratio"
        player "A ratio is ..."

        menu:
            "Definition Of Ratio":
                pass
            "Definition of Interval":
                Friend "Wasn't this interval?"
                jump RatioDef
            "Definition of Binary":
                "This doesn't seem right"
                jump RatioDef
            "Definition of Ordinal":
                "This doesn't seem right"
                jump RatioDef

    label ratioExample:
        "Looking around the room"
        menu:
            "The time on a brocken clock":
                "I already said this was an interval"
                jump ratioExample
            "The color of the chair":
                player "For example, the color of this chair"
                Friend "Is considered nominal data right?"
                player "right"
                jump ratioExample
            "The weight of this bottle cap":
                player "Weight is an example of ratio data. Theres an absolute 0 and we can multiply, divide and form ratios from weight."
            "Grade level in school":
                player "Nope. I can't form ratios out of grade levels. 9th grade over 12th grade makes no sense, and the zero point is arbituary. Some people start counting from kindergarten, other start at first grade."
                jump ratioExample

    LI "Then there were two"
    menu:
        "Binary Data?":
            player "You're making a lame joke about binary data right?"
            LI "Its not lame. And yes"
        "Ordinal Data?":
            player "You're making a lame joke about binary data right?"
            LI "I was thinking more along the lines of binary"

    label binaryDef:
        player "Binary data is"

        menu:
            "Definition of Nominal":
                Friend "Sounds exactly like nominal to me"
                jump binaryDef
            "Definition Of Ratio":
                Friend "Sounds exactly like ratio to me"
                jump binaryDef
            "Definition of Interval":
                Friend "Sounds exactly like interval to me"
                jump binaryDef
            "Definition of Binary":
                pass
            "Definition of Ordinal":
                player "Hold on. Let me start from the top"
                jump binaryDef

    player "To demostrate I'll ask [L.I] a question"

    player "Do you have an ulterior motive?"

    LI "I'm 90 percent sure I don't"

    Friend "Was that a binary response?"

    menu:
        "Yes":
            LI "Well no it wasn't but .. "
        "No":
            player "I'm looking for a yes or no. All or nothing answer"

    LI "Fine, maybe I do have an ulterior motive"
    Friend "Oooh this is getting spicy"
    LI "I don't know what ordinal data is and I'm hoping you'd define it for me"
    LI "I know we're competing for the same position but ..."
    player "I dont see an issue with helping you."
    LI "Really?"
    Friend "Heres a binary answer they(p) means yes"

    label ordinalDef:
        player "Ordinal data is"
        menu:
            "Definition of Nominal":
                Friend "Sounds exactly like nominal to me"
                jump ordinalDef
            "Definition Of Ratio":
                Friend "Sounds exactly like ratio to me"
                jump ordinalDef
            "Definition of Interval":
                Friend "Sounds exactly like interval to me"
                jump ordinalDef
            "Definition of Binary":
                player "Hold on. Let me start from the top"
                jump ordinalDef
            "Definition of Ordinal":
                pass

    label ordinalExample:
        player "[Friend] pull out the"

        menu:
            "Ruler":
                player "Wait let me try again"
            "Measuring Scale":
                player "hold on that works better for ratio"
            "Colored Markers":
                player "we can't really assigned an order to these"
            "Lab Satisifaction Survey Poster":
                player "You stole from [Scientist] and kept it this long?"
                Friend "Back on topic please?"
                player "Do you see the scale that goes from unsatisfied 1 to very satisfied 5"
                Friend "It's an ordinal scale because you can assign an order, but if I rated you at a 3."
                player "You wouldn't know exactly how much more I was satisifed then if I say rated you at 1. All you can say is that, I'm somewhere between very satisfied and unsatisfied with you"
                LI "So I can add or subtract these ratings"
                player "right"

    LI "Well I give your explanation a 5. Thanks for helping me"
    player "I think I'll be seeing you soon"
    LI "I hope so"

    return

label wrongAnswer1:
    LI "Not sure if this is correct"
    jump NominalDef
