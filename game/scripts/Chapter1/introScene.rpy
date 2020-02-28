# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label introSceneChapter:

    call flashbackMinigame

    call discoverTheLab

    call applyingForTheLab

    call partnerMinigame

    call sortingGame1
    # This ends the game.


    # return

label discoverTheLab:
    Friend "[player]? [player]?!"
    player "AHHHHHH"
    "You wake up, faceplanted on the dusty floor. "
    Friend "[player]? Are you okay?"
    player "Yeah."
    Friend "Was it about that again?"
    player "Huh? Oh. No."
    Friend "Then what?"
    player "Remember the field trip we took to SC**NCE LAB in the third grade?"
    Friend "I just remember that the teacher was HOT"
    player "OMIGOD [Friend], no way he's way too old."
    Friend "Age is just a quantitative thing. Its the qualitative data like his looks that matter."
    player "Do you even know what those words mean?"
    Friend "Shut Up! Of course I do."
    "[Friend] and I recently came upon a notebook with numbers and graphs. In the pages we also found some
    notes. We started using scientific terms as part of an inside joke"
    "It'd made us feel special like a secret agents."
    player "Are you ready the notebook says we should be getting close to the meeting place."
    Friend "Are you sure we should be trusting a random notebook from a scientist. You remember they caused this whole
    mess right?"
    "What a dream. It’s been ten years since the apocolypse. Yet people are still afraid of scientist and science."
    player "We don't know that. Plus were already here."
    Friend "*Knocks on a big metallic door* Hello? Anybody there?"
    return

label applyingForTheLab:

    Scientist "Have you filled out the applications on page 34"
    Friend "Applications? They world has fallen apart.Over half of humanity has been wiped out, and you want us to
    fill out applications?"
    Scientist "It's just a formality but please fill them out. I'll need some nominal data such as yor name. Some interval data like your age.
    And maybe some ordinal data on your food preferences"
    player "You have food options?"
    Scientist "I'm well stocked on rations"
    "20 minutes later"

    Friend "Hey [player] I'm almost done with my application. How about you?"
    player "Almost let me double check a few things"
    "Name: [player]"

    python:
        seperator = ", "
        pronouns = seperator.join(list(set(gender_lookup.values())))

    "Gender pronouns: [pronouns]"

    menu:
        "Looks good":
            pass
        "Let me fix this":
            call fixPronouns
    "Would you be interested in dating"

    menu:
        "I'd be interested in dating a guy":
            $gender_lookup.update(dict(zip(love_interest_keys,male_pronouns)))
            pass
        "I'd be interest in dating a girl":
            $gender_lookup.update(dict(zip(love_interest_keys,female_pronouns)))
            pass

    player "Are you sure the last question is neccesary"
    Scientist "Just taking precautions"

    "You slide the applications under the metal door"

    Scientist "Welcome to the lab [player] and [Friend]. We're just about to start orientation. My name is [Scientist]"
    Scientist "Take a seat. Alright that looks like everyone is here. Let's play an icebreaker"
    Scientist "I'm sure all of you have read one my notebooks. Inside you should of found definitions
    for five types of data nominal,interval,ratio,ordinal and binary."
    Scientist "For this ice breaker, I want each of you to state a fact about yourself for each category"
    Friend "What if we don't remember the categories?"
    Rival "Then you shouldn't be here."
    Scientist "Questions are absolutely fine. Please ask me or each other if you need something defined."

    label questions:
        menu:
            "No questions":
                jump icebreaker
            "What is nominal data?":
                Rival "Obviously nominal means Definition of nominal"
            "What is binary data?":
                LI "I think binary means Definition of binary. For example, did I think that was a good question."
                LI "A binary answer would be yes or no. Yes I think that was good question"
            "What is interval data?":
                Scientist "Interval data is ..."
            "What is ratio data?":
                Scientist "Ratio data is ..."
            "What is ordinal data?":
                Friend "Ooh I know this one"
                Friend "Ordinal data is ..."
        jump questions

    label icebreaker:
        "[Rival],[Friend], and I, have all answered the questions"
        LI "Oh wow. This makes me kind of nervous"
        LI "For nominal data, my name is [LI]. For binary data, between dead and alive. I am alive."
        Friend "Keep it up only three more to go."
        LI "My age is 25. That counts as interval right? For ratio data my height is 167cm"
        Scientist "What about ordinal?"
        LI "What about ordinal?"
        player "How about on a 1 to 5 scale. 1 being extremely easy and 5 being extremely hard. How hard was your trip to this lab?"
        LI "I'd say a solid 4."

    Scientist "Great thats everyone. Be sure to review your categories, you'll need them for tommorow's expedition"
    Friend "Expedition? We just got here."
    Rival "Speak for yourself."

    "[LI] pulls me aside"
    LI "Thanks for helping me out back there"
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
