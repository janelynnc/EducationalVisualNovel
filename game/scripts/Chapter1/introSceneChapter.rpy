# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
image room = "Backgrounds/room.png"
image outside = "Backgrounds/Outside.png"
image outside mark = "Backgrounds/OutsideWithMark.png"
image outside cave = "Backgrounds/OutsideofCave.png"
image cave = "Backgrounds/NewCave.png"
image cave door = "Backgrounds/CaveDoor.png"
image cave door open = "Backgrounds/OpenedCaveDoor.png"
image cave door app = "Backgrounds/AppsCaveDoor.png"
image indoor = "Backgrounds/InsideCaveDoor.png"
image lab = "Backgrounds/LabDirty.png"
image rock = "Backgrounds/RockCloseUp.png"
label introSceneChapter:

    call flashbackMinigame from _call_flashbackMinigame

    call wakeUp from _call_wakeUp

    call loveInterestMeeting from _call_loveInterestMeeting

    call rivalMeeting from _call_rivalMeeting

    call discoverTheLab from _call_discoverTheLab

    call applyingForTheLab from _call_applyingForTheLab

    call enterHideout from _call_enterHideout

    call partnerMinigame from _call_partnerMinigame

    call rivalComment from _call_rivalComment

    call sortingGame1 from _call_sortingGame1
    # This ends the game.
    return

    # return

label rivalComment:
    scene cave
    "I see [Rival] by the entrance."
    show Rival
    "I wonder what she wants."
    $renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "<to 4>audio/Music/rival.wav"
    Rival "Looking at you guys getting all friendly makes me sick. "
    player "{i}No one asked{/i} you."
    Rival " And no one {i}asked{/i} {b}you{/b} to come all the way knocking on {b}our{/b} door."
    Rival " I hope you're worth the rations."
    show LI at right with moveinright
    show Rival at left with move
    LI "Hey, that's uncalled for. [player] and [Friend] have every right to be here."
    Rival "Whatever ... "
    Rival "This conversation isn't worth my time."
    hide Rival with moveoutleft
    show LI at center with move
    play music "audio/Music/Blue-Ridge_Looping.mp3"
    player "You didn't have to do that, you know?"
    LI "Do what?"
    player "Stand up for us."
    LI "Consider it a token of gratitude for helping me out."
    LI "There's only a few of us left as is. We better work together if we want to find a cure."
    player "Well, I appreciate it. I'm looking forward to working with you tomorrow."
    LI "Likewise."
    hide LI
    stop music

    scene indoor
    show Friend
    Friend "What took you so long?"
    player "[Rival] had a few things to say."
    player "Luckily [LI] was there to help."
    Friend "You are totally in love with him."
    player "I am not."
    Friend "Let me put this in your language."
    Friend "On an ordinal scale, with 7 meaning totally in love."
    Friend "You're at 7."
    player "Based on your opinion."
    Friend "Fine lets collect some more data on this."
    Friend "Tommorow on your date, ..."
    player "It's not a date."
    Friend "You should record some qualitative data."
    Friend "Record all the different feelings you when you're with [LI]."
    Friend "Then I want you to count every time you feel an emotion."
    player "So you you want me to count every time some feeling falls into a nominal category."
    Friend "Uh. Sure."
    return

screen genderSelect:
    fixed:
        imagebutton:
            idle "Characters/TobyMale.png"
            hover "Characters/TobyMaleHighlighted.png"
            focus_mask True
            at left, zoom(.65)
            action [Call("male"),Return()]
        imagebutton:
            idle "Characters/TobyFemale.png"
            hover "Characters/TobyFemaleHighlighted.png"
            focus_mask True
            at right, zoom(.65)
            action [Call("female"),Return()]

label male:
    $gender_lookup.update(dict(zip(love_interest_keys,male_pronouns)))
    $li_gender = 'male'
    return

label female:
    $gender_lookup.update(dict(zip(love_interest_keys,female_pronouns)))
    $li_gender = 'female'
    return

label wakeUp:
    hide screen objOverlay
    #swap background here
    scene room with fade
    show Friend at left
    Friend "[player]? {size=+10}[player]?!{/size}"
    player "{size=+10}AHHHHHHHHHHHHHHHHHHHHHHHH!{/size}"
    play sound "audio/SFX/thud.wav"
    show Friend Shocked at center with vpunch
    "(*thud*) Oww... "
    Friend "{size=+10}[player]? Are you okay?{/size}"
    play music "audio/Music/NeverWorkedThere.mp3" fadein 5.0
    player "Yeah. Other than the fact that I just faceplanted to the floor."
    show Friend Sad
    Friend "Your'e so mean! And here I was trying to help you."
    Friend "..."
    show Friend
    Friend "Was it about {i}that{/i} again?"
    player "Huh? Oh. No."
    Friend "Then what?"
    player "Remember the field trip we took to that one science lab in the third grade?"
    show Friend Wink
    Friend "I just remember that the teacher was {b}HOT{/b}."
    show Friend
    player "OMIGOSH, [Friend]! No way! He's {i}waaaaaay{/i} too old."
    Friend "Hey, age is just a quantitative thing. It's the qualitative data, like his looks, that matter."
    player "Do you even know what those words mean?"
    Friend "Shut up! Of course I do."
    Friend "Anyways, what about you?"
    Friend "Are you still in love with that kid from third grade?"
    player "Sometime. I'd imagine meeting them again."
    hide Friend
    call screen genderSelect
    show Friend

    player "They(li) would be running with toast in their(li) mouth."
    Friend "They(li)'d be running late to class."
    player "Then ..."
    Friend "Bam! You'd crash into them(li)."
    player "They(li)'d start apologizing. We'd talk and realize that were childhood friends ."
    Friend "You're {i}so{/i} unoriginal."
    Friend "That's the plot device of at least half the shoujo manga out there."
    player "Still, I think it'd be nice."
    Friend "Too bad the chances of that happening are close to zero."
    player "Based on what data?"
    Friend "Based on ordinal data."
    Friend "On a scale from zero to five."
    Friend "Zero being impossible and five being guaranteed ..."
    Friend "How likely do you think this scenerio is? "
    player "Well, I don't think this is even valid evidence."
    Friend "Just answer the question!"
    player "Fine. I'd say a two."
    Friend "And, I'd say zero."
    Friend "And when you take the average, you get one."
    Friend "One is close to zero. Therefore, the chances are close to zero."
    player "That makes absolutely no sense."
    player "First of all, you can't take the average of ordinal data."
    player "Plus, those response are based off opinions."
    show Friend Wink
    Friend "But I sounded smart, didn't I?"
    show Friend
    player "I'd give the quality of these notes an A for effort."
    stop music

    Friend "So are you sure about leaving?"
    "It's not like [Friend] to be so concerned."
    player "Are you having doubts [Friend]."
    Friend "A little. I mean we have roof over our head and food."
    Friend "What more could we hope for?"
    player "A real mattress for starters. Plus we can't stay here forever [Friend]."
    show Map at pos(600,300) with easeinbottom
    Friend "But are you sure about following this old map?"
    hide Friend
    player "This old map led us to this shelter in the first place."
    hide Map
    Friend "But don't you find it suspicious."
    show Notebook at pos(600,300) with easeinbottom
    Friend "A notebook full of data, terms and a map."
    Friend "Why would the scientist, over ten years ago, give little kids notebooks full of data?"
    hide Notebook
    show Friend
    player "What you don't trust the HOT scientist"
    Friend "HOT and CRAZY scientist. It still doesn't make any sense."
    player "We got no where else to go [Friend]."
    Friend "but ..."
    player "Do you want to be foraging for food for the rest of your life?"
    Friend "Fine. Lets go."
    Friend "When we get dissected, I'm going to tell you, I told you so."
    return

label rivalMeeting:
    scene outside mark with dissolve
    "Some time later, you see a smoldering fire and a makeshift tent."
    player "Maybe we can trade for some water with whoever lives here."
    show Friend
    Friend "(*shrugs*) Eh, worth a shot I guess."
    hide Friend
    player "{size=+10}Hello?{/size}"
    player "{size=+10}Anyone home?{/size}"
    "I think I see someone coming out of the tent."
    show Rival with easeinbottom
    $renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "<to 4>audio/Music/rival.wav"
    Rival "Yes. Now shoo."
    player "We want to trade."
    Rival "Judging by your clothes, I doubt you have anything worthwhile."
    Friend "How rude."
    Rival "That applies to your tiny friend over there too."
    Rival "Now shoo."
    player "[Friend] and I just want to trade some supplies."
    Rival "Oh, we're doing names now?"
    Rival "I'll humor you with some nominal data."
    Rival "My name is [Rival]. Now {i}shoo{/i}."
    player "Will you at least take a look?"
    play sound "audio/SFX/refusal_1_karen.mp3"
    Rival "I'm doing real research and don't have time for your riffraff."
    player "Fine. We're leaving"
    player "Well that was a waste of time."
    Friend "Not a complete waste of time."
    Friend "While you we're busy talking, I collected some quantitative data."
    Friend "Take look at this."
    scene rock
    pause
    Friend "Doesn't this symbol look familiar?"
    player "I looks like the ones on the map."
    Friend "And the one we found at the shelter."
    player "We must be halfway there."
    stop music
    return

label loveInterestMeeting:
    scene outside with dissolve
    $renpy.music.set_volume(0.2, delay=0, channel='sound')
    queue sound ["audio/SFX/footstep_dirt_walk_run_01.wav","audio/SFX/footstep_dirt_walk_run_02.wav"]
    player "Shh... {size=10}[Friend], do you hear that?{/size}"
    Friend "Hear what?"
    $renpy.music.set_volume(0.5, delay=0, channel='sound')
    queue sound ["audio/SFX/footstep_dirt_walk_run_01.wav","audio/SFX/footstep_dirt_walk_run_02.wav","audio/SFX/footstep_dirt_walk_run_03.wav","audio/SFX/footstep_dirt_walk_run_04.wav","audio/SFX/footstep_dirt_walk_run_01.wav","audio/SFX/footstep_dirt_walk_run_03.wav","audio/SFX/footstep_dirt_walk_run_02.wav","audio/SFX/footstep_dirt_walk_run_04.wav"]
    player "That."
    play sound "audio/SFX/thud.wav"
    "{size=+10}*Crash*{/size}"
    scene outside with vpunch
    "You see a person with toast in their(li) mouth."
    show LI with easeinbottom
    LI "I'm so sorry. Are you okay?"
    "Could this be fate?"
    player "I'm alright. (You back away slowly)."
    LI "Are you sure? I have some band aids if you need it."
    play music "audio/Music/Fancy cakes 120 BPM.wav" fadein 5.0
    LI "My name is [LI] by the way."
    player "I'm [player], and this is [Friend]"
    LI "I'm glad you're okay. I shouldn't have been running blindly like that."
    LI "Where are you guys heading?"
    show Friend at left with easeinleft
    Friend "{size=+10}We're heading to a secret ...{/size}"
    show Friend at offscreenleft with easeoutbottom
    "I quickly covered [Friend]'s mouth. It would be too risky telling a random person our plans."
    player "I don't think we should be telling you."
    player "After all, we just met."
    "I hope I don't sound nervous."
    LI "That's fair."
    LI "I'm heading out to a shelter. I heard they have plenty of rations."
    LI "You two can come along if you'd like."
    "This sounds suspicious. Why all the friendliness towards two strangers?"
    player "And what do you gain by telling us this?"
    LI "Satisfaction of helping out a fellow traveler."
    "Satisfaction? Seriously?"
    player "We'll pass on the offer."
    LI "Then, I guess this where we part ways."
    player "Yeah."
    LI "It was nice meeting you two."
    Friend "It was nice meeting you too, totally-not-suspicious stranger."
    hide LI
    show Friend at center
    Friend "Are you ok [player]. You look at bit flustered."
    player "Flustered? What data are you basing that off of?"
    Friend "Not everything has to be based on data you know."
    player "So you have no proof."
    show Friend Wink
    Friend "The nominal data says otherwise. Your face is completely red."
    $renpy.music.set_volume(0.2, delay=0, channel='sound')
    queue sound ["audio/SFX/footstep_dirt_walk_run_01.wav","audio/SFX/footstep_dirt_walk_run_02.wav","audio/SFX/footstep_dirt_walk_run_03.wav","audio/SFX/footstep_dirt_walk_run_04.wav"]
    stop music
    return

label discoverTheLab:
    scene outside
    show Map at pos(600,300)
    player "Are you ready? The map says we should be getting close to the meeting place."
    hide Map with easeoutbottom
    show Friend
    Friend "Are you sure we should be trusting a random notebook from a scientist?"
    Friend "You remember they caused this whole mess right?"
    Friend "It’s been ten years since the apocalypse. Yet, people are still afraid of scientist and science."
    player "We don't know that. Plus, we're already here."
    scene outside cave
    Friend "Are you sure this is the place?"
    Friend "Just looks like a cave to me."
    player "Well lets take a closer look."
    "I see a big wooden door."
    scene cave
    Friend "You go first, afterall this is your idea."
    $renpy.music.set_volume(1, delay=0, channel='sound')
    play sound "audio/SFX/Knocking-on-door-two-knocks.mp3"
    scene cave door
    player "{size=+10}*knock* *knock*{/size}"
    player "Hello? Anybody there?"
    return

init python in puns:
    nominal = "What a phe-{color=#259ce6}nominal{/color} question"
    ordinal = "Looks like just another {color=#259ce6}ordinal{/color} question"
    binary = "It's two hard to come up with a {color=#259ce6}binary{/color} pun."
    ratio = "I got absolute zero puns about {color=#259ce6}ratio{/color} data."
    interval = "It's hard coming up with an average pun for this {color=#259ce6}interval{/color}."

screen form():
    modal not interacting
    imagemap:
        align (0.5,0.5)
        idle "Form/Form_idle.png"
        hover "Form/Form_hover.png"
        ground "Form/Form_filled.png"

        showif(not "formName" in questionsAnswered):
            hotspot (270, 93, 229, 62) action [If(not interacting, true=Jump("formName"), false=NullAction())]
        else:
            text "{color=#000000}[player]{/color}" pos(300,113) size(20)

        showif(not "formGender" in questionsAnswered):
            hotspot (269, 159, 233, 65) action If(not interacting, true=Jump("formGender"), false=NullAction())
            text "{color=#000000}they(p),them(p),their(p){/color}" pos(275+30,169+20)
        else:
            text "{color=#000000}they(p),them(p),their(p){/color}" pos(275+30,169+20)

        showif(not "formWeight" in questionsAnswered):
            hotspot (270, 227, 233, 65) action If(not interacting, true=Jump("formWeight"), false=NullAction())

        showif(not "formSick" in questionsAnswered):
            hotspot (263, 294, 240, 69) action If(not interacting, true=Jump("formSick"), false=NullAction())

        showif(option != 1):
            hotspot (50, 464, 86, 79) action [SetVariable("option",1),If(not interacting, true=[Jump("formInterest")], false=NullAction())]
        showif(option != 2):
            hotspot (154, 466, 73, 73) action [SetVariable("option",2),If(not interacting, true=[Jump("formInterest")], false=NullAction())]
        showif(option != 3):
            hotspot (249, 468, 76, 71) action [SetVariable("option",3),If(not interacting, true=[Jump("formInterest")], false=NullAction())]
        showif(option != 4):
            hotspot (346, 469, 76, 68) action [SetVariable("option",4),If(not interacting, true=[Jump("formInterest")], false=NullAction())]
        showif(option != 5):
            hotspot (443, 466, 72, 72) action [SetVariable("option",5),If(not interacting, true=[Jump("formInterest")], false=NullAction())]

label applyingForTheLab:
    #swap background
    scene cave door
    play music "audio/Music/bensound-enigmatic.mp3"
    Scientist "Have you filled out the applications on page 34?"
    show Friend
    Friend "Applications?"
    Friend "The world has fallen apart. Over half of humanity has been wiped out, and you want us to fill out {i}applications?{/i}"
    Scientist "It's just a formality, but please fill them out."
    Scientist "Oh, and since you're a group of two, I'll be expecting something extra."
    Friend "Dude, we have nothing valuable on us."
    Scientist "I was think something more punny."
    player "Excuse me?"
    "Did he just say-"
    Scientist "I'll take payment in the form of data puns."
    $option = -1
    $questionsAnswered = Set([])
    label formContinue:
        $interacting = False
        window hide
        show screen form()
        pause

    label formFinished:
        hide screen form
        pass
    return

label formName:
    $interacting = True
    show screen form()
    play sound "<to 1>audio/SFX/Slow-Writing-With-A-Pen.mp3"
    $questionsAnswered.add("formName");
    menu:
        "Hm, this looks like ..."
        "nominal":
            player "[puns.nominal]"
            if(len(questionsAnswered)>=5):
                jump formFinished
            jump formContinue
        "ordinal":
            player "[puns.ordinal]"
        "interval":
            player "[puns.interval]"
        "ratio":
            player "[puns.ratio]"
        "binary":
            player "[puns.binary]"

    Scientist "I think it was a phe - {color=#259ce6}nominal{/color} question"
    Scientist "Get it? It's a pun on 'phenomenal' and the type of data this question is asking for."
    Scientist "Not funny? Tough crowd."
    if(len(questionsAnswered)>=5):
        jump formFinished
    jump formContinue


label formGender:
    $interacting = True
    show screen form()
    $questionsAnswered.add("formGender");
    python:
        seperator = ", "
        pronouns = seperator.join(list(set(gender_lookup.values())))

        "Gender pronouns: [pronouns]"

    menu:
        "Looks good!":
            pass
        "Let me fix this...":
            call fixPronouns from _call_fixPronouns

    play sound "<to 1>audio/SFX/Slow-Writing-With-A-Pen.mp3"
    if(len(questionsAnswered)>=5):
        jump formFinished
    jump formContinue
    return

label formWeight:
    $interacting = True
    show screen form()
    play sound "<to 1>audio/SFX/Slow-Writing-With-A-Pen.mp3"
    $questionsAnswered.add("formWeight");
    "Well, maybe I can fit a pun in here"
    menu:
        "[puns.nominal]":
            pass
        "[puns.ordinal]":
            pass
        "[puns.interval]":
            pass
        "[puns.ratio]":
            if(len(questionsAnswered)>=5):
                jump formFinished
            jump formContinue
        "[puns.binary]":
            pass
    Scientist "It was a good try, but that joke doesn't quite work for ratio data."
    if(len(questionsAnswered)>=5):
        jump formFinished
    jump formContinue
    return

label formSick:
    $interacting = True
    show screen form()
    play sound "<to 1>audio/SFX/Slow-Writing-With-A-Pen.mp3"
    $questionsAnswered.add("formSick");
    "I'm glad both [Friend] and I are healthy."
    "This question is obviously ..."
    menu:
        "nominal":
            "[puns.nominal]"
        "ordinal":
            "[puns.ordinal]"
        "interval":
            "[puns.interval]"
        "ratio":
            "[puns.ratio]"
        "binary":
            player "[puns.binary]"
            if(len(questionsAnswered)>=5):
                jump formFinished
            jump formContinue
    "Hold on. Maybe this one was trickier than I thought."
    "According to the notebook, this would be binary"
    if(len(questionsAnswered)>=5):
        jump formFinished
    jump formContinue
    return

label formInterest:
    $interacting = True
    show screen form()
    play sound "<to 1>audio/SFX/Slow-Writing-With-A-Pen.mp3"
    $questionsAnswered.add("formInterest");
    "I bet [Friend] would have a good pun for this."
    menu:
        "[puns.nominal]":
            pass
        "[puns.ordinal]":
            if(len(questionsAnswered)>=5):
                jump formFinished
            jump formContinue
            return
            return
        "[puns.interval]":
            pass
        "[puns.ratio]":
            pass
        "[puns.binary]":
            pass

    Friend "Hold on [player]! That's no ordinary question."
    Friend "That there is an ordinal question."
    Friend "[puns.ordinal]"
    if(len(questionsAnswered)>=5):
        jump formFinished
    jump formContinue
    return

label enterHideout:
    "I'll just leave this under the door."
    scene cave door app
    pause
    play sound "audio/SFX/door_old_wooden_squeak_01.wav"
    scene cave door open
    pause
    show Scientist
    Scientist "Welcome to the lab, [player] and [Friend]. We're just about to start orientation. My name is [Scientist]"
    Scientist "Follow me. There were a couple travelers who arrived before you two."
    play music "audio/Music/NeverWorkedThere.mp3"
    scene indoor
    "Across the room you see two familiar faces."
    show LI at left
    show Rival at right
    "It's [LI] and [Rival]"
    Scientist "Take a seat. Let's play an icebreaker."
    Scientist "I'm sure all of you have read one of my notebooks. Inside, you should have found some definitions."
    Scientist "Those definitions are for five types of data: nominal, interval, ratio, ordinal, and binary."
    Scientist "For this ice breaker, I want each of you to state a fact about yourself for each category."
    hide Scientist
    hide LI
    show Friend at left
    show Rival at right
    Friend "What if we don't remember the categories?"
    Rival "Then you shouldn't be here."
    hide Friend
    hide Rival
    show Scientist
    Scientist "Questions are absolutely fine. All we have left are questions."
    Friend "Um..."
    Scientist "Yes, feel free to inquire if you need something defined."

    label questions:
        show Scientist at center with move
        menu:
            "No questions":
                jump icebreaker
            "What is nominal data?":
                show Scientist at left with move
                show Rival at right with moveinright
                Rival "Obviously nominal means name. Therefore, it is a type of data that is used to label variables without providing any quantitative value."
                Rival "It is the simplest form of a scale of measure. Unlike ordinal data, nominal data cannot be ordered and cannot be measured. {i}Duh.{/i}"
                hide Rival
            "What is binary data?":
                show Scientist at left with move
                show LI at right with moveinright
                LI "I think binary means that there can only be two values. For example, did I think that was a good question?"
                LI "A binary answer would be yes or no. Yes I think that was good question"
                hide LI
            "What is interval data?":
                Scientist "Interval data is when we have a variable that contains numeric values that are ordered and where we know the exact differences between the values. "
                Scientist "Keep in mind that there's no true zero here."
                Friend "Huh?"
                show Rival at right with moveinright
                Rival "In other words, you can't add or divide these values. {i}Duh.{/i}"
                hide Rival
            "What is ratio data?":
                Scientist "Ratio data consists of ordered units, and we know the exact difference between two values."
                Scientist "Ratio data have a true zero, and can be multiplied or divided."
                show Scientist at left with move
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
        scene indoor
        "[Rival],[Friend], and I, have all answered the questions"
        show LI
        LI "Oh wow. This makes me kind of nervous"
        LI "For nominal data, my name is [LI]. For binary data, between dead and alive. I am alive."
        show LI at left with move
        show Friend at right with moveinright
        Friend "Keep it up! Only three more to go."
        hide Friend
        show LI at center with move
        LI "My age is XX. That counts as interval right? For ratio data my height is 167cm"
        Scientist "What about ordinal?"
        LI "What {i}about{/i} ordinal?"
        Scientist "Do you have an ordinal example?"
        LI "Um, let me think..."
        player "If [LI] doesn't come up with an example of ordinal data, they(li) might be kicked out of the team."
        player "This might be a good thing. It would mean less competition."
        player"..."
        player "But competition should be the last thing on my mind right now..."
        player "Stupid good conscience."
        player "How about on a 1 to 5 scale? One being extremely easy and five being extremely hard. How hard was your trip to this lab?"
        LI "I'd say a solid 4."
        Scientist "Nice teamwork, you two."
        Scientist "It's normal to not know everything all at once."
        Scientist "{size=10}I certainly didn't. Who could of known...{/size}"
        Friend "Um..."
        Scientist "I hope this set a good example for all of you."
        Scientist "Cooperation is key, especially during these dark times."
        hide LI

    Scientist "Great, that's everyone. Be sure to review your categories. You'll need them for tomorrow's expedition"


    show Friend at left
    show Rival at right
    Friend "Expedition? We just got here."
    Rival "Tch. Speak for yourself."
    hide Friend with moveoutleft
    hide Rival with moveoutright
    show LI
    "[LI] pulls me aside"
    play music "audio/Music/Blue-Ridge_Looping.mp3"
    LI "Thanks for helping me out back there."
    player "I didn't do it because I like you or anything."
    LI "You like me?"
    player "No no no. I'm just a bit flustered from ice breakers."
    LI "Well, regardless I'm grateful."
    player "Of course. It's like what the weird science guy said. We're a team now."
    player "We should be focused on the main goal instead of trying to sabotage each other."
    LI "You're absolutely right. Although, it was super unexpected."
    player "What was?"
    LI "You helping me. Considering how our first meeting went, I didn't think you'd care if I messed up."
    LI "You were like my knight in shining armor, haha."
    player "(*blush*) A-anyways, it was nothing."
    player "But, you're welcome."
    hide LI
    stop music
    return

label fixPronouns:
    python:
        seperator = ", "
        male = seperator.join(list(set(male_pronouns)))
        female = seperator.join(list(set(female_pronouns)))
        nonbinary = seperator.join(list(set(nonbinary_pronouns)))

    menu:
        "[male]":
            $store.gender_lookup.update(dict(zip(player_keys,male_pronouns)))
            pass
        "[female]":
            $store.gender_lookup.update(dict(zip(player_keys,female_pronouns)))
            pass
        "[nonbinary]":
            $store.gender_lookup.update(dict(zip(player_keys,nonbinary_pronouns)))
            pass
