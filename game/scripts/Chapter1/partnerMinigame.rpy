image poster = At("Poster.png",zoom(.2))

init python in definitions:
    nominal = "a type of data that is used to label variables without providing any quantitative value."
    ratio = "defined as a quantitative data, having the same properties as {color=#259ce6}interval{/color} data, with an equal and definitive ratio between each data and absolute zero"
    interval = "when we have a variable that contains numeric values that are ordered and where we know the exact differences between the values"
    binary = "a type of data where there can only be two values."
    ordinal = "when the values follow a natural order."

label partnerMinigame:
    play music "audio/Music/bensound-photoalbum.mp3"
    scene outside
    "I decided to help [Friend] prepare for the field study outside the cave."
    player "Hey, [Friend]!"
    show LI with easeinright
    Friend "(*Pointing at [LI]. *) What's he doing here?"
    player "He's here to help."
    LI "There's not much else to do here."
    Friend "Or maybe you just like [player]"
    player "[Friend]! Anyways, let's get started."
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
            LI "This works as an example. I’m single *blush* but I could be in other categories such as engaged or married {size=10}(one day){/size}"
        "[LI] His temperature":
            LI "I'd say this would be {color=#259ce6}ratio{/color} data"
            jump NominalExample


    show LI at right with move
    show Friend at left with moveinleft
    Friend "Well, that one makes sense."
    Friend "What I really have trouble with is Ratio and {color=#259ce6}interval{/color}. Aren't they like the same thing? Like, they both got numbers right?"
    player "Not quite. There is a difference between the two."
    player "Let's start with {color=#259ce6}interval{/color} data."

    label IntervalDef:
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
            "The time on a watch":
                "You grab [LI]'s wrist."
                player "The time on this watch could be considered a {color=#259ce6}interval{/color}."
                player "You can subtract two different times from each other. But unlike a {color=#259ce6}ratio{/color}, it doesn't make sense to perform division.
                Dividing 2pm by 12am doesn't make any sense."
                LI "*nods* There's also no true 0 or starting point."
                LI "By the way you can let go now."
                player "Oh sorry. (*blush*)"
            "The color of [LI]'s face":
                "You lean in closely and examine [LI]'s face"
                player "For example, the shade red [LI]'s face is turning."
                Friend "Is considered {color=#259ce6}Nominal{/color} data right?"
                player "If you knew why didn't you stop me."
                Friend "It's kind of cute seeing [LI] react to you."
                jump IntervalExample
            "Measuring Cups":
                LI "Remember, intervals don't have a true zero and can't form ratios."
                LI "So 1/4 cup would not be part of an {color=#259ce6}interval{/color}. Since there is a 0 cup and you can form ratios. Like 1/4 cup is exactly half of a half cup."
                jump IntervalExample
        Friend "So what about {color=#259ce6}ratio{/color}?"

    label RatioDef:
        player "{color=#259ce6}Ratio{/color} data is ..."

        menu:
            "[definitions.ratio]":
                pass
            "[definitions.binary]":
                "This doesn't seem right"
                jump RatioDef
            "[definitions.ordinal]":
                "This doesn't seem right"
                jump RatioDef

    label ratioExample:
        "Looking around the room..."
        menu:
            "Heart rate":
                player "Heart rate is an example of {color=#259ce6}ratio{/color} data."
                LI "Well it depends how we measure it."
                Friend "How so?"
                LI "Is it ok if I demostrate on you?"
                player "Um. Ok."
                "LI takes out a stethoscope and puts above your heart."
                LI "140 beats per minute. Thats very fast."
                LI "Are you okay?"
                player "Yeah. I think so ... "
                Friend "You guys can stop. I think I get it"
                Friend "It's a ratio because you're counting the number of heartbeats per minute:"
                player "And like other ratio data theres a true zero so we can multiply and divide this data."
                Friend "Yeah and zero means you're dead."
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
            "[definitions.binary]":
                pass
            "[definitions.ordinal]":
                player "Hold on. Let me start from the top."
                jump binaryDef

    player "To demonstrate I'll ask [LI] a question."

    player "Do you have an ulterior motive?"

    hide Friend with moveoutleft
    show LI at center with move
    LI "I'm 90 percent sure I don't."

    Friend "Was that a {color=#259ce6}binary{/color} response?"

    player "I'm looking for a yes or no. All or nothing answer."

    LI "Fine, maybe I do have an ulterior motive."
    show Friend at left with moveinleft
    show LI at right with move
    Friend "Oooh this is getting spicy."
    LI "I'm here to impress someone."
    player "[Friend]?"
    LI "No."
    Friend "Oh this is another binary question!"
    Friend "If it's not me Toby's here to impress."
    Friend "It must be you."
    player "Lets get back on topic."

    label ordinalDef:
        player "{color=#259ce6}Ordinal{/color} data is categorical data where order matters."

    label ordinalExample:
        player "[Friend] pull out the ..."

        menu:
            "Colored Markers":
                player "We can't really assign an order to these."
                jump ordinalExample
            "Lab Satisfaction Survey Poster":
                show poster at pos(640,250)
                player "You stole from [Scientist] and kept it this long?"
                Friend "Back on topic please?"
                player "Do you see the scale that goes from unsatisfied 1 to very satisfied 5"
                Friend "It's an {color=#259ce6}Ordinal{/color} scale because you can assign an order, but if I rated you at a 3."
                player "You wouldn't know exactly how much more I was satisfied then if I say rated you at 1. All you can say is that I'm somewhere between very satisfied and unsatisfied with you."
                LI "So, I can't add or subtract these ratings?"
                player "Right."
                hide poster
    hide Friend
    hide LI
    return
