# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
image room = "Backgrounds/room.png"
image outside = "Backgrounds/Outside.png"
image cave = "Backgrounds/Cave.png"
image lab = "Backgrounds/LabDirty.png"
label introSceneChapter:

    call flashbackMinigame

    call discoverTheLab

    call applyingForTheLab

    call partnerMinigame

    call introRival

    call sortingGame1
    # This ends the game.


    # return

label introRival:
    show Rival
    Rival "Looking at you guys getting all friendly makes me sick. "
    player "No one asked you."
    Rival " And no one asked you to come all the way knocking on our door."
    Rival " I hope you're worth the rations."
    show LI at right with moveinright
    show Rival at left with move
    LI "Hey that's uncalled for. [player] and [Friend] have every right to be here"
    Rival "Whatever ... "
    Rival "This conversation isn't worth my time"
    hide Rival with moveoutleft
    show LI at center with move
    player "You didn't have to do that you know?"
    LI "Do what?"
    player "Stand up for us."
    LI "Consider it a token of gratitude for helping me out"
    LI "There's only a few of us left as is. We better work together if we want to find a cure."
    player "Well, I appreciate it. I'm looking forward to working with you tommorow."
    LI "Likewise"
    hide LI
    return


label discoverTheLab:
    #swap background here
    scene room with vpunch
    show Friend
    Friend "[player]? [player]?!"
    player "AHHHHHHHHHHHHH!"
    "(*thud*) Oww... "
    Friend "[player]? Are you okay?"
    player "Yeah. Other than the fact that I just faceplanted to the floor."
    Friend "Your'e so mean! And here I was trying to help you."
    Friend "..."
    Friend "Was it about that again?"
    player "Huh? Oh. No."
    Friend "Then what?"
    player "Remember the field trip we took to that one science lab in the third grade?"
    Friend "I just remember that the teacher was HOT."
    player "OMIGOD [Friend], no way he's way too old."
    Friend "Age is just a quantitative thing. It's the qualitative data like his looks that matter."
    player "Do you even know what those words mean?"
    Friend "Shut up! Of course I do."
    "...TIMESKIP"
    scene outside
    "[Friend] and I recently came upon a notebook with numbers and graphs."
    "In the pages, we also found some notes."
    "We started using scientific terms as part of an inside joke."
    "It made us feel special like secret agents."
    player "Are you ready? The notebook says we should be getting close to the meeting place."
    Friend "Are you sure we should be trusting a random notebook from a scientist."
    Friend "You remember they caused this whole mess right?"
    Friend "It’s been ten years since the apocalypse. Yet, people are still afraid of scientist and science."
    player "We don't know that. Plus, we're already here."
    scene cave
    Friend "(*knock* *knock*)"
    Friend "Hello? Anybody there?"
    return

label applyingForTheLab:
    #swap background
    scene cave
    Scientist "Have you filled out the applications on page 34?"
    show Friend
    Friend "Applications?"
    Friend "The world has fallen apart. Over half of humanity has been wiped out, and you want us to fill out applications?"
    hide Friend
    Scientist "It's just a formality, but please fill them out."
    Scientist "I'll need some nominal data such as yor name, some interval data like your age, and maybe some ordinal data on your food preferences."
    player "You have food options?"
    Scientist "I'm well-stocked on rations"
    "20 minutes later"
    show Friend
    Friend "Hey [player]! I'm almost done with my application. How about you?"
    hide Friend
    player "Almost. Let me double check a few things"
    "Name: [player]"

    python:
        seperator = ", "
        pronouns = seperator.join(list(set(gender_lookup.values())))

    "Gender pronouns: [pronouns]"

    menu:
        "Looks good!":
            pass
        "Let me fix this...":
            call fixPronouns
    "Would you be interested in dating"

    menu:
        "I'd be interested in dating a guy.":
            $gender_lookup.update(dict(zip(love_interest_keys,male_pronouns)))
            $li_gender = 'male'
            pass
        "I'd be interest in dating a girl.":
            $gender_lookup.update(dict(zip(love_interest_keys,female_pronouns)))
            $li_gender = 'female'
            pass

    player "Are you sure the last question is necessary?"
    Scientist "Just taking precautions."

    "I'll just leave this under the door."

    show Scientist
    Scientist "Welcome to the lab, [player] and [Friend]. We're just about to start orientation. My name is [Scientist]"
    Scientist "Take a seat. Alright that looks like everyone is here. Let's play an icebreaker."
    Scientist "I'm sure all of you have read one of my notebooks. Inside you should of found definitions."
    Scientist "For five types of data nominal, interval, ratio, ordinal, and binary."
    Scientist "For this ice breaker, I want each of you to state a fact about yourself for each category"
    hide Scientist
    show Friend at left
    show Rival at right
    Friend "What if we don't remember the categories?"
    Rival "Then you shouldn't be here."
    hide Friend
    hide Rival
    show Scientist
    Scientist "Questions are absolutely fine. Please ask me or each other if you need something defined."

    label questions:
        show Scientist at center with move
        menu:
            "No questions":
                jump icebreaker
            "What is nominal data?":
                show Scientist at left with move
                show Rival at right with moveinright
                Rival "Obviously nominal means name. Therefore, it is a type of data that is used to label variables without providing any quantitative value."
                Rival "It is the simplest form of a scale of measure. Unlike ordinal data, nominal data cannot be ordered and cannot be measured. Duh."
                hide Rival
            "What is binary data?":
                show Scientist at left with move
                show LI at right with moveinright
                LI "I think binary means there can only be two values. For example, did I think that was a good question?"
                LI "A binary answer would be yes or no. Yes I think that was good question"
                hide LI
            "What is interval data?":
                Scientist "Interval data is when we have a variable that contains numeric values that are ordered and where we know the exact differences between the values. "
            "What is ratio data?":
                Scientist "Ratio data is Ratio values are also ordered units that have the same difference."
                show Scientist at left with move
                show LI at right with moveinright
                LI "Ratio values are the same as interval values, with the difference that they do have an absolute zero. "
                hide LI
            "What is ordinal data?":
                show Scientist at left with move
                show Friend at right with moveinright
                Friend "Ooh I know this one!"
                Friend "Ordinal data is data in which values follow a natural order."
                hide Friend
        jump questions

    label icebreaker:
        hide Scientist
        scene cave
        "[Rival],[Friend], and I, have all answered the questions"
        show LI
        LI "Oh wow. This makes me kind of nervous"
        LI "For nominal data, my name is [LI]. For binary data, between dead and alive. I am alive."
        show LI at left with move
        show Friend at right with moveinright
        Friend "Keep it up only three more to go."
        hide Friend
        show LI at center with move
        LI "My age is 25. That counts as interval right? For ratio data my height is 167cm"
        Scientist "What about ordinal?"
        LI "What about ordinal?"
        player "How about on a 1 to 5 scale. 1 being extremely easy and 5 being extremely hard. How hard was your trip to this lab?"
        LI "I'd say a solid 4."
        hide player
        hide LI

    Scientist "Great that's everyone. Be sure to review your categories, you'll need them for tomorrow's expedition"


    show Friend at left
    show Rival at right
    Friend "Expedition? We just got here."
    Rival "Speak for yourself."
    hide Friend with moveoutleft
    hide Rival with moveoutright
    show LI
    "[LI] pulls me aside"
    LI "Thanks for helping me out back there"
    hide LI
    return

label fixPronouns:
    python:
        seperator = ", "
        male = seperator.join(list(set(male_pronouns)))
        female = seperator.join(list(set(female_pronouns)))
        nonbinary = seperator.join(list(set(nonbinary_pronouns)))

    menu:
        "[male]":
            $store.gender_lookup = dict(zip(player_keys,male_pronouns))
            pass
        "[female]":
            $store.gender_lookup = dict(zip(player_keys,female_pronouns))
            pass
        "[nonbinary]":
            $store.gender_lookup = dict(zip(player_keys,nonbinary_pronouns))
            pass
