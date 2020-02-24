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
    Frient "Then what?"
    player "Remember the field trip we took to SC**NCE LAB in the third grade?"
    Friend "I just remember that the teacher was HOT"
    player "OMIGOD [player], no way he's way too old."
    Friend "...and that was the day you decided to pursue SCIENCE for the rest of your life."
    player "Yeah."
    Friend "It’s a shame you didn’t get to finish your degree in SCIENCE"
    "What a dream. It’s been five years since modern science has been erased from our lives."
    "Extra! Extra! Read all about it!"
    "Oh, it’s the paperboy."
    Friend "Hey, [player]. Can you get the newspaper? I’m gonna make food."
    player "Sure"
    "You open the door to find the local paperboy throwing newpapers at people’s doorsteps."
    "A new lab is opening up, and they wanna create medicine!"
    "Medicine?"
    "Yup! I hear they’re looking the best of the best!"
    player "Oh"
    "I hear that if you get in, you get the best benefits."
    "best benefits, huh?"

    return
label applyingForTheLab:
    "[Friend] and I chased down the paper boy and recieved two applications for the lab"
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

    "What a weird question, maybe its just my imagination. After all there aren't many options in this small outpost."
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
