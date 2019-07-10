label poemresponse_start:
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day
            with wipeleft_scene
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5
    label poemresponse_start2:
        $ skip_poem = False
        if persistent.playthrough == 2:
            $ pt = "2"
        else:
            $ pt = ""
        if poemsread == 0:
            $ menutext = "Who should I show my poem to first?"
        else:
            $ menutext = "Who should I show my poem to next?"

        menu:
            "[menutext]"

            "Satori." if not s_readpoem and persistent.playthrough == 0:
                $ s_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "I'm definitely most comfortable sharing it with Satori first."
                    "He's my good friend, after all."
                call poemresponse_sayori
            "Natsuko." if not n_readpoem:
                $ n_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "I told Natsuko I was interested in his poems yesterday."
                    "It's probably only fair if I shared mine with him first."
                call poemresponse_natsuki
            "Yuuri." if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "Yuuri seems the most experienced, so I should start with him."
                    "I can trust his opinion to be fair."
                call poemresponse_yuri
            "Mateo." if not m_readpoem:
                $ m_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "I should start with Mateo."
                    "Yesterday he seemed eager to read my poem, and I want him to know I'm putting in effort."
                call poemresponse_monika
        $ poemsread += 1
        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4):
            jump poemresponse_loop

    # Reset variables for next time
    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

label poemresponse_sayori:
    scene bg club_day
    with wipeleft_scene
    $ poemopinion = "med"
    if s_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif s_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_s_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_s_end"
        call expression nextscene
    return

label poemresponse_natsuki:
    scene bg club_day
    with wipeleft_scene
    $ poemopinion = "med"
    if n_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif n_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_n_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_n_end"
        call expression nextscene
    return

label poemresponse_yuri:
    scene bg club_day
    with wipeleft_scene
    $ poemopinion = "med"
    if y_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif y_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_y_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_y_end"
        call expression nextscene
    return

label poemresponse_monika:
    scene bg club_day
    with wipeleft_scene
    if m_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif m_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_m_start"
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_m_end"
        call expression nextscene
    return

label ch1_y_end:
    call showpoem(poem_y1, img="yuuri 1t")
    y "I'm sorry if you have any trouble reading my handwriting."
    mc "...did you not just see my handwriting?"
    mc "I'm surprised you were able to read it."
    mc "Your penmanship is perfect."
    mc "Don't even worry about that."
    y 1u "Well... Thank you."
    y 6v "It's just...it took you a long time to read it."
    mc "Well, maybe I was just re-reading it a few times because I really liked it."
    mc "Have you considered that?"
    "Yuuri's face turns beet-red."
    "He quickly looks away, laughing nervously."
    y 7q "There... there's no way you could think that."
    mc "Well, I do."
    mc "I really like your poem, Yuuri."
    mc "I like the imagery and the atmosphere."
    mc "I like how it made me feel while I was reading it."
    mc "And I really like how it was short, yet descriptive."
    y 7t "It wasn't too short, was it?"
    y 4q "I usually prefer shorter poems... but can write a longer one next time if you'd prefer!"
    "I could make a dirty joke right now...but I'm bigger than that."
    mc "Not at all."
    y 6i "I'm...really happy that you liked it."
    y 1b "Since it's our first time sharing, I wanted to write something a little more mild."
    y 1d "Something easy to digest, I suppose."
    mc "Tell me more about this metaphorical thirst in your story."
    mc "What are you thirsty for?"
    y 6q "Well...uh...I suppose the answer could be interpreted in many ways."
    y 4q "You, as the reader, can feel free to look into it as you'd like."
    "Okay, fine. Don't tell me what it's about."
    mc "You sure know a lot about writing."
    mc "I'm very impressed!"
    y 1i "It's nothing, really."
    y 1c "But it does make me happy that you think that."
    y 3b "Remember, it won't be long before you pick up on these things too."
    mc "Well, I'm feeling very inspired by your feedback."
    mc "So I'll be sure to apply it to my next poem."
    y 1d "I'm excited to hear that."
    y 1b "I look forward to seeing what you've learned."
    return

label ch2_y_end:
    call showpoem(poem_y2)
    y 1u "Um...I was a little more daring with this one than yesterday's."
    mc "I can see that."
    mc "It's a lot more...uh...metaphorical."
    y 1b "That's right."
    y 4b "It's a bit closer to my preferred writing style."
    y 4k "Using the poem as a canvas to express vivid imagery and conveying emotions through them."
    mc "So...what's this poem about?"
    y 4u "Ah...well...I wanted to express the way it feels for me to indulge in my more unusual hobbies..."
    y 4v "The sorts of things I'm usually forced to keep to myself."
    y 1s "So, I sometimes enjoy writing about them."
    mc "Like, what kind of hobbies?"
    show yuuri 7p
    "I ask without thinking."
    "Yuuri is visibly shaken."
    y 7o "Ah--! Well, that...that's not important at the moment."
    y 1q "Perhaps we'll discuss it another time."
    mc "It's fine."
    mc "I'm sorry for prying."
    mc "I was just curious."
    mc "I understand how it can be embarrassing to talk about what many might consider an unusual interest."
    y 1f "Do you have any of your own, [player]?"
    mc "Well...it depends on what the definition of 'unusual' is."
    mc "What's normal for me might be considered weird for someone else, you know?"
    y 1a "That's true." 
    y 4b "That's why people should respect each other's individuality rather than make fun of them for it, even if it's difficult." 
    y 4h "After all, if I hadn't learned to embrace my own weirdness, I'd probably hate myself." 
    y 1u "Sorry...I'm just ranting a bit now." 
    y 1s "But I'm glad you're a good listener." 
    y 1c "In fact...you're good at a lot of things." 
    y 1a "Writing...listening...even breaking up fights..."
    y 1u "There really aren't a lot of people like you, [player]..."
    mc "Yuuri ..."
    y 6t "Sorry...It's just how I feel." 
    y 4u "I never thought I would be so comfortable sharing my writing." 
    y 1s "But now, I look forward to it." 
    y "It's a nice feeling and I thank you for that."
    "Yuuri smiles at me sincerely."
    return
label ch3_y_end:
    if y_appeal >= 3:
        jump ch3_y_end_special
    call showpoem(poem_y3, img="yuri 2v")
    y "Um..."
    y "I'm aware that the beach is kind of an inane thing to write about."
    y "But I did my best to take a metaphorical approach to it."
    if not n_readpoem or n_appeal >= 3:
        mc "You say that like you didn't even want to write about it..."
        y 2e "Oh, you haven't heard...?"
        y 2h "After yesterday, Natsuki and I...well..."
        y "It was...amusing that we wrote about something similar in such different ways."
        y "So, Natsuki wanted us to write about the same topic as each other again."
        if n_readpoem:
            mc "I see..."
            "Something tells me the poem Natsuki showed me isn't the one she plans on sharing with everyone else..."
            "Of course, I choose not to mention that to Yuri."
    else:
        mc "Yeah, Natsuki already told me about it."
        y 3t "S-She did...?"
        y "She didn't say anything weird, did she?"
        y "She just wanted us to write about the same topic again..."
    y 2f "I suppose to better compare the differences in our writing styles...or thought processes."
    y 2w "Anyway, it was her idea...!"
    y "Knowing her, it's no surprise that she'd want to do something like that."
    y "She probably just wants to show off."
    y 2v "It's not like I have a particular interest in her writing style..."
    y "I just went with her request."
    y "But..."
    y 1s "Well, I suppose it's not so bad to write about something simple on occasion."
    y 1m "It can be refreshing, you know?"
    y "It's good for me to calm my thoughts once in a while."
    mc "Yeah...I think I agree."
    mc "Thanks for sharing."
    return
label ch3_y_end_special:
    call showpoem(poem_y3b, img="yuri 4b")
    "Finishing the poem, I start to hand it back to Yuri."
    "But instead of taking it from me, she looks away."
    y "..."
    y "Do you...dislike it?"
    mc "Ah--no, of course not."
    mc "I just...don't really know how I should respond."
    "Despite Yuri's poems usually being cryptic, it wasn't hard to figure out what this one was about."
    if n_readpoem:
        "Also, this clearly isn't the poem that Natsuki said she wrote about..."
        "...Meaning I'm probably the only one she's showing this to."
    y 2v "I-I don't know if I'll be able to explain this one..."
    mc "That's fine."
    mc "I understand this one."
    y 4c "..."
    "Yuri is having an even harder time speaking than usual."
    mc "Does this one...mean a lot to you?"
    "Yuri nods."
    mc "I'm not really good with words, but..."
    mc "I'm happy that you shared it with me."
    mc "So, thank you."
    mc "And I hope we keep spending time together."
    show yuri 4e
    "Despite my inability to make eye contact, I see a faint smile emerge on Yuri's lips."
    "I once again try to hand the poem back to her."
    show yuri 4a
    "But instead, Yuri gently takes my hands and pushes them back toward me."
    "I hesitate in response to her warm touch."
    y 1v "You can..."
    y "Um..."
    y "The poem is..."
    "Once again, Yuri fails to form a complete sentence."
    mc "You mean I can keep it?"
    "Yuri nods."
    mc "I'd love to."
    show yuri 1u
    "Again, Yuri faintly smiles, as if she doesn't want me to notice."
    y "You always..."
    y "You always...make me feel nice."
    y "I know I'm not good with people, but..."
    y "I hope that...I can return the favor sometimes."
    mc "Yeah."
    mc "Don't worry."
    mc "I think you do a good job."
    "Yuri finally turns back toward me."
    y 1s "I guess...we should move on before Monika says something."
    y "But I'm sure we can talk again later..."
    mc "Yeah."
    mc "I'm sure we will."
    "With that, Yuri timidly smiles at me, and I return to my seat so I can put her poem away."
    return

label ch1_n_end:
    call showpoem(poem_n1, img="natsuko 7y")
    n 7y "Impressive, right?"
    mc "Well... Um... It's..."
    "...Kind of dumb?"
    n 5z "Yeah, I knew you'd love it."
    n 7k "Most everyone in high school thinks writing has to be all sophisticated and stuff."
    n 7m "So, people usually don't take my writing seriously."
    n 3d "But you seem like the type who understands how effective simple writing can be."
    mc "Well the point of writing is for people to express themselves."
    mc "A person's writing style wouldn't make their message any less valid."
    n 5l "Yes, exactly!"
    n "I knew you'd understand!"
    n 3l "I like when something is easy to read..."
    n "But it hits you hard. Like in this poem."
    n 3m "Seeing everyone around you do great things can be really disheartening."
    n 1k "So I decided to write about it."
    "Wait...this poem was actually about something?"
    n 3l "The other nice thing about simple writing is that it puts more weight on the wordplay."
    n 5z "And, to me, nothing brings out feeling like poems that rhyme!"
    "I re-read the poem, fascinated."
    "Now that I know the thought process behind it, I can definitely see the message."
    "I'm actually kind of amazed I missed it the first time."
    mc "So you did!"
    mc "Wow, more when into this than I realized."
    n 7y "That's what it means to be a pro!"
    n 7d "I'm glad I was able to teach you something!"
    n 5d "I bet you didn't expect that from me, did you?"
    mc "I guess not. Thank you for the lesson."
    "I decide to humor him with that last comment."
    "I'm not sure what he meant by that."
    "But if Natsuko is feeling proud, than I won't take that away from him."
    return

label ch2_n_end:
    call showpoem(poem_n2)
    n 1d "Not bad right?"
    "I re-read the poem a couple times, nodding to myself."
    mc "..."
    mc "I think I get it. The message in this poem is, don't be a jerk and judge someone for their weird hobbies."
    mc "Am I right?"
    n 1c "..."
    n "What? No..."
    n "Are you serious?"
    mc "Uh..."
    n 7q "Jeez, and here I thought I made the message pretty straight forward, too."
    n 7c "Do I really need to explain it?"
    mc "Huh? So Trevor and his dolls aren't an analogy for you and your comic books?"
    "Natsuko merely smirks and rolls his eyes at me."
    n 5z "Haha! Gosh, you're such a dummy sometimes!"
    "My face burns with embarrassment."
    mc "Well, I thought you were using a simple analogy to tackle complicated issues!"
    n 4e "I did! But you missed the point entirely."
    mc "..."
    n 5s "*Sigh*. Alright, let me explain."
    n 3w "See, sometimes...we come across people that annoy the hell out of us."
    n "They could be the sweetest person in the world, be talanted, super smart...whatever, right?"
    n 3c "But, like...no matter how cool that person may be...there's just something about them that rubs us the wrong way."
    n "The subject of the poem literally has no reason to hate Trevor."
    n "They don't even know why they hate him."
    n "They're just annoyed by everything he does."
    n "WE know why the subject hates Trevor. It's because they're jealous of him."
    n 1w "And jealousy makes people do some pretty immature things."
    n 1c "Don't you see?"
    n 3b "The subject doesn't really care that Trevor plays with dolls." 
    n "They're just trying to find something--anything--to nit-pick about him in order to try and justify their contempt."
    n 1k "The message here is; yes, you will get annoyed with perfectly harmless people."
    n "But instead of trying to fuel your hatred by finding the one thing wrong with the person who annoys you..."
    n 1k "You need to focus more on people's good qualities in order to get yourself out of that mindset born of envy." 
    n "I mean...you can't just hate someone because they happen to be good at things you're not good at."
    n "Right?"
    "I'm a little taken aback by Natsuko's message."
    "It's a lot deeper than I thought."
    "But after giving the poem one more look, I finally catch on."
    mc "Oh, I see!"
    mc "So *you're* the subject of the poem...and Yuuri is the Trevor metaphor."
    n 6p "Gah! I...well...that's not...!"
    n 7w "Whatever!"
    n "It can be about anything."
    n 7b "I wrote it to be easy for anyone to relate to."
    mc "Well, if you really think about it, it can also be interpreted as not judging people for their weird hobbies or guilty pleasures."
    mc "Like collecting dolls. Or comic books."
    "I mutter that last part to myself."
    n 7q "There's really nothing to interpret. I already told you exactly what it's about."
    mc "Well, yesterday Yuuri taught me that writing can be interpreted in any way the reader likes, even if there is a straight forward message."
    n 7r "Oh, Yuuri's an idiot! What does *he* know?!"
    n 7s "Just because he uses big complicated words doesn't mean he's a literary genius..."
    mc "I knew it! He *is* the Trevor metaphor!"
    n 7x "...!"
    "I smile as I hand Natsuko his poem."
    mc "You can learn from your own messages, Natsu."
    mc "In any case, I can definitely relate to both messages in this poem, and I'm sure everyone else can too."
    mc "If it makes you feel better, I really like this poem more than yesterday's. I like the sass and flow of it."
    show natsuko 7k
    mc "You did a very good job with this one." 
    n 7ac "Hm. I figured you would like it." 
    n 7t "My writing always has good messages to take away."
    n 3y "My poems don't just make you feel emotions, it helps you learn what those emotions are in a simple and fun way."
    n 3d "Remember that."
    n 1a "Tomorrow's poem is gonna be even better, so look forward to it."
    return
label ch3_n_end:
    if n_appeal >= 3:
        jump ch3_n_end_special
    call showpoem(poem_n3)
    n 2a "Yeah..."
    n "I felt like I kept writing about negative things, so I wanted to write something with a nice message for once."
    n 2z "Besides...the beach is awesome!"
    n 2j "Kinda hard to write anything negative about the beach."
    if not y_readpoem or y_appeal >= 3:
        mc "So you decided to write about the beach first, and then came up with the message later?"
        n 2c "Yeah, well..."
        n "It's only because of what happened yesterday."
        n 5q "I mean, after Yuri and I realized we kind of wrote about the same thing..."
        n "She wanted to pick a topic and have us both write about it, or whatever."
        if y_readpoem:
            mc "I see..."
            "Something tells me the poem Yuri showed me isn't the one she plans on sharing with everyone else..."
            "Of course, I choose not to mention that to Natsuki."
    else:
        mc "Well, Yuri's take on it was a little more solemn."
        n 5h "Well, that's--"
        n 42c "Jeez...she better not have said anything bad about mine!"
        n "After all, she was the one who wanted us to write about the same topic."
    n 1s "Ugh...you can really see her doing that, too."
    n "Making us write about a simple topic, then trying to impress me by coming up with something all fancy."
    n 1w "Well, it's not like I care."
    n "I just did it anyway."
    n 1q "I mean, I guess mine ended up being kind of metaphorical too..."
    n "...But there's nothing wrong with doing that once in a while!"
    n "At the very least, it was good practice."
    return
label ch3_n_end_special:
    call showpoem(poem_n3b)
    n 1q "..."
    n "...Why are you looking at me like that?"
    n "If you don't like it, then just say it."
    n 1u "I won't...get mad."
    mc "No, it's not that I don't like it...!"
    mc "It was just...a little surprising to read."
    if y_readpoem:
        "This clearly isn't the poem that Yuri told me she had written..."
        "...Meaning I'm probably the only one she's showing this to."
    mc "Er...I guess I'm not used to hearing such nice things coming from you..."
    n 1h "D-Don't just say that!"
    n 1n "Dummy..."
    n "What do you think...the point of writing is?"
    n 1u "Expressing things that you can't just say..."
    mc "Yeah...I understand."
    mc "I'm sorry for missing the point sometimes."
    mc "I always mean well..."
    mc "And...I'm happy that you showed this to me."
    mc "I liked it."
    n 1h "Well...yeah..."
    n 1q "I'm...I'm a pro, so..."
    "Natsuki mumbles, completely failing to sound confident like she usually does."
    n "Just..."
    n 12c "Remember that...I can think these things sometimes, too!"
    n "You know, when you're nice to me, it's..."
    n 12a "..."
    n "...Meaningful."
    mc "Ah...I'm glad."
    "Sensing Natsuki is satisfied, I start to hand the poem back to her."
    "But as I do so, Natsuki takes my hands and pushes them back away."
    "Her small, soft hands surprise me with their assertion."
    n 12b "I don't want it."
    mc "Eh...?"
    mc "Why not?"
    n 12c "I just don't!"
    n "Jeez..."
    "I realize what Natsuki is doing."
    "Unable to be honest, she's trying to give me the poem in a roundabout way."
    mc "Well...in that case, I'm going to keep it."
    "Instead of teasing her, I choose to go along with it."
    n 1t "...Good."
    n "If you didn't, I would..."
    n "..."
    n 1h "Never mind..."
    n 1q "Just...I'm glad that you want it."
    "Natsuki backpedals on her words and leaves it at that."
    "Despite her best efforts to hide her expression, I can see her faintly smiling to herself."
    n "That's all for now, so..."
    n 1s "Go put it away before someone sees it, okay?"
    mc "Ah...yeah."
    mc "I'll go do that."
    "With that, I return to my seat so that I can put away Natsuki's poem."
    return

label ch1_s_end:
    call showpoem(poem_s1)
    mc "...Satori... when did you write this?"
    s 1k "Uhh... it's a secret."
    mc "You wrote this just this morning, didn't you?"
    s 5m "No!..."
    s 5k "..."
    s 4l "Maybe... a little bit..."
    mc "You can't answer \"a little bit\" to a yes or no question."
    s 1k "Ah--- I forgot to do it last night."
    s 7l "But, hey, I tried my best..."
    mc "Well, truthfully, it is pretty good for something that was thrown together in 5 minutes."
    mc "I like how you have bits that rhyme and bits that don't."
    mc "That's pretty cool."
    mc "It does make me wonder what you can write if you actually took the time to think about it first."
    s 10r "Hehe... well, I happen to write better when I do it last-minute than when I sit to think about it..."
    mc "Well, that sounds like something that would work for you."
    mc "This poem is all you, in fact. Especially that last line."
    s 10z "I made eggs and toast before I came to get you."
    mc "Ah. That's why we got to school later than usual."
    s 7h "It's bad to skip breakfast."
    s 1g "You know it makes me cranky."
    mc "Yeah, because you never have cranky days on a full stomach."
    mc "Anyway, thanks for sharing your poem with me."
    s 7x "Wasn't this fun?"
    s 4q "I'm really glad Mateo came up with this idea!"
    mc "...Uh, yeah. He's the {i}best{/i}."
    s 5x "And tomorrow I'm gonna write the best poem ever!"
    "Satori seems too excited about his writing to pick up on my sarcasm."
    mc"Okay, but if it sucks, I get to ridicule you harshly."
    s 1m "Eh? That... that's not..."
    mc "Satori...chill."
    mc "I'm just messing with you."
    s 3ac "Man, it's hard to tell with you sometimes."
    mc "I'm sure whatever you write will be awesome, and I look forward to reading it."
    return

label ch2_s_end:
    call showpoem(poem_s2)
    mc "Holy Crap..."
    mc "Satori... I...I can't believe you really wrote this..."
    s 10z "Well, of course I did. You were there when I wrote it!"
    s 7x "I told you yesterday that I was going to write the best poem ever."
    "I look at the poem over and over again."
    "I lower my eyebrows."
    "This poem is beautiful, but also a bit concerning."
    mc "Can I ask you a question?"
    s 1a "Sure."
    mc "...What happens when the cookie jar is empty?"
    s 1b "..."
    s "...What do you mean?"
    "I look at the poem again."
    "Each time I read it, I grow increasingly worried."
    "I don't know if I'm reading too much into this, but I do feel the need to address my concern."
    "I decide to choose my words carefully."
    mc "Satori...I need you to promise me something."
    s 1d "Anything."
    mc "I need you to promise me that, if your cookie jar ever runs out of happy thoughts...you need to tell me so that I can refill it."
    mc "Will you do that for me?"
    s 1k "..."
    s 1l "C'mon...don't read too much into it."
    s 1h "It's just a poem."
    mc "There's a lot of feelings in this one."
    mc "Feelings that make me think that maybe some of those happy thoughts should stay where they are, instead of being put into bottles."
    mc "Don't you think?"
    s 10d "Okay, okay. I get it."
    s 10y "Jeez...sometimes I think you worry about me too much."
    mc "Well, of course I do."
    mc "You're a precious cinnamon bun who needs to be protected at all costs."
    show satori 1o
    "I take immediate delight in embarrassing him."
    s 5p "Hey, I am not!"
    "I can't help but giggle a little."
    s 1ac "Jeez, that's enough."
    s 1ap "Why do you always have to ruin our moments by saying something dumb or weird?"
    "He says that, but he can't help but break into a small smile anyway."
    mc "You love me for being dumb and weird."
    mc "Admit it."
    "He tries to hold back, but he finally relents and shows me a big smile."
    s 10d "Haha! Fine! You win."
    mc "In any case...you seem really passionate about your writing."
    "I hold up his poem."
    mc "It shows."
    s 1d "Well...I'm glad."
    "I look at the poem one more time before I hand it back to him so he can finish sharing it."
    mc "Remember what I told you."
    s 1d "I will."
    return
label ch3_s_end:
    return

label ch1_m_end:
    call showpoem(poem_m1)
label ch1_m_end2:
    show mateo 6x at t11
    m "So... what do you think?"
    mc "...Um..."
    m 1t "Speechless, I see."
    mc "It's...strange."
    mc "Very...freeform, if that's what you call it."
    m 1k "Hahaha!"
    m 3v "Please don't act like you have something constructive to say."
    m 6x "We both know you're not there yet."
    mc "Well, what do you want from me?"
    mc "It's a weird poem."
    mc "I can't even fathom what it could possibly be about."
    m 6t "Ah... well..."
    m 4s "I guess you can say I had some kind of epiphany recently."
    m 4b "It's been influencing my poems a bit."
    m 1v "You might even say it's making them 'weird.'"
    mc "...An epiphany?"
    m 1k "Yeah...something like that."
    mc "Like...what kind of epiphany?"
    m 3l "Well...don't worry about it."
    m 1n "It's not important at this point."
    m 1r "It'll all make sense later."
    mc "...Okay, then."
    "I guess I'm expected to just ignore {i}that{/i} weirdness."
    mc "So...does that mean we're done?"
    m 6d "I think so."
    m 6ab "Unless you...want something else."
    mc "I mean...I didn't really learn anything from you..."
    m 6i "Oh, is that so?"
    mc "Look...you said I should let you know if I have any suggestions for things you can do better, right?"
    mc "Well...how about giving me some helpful writing tips?"
    mc "This way I can walk away with at least some useful knowledge after each of these sessions."
    show mateo 1ab
    "Mateo considers my idea for a moment."
    m 1r "You know...you might be right."
    m 1d "As President, I should offer more advice than the others."
    m 1j "Alright then."
    m 4k "...Here's Mateo's Writing Tip of the Day!"
    m 4b "Sometimes, when you're writing a poem--"
    m 4v "Or a story--"
    m 4t"Your brain gets too fixated on a specific point."
    m "If you try too hard to make it perfect, you'll never make any progress."
    m 4k "Just force yourself to get something down on paper, then tidy it up later."
    m 4b "Another way to think about it is this:"
    m "If you keep your pen in the same spot for too long, you'll just get a big dark puddle of ink..."
    mc "What if I'm using a pencil--..."
    m 4k "...So just move your hand and go with the flow!"
    m "That's my advice for today!"
    m "Thanks for listening!"
    return

label ch2_m_end:
    call showpoem(poem_m2)
    show mateo 1a
    "What the...?"
    if y_readpoem:
        "And I thought Yuuri's poem was weird."
    mc "It's, uh...even more abstract than your last one, huh?"
    m 1d "Are you not a fan of that style?"
    mc "Oh, I do like it."
    mc "I've just never really seen anything like it before."
    mc "I guess you can say it's very unique."
    m 1k "Thank you."
    m "I do like standing out in a crowd."
    m 1b "It's no different when it comes to my writing."
    mc "Is this one also about your, ah, epiphany?"
    m 3l "Well, sometimes asking what a poem is about isn't the right question."
    m 3e "A poem can be as abstract as a physical expression of a feeling."
    m 3b "Or a conversation with the reader."
    m "So, putting it that way..."
    m "Not every poem is about something."
    mc "Isn't interpretation up to the reade...-"
    m 4k "Anyway, here's Mateo's Writing Tip of the Day!"
    m 4b "Sometimes, you'll find yourself facing a difficult decision."
    m "When that happens, don't forget to save your game!"
    "..."
    "...What?"
    m 4j "You never know when you might change your mind..."
    m "Or when something unexpected may happen!"
    m 4d "...Wait..."
    m 4l "Is this tip even about writing?..."
    m 4n "...What am I even talking about?..."
    "I glance around nervously."
    "...Who the hell is he even talking to?..."
    m 1l "...Ahaha!"
    m 1m "That's my advice for today!"
    m 1n "Thanks for listening!"
    "What the hell kind of{nw}"
        stop music fadeout 0.5
    show black onlayer front:
        alpha 0.0
        0.25
        linear 0.5 alpha 1.00
    "What the hell kind of Truman Show bullshit..."{w=0.5}{nw}
    window hide(None)
    window auto
    hide black onlayer front
    return
label ch3_m_end:
    call showpoem(poem_m3)
    show mateo 1a at t11
    "I look up at Mateo quizzically."
    mc "...Am I allowed to know what this one's about?"
    m 1d "Hm. I guess I can share my thought process behind this one."
    m 3r "See, I have nothing against learning and seeking answers."
    m "Asking questions and gaining knowledge gives life meaning, after all."
    m 3d "But you don't always have control over the kind of knowledge you receive."
    m 3g "Sometimes, you end up learning something new that you wish you never had, you know?"
    mc "I think I get it."
    mc "It's like not seeing a new movie yet and having someone spoil it for you by giving away the ending."
    m 6b "Exactly!"
    m 4d "You can't predict when someone is going to reveal something to you that you didn't want to hear."
    m 4g "Or when someone will force knowledge on you that you never even thought about."
    m 4i "But after you learn it, it gets stuck in your head and you end up overthinking it."
    m 1h "It can be annoying at the very least...or it could literally drive you insane."
    m 1d "In a way, the curiosity of the human species is almost paradoxical."
    m 3g "We're so desperate to learn and explore...but if we did find all the answers, wouldn't life lose its meaning?"
    m 1d "That's why I wrote this poem."
    m 1m "Because sometimes...ignorance is bliss."
    m 1a "Wouldn't you agree?"
    mc "..."
    mc "I do, actually."
    mc "That's pretty deep stuff, man."
    m 1k "I'm glad you like it."
    m 4b "Anyway...Here's Mateo's Writing Tip of the Day!"
    "Oh, boy. This again..."
    m 4d "..."
    m 6g "..."
    m 6o "..."
    m 1r "Sigh."
    m 1g "Look... Satori trusts you more than anyone in the world."
    m "If he's going to tell anyone what's wrong with him...it's you."
    m 3l "So just give him a couple days to cool off, then try talking to him again."
    m 1j "I'm sure he'll be more willing to open up to you at that point."
    mc "...Mateo..."
    m 1m "That's my advice for today."
    m 1e "Thanks for listening~"
    return


label ch1_n_bad:
    show natsuko 1a at t11 zorder 2
    n 1g "...Hmm..."
    mc "...?"
    n 1c "Are you..."
    n 5c "Are you taking this club seriously?"
    mc "Of course I am."
    n 1s "Right."
    n 1e "Exactly how much effort did you put into this?"
    mc "A lot, actually."
    n 5k "Hey, it's cool."
    n "You're not a writer."
    n "I get it."
    n 3l "Cheer up. I'm sure you'll improve eventually."
    n 1k "I'd point out what you need to work on, but you're better off just trying again from scratch."
    mc "Fair enough."
    mc "To each their own, I guess."
    if y_readpoem == True:
        "I can see why Yuuri said Natsuko might be biased."
    n 5w "Anyway...I guess I better show you my poem now."
    n 7y "I know you're gonna really like it, but try to contain yourself."
    return

label ch1_n_med:
    show natsuko 1a at t11
    n 1y "...Hmm...Yep!"
    n 5y "This is about what I expected from you."
    mc "...Do you mind clarifying what you mean by that?"
    n 5t "Ah--!"
    n 7t "Well, I mean..."
    n 7q "It's not a bad poem."
    n "It's just that you're new to this, so I kinda figured your writing wouldn't evoke any emotions."
    n 7g "And it didn't, to be honest."
    "I'm starting to see why Yuuri said Natsuko might be biased."
    mc "Oh, I get it."
    mc "Not childish enough for your tastes, huh?"
    n 6b "Hey! This is a Literature Club, you know!"
    n 3b "If you're gonna share your writing, prepare to receive critique!"
    mc "Fine, fine."
    n 1c "Anyway...I guess I better show you my poem now."
    n 5y "I know you're gonna really like it, but try to contain yourself."
    return

label ch1_n_good:
    show natsuko 1a at t11 zorder 2
    n 5k "..."
    mc "..."
    n 5h "What's with this?"
    mc "...What do you mean?"
    n 1d "Don't play dumb now."
    n 3w "This wasn't written by an amateur."
    n 3e "You either snagged this online or Satori brought in a ringer."
    mc "Look, I wrote this myself."
    mc "And it's my first time writing a poem."
    mc "Take it for what it's worth."
    mc "I have no reason to lie about this."
    mc "In fact, remember how I said I was interested in your poems?"
    mc "That's what I had in mind when I wrote this."
    mc "I could've been doing other things, you know."
    show natsuko 1k
    "Unbelieving, Natsuko looks over my poem again."
    "He stares at me with a suspicious expression."
    n 7i "Alright, then...beginner's luck."
    n 7h "Let's see if you can do it again tomorrow."
    mc "You seem upset that I'm accidentally good at this."
    mc "I just wanted to help you feel comfortable sharing your poems."
    n 7n "...Well, thanks, [player]..."
    n 5n "But, I think I would've felt more comfortable sharing if yours was really bad!"
    n 5s "I was expecting you to show me something pathetic so I could say, 'well, it's not great, but let me show you what real writing looks like!'"
    n 5u "And, instead, you went and wrote something really good."
    n 7m "So now, I'm self-conscious about my poem."
    mc "...Well, I'm glad to hear you liked it, but I don't want you to feel bad about your writing as a result."
    n 7q "I...don't feel bad, per-say."
    n "I just wanted my poem to..."
    n 5r "Ah..."
    n 5s "Well... Never mind."
    n 1c "I should just show it to you."
    mc "Might as well."
    mc "Mateo will make you if you don't."
    return

label ch2_n_bad:
    #Didn't like last poem or this one
    if n_poemappeal[0] < 0:
        show natsuko 1l at t11 zorder 2
        n "Say...this one's actually better than your last one." 
        n "It's nice to see you putting in some effort!"
        mc "Oh...that's good."
        n 1y "I mean...I still hate it." 
        n 1c "It's trying way too hard to be serious." 
        n 3z "But, you know...nice attempt!"
        mc "...!"
        "Why you rude, little..."
        mc "Please...do explain."
        label ch2_n_bad_sharedwithch3:
            n 5b "Look, poems don't have to be all deep-sounding just to express something." 
            n 3e "It's just gonna sound like you're forcing it, unless you naturally don't suck at it." 
            n 3w "The best advice I can give: don't bother with this style until you're on Yuuri's level..."
            show natsuko 6p
            "Natsuko stops short all of a sudden."
            n "Wait a minute..."
            n 6o "You're just trying to impress Yuuri, aren't you?"
            mc "Whoa, what're you talking about?" 
            mc "And keep your voice down..."
            n 7h "Oh, don't try to play dumb, [player]." 
            n 7r "Everyone knows Yuuri is totally into this angsty crap."
            "Natsuko practically throws my poem back at me."
            n 7w "Tell you what..." 
            n "You go ahead and impress Yuuri with your whiny little emo poems." 
            n 7b "I'll be over here writing real poetry." 
            n "Hit me up when you're ready to take this seriously." 
            n 7y "Buh-bye now."
            "With that, Natsuko dismisses me." 
            "Whatever." 
            "At least he's not the one I was trying to impress in the first place."
            $ skip_poem = True
            return

    #Liked the last poem but not this one
    else:
        n 1k "...Hm."
        n "I liked your last one better."
        mc "Eh? Really?"
        n 2c "Well yeah. I can tell you were a little more daring with this one."
        n "But you're really not good enough for that yet. It fell flat."
        mc "That may be true, but I just wanted to try something different."
        mc "I'm still figuring this all out."
        n 2k "I mean, I always like poems that aren't trying too hard."
        n 2q "I hate when people try to sound fancy or add more meaning just by using annoying and complicated language."
        n 4b "Just make it simple, cute, and to the point!"
        n 4y "Yuri's head over heels for all this cryptic nonsense, but I see right through that BS. Hah!"
        n 42a "Making your reader look so hard for all this deep meaning is just an excuse to have no meaning at all."
        mc "I guess that's one way to look at it."
        n 2d "Well, everyone has their own opinion."
        n "But my opinion is the best opinion. I'm sure you've figured that out already."
        mc "Er..."
        n 2a "Anyway, here's my poem. Maybe you'll learn something."
        return

label ch2_n_med:
    #Likes this one better than the last one
    if n_poemappeal[0] < 0:
        n "Say...this one's actually better than your last one." 
        n "It's nice to see you putting in some effort!"
        mc "Oh...that's good."
        label ch2_n_med_shared:
            n 1l "Actually...you know what?"
            n 1d "This kinda reminds me of Satori's poem from yesterday."
            mc "Oh yeah?"
            n 7j "Yep! But, it's to be expected."
            n "You've been friends for so long that you're probably on the same wavelength."
            n 7l "You're a lot alike, the two of you."
            n 7z "Just a couple of dorks!"
            mc "..."
            mc "That's a fair assessment."
            "I actually have no argument. He's right."
            n 7t "Well...I don't get it, but if it works for you, whatever!"
n 1a "Anyway, here's my poem."
            return

    #Likes this one the same amount
    elif n_poemappeal[0] == 0:
        show natsuko 1s at t11 zorder 2
        n "Hm...well...I can't say it's any worse than your last poem."
        n 1c "But, it's not really much better either."
        "Whatever guilt I was feeling for eating all his cookies has completely dissipated."
        mc "Ah...well, at least it's not a total trainwreck, so that's good."
        mc "You don't offer any compliments but you sure do like to dish out the critique, don't you?"
        n 3x "Haha! Well, that's what it means to be a pro!"
        n "Every critique I offer is based on my own experiences as a writer."
        n 3d "Listen to my advice and maybe one day you'll be as good as I am!"
        "Did he just take my critique of him as a compliment?"
        "Man, I just can't win with this kid."
        jump ch2_n_med_shared

    #Likes the last one better
    else:
        n "...Hm."
        n 2c "Well, it's not terrible."
        n "But it's pretty disappointing after your last one."
        n 2s "Then again, if this one was as good as your last one, I would be completely pissed."
        mc "Well, I guess I wanted to try something a little different this time."
        n 2c "Fair enough. You're still new to this, so I wouldn't expect you to find your style right away."
        jump ch2_n_med_shared

label ch2_n_good:
    #Likes this poem better than the last one
    if n_poemappeal[0] != 1:
        n 1h "..."
        "Natsuki reads my poem."
        "She keeps glancing at me, then back at the poem."
        "By now, she must have read it more than once."
        n 1q "...Aren't you supposed to be bad at this?"
        mc "...Is that a compliment?"
        n 1o "N-No! I mean... You know..."
        "Natsuki struggles to find the words she wants."
        n 5w "I just...expected a lot less after what you showed me yesterday."
        n "That's all."
        mc "Well, I guess I just got lucky with this one."
        n 4t "Y-Yeah!! Exactly!"
        n "You just got lucky, you know?"
        n 4y "Don't get used to it."
        n "You won't always manage to write poems this cute. I mean--!"
        n 1p "I mean well-written! No, I mean--"
        mc "Ah, so that's how it is. My poem is cute?"
        n 1v "No! Why are you smiling?! It's not like I like cute things!"
        "Natsuki shoves my poem back towards me."
        n 4w "H-Huh! Reading it again, I decided that it's not so great after all."
        n "It's too cute and doki-doki."
        n 4t "It would only impress...you know, girls...who like those kinds of things."
        n "Ahaha!"
        "For some reason, Natsuki is incredibly easy to see through."
        n 1w "Well, anyway...!"
        n 1h "You're gonna read mine now, right?"
        n "Judging by your tastes, you'll probably like it a lot."
        n 2q "You'll probably learn something, too. Don't forget who the {i}real{/i} pro is."
        return
    #Likes both poems a lot
    else:
        label ch2_n_good_sharedwithch3:
            n 1n "..."
            "Natsuki reads my poem."
            "She keeps glancing at me, then back at the poem."
            "By now, she must have read it more than once."
            n 1u "Rrgh..."
            mc "...?"
            mc "Is it that bad?"
            n 1r "No! No, it's not!"
            n "It's good. It's really good, okay?!"
            n 5w "There, I said it!"
            n "Ugh, this wasn't supposed to happen at all...!"
            n 5s "Why can't you just be bad at this?"
            n "My poems are supposed to impress {i}you{/i}, not the other way around!"
            mc "You're trying to impress me?"
            n 12c "Obviously! You think I'd let you enjoy Yuri's writing more than mine?"
            n "Give me a break."
            mc "Well..."
            mc "In that case, what's the problem with me trying to impress you?"
            n 1e "I'll tell you! You--"
            n 1p "--"
            "Natsuki's face freezes, like she just realized something."
            n "Y-Y-You..."
            n "You're trying to...impress {i}me?{/i}"
            show natsuki 1q
            "Natsuki vigorously scans her eyes over my poem one more time."
            "Then, the poem slips out of her hands and flutters to the floor."
            n 1p "I...have to use the bathroom!"
            show natsuki at lhide
            hide natsuki
            "Red-faced, Natsuki quickly walks out of the room."
            show monika 1d at t11 zorder 2
            m "Hey, [player]..."
            m "Did you do something to Natsuki?"
            m "I just saw her rush out like that..."
            m 2g "You didn't do anything terrible, did you?"
            mc "N-No!"
            mc "I just told her that--"
            "My voice gets caught in my throat."
            "There's no way I could tell Monika that I'm trying to impress Natsuki."
            m 2d "Hmm?"
            "Monika sees the poem lying on the floor and swiftly picks it up."
            if m_readpoem:
                "She skims over it a second time, her smile not fading from her face."
                m 2a "I see."
                m "At first I just thought you liked her writing style..."
                m "But you wrote this {i}for{/i} Natsuki, didn't you?"
            else:
                "She reads through it, her smile not fading from her face."
                m 2a "I see."
                m "You wrote this for Natsuki, didn't you?"
            mc "I-I mean..."
            mc "Not really..."
            m 2d "In fact, didn't she like your poem a lot the other day, too?"
            m "I'm surprised you know her taste so well already."
            m 4a "Are you sure you're not cheating, [player]?"
            mc "Cheating...?"
            mc "What do you mean by that?"
            m 5a "Never mind, I'm just kidding. Ahaha!"
            "I didn't understand Monika's joke at all."
            m "Anyway..."
            m 1a "How do you think Natsuki feels about you?"
            m "Oh, you don't need to answer that."
            m "It was just something for you to think about."
            show monika at t22 zorder 2
            show natsuki 4e at l21
            n "Hey!"
            "Natsuki comes up and snatches the poem out of Monika's hands."
            "Neither of us had noticed her reenter the classroom."
            show natsuki at f21 zorder 3
            n "Did you read this, Monika?"
            show natsuki at t21 zorder 2
            show monika at f22 zorder 3
            m 1j "Of course! I liked it!"
            show monika 1a at t22 zorder 2
            show natsuki at f21 zorder 3
            n 1r "Ugh..."
            n "You should really stop reading things that aren't for you, you know."
            n "You have a bad habit of doing that."
            show natsuki at t21 zorder 2
            show monika at f22 zorder 3
            m 1d "Eh?"
            m "But [player] wrote this poem."
            m 1a "And we're supposed to share with everyone, right?"
            show monika at t22 zorder 2
            show natsuki at f21 zorder 3
            n 1x "Uu--"
            "Natsuki freezes."
            "She apparently forgot that my poem is technically for everyone to read."
            n 42c "Okay, well, I think [player] is done sharing this poem with everyone."
            n "It's not like anyone would want to read this anyway."
            n 4h "In fact, I'm just going to hold onto this."
            show natsuki at t21 zorder 2
            show monika at f22 zorder 3
            m 5 "If you insist~"
            show monika at t22 zorder 2
            show natsuki at f21 zorder 3
            n 1i "What?"
            n "Why are you looking at me like that??"
            show natsuki at t21 zorder 2
            show monika at f22 zorder 3
            m "Like what?"
            show monika at t22 zorder 2
            show natsuki at f21 zorder 3
            n 12b "Ugh..."
            n "Never mind."
            if not m_readpoem:
                $ poemsread += 1
                $ m_readpoem = True
            if poemsread >= 3:
                "Well, I guess Natsuki has my poem now."
                "Not that I really planned on keeping it."
            else:
                $ unfairto = "Sayori"
                if s_readpoem:
                    $ unfairto = "Yuri"
                show natsuki at t21 zorder 2
                mc "Ah, Natsuki..."
                mc "I'll give you the poem, but that's still not very fair to [unfairto]..."
                mc "...She hasn't gotten to read it yet."
                show natsuki at f21 zorder 3
                n 2q "So what?"
                show natsuki at t21 zorder 2
                show monika at f22 zorder 3
                m 2a "Well... I guess [player] is right, Natsuki..."
                m "It's not fair if you don't let everyone finish reading it."
                show monika at t22 zorder 2
                show natsuki at f21 zorder 3
                n "..."
                n 2h "...Fine."
                "Natsuki returns my poem."
                n "It's not like she's going to like it, though."
            show monika at thide zorder 1
            show natsuki at t11 zorder 2
            hide monika
            n 2h "Anyway, read my poem now."
            n 4h "And no, I won't let you keep it."
            n "This is my only copy."
            return

label ch3_n_bad:
    n "Ehehe...yeah, no thanks, babe." 
    n "I think I'd feel more emotion by reading an instruction manual for a toaster."
    mc "...You didn't even..."
    n 7y "Begone, thot!"
    $ skip_poem = True
    return

label ch3_n_med:
    show natsuko 1k at t11
    n "...This one's alright."
    mc "Alright?"
    n "Yeah. About as good as yesterday's, anyway."
    n 5c "I see what you're going for, but it's not exactly my style."
    n 1j "It's fine, though!"
    n "You're trying, and that's what counts."
    mc "Of course I'm trying."
    mc "And I'll consider that as another compliment."
    mc "I appreciate you being this emotionally invested in my poems."
    n 1z "Haha! Well, someone in this club has to make sure you're not slacking off!"
    n 5c "Shame on you for being late today, though."
    mc "Take it easy."
    mc "I don't plan on making it a habit."
    n 1j "I'm glad to hear that!"
    n 3d "I'd hate to think my critique on your writing might be scaring you off!"
    mc "Like I'd actually do that."
    mc "I like it here, even if I have to put up with you."
    n 1g "Put up with me, eh?"
    n 7y "I guess that means I'll need to take my cookies and donuts elsewhere..."
    mc "Guh--!"
    mc "I'm sorry, I'm sorry!"
    mc "I was just joking!"
    n 7ag "Oh, I know!"
    n 7z "Don't worry, I was too! Hahaha!"
    "Shorty better not be joking around when it comes to those cookies and donuts..."
    n 1z "Anyway..."
    "He holds his poem out to me."
    n 1d "I think you're gonna really love this one!"
    return

label ch3_n_good:
    #Didn't like the last two poems
    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch3_n_bad
    #Loved the last two
    elif n_poemappeal[0] > 0 and n_poemappeal[1] > 0:
        show natsuko 1l at t11
        n "This is a temporary placeholder till we get Nat's Poem Response here."
        n "In the meantime check if the poem shows up and the end also."
        mc "W-wha?"
        n "Here you go!"
        return

label ch1_s_bad:
    show satori 1s at t11 zorder 2
    s "... Hahahaha!"
    s "[player]..."
    s 7l "You know I love you..."
    s 10z "But this poem is really bad!"
    mc "...!"
    mc "What the actual hell, man?!"
    mc "I mean...I love you too...but damn..."
    s 1r "Haha! It's fine, it's fine." 
    s 7x "It's your first time after all." 
    s 10r "To be honest, I'm just happy that you actually wrote one." 
    s 1d "It shows that you're taking this seriously."
    mc "Of course."
    mc "I may not be totally into it yet, but I'm still gonna put in some effort."
    s 1q "Well it definitely shows."
    s 1d "You didn't have to do this, you know."
    s 1l "I mean...we both know why you decided to join."
    s 7x "But it seems like you're really putting effort into writing..."
    s 7d "And I appreciate that."
    "It's true that I initially joined this club in the hopes of getting to know the others."
    "But, I'd be lying if I said Satori had nothing to do with it."
    "This club does mean a lot to him after all."
    s 1d "And don't worry."
    s 1y "I'll keep my word to help you impress whoever you're interested in."
    s 1d "It'll be my way of thanking you."
    mc "I'm gonna hold you to that."
    s 1z "Haha, deal!"
    s 1x "Anyway-- wanna read my poem now?"
    s 10l "I'm, umm... not very good at this."
    mc "I'll be the judge of that."
    return

label ch1_s_med:
    show satori 1a at t11 zorder 2
    s 5q "...This is a good poem, [player]!"
    s 1x "Is this really your first time?"
    mc "Of course it is."
    mc "You know I don't write poetry in my spare time."
    s 1y "That's true."
    s 7d "But that just makes it even more impressive."
    s 1l "I mean...we both know why you decided to join."
    s 7x "But it seems like you're really putting effort into writing..."
    s 7d "And I appreciate that."
    "It's true that I initially joined this club in the hopes of getting to know the others."
    "But, I'd be lying if I said Satori had nothing to do with it."
    "This club does mean a lot to him after all."
    mc "Well, I may not be that into it yet, but I'm still gonna try."
    mc "I don't wanna let any of you down."
    s 1q "Aw. Even Mateo?"
    mc "Mateo can go f..." #Go Fuck Himself
    s 1ab "[player]..."
    mc "{i}Sigh.{/i}"
    mc "Yeah, Mateo, too."
    s 4z "Haha! Good!"
    s 1d "And don't worry."
    s 1y "I'll keep my word to help you impress whoever you're interested in."
    s 1d "It'll be my way of thanking you."
    mc "I'm gonna hold you to that."
    s 1z "Haha, deal!"
    s 1x "Anyway-- wanna read my poem now?"
    s 10l "I'm, umm... not very good at this."
    mc "I'll be the judge of that."
    return

label ch1_s_good:
    show satori 1a at t11
    s 4n "...Holy smokes..."
    s 5r "This is soooooo good, [player]!"
    s 4ar "I really love it!"
    s 4d "I had no idea you were such a good writer!"
    mc "I think you may be overreacting."
    mc "I'm not a good writer at all."
    mc "I have no idea what I'm doing."
    s 1z "Well that's perfect, then."
    s 9s "Because I have no idea what I like!"
    "Satori chuckles."
    "Hopefully Yuuri's and Natsuko's opinions are more constructive than this."
    mc "Bah, you just like it because I wrote it."
    s 1c "Well, that's part of it."
    s 10y "I do understand you better than anyone else."
    s 10d "Your poem isn't just a poem to me, you know?"
    s 10y "It's...well..."
    s 7q "It's a [player] poem!"
    s 4d "So, it makes it extra special to me."
    s 4x "I feel like I can feel your feelings through it."
    mc "You're sweet, Satori."
    mc "You had no advice to offer and I've learned absolutely nothing about writing from this exchange..."
    mc "But you're very sweet."
    s 10r "Ahahaha! I'm just happy that you actually wrote one."
    s 1d "It shows that you're taking this seriously."
    mc "Of course."
    mc "I may not be totally into it yet, but I'm still gonna put in some effort."
    s 1q "Well it definitely shows."
    s 1d "You didn't have to do this, you know."
    s 1l "I mean...we both know why you decided to join."
    s 7x "But it seems like you're really putting effort into writing..."
    s 7d "And I appreciate that."
    "It's true that I initially joined this club in the hopes of getting to know the others."
    "But, I'd be lying if I said Satori had nothing to do with it."
    "This club does mean a lot to him after all."
    s 1d "And don't worry."
    s 1y "I'll keep my word to help you impress whoever you're interested in."
    s 1d "It'll be my way of thanking you."
    mc "I'm gonna hold you to that."
    s 1z "Haha, deal!"
    s 1x "Anyway-- wanna read my poem now?"
    s 10l "I'm, umm... not very good at this."
    mc "I'll be the judge of that."
    return

label ch2_s_bad:
    s "..."
    s 1q "Ehehe, I love reading your poems~"
    s "It's like I never know what I'm going to get!"
    mc "So basically you're saying it sucks."
    s 4c "No! Not at all!"
    s 4l "...Maybe!"
    s 5a "Just a little?"
    s "Yuri must have spoiled me a little bit with her poems..."
    s "Ehehe..."
    mc "It's fine, it's fine."
    mc "After all, I still have no idea what kinds of writing you even like."
    label ch2_s_shared:
        s 1q "Yeah!"
        s "Me neither!"
        mc "Ugh..."
        mc "Why don't you at least try giving it some thought?"
        s 2d "Aww, you want to write something for me?"
        s "That's so sweet~"
        mc "Yeah, right."
        mc "But you're always thinking about other people."
        mc "You need to think about yourself once in a while."
        mc "If you don't, you might end up getting hurt at some point."
        s 1n "Ehh?"
        s "Well..."
        s 1o "I don't really know what you mean, but I'll try to keep it in mind!"
        mc "Well, whatever..."
        s 1b "Anyway, let's see..."
        s "Hmm..."
        s 4q "I guess I like...happy poems~"
        s 4i "Wait, sometimes I like sad poems too..."
        s 1i "Sometimes a little bit of both..."
        s "There's a word for that, right...?"
        s "What's the word I'm looking for..."
        s 4r "...Bittersweet!"
        s "Yeah!"
        s 1x "I like things that are happy and things that are sad."
        mc "Happy and sad?"
        mc "I can't see you liking something sad, Sayori..."
        s 1c "Well..."
        s "I like happy the most!"
        s 1d "But sometimes when you have a little raincloud in your head..."
        s "A sad poem can help give the raincloud a little hug..."
        s 4q "...And make a nice happy rainbow!"
        mc "...Sayori, that's unexpectedly poetic."
        s 4n "Eh? It is?"
        s "Maybe I'm getting better at expressing my feelings after all!"
        s 2q "Thanks, [player]!"
        s "I should go write that down, then~"
        s 2a "You can read my poem now, okay?"
        return

label ch2_s_med:
    #This one is better than the last one
    if s_poemappeal[0] < 0:
        show satori 4q at t11 zorder 2
        s "Ooh...I like this one, [player]!" 
        s "It has some nice feelings in it."
        mc "Ah. So you're saying it's better than yesterday's?"
        s 4x "Way better!"
        mc "I'm glad for that." 
        mc "Maybe my writing isn't terrible after all."
        label ch2_s_med_shared:
            s 7a "Well, writing is about expressing yourself."
            s "So, technically, there's no such thing as a 'bad' poem."
            s 4aq "Except yesterday." 
            s 4z "Yesterday's poem sucked out loud."
            mc "..."
            mc "Thank you for reminding me."
            s 7d "But that's why I go by my feelings." 
            s "If it makes me feel things, then it must be good."
            mc "What kind of writing do you even like?"
            s 9r "I dunno!"
            mc "Ah, okay." 
            mc "Glad we cleared that up."
            s 1i "Why do you care all of a sudden?" 
            s 1aq "You wanna write me a poem tomorrow?" 
            s 1z "You're so sweet."
            mc "Yes, that's exactly what I was getting at." 
            mc "Hell, I'll write you a poem right now."
            mc "Check this out.."
            mc "'There once was a man named Enus...'"
            s 7ac "Please don't finish that."
            mc "Aw, c'mon."
            mc "Are you telling me you already don't like it?"
            s 1ab "You're so immature."
            mc "See, this is why I don't write things for you."
            mc "The next line was gonna be so epic..."
            mc "Spoiler alert: I was gonna rhyme Enus with..."
            s 5m "If I tell you what kind of poems I like, will you stop!?"
            mc "...That's a fair trade."
            s 1k "Well, let's see..." 
            s 7x "I guess I like happy poems." 
            s 4k "And sad poems." 
            s 8a "A little bit of both." 
            s 1b "There's a word for that. What was it..." 
            s 4r "Bittersweet!" 
            s 7x "Yeah. I like happy and sad." 
            s 1q "Maybe a little rage thrown in for balance."
            mc "That's cool." 
            mc "Though, I can't really see you liking anything sad."
            s 7c "Don't get me wrong." 
            s "I prefer happy poems." 
            s 7d "But, every so often, it's alright to feel sad." 
            s 7q "It's almost cathartic." 
            s 1x "I think it's important to be in touch with all of your feelings, including the negative ones." 
            s "We need to be balanced, you know?"
            mc "That's true." 
            mc "And it's also kinda poetic."
            s 1z "You think so?" 
            s 10r "Haha, maybe I should write that down!" 
            s 1d "You can read my poem now, okay?"
            jump ch2_s_shared
    #This one is the same as the last one
    elif s_poemappeal[0] == 0:
        s "..."
        s 4x "Ooh!"
        s "I like this one, [player]!"
        s "It has some nice feelings in it~"
        mc "Ah, I'm glad."
        mc "Does that mean it's better than yesterday's?"
        s 4b "Mmm, lemme think..."
        s 1q "I dunno!"
        s "I guess I like them both!"
        s "Ehehe~"
        mc "That's not very helpful, you know..."
        jump ch2_s_med_shared
    #This one is not as good as the last one
    else:
        s "..."
        s 4x "Ooh!"
        s "I like this one, [player]!"
        s "It has some nice feelings in it~"
        mc "Ah, I'm glad."
        mc "Still, though..."
        mc "Your tone makes it sound like you liked yesterday's poem better."
        s 2l "Ehehe, I guess you caught me..."
        s "Sometimes you know me a little too well for my own good!"
        mc "Well, don't just try to be nice about it."
        mc "If I'm doing a bad job then I'd rather just hear it."
        s 1c "No, no!"
        s "I still liked this one! I promise!"
        s 1h "You know I wouldn't lie to you, [player]...!"
        s "Never ever!"
        mc "Yeah, I guess so..."
        mc "What made yesterday's poem so great compared to this one, then?"
        s 1b "Umm....."
        jump ch2_s_med_shared

label ch2_s_good:
    #This one is better than the last one
    if s_poemappeal[0] < 1:
        s 1n "..."
        s "...Oh my goodness!"
        s 4r "This is sooooo good, [player]!"
        mc "Eh?"
        s "I love it~!"
        s "Especially after yesterday's poem!"
        mc "Ugh..."
        mc "You're too honest sometimes, Sayori."
        s 4x "No, but really!!"
        s 1x "I wanna put this on my wall~"
        s "Can I?"
        mc "Sayori..."
        mc "You must be seriously overreacting."
        mc "I'm not a good writer at all."
        mc "I honestly have no idea what I'm doing."
        s 1l "Well..."
        s "Maybe that's why!"
        s "Because I have no idea what I like, either!"
        s 4r "Ahahaha!"
        mc "Jeez..."
        "I'm sure Yuri's opinion has to be a little more constructive than this."
        "Maybe even Natsuki's."
        mc "Are you sure you don't like it just because I wrote it?"
        s 4b "Eh?"
        s 1b "Well, I'm sure that's part of it."
        s "I think I understand you better than a lot of other people, you know?"
        s "So when I read your poem..."
        s "It's not just a poem..."
        s 4q "It's a [player] poem!"
        s "And that makes it feel extra special!"
        s "Like I can feel your feelings in it~"
        "Sayori hugs the sheet against her chest."
        mc "You're so weird, Sayori..."
        s 4l "Ehehe..."
        jump ch2_s_med_shared
    #Loved both poems
    else:
        show satori 1d at t11 zorder 2
        s "Wow...[player], I really love your poems!"
        s 1q "I can't believe you've been hiding this talent from me!"
        mc "I'm glad you like them, but really, I'm not hiding anything!"
        s 7d "But, your poems are so good, both yesterday's and this one."
        s 7x "Have you really never done this before?"
        mc "You know I haven't."
        mc "Anyway, you're literally the only one in the club who feels that way."
        s 1c "C'mon...you're telling me that not even Nat likes your poems?"
        mc "Natsu thought my poem sucked last time."
        mc "I can't really see him liking this one any better."
        mc "Besides, I already know why you like them so much."
        s 1b "Eh? Why is that?"
        mc "Because...whenever I write my poems..."
        mc "I-I'm thinking about you."
        s 1o "..."
        s 1k "Me? But, why"
        mc "Why do you think?"
        mc "We're best friends."
        mc "We spend a lot of time together."
        mc "So much time, in fact, that I think we kinda know each other's thoughts sometimes."
        mc "We have that kind of connection, you know?"
        s 1y "[player]...can I have this poem?"
        "I give a little sigh and soft chuckle."
        mc "Of course you can, buddy."
        mc "You can take it home once everyone else sees it."
        s 1q "Thank you. It really is a great poem, you know."
        mc "Alright, alright. No need to make me feel all special about it."
        "I playfully push him."
        mc "Lemme see your poem now."
        s 1q "Fine."
        s 1d "Here...I hope you like it."
        mc "I'm sure I will."
        return

label ch3_s_bad:
    $ currentname = "Yuri"
    if n_poemappeal[2] > y_poemappeal[2]:
        $ currentname = "Natsuki"
    s "..."
    s "This is a temporary placeholder till we get Satori's Poem Response here."
    s "In the meantime check if this skips."
    mc "W-wha?"
    s "Begone!"
    $ skip_poem = True
    return


label ch3_s_med:
    jump ch3_s_bad

label ch3_s_good:
    show satori 1k at t11 zorder 2
    s "[player]...this is your best one yet."
    s 1d "It's really amazing..."
    mc "Thanks, buddy."
    s 1d "Mhm."
    "He seems much calmer."
    "Almost too calm."
    mc "Satori...are you alright?"
    s 1g "Hm? Oh. Right."
    s 10k "Hm? Oh. Right."
    s "I'm...I'm sorry about yelling at you earlier."
    s 10e "I'm just a little moody today."
    s 1d "Don't worry about me, though."
    s "I'll be fine."
    mc "...Are you sure you're okay?"
    s 1k "Yeah, I'm sure."
    s "I don't think I got much sleep last night, so I'm a little tired, too."
    mc "Do you..."
    mc "Do you need a nap or something?"
    s 1d "Don't be silly. I'm fine."
    s "Stop worrying so much."
    mc "Well, I'll try."
    stop music fadeout 2.0
    s 1k "...You know, I'm a little surprised..."
    s 7k "I really thought you'd start writing your poems like the way Yuuri does."
    s 3k "Or even Nat."
    s 1g "But, in the end..."
    mc "It shouldn't be all that surprising."
    mc "I spend most of my time with you."
    mc "Even in the club."
    play music t9
    s 4h "But..why?..."
    s "Don't you want to get closer to everyone else?"
    s "Wasn't that the plan?"
    mc "Well, yeah it was..."
    mc "But, I understand you the most."
    mc "I'm the most comfortable around you."
    mc "And we have this connection."
    mc "It makes it easier for me to write when I think about you."
    mc "Nothing can ever change that."
    s 5ag "NO!"
    "The unexpected outburst causes me to jump a little in surprise."
    "I'm prepared to snap at him..."
    show satori 5an at t11
    "But then I notice the tears in his eyes."
    s 5am "Why...are you doing this?!"
    "He's having trouble keeping his voice steady."
    mc "Doing what? Satori..."
    s 5v "This would be..."
    s "So much easier..."
    s 5w "If you'd just start spending time with them instead..."
    mc "What would be easier?"
    "I look around to see if anyone's watching us."
    "But they all seem preoccupied."
    "I lean into Satori and whisper."
    mc "Look, I knew something was off with you today, and you've just confirmed it."
    mc "Now you better tell me what's going on with you..."
    s 4aw "Just...forget it."
    s "I'm sorry I said anything."
    mc "I just want you to talk to me..."
    "I stop when I see Satori grab his book bag."
    mc "Wh-what're you doing?"
    s 1u "I'm going home early today."
    mc "Then I'm going, too."
    s 5w "No!"
    s 5v "Please...I need to be left alone right now, okay?"
    s 1aw "Just...just tell Mateo I wasn't feeling well."
    s 1u "I'll see you...whenever."
    show satori at thide
    hide satori
    "Before I can say anything else, Satori turns and walks out the door, mumbling to himself."
    "I watch him go, helplessly clutching my wrinkled poem."
    "As much as I'd love to follow him out the door, something tells me it's best to leave him be for now."
    $ skip_poem = True
    return

label ch1_y_bad:
    show yuuri 1g at t11
    y "...Hmm..."
    "Yuuri stares at the poem."
    "A minute passes."
    "More than enough time for him to finish reading."
    mc "Um..."
    y 7n "--Oh!"
    y 7o "Ah... I'm sorry."
    y 7t "I promise I'm not ignoring you..."
    mc "It's fine...take your time. Don't force yourself."
    "I keep forgetting that the big guy is jumpy."
    y 6h "I just... I need some time to put my thoughts into words."
    y 6g "Hold on..."
    y 6l "Alright."
    y 1f "Is this your first time writing a poem?"
    mc "Uh, yeah. Yeah it is. It shows, right?"
    y 1g "Yes, I'm afraid it does."
    mc "Ah. So it's that bad huh?"
    y 6v "No, no."
    y 1v "It's not 'bad'...it's just..."
    show yuuri 6g
    "Yuuri furrows his brows and bites down on his thumb, deep in thought once again."
    "It's been several minutes and we haven't really gotten anywhere."
    "Yuuri sure likes to really think things through before he speaks."
    "Huh."
    "Maybe I could learn something from that."
    y 6m "Alright... So..."
    label ch1_y_shared:
        y 4f "There are specific writing habits that are usually typical of new writers."
        y 4h "Having been through that myself, I've learned how to pick up on them."
        y 3k "See, new writers try to make their style more deliberate..."
        y 3h "Often picking a subject matter different from the style and then just form-fitting them together."
        y 1k "The end result is that both the style and the expressiveness are weakened."
        "Once Yuuri finds his train of thought, his demeanor does a complete 180."
        "His stammering disappears and he sounds more like a teacher than a student."
        y 1f "Now this is not something you can be blamed for, of course."
        y 3f "There are many techniques that can go into writing even a simple poem."
        y 3k "Not just finding them and building them..."
        y "But getting them to work together is probably the most challenging part."
        y 3m "All of this comes with practice, learning from example and trying new things."
        y 1a "It also helps that everyone else in the club gives you valuable feedback."
        y 6h "Natsuko can be a bit biased though."
        mc "Biased? How?"
        y 6o "Ah..."
        y 6g "Well..."
        y 4j "I suppose you'll see what I mean, eventually."
        mc "Alright..."
        "That was weird."
        "I wonder what he has against Natsuko?"
        mc "So how about I check out your poem now?"
        y 1c "Yes, of course!"
        y 1d "I would love to share my thought process behind it."
        "Yuuri smiles dreamily as he hands me his poem."
        "He's actually really handsome when he smiles."
        "He seems so serious all the time."
        "I doubt he's this happy about anything very often."
        $ yuuri_readearly = True
        return

label ch1_y_med:
    jump ch1_y_bad

label ch1_y_good:
    show yuuri 1a at t11 zorder 2
    y 1e "..."
    "As he reads through my poem, I notice his eyes lighten."
    y "Exceptional..."
    mc "Yeah?"
    mc "You really think so?"
    y 7n "...!"
    y 6o "I...didn't mean for that to come off as creepy or anything..."
    mc "No, no! I'm super happy that you like it!"
    y 6q "Well...in that case..."
    y 3b "I'm very impressed, [player!]"
    y 1b "What kind of experience do you have?"
    y 1c "Your use of metaphors and imagery indicate you've done a lot of writing before."
    mc "That's a really huge compliment coming from you."
    mc "This is actually my first time writing."
    show yuuri 1e
    "Yuuri looks at me quizzically before looking over my poem again."
    y 6g "Interesting..."
    "Yuuri traces the words of my poem with his finger, as if breaking it down more thoroughly."
    y 6h "The thing is..."
    y 4f "There are specific writing habits that are usually typical of new writers."
    y 4h "Having been through that myself, I've learned how to pick up on them."
    y 3k "See, new writers try to make their style more deliberate..."
    y 3h "Often picking a subject matter different from the style and then just form-fitting them together."
    y 1k "The end result is that both the style and the expressiveness are weakened."
    "Once Yuuri finds his train of thought, his demeanor does a complete 180."
    "His stammering disappears and he sounds more like a teacher than a student."
    y 1f "Now this is not something you can be blamed for, of course."
    y 3f "There are many techniques that can go into writing even a simple poem."
    y 3k "Not just finding them and building them..."
    y "But getting them to work together is probably the most challenging part."
    y 3m "All of this comes with practice, learning from example and trying new things."
    y 3b "That's why I thought you were experienced." 
    y 3d "Because I see none of these mistakes in your poem."
    mc "Haha! Probably just beginner's luck!" 
    mc "Please don't be disappointed if tomorrow's doesn't come out as good."
    y 1a "It's okay." 
    y 1b "You're new, so I expect you to try to new things." 
    y 4m "Receiving valuable feedback from everyone else will influence you as well." 
    y 6h "Natsuko can be a bit biased though."
    mc "Biased? How?"
    y 6o "Ah..." 
    y 6g "Well..."
    y 4j "I suppose you'll see what I mean, eventually."
    mc "Alright..."
    "That was weird."
    "I wonder what he has against Natsuko?"
    mc "So how about I check out your poem now?" 
    y 1c "Yes, of course!"
    y 1d "I would love to share my thought process behind it."
    "Yuuri smiles dreamily as he hands me his poem."
    "He's actually really handsome when he smiles."
    "He seems so serious all the time."
    "I doubt he's this happy about anything very often."
    return

label ch2_y_bad:
    #Dislikes both poems
    if y_poemappeal[0] < 0:
        y "..."
        y 2h "Um..."
        y "...Are you still mad at me?"
        mc "Eh?!"
        y "For disrespecting Natsuki yesterday..."
        y "Because reading this poem..."
        y "Now I know why you got mad at me."
        y "Because you..."
        y 3v "You prefer her writing over mine!"
        mc "That's not really true...!"
        y "Meaning when I disrespected her..."
        y "I disrespected you too...didn't I?"
        y 4c "Oh no..."
        mc "Yuri..."
        mc "You might be reading into this a little too much..."
        y "How could I be so stupid...?"
        y "I always let these things happen..."
        y "Whenever I think before I speak, I just come off as awkward and unlikable."
        y "But if I speak without thinking, the things I want to keep inside come out and make people hate me."
        y 2v "So...please don't force yourself to be around me."
        y "I know this is what Monika wants."
        y "But it's not fair to you when you could be enjoying your time with Natsuki and Sayori."
        mc "Yuri--"
        y 4b "Please..."
        y "It makes it easier for me if you don't express any concern."
        y "Besides..."
        y "I have my books with me."
        y 3u "That's...all I need."
        mc "..."
        "Yuri smiles sadly and puts her head down on her desk."
        "I'm frustrated."
        "I don't hate her, but it's as if she's not capable of listening to me over her own thoughts."
        "I sigh to myself."
        "All I can do is accept that that's how she is."
        "If she wants to be left alone, then I have no choice but to abide to that request."
        $ skip_poem = True
        return
    #Liked the last one more
    else:
        y 2a "Ah, is it my turn?"
        y "Let's see how it compares to yesterday's..."
        y "Mm..."
        y "I see..."
        y "It's a bit different."
        y 1a "I respect you for trying different things, [player]."
        y "Were you inspired by Natsuki's poem?"
        y "Or Sayori's, perhaps?"
        mc "Well..."
        mc "I guess you could say that..."
        y "I thought so."
        y 2u "I'm happy for you."
        y "You don't need to find inspiration in my poems."
        y "I write them for myself..."
        y 4b "...Not for anyone else."
        y "So I don't really...need for people to like them or anything."
        mc "Yuri!"
        y 3t "E-Eh?"
        mc "I'm sorry for being blunt, but you're overthinking this a little."
        mc "Just because our styles are different doesn't mean I dislike your poems..."
        mc "In fact, if I tried to do something in your style, I would probably just do a terrible job."
        y 4a "I...I see..."
        y "I'm sorry..."
        y "My stupid mind...it likes to do that sometimes."
        y "Anyway..."
        label ch2_y_shared:
            y 2h "You don't need to be afraid to be a little more daring..."
            y "Metaphors can go a long way."
            y "Don't feel like you need to work your brain like turning a bunch of gears."
            y 1m "Try letting your mind wander through your feelings..."
            y "And write down the things you see and hear."
            y "That's one way to truly enable your reader to see into your mind."
            y 2u "It's a very intimate exercise..."
            mc "I see."
            mc "That's a certainly interesting technique."
            mc "Thanks for sharing."
            y 2v "I have, um..."
            y "...Well, an example of that, if you'd like to read it..."
            mc "Of course."
            mc "Is this the poem you wrote for today?"
            "Yuri nods, and timidly hands me her poem."
            return

label ch2_y_med:
    #likes this one more than yesterday's, or the same amount
    if y_poemappeal[0] <= 0:
        y 1a "Let's see what you've written for today."
        y "..."
        y "Mm..."
        y 1c "Well done, [player]."
        y "Your skills are already improving."
        mc "Really?"
        mc "Thanks, Yuri."
        mc "Coming from you, that means a lot."
        y 3f "Eh?"
        y 3v "I-It's nothing!"
        y "I'm just happy to help inspire fellow writers..."
        y "I know you're new to this, so don't worry so much if it seems like you can't get your poem to feel perfect."
        jump ch2_y_shared

    #likes this one less
    else:
        y 1a "Let's see what you've written for today."
        y "..."
        y "Mm..."
        y "This is pretty good, [player]."
        y "Were you influenced by seeing everyone's writing styles yesterday?"
        mc "I guess you could say that..."
        y 1m "I was also a bit surprised by how differently everyone writes."
        y "So I respect you for trying new things."
        jump ch2_y_shared

label ch2_y_good:
    #likes this one more than yesterday
    if y_poemappeal[0] < 1:
        show yuuri 1a at t11 zorder 2
        y 1a "Let's see what you've written for today."
        y 1d "Hmm...well done, [player]. Your skills are already improving."
        mc "You really think so?"
        mc "Wow, thanks, Yuuri!"
        mc "That means a lot coming from you!"
        y 1c "Haha! It's nothing."
        y 1b "I'm happy to inspire my fellow writers."
        y "I know you're new to this..."
        y "So, don't worry too much if it feels like you can't get your poem to feel perfect."
        y "You needn't be afraid to be a little more daring."
        mc "How can I do that?"
        y 1i "Well...metaphors can go a long way."
        mc "Coming up with clever or beautiful metaphors is super challenging for me."
        y 1b "It doesn't have to be."
        y 3b "Writing shouldn't be a robotic activity."
        y 3m "The secret is to just let your mind wander through your feelings and write down the things you see and hear."
        y "That's one way to truly enable your reader to see inside your mind."
        y 1y "When you think about it, it's a very intimate exercise."
        mc "I see."
        mc "That's certainly an interesting technique!"
        mc "Thank you for sharing that with me."
        y 1d "I have an example of that, if you'd like to read it."
        mc "Of course."
        mc "Is this the poem you wrote for today?"
        "Yuuri nods and hands me his poem." 
        return
    #likes both poems a lot
    else:
        show yuuri 1a at t11 zorder 2
        y 1a "Let's see what you've written for today."
        show yuuri 1e
        "Yuuri stares at the poem with a surprised expression."
        mc "Do you like it?"
        y 1f "[player]...this one might be even better than yesterday's!" 
        y 4f "How did you pick up on this so quickly?"
        jump ch2_y_good_shared

label ch2_y_good_shared:
    y "Just yesterday I was telling you about the techniques worth practicing..."
    mc "Maybe that's why." 
    mc "You did a great job explaining." 
    mc "I really wanted to try and give it more imagery."
    y 6u "I am honored to have my advice so appreciated." 
    y "I'm...I'm not used to it." 
    y 1s "Seeing someone so motivated by my writing makes...well, it makes me really happy."
    mc "You give amazing advice, Yuuri." 
    mc "I'm surprised you've never shared your poems before yesterday."
    y 1v "Well...I generally just write for myself."
    mc "That's a shame." 
    mc "Your talent should be displayed."
    "Yuuri's blush intensifies." 
    y 1q "You...you're too kind..."
    mc "Anyway...do you want to share the poem you wrote for today?"
    y 1y "With you...yes. I do."
    return

label ch3_y_bad:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        label ch3_y_bad12_shared:
            show yurri 4b at t11
            y "This is a temporary placeholder till we get Yurri's Poem Response here."
            y "In the meantime check if this skips or not."
            mc "W-wha?"
            y "Begone!"
            $ skip_poem = True
            return
    elif y_poemappeal[1] < 0 or y_poemappeal[0] < 0:
        show yurri 1i at t11
        y "This is a temporary placeholder till we get Yuuri's Poem Response here."
        y "In the meantime check if the poem shows up and the end also."
        mc "W-wha?"
        y "Begone!"
        $ skip_poem = True
        return
    else:
        y 1a "..."
        label ch3_y_shared:
            y "This is a temporary placeholder till we get Yuuri's Poem Response here."
            y "In the meantime check if the poem shows up and the end also."
            mc "W-wha?"
            y "Here you go!"
            return


label ch3_y_med:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    elif y_poemappeal[0] < 1 or y_poemappeal[1] < 1:
        y "..."
        jump ch3_y_shared
    else:
        y 1e "..."
        jump ch3_y_shared

label ch3_y_good:
    show yuuri 1b at t11
    y "Well done, [player]."
    y 1a "You've definitely improved your writing over the course of these few days."
    y "Has my advice been helpful to you?"
    mc "Yeah, for sure!"
    y 1c "I'm glad."
    y "Sharing our writing like this is a lot more fun and rewarding than I anticipated."
    y 1d "I need to remember to thank Mateo."
    y 1u "I think we all felt a little awkward at first."
    y 3b "But now, it seems like everyone is enjoying sharing their writing and seeing what others think."
    mc "I agree."
    mc "This isn't the dull spike to the forehead I thought it would be."
    "At least I get to spend an hour after school every day hanging out with a room full of cute guys."
    "That's my silver lining."
    mc "It's actually fun trying something new and getting to know everyone through their writing."
    y 1a "Well, you know how I like to say writing is a very personal way to get in touch with yourself?"
    y "Let me ask you..."
    y "Have you learned anything new about yourself, [player]?"
    mc "I'm...I'm not sure..."
    mc "I guess I haven't really stopped to think about it."
    y 1c "You know, in the end, it doesn't even matter if you're a good writer or a bad writer."
    y "The most important thing is exploring and discovering yourself."
    mc "That's good to know."
    mc "You know so much, I'm so afraid of disappointing you in some way or another."
    mc "You're so sophisticated with your writing and have so much advice to share."
    y 3q "Well, my opinions are just opinions."
    "Yuuri thinks for a minute."
    "He suddenly looks embarrassed."
    y 6t "I do apologize if my opinion comes off as pretentious."
    y "I haven't made you feel uncomfortable or intimidated, have I?"
    y 6v "That would be awful if I did."
    "Aw."
    "He's so adorable when he thinks he did something wrong."
    "Now I feel bad for my poor phrasing."
    mc "You're fine, big guy!"
    mc "I was just saying that I really respect your opinion."
    mc "You're so knowledgeable."
    mc "I've learned a lot from you."
    y 6e "You have?"
    y 6c "I'm so relieved to hear that."
    y 1u "I'm sorry I jumped to that conclusion."
    y 1t "I...I just don't want you to think I'm some condescending know-it-all."
    mc "Ahaha! No!"
    mc "Not at all!"
    mc "I think you're really helpful and smart."
    mc "I always learn something new from you."
    y 1u "I'm glad."
    y 1t "Please let me know if I ever come off as arrogant, or if I overstep my bounds."
    mc "Hehe...I don't think that's ever gonna be a problem, Yuuri!"
    mc "Anyway, ready to share your poem now?"
    y 1s "Yes. Here you go."
    jump ch3_y_good_shared


label ch1_m_start:
    show mateo 1d at t11 zorder 2
    m "So, [player]... Having fun so far?"
    mc "Um, yeah. Absolutely."
    m 1ab "I suppose that's good, then."
    m 6d "By the way, since you're new and all..."
    m 4d "If you ever have any suggestions for the club..."
    m 4r "Maybe new activities, or things we can improve on..."
    m 1s "Remember, I'm always listening."
    m 3b "So don't be afraid to bring things up."
    mc "Alright, I'll keep that in mind."
    "I mean, I am better off just going with the flow until I'm more settled in..."
    "But now that I have the go-ahead to speak up about things, I'm probably going to when I can."
    m 1b "Anyway, do you want to share your poem with me?"
    mc "It's kinda embarrassing, but it's what I agreed to."
    m 6t "Oh, I'm sure it's very embarrassing."
    m 6x "But, don't worry. I won't hold it against you."
    mc "... Thanks."
    "I hand the horse's ass my poem."
    m 6j "Hmhmhmhmhm..."
    "Mateo chuckles softly to himself."
    $ nextscene = "m_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    m 1j "Anyway, are you ready to read my poem now?"
    mc "Yeah. Looking forward to it."
    m 6v "You sound thrilled."
    mc "I mean... we both know you're going to make me look like an untalented hack."
    mc "So I'm sorry I'm not leaping for joy at that opportunity."
    m 4r "It's not my fault you choose to see it that way."
    mc "Whatever. Let's just see it already."
    return

label ch2_m_start:
    show mateo 1b at t11 zorder 2
    m "Hi again, [player]."
    m "How's the writing going?"
    mc "It's...ah..."
    mc "It's going fine."
    m 1k "Good. You're applying yourself."
    m 1b "That's what matters."
    mc "I'm trying."
    m 6x "Let's see if trying is paying off."
    m "Show me what you wrote for today."
    mc "Sure. Here you go."
    "I hand Mateo my poem."
    $ nextscene = "m_" + poemwinner[1] + "_" + str(eval(poemwinner[1][0] + "_appeal"))
    call expression nextscene

    m 6b "Anyway... are you ready to read my poem now?"
    m 1b "I'm quite proud of how this one turned out."
    mc "Sure, let's take a look."
    return

    
label ch3_m_start:
    show mateo 6b at t11
    m "Hi [player]~"
    m "Have you thought about what you want to submit to perform at the festival?"
    if poemwinner[0] or poemwinner[1] == "sayori":
        mc "What? No..."
        mc "I'll think about that over the weekend."
        mc "Right now, I want to know what you found out about Satori."
        "His friendliness diminishes a bit."
        m 1h "Straight to the point, I see."
        m 1aa "You must care about him more than I realized."
        m 1d "It's understandable."
        m "Your history with him...that's what holds you two together."
        m 3q "It's an important thing; history."
        m 3r "It defines who we are and the relationships we develop with others."
        "Mateo gives me a curious look."
        m 1f "History with someone...defines how that person sees you."
        m "And how you see them."
        "I'm not sure what Mateo's getting at."
        "But it's making me weirdly uncomfortable."
        mc "Look, just tell me what you found out."
        show mateo 6r at t11
        "Mateo gives a sigh."
        "He seems almost disappointed, though I have no idea why that could be."
        m 1d "Tell me, [player]..."
        m 1i "Have you been flirting with Satori lately?"
        mc "Flirting??"
        "What the hell does that have to do with anything?"
        "I'm not sure how to respond to that."
        mc "I mean..."
        mc "I treat him like I always do!"
        m 1y "...Like a brother?"
        mc "..."
        mc "Brother?"
        m 1aa "Nevermind."
        m 1d "Look, I know how much you care about Satori."
        m 1i "And I know how awful you'd feel if something bad happened to him."
        m 1c "So, keep an eye on him."
        m 1d "He was very happy when you joined the club."
        m 6r "To be honest, he didn't tell me why he's acting up."
        m 6d "I still stick to my original theory on that."
        m 5r "In any case, this really isn't the time to be talking about it."
        m 1a "Anyway, let's take a look at today's poem."
        "I let Mateo take the poem I'm holding."
        m 1d "Hm..."
        m 1aa "Why does this not surprise me?"
        mc "..."
        show mateo 1q at t11
        "Mateo sighs and shakes his head as he hands my poem back."
        m 1e "It's a good poem."
        m "Perhaps reading it will put Satori in a better mood."
        m 1m "Since you clearly wrote it for him."
        mc "Huh? I-I didn't..."
        m 1o "It doesn't matter."
        m 1f "It really doesn't."
        "He forces a sad smile."
        m 1e "Anyway, I'll share my poem with you now."
        mc "Erm...alright..."
        return
    if poemwinner[0] or poemwinner[1] == "yuri":
        mc "No."
        mc "It's not exactly the first thing on my mind right now."
        m 4k "Well, really try to think about it and let me know as soon as you decide." 
        m 6a "Anyway, let's take a look at today's poem."
        "I let Mateo take the poem I'm holding."
        m "Hmm...I guess we know what the first thing on your mind really is..."
        m "But I suppose you can't spend this much time with Yuuri and not pick up any of his writing habits." 
        m "He must be one hell of a teacher."
        mc "You could put it that way." 
        mc "Or you could look at it as, I'm just a really good student."
        m "Ahaha! Nice try, but that's not gonna fly with me!" 
        m "I've noticed how much time you spend with him." 
        m "I think I've heard him speak more these past couple days than he has in the entire year." 
        m "Not to mention how happy he's been acting." 
        m "Something's been putting a smile on his face..."
        mc "Hey, don't get the wrong idea." 
        mc "We've just been reading together."
        m "Oh, don't downplay it." 
        m "You spend every day with him reading that weird novel..."
        mc "And...what's your point?" 
        mc "The guy has problems socializing." 
        mc "When he spends time with me, he doesn't feel alone." 
        mc "I'm pretty sure that's a good thing." 
        mc "And I'll have you know, that weird novel kicks ass." 
        m "So defensive." 
        m "I get it." 
        m "Just...be careful." 
        m "Yuuri isn't used to opening up." 
        m "So if something bad happens while he's vulnerable, it can be really hard on him." 
        m "Those books aren't a total escape from reality." 
        m "They're just a bandage."
        mc "You say that like you think I'm going to hurt him..."
        m "On the contrary." 
        m "If anything, he might accidentally hurt himself."
        mc "Maybe you should worry less about Yuuri and more about Satori." 
        mc "Did you find out what was wrong with him?"
        mc "Did you find out what was wrong with him?" 
        m 1ab "Ah, yes."
        m "The other important guy in your life."
        m 1aa "You must care about him more than I realized."
        m 1d "It's understandable."
        m "Your history with him...that's what holds you two together."
        m 3q "It's an important thing; history."
        m 3r "It defines who we are and the relationships we develop with others."
        "Mateo gives me a curious look."
        m 1f "History with someone...defines how that person sees you."
        m "And how you see them."
        "I'm not sure what Mateo's getting at."
        "But it's making me weirdly uncomfortable."
        mc "Look, just tell me what you found out."
        m 6r "To be honest, he didn't tell me why he's acting up."
        m 6d "I still stick to my original theory on that."
        m 4r "In any case, this really isn't the time to be talking about it."
        m 1a "Anyway, I'll share my poem with you now, okay?"
        mc "Erm...alright..."
        return
    if poemwinner[0] or poemwinner[1] == "natsuki":
        m "This is a temporary placeholder till we get Nat's Poem Response here."
        m "In the meantime check if the poem shows up and the end also."
        mc "W-wha?"
        m "Here you go!"
        return

label m_natsuki_1:
    mc "...Do you like it?"
    m 6k "[player]...your handwriting is atrocious."
    mc "...!"
    m 6u "It's hardly legible."
    m 1x "Tell me...were you holding the pencil with your feet?"
    mc "Okay, okay!"
    mc "I get it!"
    mc "I'll work on my handwriting! Jeez!"
    mc "You don't have to be such a jerk about it."
    show mateo 1k
    "Mateo chuckles again, a bit louder this time."
    "His smug attitude only pisses me off even more."
    m 3v "From the small assembly of letters I could actually decipher as words, it sounds like the childish dribble Natsuko writes."
    m 1d "Not that he's a particularly bad writer."
    m 1c "I'm just not fond of that style."
    m 3r "It's very 'Shel Silverstein'."
    mc "Who's she?"
    m 3d "{i}He{/i} is famous for telling all kinds of stories in just a few simple words."
    m 3q "His poems can be funny, endearing, or even sad."
    m 3d "And sometimes, they're only a few lines long."
    m 3a "They feel like they're written for little kids, but they can express views of the world that would apply to anybody."
    mc "So...you're saying Natsu writes like that?"
    m 1j "Exactly."
    m 6j "I hope to see your style evolve into something more, though."
    m 6k "You're not a lost cause just yet."
    mc "I definitely plan on trying different things."
    mc "It will take a while before I feel comfortable doing this."
    mc "But rest assured, I am NOT a lost cause."
    m 6a "Good to hear."
    m 4b "I want to see you try new things."
    m 4k "That is the best way to find the kind of style that suits you, after all."
    m 4j "Don't force yourself to write the way everyone wants you to write."
    m 1s "I mean..."
    m 1t "It's not like you have to worry about impressing them..."
    return

label m_sayori_1:
    mc "...Do you like it?"
    m 6k "[player]...your handwriting is atrocious."
    mc "...!"
    m 6u "It's hardly legible."
    m 1x "Tell me...were you holding the pencil with your feet?"
    mc "Okay, okay!"
    mc "I get it!"
    mc "I'll work on my handwriting! Jeez!"
    mc "You don't have to be such a jerk about it."
    show mateo 1k
    "Mateo chuckles again, a bit louder this time."
    "His smug attitude only pisses me off even more."
    m 3v "From the small assembly of letters I could actually decipher as words, it sounds like something Satori would like."
    mc "...Is that so?"
    m 6d "Well, you're good friends."
    m 6c "It's not surprising that your writing styles are so similar."
    mc "Well, we're best friends who have a lot in common."
    mc "But we do have our differences too."
    m 6ab "If you say so."
    mc "What do you know about Satori's writing style anyway?"
    mc "I thought this was out first time sharing poems."
    m 6i "That may be true, but it doesn't take a genius to know what style each of us are bound to like if you just pay attention."
    m 3t "Assuming you're even capable of that."
    m 3r "Take Satori for example..."
    m 3d "I see his writing having a really gentle feel to it..."
    m 3t "With an occasional spike of hostility."
    m 3b "He's an emotional guy who would explore with emotions, like happiness and anger."
    m 1a "Perhaps even sadness."
    mc "...Sadness?"
    mc "That's where you're wrong, Mateo."
    mc "I think I would know if my best friend was feeling sad."
    m 1h "Would you?"
    mc "..."
    m 6j "Anyway, since it's your first time writing, I suppose you can still experiment with various styles."
    m 6k "You're not a lost cause just yet."
    mc "I definitely plan on trying different things."
    mc "It will take a while before I feel comfortable doing this."
    mc "But rest assured, I am NOT a lost cause."
    m 6a "Good to hear."
    m 4b "I want to see you try new things."
    m 4k "That is the best way to find the kind of style that suits you, after all."
    m 4j "Don't force yourself to write the way everyone wants you to write."
    m 1s "I mean..."
    m 1t "It's not like you have to worry about impressing them..."
    m 1ag "Right?"
    mc "..."
    mc "Right."
    return

label m_yuri_1:
    mc "...Do you like it?"
    m 6k "[player]...your handwriting is atrocious."
    mc "...!"
    m 6u "It's hardly legible."
    m 1x "Tell me...were you holding the pencil with your feet?"
    mc "Okay, okay!"
    mc "I get it!"
    mc "I'll work on my handwriting! Jeez!"
    mc "You don't have to be such a jerk about it."
    show mateo 1k
    "Mateo chuckles again, a bit louder this time."
    "His smug attitude only pisses me off even more."
    m 3v "Actually...it would be a great poem if your handwriting weren't so distractingly bad."
    m 1j "I wasn't expecting you to go for something so deep."
    m 4k "I'm impressed."
    mc "Well...crappy handwriting aside, I guess my effort kinda blew away your low expectations of me, didn't it?"
    m 6n "Alright, alright."
    m 6u "Don't get too proud of yourself."
    m 6w "It's a pretty good poem."
    m 4v "From the small assembly of letters I could actually decipher as words, it sounds like something Yuuri would like."
    m 4d "He loves writing that's full of imagery and symbolism."
    m 4r "This style leaves readers to derive their own meaning out of it."
    m 4q "It's actually very challenging to write like that effectively."
    m "It can take years of practice, which I'm assuming Yuuri has at this point."
    m 4a "But you..."
    m 1b "You seem to be a bit of a natural."
    mc "Well, I mean..."
    mc "I'm sure I'm nowhere near his level yet."
    m 1s "I agree."
    m 4t "Your use of imagery may be impressive, but you still obviously have a lot to learn."
    m 6k "You're not a lost cause just yet."
    mc "I definitely plan on trying different things."
    mc "It will take a while before I feel comfortable doing this."
    mc "But rest assured, I am NOT a lost cause."
    m 6a "Good to hear."
    m 4b "I want to see you try new things."
    m 4k "That is the best way to find the kind of style that suits you, after all."
    m 4j "Don't force yourself to write the way everyone wants you to write."
    m 1s "I mean..."
    m 1t "It's not like you have to worry about impressing them..."
    m 1ag "Right?"
    mc "..."
    mc "Right."
    return

label m_natsuki_2:
    m "This is a temporary placeholder till we get Nat's Poem Response here."
    m "In the meantime check if the poem shows up and the end also."
    mc "W-wha?"
    m "Here you go!"
    return

label m_sayori_2:
    m 6a "Hmm... Another Satori poem?"
    m "Well, aren't you two the dynamic duo?"
    mc "Well...we are pretty dynamic."
    mc "And...there's two of us..."
    m 6v "Witty, as usual."
    "He hands me back my poem."
    m 1w "You spend a lot of time with him, don't you?"
    m "Even in the club, you two are inseparable."
    m 1t "It's... Sweet."
    m 1aa "Almost nauseating."
    m 1d "I know it's none of my business..."
    m 1i "But, would it kill you to hang out with anyone else?"
    mc "..."
    m "I mean..."
    m 6i "If you spent time with the other members in this club, there may be a change or even an improvement in your writing style."
    m 4i "I'm just saying..."
    "Oh...we're talking about my writing?"
    "I mean...of course we are."
    mc "Well...I guess..."
    m 1h "Because, right now..."
    m "I feel like you're just piggybacking on Satori's personal style."
    "Wait...what??"
    mc "That's not what I'm doing at all!"
    m 1c "..."
    m 6k "Hahaha! Relax!"
    m "I'm just teasing!"
    mc "...?"
    m 6m "I mean, sure..."
    m 6n "You could stand to spend some time with the rest of us..."
    "I raise a suspicious brow."
    "We're definitely not talking about my writing anymore..."
    m 6j "...But your style is different enough from Satori's to be your own."
    m "So, that's good."
    m 6b "Anyway... are you ready to read my poem now?"
    m 1b "I'm quite proud of how this one turned out."
    mc "..."
    mc "Y...yeah. Let's have a look."
    return

label m_yuri_2:
    m 6a "This one's not bad." 
    m 6b "It's like yesterday's, only the imagery is better." 
    m 1b "Are you continuing to find inspiration in Yuuri's work?"
    mc "For sure." 
    mc "Can't deny that he's talented."
    m 3i "Indeed." 
    m 3m "His poems are the most... intense." 
    m 1a "He sure turns into a very different person when he picks up a pen."
    mc "I noticed that too."
    m 1x "It's always the quiet, mysterious ones who are the most appealing, aren't they?"
    mc "Um..."
    "I'm not 100% sure what Mateo is getting at right now."
    m 1t "Are you hoping to solve the mystery, [player]?" 
    m 1ag "Perhaps if you write the way into his heart, he'll let you into his dark little world..."
    mc "Gah!" 
    mc "I... I wasn't..."
    m 6k "Ahahaha!" 
    m "Calm down. I'm only joking." 
    m 6v "Besides..." 
    m "I'm pretty sure he already has a girlfriend."
    mc "...!"
    mc "Are you fu..."
    mc "Ah...I mean..."
    mc "He does?"
    m 6w "Yeah." 
    m 6t "A fictional one, anyway."
    "He kind of whispers that last part." 
    "What a colossal jerk." 
    mc "Funny stuff."
    m 1k "Ha! I thought so." 
    return
