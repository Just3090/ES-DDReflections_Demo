label ch3_main:
    window hide
    show bg bedroom
    with dissolve_scene_full
    "Hoy es lunes, y la semana no ha podido ser más anodina."
    "Me hallo en mi habitación, tirado en la cama y mirando al techo."
    "Para mi sorpresa, Monika y yo nos hemos escrito bastante."
    "Aunque bueno..., la mayoría era sobre el festival."
    "Ayer por la tarde, Monika me recordó que iba a colocar los folletos en el club antes de que empezasen las clases."
    "Aún así..."
    "Cuando le volví a preguntar acerca de su dimisión del club de debate, prácticamente me evadía la pregunta sin siquiera esforzarse."
    "Desde entonces, solamente pienso en por qué actúa así. "
    "Una parte de mí sabe con claridad que esconde algo que no me quiere contar acerca de esto."
    "Miro la hora en el despertador."
    "{i}6:30 AM{/i}"
    "Debería ir preparándome para ir al instituto."
    "Me levanto de la cama y voy al baño para darme una ducha rápida."
    show bg kitchen
    with dissolve_scene_full
    "Una vez que me he duchado, me pongo el uniforme limpio y agarro mis cosas mientras me dirijo a la cocina."
    "Saco un sándwich común del refrigerador y lo meto en mi mochila."
    mc "Disfruté comer en el techo de la escuela el viernes durante el almuerzo."
    "Me siento en la silla y tomo un desayuno rápido."
    "Una vez que termino, me dirijo a la puerta principal y me pongo los zapatos antes de salir de la casa."
    play sound closet_open
    show bg residential_day
    with wiperight_scene
    play music morning
    $ pause (0.1)
    play sound closet_close
    "Cierro la puerta detrás de mí y me detengo en la acera, pensando en algo."
    "Sayori me dijo el viernes pasado que vivía a unas pocas cuadras de aquí."
    "¿Tal vez pueda esperarla?"
    "Miro de reojo mi teléfono."
    "{i}7:30 AM.{/i}"
    "Asiento con la cabeza."
    "Probablemente no ha salido aún para la escuela."
    "Está bien, puedo esperarla."
    "..."
    "Han pasado veinte minutos."
    "Y aún no he visto a Sayori, ¿quizás se fue antes que yo al final?"
    "..."
    "Probablemente me estoy retrasando por culpa de esto."
    "Camino un poco más rápido hacia la escuela."
    stop music fadeout 2.0
    window hide
    pause 2
    $ s_name = "??????"
    s "¡Heeeeeeeeeeeeeey, [player], espera por mí!"
    mc "Huh?"
    $ s_name = "Sayori"
    play music t2 fadein 3.0
    "Me doy la vuelta para ver a Sayori corriendo en mi dirección, agitando los brazos en el aire."
    "Decido detenerme para que pueda alcanzarme."
    show sayori base uniform neut ml e4c awkw rup lup at t11
    s "...Haaah... ...Haaaaah."
    show sayori base uniform neut mb e1a rdown ldown
    s "[player], ¿eres un dormilón como yo también?"
    mc "¿Un dormilón?"
    mc "No, la verdad no. He estado despierto desde las seis y media."
    mc "Y en realidad... te estaba esperando, pero pensé que te habías ido antes que yo."
    show sayori base uniform rup b2c mh e1a nobl
    s "¿En serio? ¡Lo siento!"
    show sayori base uniform e2a mi rup lup b1a awkw
    s "Mi alarma no sonó, aunque estaba segura de haberla puesto anoche antes de irme a dormir."
    show sayori base uniform neut e1a ldown mb nobl
    s "¡Pero deberías haberme enviado un mensaje!"
    mc "¿Enviarte un mensaje?"
    mc "Sayori... no tengo tu número."
    show sayori base uniform e2a b1c mh rdown
    s "¿Ooooh?"
    show sayori base uniform neut e1a b1a mb
    s "I thought I gave it to you on Friday!"
    mc "Well... no."
    mc "Anyways, we should go or we'll be late."
    show sayori base uniform e2a ml rup lup at rhide
    s "Aaaaah! Yes, let's go quickly, [player]--!"
    $ pause (0.4)
    hide sayori
    "Sayori runs off without telling me."
    mc "Heyyy, wait for me!"
    "I speed up my pace to catch up to her."
    show bg re2
    with wiperight_scene
    "On the way to school, Sayori and I quickly exchanged phone numbers."
    "We chatted a bit about how the weekend went but didn't get into it further."
    show bg school_front
    with wiperight_scene
    "Arriving just in time before the school bell rang, we said our goodbyes as we headed to our classes."
    mc "Let's get this day over with..."
    stop music fadeout 2.0
    show bg class_day
    with dissolve_scene_full
    play music t3
    play sound bell
    "The school bell rings signaling the end of classes and the beginning of lunch break."
    "I collect my things and head to the roof of the school."
    scene bg roof
    with wiperight_scene
    stop music fadeout 2.0
    "After opening the door, I see Monika standing on the railing, looking at the view."
    play music evening
    show monika base uniform neut e4a at t11
    "I put my bag down on the bench and walk towards her discreetly."
    "I land to her right looking straight ahead."
    "We both say nothing to each other."
    "Just the wind blowing and the sound of nature is audible to our ears."
    "After a moment of silence I decide to cut the silence that had settled."
    mc "Nice view isn't it, Monika?"
    "Monika nods her head."
    show monika base uniform neut e1c me
    m "Indeed. It's a beautiful view, [player]."
    show monika base uniform neut e1c md
    mc "...Isn't Sayori eating on the roof?"
    show monika base uniform neut e1c me
    m "...She's not coming for a while, she had to talk with one of the teachers."
    show monika base uniform neut e1c md
    "So that means there will be a little alone time between Monika and I.."
    "Maybe I can dig a little deeper to find out what happened when she left the debate club."
    "I'm still a little afraid of her reaction though, she's been pretty vaguely cold every time I've asked her that question via S.M.S."
    mc "Say Monika, I have this question for you--"
    show monika base uniform neut e1a me b1c
    m "Is it that question again?"
    show monika base uniform neut e1a me rhip
    m "[player], do you know you're really forceful with that?"
    show monika base uniform neut e1a me rdown
    m "How many times have I told you by message?"
    show monika base uniform neut e1c md rhip
    "Monika dryly cuts me off looking me straight in the eye."
    mc "Monika, I know I sound like I'm overreacting, but listen--"
    show monika base uniform neut e1a me rdown
    m "Yes, you are exaggerating."
    m "Remember what I told you?"
    show monika base uniform neut e1a me lpoint
    m "It's better to focus on the present instead of the past."
    show monika base uniform neut e1a me ldown
    m "What don't you understand about it, [player]?"
    show monika base uniform neut e4a b3b me
    "I feel annoyance coming out in Monika's voice, which has destabilized me a little bit, making me lost in my thoughts."
    "There is a small moment of silence before I decide to break it."
    show monika base uniform neut e1a b1c md
    mc "You're absolutely right, Monika, we must concentrate on the present and not remain stuck in the past."
    mc "But listen, I know that something happened and you want to hide it."
    show monika base uniform e4a b2b me
    mc "You know Monika, I really like you and I want you to know that."
    mc "But the fact that you don't want to tell me is proof that you still don't fully trust me."
    show monika base uniform e1a b1b
    mc "Yet... remember last year when we were in the same class?"
    mc "How we worked together?"
    show monika base uniform e1c me
    mc "We trusted each other, at least I thought so."
    show monika base uniform e4a md
    m "..."
    mc "Does Sayori, your best friend, know about it?"
    show monika base uniform e1c me
    m "No, she doesn't know the story."
    show monika base uniform e4a me
    m "I am just ashamed."
    mc "Ashamed of what?"
    show monika base uniform e1c md
    m "Ashamed to say it, that's all."
    mc "Monika, you can really tell me."
    mc "I will keep it inside of me. Believe me, please."
    show monika base uniform e4a me
    mc "No one else but me will know what you are holding inside.."
    $ renpy.music.set_volume(0.8, delay=3)
    m "..."
    "Monika inhales briefly closing her eyes."
    play channel1("<loop 06.058>mod_assets/bgm/piano.ogg") volume 0.1
    show monika base uniform e1c me
    m "It's just, I've been thinking about a new activity for the debate club."
    show monika base uniform e1b mi
    m "I wanted to get out of this vicious cycle since I had taken the vice president position."
    show monika base uniform e4a lpoint mh b2a
    m "I was optimistic!"
    show monika base uniform e1b me ldown b1b
    m "I thought it was a great idea, fun to do."
    show monika base uniform e4d md b1a
    m "But if only I had known what was going to happen..."
    mc "What happened, Monika?"
    "Monika takes a gulp of air with her mouth."
    show monika base uniform e1c b1b me
    m "It was a nightmare."
    show monika base uniform e1g
    m "Nobody found my activity interesting."
    show monika base uniform e4d mj
    m "Nobody."
    show monika base uniform e4d mj
    m "Not only had I wasted time for nothing working all this out, but..."
    m "...But they trashed everything I had done."
    show monika base uniform e1h mk
    m "Everything I had planned for the club to run the festival.."
    show monika base uniform e4e ml
    m "...They tore up the posters that I had planned and prepared for the festival."
    show monika base uniform e1h ml
    m "It took me a long time to do everything..."
    show monika base uniform e1h mk
    m "It took me almost two whole weeks!"
    show monika base uniform e4e ml
    m "Two whole weeks where I was sacrificing my free time to be able to move the club forward."
    show monika base uniform e4e mm
    m "...They told me it was shit, that it was sloppy work.."
    show monika at thide
    hide monika
    "Monika buries her head on my shoulder, sobbing."
    "I take her by the arm."
    "A stream of tears run down her face and stain my jacket at the same time."
    m "It all went up in smoke...!"
    m "In a few moments..."
    "I feel Monika's hand tightening on my forearm."
    "Only the sounds of her sobs are audible."
    "Monika, I'm really sorry that you went through this."
    mc "They are just assholes and I mean that sincerely. They don't deserve someone as talented as you."
    "There is a slight silence before I decide to speak again."
    mc "Listen carefully, Monika.."
    mc "... In my club, you will be respected."
    mc "You will be listened to."
    mc "And above all..."
    mc "You will be loved by me and the other members."
    mc "No one has the right to treat you in such a way."
    mc "Your ideas that you proposed to me this Friday were excellent, believe me."
    mc "I'm sure Sayori, Natsuki and Yuri will think of the same thing."
    "Finally, Monika's sobs start to stop. But she still has her head buried on my shoulder."
    "I hear footsteps approaching from the stairs."
    "Is it Sayori?"
    "It's very likely, but you never know."
    "I release Monika from my arm."
    s "{i}Sorry for the delay, the teacher yelled at me about a test I missed--{/i}{w=0.04}{nw}"
    show sayori base uniform e4b mc at l21
    show monika base uniform e4d mj at t22
    s "I have a sudden urge to--{w=0.02}{nw}"
    show sayori base uniform e2a mi rup lup
    s "Monika, are you okay???"
    show sayori base uniform e1a b1c md rdown ldown
    "I look at Sayori who is displaying a worrying look on her face and slowly starts to move closer to the two of us."
    show monika base uniform e1b me
    m "It's okay Sayori.. It was just.."
    show monika base uniform e4d mj
    "Monika's having trouble forming her sentence."
    "I walk towards her and whisper to her, so that it can't be heard by Sayori."
    mc "{i}Do you want to tell her your story, Monika?{/i}"
    "..."
    "She doesn't answer."
    "She just glances from Sayori to me."
    show sayori base uniform e1a b1b mh rup
    s "What did you tell her, [player]?"
    mc "Uuumh... I-"
    "My thoughts scramble with a snap of my finger. Monika didn't even answer me if I could tell her or not!"
    "Should I tell her or not?"
    "..."
    "....."
    "I made a promise to her not to tell."
    "If she wants to know, she'll have to go through Monika."
    "As a sign of respect for her."
    show monika base uniform e1c b1b me
    m "Sayori... it's a long story."
    show monika base uniform e4e b1b me
    show sayori base uniform rup lup b1b md
    s "Can I give you a hug, Monika..?"
    show sayori behind monika at t22s
    "Monika doesn't say anything, but Sayori approaches to hug her."
    show sayori base uniform e4a md ldown b1b
    "Sayori closes her eyes and starts to use a relaxed voice."
    show sayori base uniform e4a me lup b1a
    s "Monika, You can tell me everything. I'm your friend."
    show sayori base uniform e4a mg ldown b1b
    s "And a friend... listens to everything you hold inside."
    s "I don't like to see you sad like this, Monika."
    show sayori base uniform e4a me rup b1a
    s "Just tell me what you hold inside of your heart."
    m "..."
    "Finally, Monika dictates everything she told me to Sayori."
    "I couldn't do anything else but stand in front of them like a common lamp post."
    window hide
    stop channel1 fadeout 2.0
    stop music fadeout 2.0
    show bg roof_r
    show sayori base uniform neut b1b ma rup
    show monika base uniform neut e1c md b1b
    with dissolve_scene_full
    "It seems that Sayori has managed to lighten the mood, in a way that escapes me."
    "..."
    show monika base uniform neut e1a me b1b
    m "Just.."
    show sayori base uniform e1a b1b at t21
    show monika base uniform neut e1a md b1b
    m "Do you promise to keep this just to yourself?"
    mc "I promise, Monika."
    "I imitate a zipper with my mouth and finger."
    show sayori base uniform b1b e1a lup rup
    s "This will stay between the three of us, Monika. You have our trust."
    show monika base uniform e1a b1b ma
    m "Thank you so much. You really are precious friends."
    mc "Don't worry Monika, if you have anything to say, you can say it directly to me or Sayori."
    s "Yes, and..."
    show sayori base uniform e4b b1a mc rup lup
    s "You're really smart and beautiful, Monika!"
    show monika base uniform e1c b1b lpoint blaw mb
    m "Haha.. how many times did you tell me that, Sayori..?"
    show monika base uniform e1c b1b lpoint blaw ma
    show sayori base uniform e2a b1a mf rup at h21
    s "Ah!... uh... I don't know, I didn't count!"
    show sayori base uniform neut e4b mc rup lup
    s "But my words are sincere!"
    show sayori base uniform neut e1a mb rdown lup
    s "And I will repeat it again and again!"
    show sayori base uniform neut e4b ma rup lup at face
    s "And thanks again to you, [player], for being the best president!"
    show monika base uniform e4b awkw mb b1a
    "All of a sudden Sayori quickly wraps her arms around me."
    "Which surprises me slightly to be honest."
    mc "Hey, hey!"
    show sayori base uniform neut mb rup ldown at t21
    s "Ahaha, sorry! It's just that I'm a hugger!"
    show monika base uniform neut ma e1a rhip nobl
    m "Don't be surprised, [player]. It's Sayori's natural behavior."
    mc "I've noticed it since she's been in the club, don't worry, Monika."
    show monika base uniform ma e4b rdown ldown
    "Monika sneers in a tender way."
    show monika base uniform me b1a rhip e1a
    show sayori tap m1 e2 blaw b1 at s21
    "An audible growl can be heard from Sayori's belly."
    show sayori tap m1 e1 nobl at t21
    s "Hehehehe.. How about we go eat?"
    show sayori base uniform e1b b1b mc
    show monika base uniform ma b1a rhip
    s "Mister Mumty is getting hungry!"
    mc "Mister Mumty..?"
    mc "You gave your stomach a nickname, Sayori?"
    show sayori base uniform e4b b1a rup lup mc
    s "Yeeeeeees!"
    mc "And where did you get that nickname?"
    show sayori base uniform e2a mf b1f
    "Sayori displays a puzzled look thinking for a little while."
    show sayori base uniform e1a mb b1a
    s "I saw it on the internet and thought the name was funny and cute at the same time!"
    show monika base uniform e4b mb rdown
    "Monika and I both share a laugh."
    show sayori tap m2 e1 b1 awkw at s21
    s "Eeeeeh, don't judge like that!"
    show monika base uniform neut ma
    show sayori tap m2 e2 b1 awkw at t21
    mc "Ahaha, don't worry. I'm not judging you, Sayori."
    mc "Anyway, we should enjoy the time we have left to go eat."
    show sayori base uniform neut e4b mc b1a at h21
    s "Yeeeeees!, I'm so hungry!"
    show sayori at rhide
    $ pause (0.01)
    hide sayori
    "Sayori runs to the bench to sit in the middle."
    show monika at thide
    hide monika
    "Monika and I follow her behind."
    "We take out our food and start eating."
    stop music fadeout 2.0
    show bg corridor
    with dissolve_scene_full
    "The rest of the lunch on the roof of the school with Sayori and Monika went on in an ordinary way."
    "We talked about various and varied topics again."
    play sound bell
    "After the bell rang to signal the resumption of classes and the end of the lunch break, Sayori and Monika being in the same class, we parted saying goodbye."
    show bg class_day
    with dissolve_scene_full
    pause 1
    play music t3
    "The rest of the afternoon classes are nothing more than ordinary."
    "I wrote a poem for Monika quickly while I was bored."
    call showpoem (poem_p11, music=False) from _call_showpoem_18
    stop music
    pause 1
    play sound bell
    "The bell rings at the end after a long wait."
    "I pack my things and get up from my chair."
    t "Just a minute, [player]. You're going to clean the classroom today."
    mc "Why?"
    t "The cleaning staff is not here today, so I had to designate a random student for today."
    t "Management's order."
    "That doesn't make any fucking sense!"
    "They don't have a substitute or I don't know instead of putting a student who didn't ask for anything in cleaning?!"
    "It's not fair."
    "I'm grumbling inside."
    mc "Okay.."
    "All the other students in the class are already out with the teacher leaving last, leaving only me in the classroom."
    mc "Great, let's get this over with already."
    pause 5
    "After vaguely cleaning the classroom until I find it clean to my liking, I finally leave the classroom."
    show bg corridor
    with wiperight_scene
    "I take the stairs to the clubroom."
    mc "Great, I'm late for the club..."
    play sound closet_open
    show bg club_day
    with wipeleft_scene
    play music t3
    "Once I arrived at the club, I was directly approached by Monika."
    show monika base uniform neut me rhip at r11
    m "[player]! Why are you late?"
    mc "Ah, I'm sorry. I had to take care of cleaning my classroom."
    mc "For some reason I don't even want to say.."
    show monika base uniform neut mb rdown
    m "Mmmh, okay as long as you're here that's what counts!"
    mc "Didn't I miss anything otherwise?"
    show monika base uniform neut md rhip
    m "Not really."
    show monika base uniform mb ldown
    m "Only Yuri who brought her electric kettle and some teacups today to make tea."
    show monika base uniform e4b ma rhip
    m "She seems very pleased."
    show monika base uniform e1a ma rhip
    mc "I'm happy for her then."
    show monika at thide
    hide monika
    "I glance around the room."
    "I can see a tray sitting on a desk with, as Monika said, tea tassels and an electric kettle on top."
    "Natsuki and Sayori are sitting on the floor next to the cupboard reading a manga."
    "And Yuri is immersed in her book with a teacup in her right hand."
    "I turn back to Monika."
    show monika base uniform neut ma at t11
    mc "We'll talk about the plans for the festival to the others after we share the poems."
    show monika base uniform neut me rhip
    m "Okay. I'll tell them, [player]."
    show monika base uniform neut ma rdown
    m "I'll know how to do it."
    mc "No worries, Monika. I trust you anyway."
    show monika base uniform neut e4b
    "Monika smiles happily."
    show monika base uniform neut e1a mb
    m "I'll writes something on my notebook."
    mc "Alright, Monika."
    show monika at rhide
    hide monika
    "..."
    "I slump down on a desk, looking around and..."
    "... And I do nothing."
    "I could start poem sharing, but it's too early."
    "I could work more on the festival preparations, but that would be unfair to Monika."
    "And Monika seemed determined to tell the members about it."
    "I take another look around the room."
    "Sayori and Natsuki seem to be discussing about manga. I lay down my head at the desk, vaguely listening to their discussion."
    show natsuki cross uniform happ at t22
    show sayori base uniform ma at t21
    n "So what did you think of the first chapter, Sayori?"
    show sayori base uniform mb rup
    s "It was great!"
    show natsuki base uniform rhip lhip
    n "If you want next time we can continue reading the next chapter."
    show natsuki base uniform e4b mo rhip ldown
    n "I don't want to tell you more, but the story will be ten times better!"
    show sayori tap m1 n2 at s21
    s "...Hehehe... say, Natsuki... this reading made me a little hungry. Want to go to the vending machine?"
    show natsuki base uniform mh e1a rdown
    show sayori tap m1 e1
    n "What?"
    show natsuki e1a mi b1e blaw at h22
    n "Wait, don't tell me you came to read with me just to ask me that?!"
    show sayori tap m1 e2
    s "Hehe, no... A little bit... but it was Mister Mumty who told me that!"
    show natsuki e1a mi rhip lhip b1f
    n "You could have told me in advance that you weren't serious about reading with me, Sayori!"
    show natsuki e1a md rhip lhip b1f
    show sayori base uniform e1a b1b mg
    s "Huh? But, I was serious!"
    show sayori base uniform e4b b1a mc rup nobl at h21
    s "Pleaseeeeeeeeeeeeeeeeeeee, Natsuki!"
    show natsuki base uniform e4a b3b mi
    n "No, no, and no!"
    show natsuki cross uniform e1a b1c mh
    n "Sayori, I won't change my decision."
    show sayori base uniform e4b mc b1a rup lup
    s "Pleaseeeeeeee!"
    $ AutofocusStore.disable_zoom()
    $ AutofocusStore.disable_zorder()
    show sayori behind natsuki at t22s
    "Sayori wraps her arms around Natsuki holding her tightly."
    show natsuki base uniform fs e4 m3 b2 n1
    n "Raaah, please stop!"
    show sayori at h22s
    s "Pleaseeeeeeeeeeeeeeeeeeee Natsuki!"
    $ nref()
    show natsuki cross uniform e4a mm b3b blaw
    n "{i}-sigh-{/i}.. Okay! Okay!... I got it, I got it!"
    n "You won...!"
    $ sref()
    show sayori base uniform e4b mc rup lup nobl at t21
    s "Yeeeeeees!"
    "I'm slowly closing my eyes."
    $ AutofocusStore.enable_zoom()
    $ AutofocusStore.enable_zorder()
    scene black with close_eyes
    hide natsuki
    hide sayori
    pause 3
    "I don't know why, but I have a feeling that someone is right above me."
    "Out of reflex, I quickly open my eyes and raise my head too."
    show bg club_day
    show monika lean uniform at face (y=750)
    "Suddenly, I see Monika filling my field of vision."
    "I jump from my chair, missing a heartbeat."
    mc "Monika?!"
    show monika base uniform e4b mb awkw at t11
    m "Ahahaha! I'm sorry, I couldn't help it."
    show monika lean uniform ma nobl
    m "Didn't we get enough sleep last night, president?"
    mc "Not even, I was just in my thoughts!"
    show monika base uniform lpoint ma
    m "Come on, be a little more serious, [player]."
    show monika base uniform ldown mb
    m "You shouldn't slouch on the table like that."
    show monika lean uniform ma
    m "That's not worthy of a president, [player]~"
    mc "Aren't you exaggerating a little too much, Monika...?"
    show monika base uniform e4b ma
    "Monika laughs teasingly."
    show monika base uniform e1a mb
    m "I'm just kidding!"
    show monika base uniform me lpoint
    m "But seriously..."
    show monika base uniform mb ldown
    m "We should start sharing our poems so we have time to talk about the preparations afterwards!"
    mc "Yes, you're right. Let's go."
    show monika at thide
    hide monika
    "I get up from the chair heading to the front of the room."
    mc "Okay everyone!"
    mc "We'll start sharing our poems!"
    stop music fadeout 2.0
    show bg club_day1
    with wiperight_scene
    play music t5
    show sayori base uniform rup mb at t11
    s "Hi, [player]!"
    mc "Hi, Sayori."
    mc "How are you feeling in the club?"
    show sayori base uniform e4b mc rup lup
    s "I feel great!"
    mc "That's good then!"
    show sayori base uniform e1a ma rdown ldown
    mc "If you feel good, that's wonderful for me."
    show sayori base uniform e4b mc
    "Sayori smiles happily."
    show sayori base uniform e1a ma
    mc "Ready to share your poem, Sayori?"
    show sayori base uniform e1a mb
    s "Yep!"
    show sayori base uniform e4b mc rup
    s "You'll see that I wrote the best poem!"
    mc "I'm waiting for that."
    "Sayori hands me her poem with a big smile, I grab it and start to read it."
    call showpoem (poem_s2, img="sayori base uniform neut e1b b1b ma blaw lup rup") from _call_showpoem_19
    show sayori base uniform neut e1a b1a ma nobl rdown ldown
    mc "Damn it..."
    mc "Sayori, in a word..."
    mc "Impressive."
    show sayori base uniform e4b mc rup
    s "Hehehe, I told you I would write the best poem!"
    show sayori base uniform e1a ma
    mc "No kidding..."
    mc "Your poem is amazing Sayori, well done."
    show sayori base uniform e4b mc rup at h11
    s "Yaaaay! I got the congratulations from the president!"
    mc "Sayo--"
    show sayori base uniform e4b mc rup at h11
    s "That means it's the best poem of the day!"
    mc "Sayori.. this is not a competition."
    show sayori tap uniform e2 m2 b1 awkw at s11
    s "Pfffff, you're not funny, [player]."
    mc "But...!"
    mc "Well okay... congratulations Sayori, you won this competition.."
    show sayori base uniform e4b mc rup at h11
    s "Yaaaaay!"
    show sayori base uniform e4b mc rup lup nobl at h11r
    "I'm holding back from laughing, I just let a little amused smile show."
    show sayori base uniform neut e1a ma at t11
    mc "...Will you read my poem now?"
    show sayori base uniform mb
    s "Okay!"
    show sayori base uniform e2a b1f rdown ldown mf
    s "..."
    show sayori base uniform e1a b1a lup mb
    s "Your poem is excellent, [player]!"
    show sayori base uniform e4b mc rup lup
    s "But not more than excellent than mine!"
    mc "Uh... what do you mean?"
    show sayori base uniform e1a mb rdown
    s "Just kidding!"
    show sayori base uniform e4b mc rup lup
    s "Ahahaha, you're really good at writing poems!"
    show sayori base uniform e2a b1f mf ldown rdown
    s "Even if I didn't understand everything in your poem..."
    mc "Thanks, I guess..."
    show sayori base uniform e4b ma b1a
    "I'm not surprised. Sayori tends to write things that are a bit simpler, poems using more extensive vocabulary isn't really her strong point."
    "But I can honestly say that she is gifted and goes out of her way to write wonderful things."
    "I don't regret having her in my club."
    mc "Thank you for sharing your poem, Sayori."
    show sayori base uniform e1a mb lup
    s "You're welcome!"
    show bg club_day1
    hide sayori
    with wiperight_scene
    show monika base uniform neut ma at t11
    mc "Hi, Monika!"
    show monika base uniform neut mb
    m "Hey, [player]!"
    mc "How are you feeling?"
    show monika base uniform neut e4b mb rhip
    m "I'm feeling much better! Thanks for asking me."
    show monika lean uniform ma
    m "And how are you doing? Not many people ask if you're feeling good."
    mc "I'm doing great too, if I can say it like that."
    mc "Ready to share your poem, Monika?"
    show monika base uniform neut ma
    m "Yep!"
    "I hand my special poem to Monika."
    "..."
    show monika base uniform e2a md
    m ".... Hmmmm!"
    "Monika's eyes goes wide."
    show monika base uniform e1a b1b rhip ma
    m "[player]... did you really write this?"
    mc "Yes, I wrote that poem especially for you."
    show monika base uniform e1a b1b rdown ma
    m "You know, [player]... I'm sorry again for being so busy because of that crappy debate club."
    m "But from now on, we can rebuild our friendship."
    "Monika flashes me a sincere smile, glancing between the poem and me."
    mc "If you want... Monika, you can keep it..."
    show monika base uniform e1a b1b rhip ma
    m "I'll keep it, honestly."
    show monika base uniform e1a b1b rdown mb
    m "It will prove to me every day what a sincere person you are."
    m "I'm really glad I could be there."
    mc "Me too, Monika."
    show monika lean uniform ma
    m "Now, would you like to read my poem?"
    show monika base uniform mb
    m "I wanted to try something new."
    "Monika hands me her poem and I take it with my right hand."
    mc "All right, let's see..."
    call showpoem (poem_m12, img="monika base uniform neut ma b1b") from _call_showpoem_20
    mc "..."
    show monika base uniform neut ma b1a
    mc "Wow... Monika did you really write this?"
    mc "You really amazed me."
    show monika lean uniform ma
    m "Ahahaha! Thank you so much, [player]."
    show monika base uniform neut mb lpoint
    m "I wanted to try a new writing style as I said."
    show monika base uniform neut e4b ma ldown
    m "And I wrote it this morning, I was... really inspired."
    mc "Your poem is about the old days you lived in?"
    show monika base uniform neut e1a md rhip
    m "Hmmm..."
    show monika base uniform neut mb rdown
    m "Yes, you can say that."
    m "That was until I left the debate club."
    show monika base uniform b1b ma rhip
    m "I'd rather not really talk about it again now that I've said everything at the launch."
    mc "Yeah, you're right, now that I know what happened, I think we can forget about it."
    mc "Thank you for sharing your poem, Monika."
    mc "It was really an experience to read, I really enjoyed it."
    show monika base uniform b1a e4b mb
    m "Thanks to you too!"
    "Monika suddenly walks up to me, speaking in a low voice."
    show monika lean uniform ma
    m "{i}And... thanks again for your poem~{/i}"
    m "{i}I'll take care of it.{/i}"
    m "{i}I promise you.{/i}"
    mc "A-Ah.. Uh.. thank you.."
    "I don't know what to say, my heart is starting to race."
    show monika at thide
    hide monika
    "No time to recover, Monika has already left to share her poem with someone else."
    "I sigh heavily."
    show bg club_day1
    with wiperight_scene
    show natsuki base uniform rhip ma at t11
    mc "Hey, Natsuki!"
    show natsuki base uniform rdown mc
    n "Hi, Mr. President."
    mc "Please Natsuki, don't call me that."
    show natsuki base uniform rhip lhip mb
    n "Ahaha, why not, Mr. President?"
    show natsuki base uniform e4a b3c mc
    n "You hate it when people call you Mr. President?"
    mc "..."
    show natsuki base uniform b1a e4b mo rhip ldown
    n "Misteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeer. Presideeeeeeentttt."
    mc "Well, come on cute little girl, we should start sharing our poems."
    show natsuki base uniform e2a b1a mi
    n "You're not making fun of me?!"
    mc "You started first."
    show natsuki e1d mh rhip lhip
    n ".. Well okay, okay! I get it."
    show natsuki e1a md b1d ldown
    n "Give me your damn poem."
    "I laugh to myself, handing her my poem."
    show natsuki cross uniform md b1a
    "..."
    show natsuki cross uniform mg b1a
    n "Your poem is nice."
    show natsuki base uniform mh
    n "Better than yesterday's though."
    mc "Ah, thanks."
    mc "I appreciate your... honesty."
    mc "I wanted to try something different."
    show natsuki base uniform lhip
    n "No kidding, it's not like I noticed."
    n "Even Monika tried something new."
    show natsuki base uniform rhip
    n "Are you two connected or what?"
    mc "Huh?"
    mc "No, maybe yesterday's sharing influenced us on our writing!"
    mc "Who knows?"
    show natsuki cross uniform mg
    n "Yeah well I don't."
    mc "That's nice to hear from you..."
    mc "Will you share your poem with me now?"
    show natsuki base uniform ma
    n "Sure."
    show natsuki cross uniform mc
    n "I'll warn you, it's a little longer than Friday's."
    mc "Alright, let's see..."
    call showpoem (poem_n2, img="natsuki base uniform rhip lhip neut ma") from _call_showpoem_21
    "I want to act stupid."
    mc "Say Natsuki... Don't you hate spiders?"
    show natsuki base uniform e1a b1d mg
    n "What?"
    show natsuki base uniform e1a b1d mi
    n "Are you doing it on purpose?!"
    mc "Will you answer me?"
    show natsuki cross uniform e1a b1d mm blaw
    n "Would you like a kick to your groin so I can calm you down?!"
    mc "Hey hey! I was kidding, Natsuki."
    show natsuki cross uniform e1b b1f mh nobl at s11
    n "{i}-sigh-...{/i} Dummy."
    show natsuki cross uniform e1a b1f md at t11
    mc "More seriously, your poem is about the weird things another person would do?"
    show natsuki base uniform e1a b1a mh rhip lhip
    n "Yes and no."
    show natsuki base uniform e1a b1a mg ldown
    n "My poem is about the strange or weird passions that some people might have."
    "{i}(Isn't that what I more or less just said...?){/i}"
    show natsuki cross uniform mh
    n "This poem is put in the in the perspective of a person who likes and want to be friend with Amy, but she have a huge phobia for spiders."
    show natsuki base uniform blaw mi b1e rhip lhip
    n "I mean, as long as it doesn't hurt other people, people shouldn't have to judge!"
    show natsuki base uniform mg nobl rdown ldown b1a
    n "So to go back to what I was saying, she's holding back on not being friends with her because she'll judge her for her passion for spiders."
    show natsuki cross uniform mc
    n "And my poem wants to get that message across."
    show natsuki base uniform ma rhip
    mc "That's a really powerful message you're putting out there."
    mc "Would this Amy be one of your old friends that you knew or maybe yourself?"
    show natsuki base uniform e2a b1f mi blaw rhip at h11
    n "No!"
    show natsuki cross uniform e1b b1b mf
    n "It's... just like that."
    show natsuki cross uniform e1a b1a mg
    n "And why do you even ask that?"
    mc "Just like that."
    mc "Most of your poems that I've read so far were about what we're going through, what we've been through or a thought that's going through our head."
    "..I think?"
    show natsuki cross uniform e4a mc b3c
    n "Ha ha ha!"
    show natsuki base uniform e4b mo b3c rhip nobl
    n "I stand out from the club. Impressive coming from me, isn't it?"
    mc "Uh...yeah if you want."
    "Natsuki stands on herself, striking a flamboyant pose."
    "I decide to give her back her poem."
    mc "Thank you for sharing your poem, Natsuki."
    show bg club_day1
    hide natsuki
    with wiperight_scene
    show yuri base uniform neut md at t11
    mc "Hi Yuri!"
    mc "How are you?"
    show yuri base uniform neut mb
    y "Hello, [player]. I'm very well, thank you."
    mc "Great! Do you want us to start sharing our poems?"
    show yuri base uniform rup lup e1b
    y "It would be a pleasure to see your poem first, I want to see what you have wrote for today."
    show yuri base uniform e4b ma
    "Yuri smiles happily as I hand her my poem."
    show yuri base uniform e1b rdown ldown mf
    "..."
    show yuri base uniform rup lup b1b e1b ma
    "More and more, as Yuri reads my poem, her happy smile turns into a sad smile."
    "Finally she puts my poem on the desk."
    show yuri shy uniform b1 e2 m1
    y "I.. I'm sorry about how I acted on Friday, [player]..."
    show yuri shy uniform b1 e1 m2
    y "You probably hate me..."
    show yuri shy uniform b1 e2
    y "That must be why your poem is completely different from Friday's.."
    show yuri shy uniform n5 m2
    y "What a horrible person I am..."
    "Yuri buries her face in her hair, looking away."
    mc "Huh? No! Not at all, Yuri!"
    mc "Honestly, I don't hate you!"
    mc "I will never hate any of you."
    mc "In the end, you apologized and everything went back to normal."
    show yuri shy uniform n1 e1 m1
    mc "I just changed my style of poem to try something different!"
    mc "And I realize that wasn't really my strong point, so I think I'll go back to the style of my previous poem."
    show yuri base uniform e4a b2b mf rup lup at s11
    y "I.. It's really a relief."
    show yuri base uniform e1b ma at t11
    y "Maybe I overthought it after all.."
    show yuri base uniform e1b ma rdown ldown
    "Yuri smiles weakly to herself."
    "I quietly get my poem back."
    mc "May I see your poem Yuri?"
    show yuri base uniform e1a b1a mb
    y "It would be a pleasure."
    show yuri base uniform e4b ma rup lup
    y "I changed the form of my verses a bit, but I hope you still like it!"
    "Yuri hands me her poem, and once it's in my hands I start reading it..."
    call showpoem (poem_y12, img="yuri shy uniform e1 b1 m1") from _call_showpoem_22
    mc "I see you were a little inspired by me, Yuri."
    show yuri base uniform e1a mb rup
    y "Yes, indeed."
    show yuri shy uniform b1 e2 m1
    y "Your poem was..."
    show yuri shy uniform e1 m1
    y "...impressive, so I was a little inspired by yours..."
    show yuri base uniform e1a rup lup ma
    y "And I had started writing the beginning shortly after we shared our poems...{nw}{done}so uh..."
    show yuri base uniform e2b b1b mk blaw ldown
    y "And I had started writing the beginning shortly after we shared our poems...{fast}so uh..."
    show yuri base uniform rdown at s11
    y "I.."
    "Yuri gets lost in the middle of her sentence, I decide to step in."
    mc "I'm really glad, Yuri. Well done."
    mc "Glad in the sense that you are trying new things."
    show yuri base uniform e1a b1a md rup lup nobl at t11
    mc "Maybe one day you can see Natsuki to try something with the both of you?"
    mc "I know your writing styles are vastly different."
    mc "I'll be very interested to see what the result could be."
    show yuri base uniform e2a b1b rup ml awkw
    y "Ummh...!"
    mc "Ah.. sorry, I didn't want you to feel obligated to do that!"
    show yuri base uniform e2b b1b rup mk blaw
    mc "It was just... a suggestion like that."
    show yuri base uniform e2b mb ldown b1b awkw at s11
    y "Umh... I'll see about that.."
    show yuri shy uniform e2 b1 m1 n1 at t11
    y "I'd really like to get back on track with Natsuki... I've come to realize that our fight was stupid and should never have happened..."
    mc "I--"
    "Not giving me time to answer her, Yuri continues her sentence."
    show yuri shy uniform
    y "I... I will try to talk to her..."
    show yuri shy uniform e1
    mc "I'm counting on you Yuri, you can do it."
    mc "Thank you for sharing your poem."
    show yuri base uniform e1a mb rup nobl
    y "Thanks to you too."
    stop music fadeout 2.0
    show bg club_day
    hide yuri
    with wiperight_scene
    play music t3
    mc "Okay, everyone! Come to the front, Monika would like to talk to you about something."
    show natsuki base uniform neut mg rhip at t22
    show monika base uniform neut ma at t21
    n "We're going to talk about the festival I guess?"
    show monika base uniform e4b mb rhip
    m "Exactly!"
    show monika base uniform neut e1a ma lpoint
    m "Last weekend, [player] and I worked together by phone on the organization of the next few days for the festival that will take place this Friday."
    show natsuki cross uniform neut mh
    show monika base uniform neut ldown me
    n "Uugh.. do we really have to do this?"
    show natsuki base uniform neut lhip mg
    n "I mean, there are only three days left until the festival starts."
    n "We won't get much done in that amount of time, we'll just get humiliated in front of everyone in this school."
    $ yref()
    show yuri base uniform e1a rup lup mg at t33
    show natsuki base uniform neut lhip mg at t32
    show monika base uniform b1b at t31
    y "I-I agree with Natsuki."
    show yuri base uniform e1b rdown ldown b1b mg awkw
    y "Usually, last minute plans always lead to disaster..."
    mc "Everyone... please listen to Monika first and then we'll discuss it."
    show monika base uniform b1a e1a mb rhip
    m "So, as you know, the festival is coming soon!"
    show monika base uniform e1a ma lpoint
    m "With [player], we want to show that literature which can be something boring for most students in this school.... into something very intensive if I may say so!"
    show monika base uniform e4b ma rdown ldown
    m "That's why we decided we were going to do a poetry performance in front of an audience!"
    show monika base uniform e1a
    show natsuki base uniform md
    show yuri base uniform e2a b1b rup ml
    y "W-What???"
    show yuri base uniform mk
    y "A poetry performance??"
    show yuri base uniform e2b mk lup blaw
    "Yuri puts both hands towards her chest, and I can see her face is starting to turn an anxious red."
    show monika base uniform e4b mb
    m "Yes!"
    show monika base uniform e1a ma rhip
    m "We've already worked on the flyers and started putting them up in the school hallways this morning before the club meeting."
    show monika base uniform e1a md rdown
    show yuri base uniform e2a ml ldown
    y "Monika-!"
    show yuri base uniform mk rdown
    y "T-That's so sudden!"
    show monika base uniform e1a b1b md rdown
    show yuri shy uniform b1 m1 e2 n2
    y "I-I could never do that."
    show natsuki cross uniform mi e1a b1f
    n "Me too!"
    show natsuki base uniform mh e1b blaw rhip
    n "You didn't even ask our opinion first!"
    show monika base uniform e1a b1b me rhip
    m "Is this a bad idea you think?"
    show monika base uniform e1a b1b ma rdown
    mc "No, Monika, it's a very good idea."
    mc "But they are right about one thing; we should have told them before the weekend."
    mc "It's my fault, sorry."
    ny "..."
    "Natsuki and Yuri remain silent."
    show monika base uniform e1a b1b ma rdown at t41
    show natsuki base uniform at t42
    show yuri shy uniform b1 m1 e2 n2 at t43
    show sayori base uniform rup b1b mb at t44
    s "Girls, please. Monika and [player] worked very hard last weekend for all of this."
    show sayori base uniform lup
    s "And Monika and I know how much [player] cares about this club."
    show sayori base uniform e4b b1a mc at h44
    s "And.. thanks to him, I got to be friends with both of you!"
    show sayori base uniform e1a b1b ldown mb
    s "So it's important to give back to him."
    show sayori base uniform e1a b1b mb
    s "And the least we can do is to participate."
    show sayori base uniform e1a b1b ma
    show yuri base uniform e4a b2b mg rup lup at s43
    y "-sigh-.. I..."
    show yuri shy uniform b1 m1 e1 n1 at t43
    "Yuri glances at me quickly."
    window hide
    pause 2
    show yuri shy uniform e2
    y "I changed my mind, I agree to do the poetry performance..."
    show sayori base uniform e4b b1a mc at h44
    s "Yaaaaaaayy, thank you, Yuri! You are the best!"
    "Sayori is hopping on the spot."
    show yuri e5 b2
    y "-sigh-... This club is seriously going to kill me..."
    show monika base uniform e4b b1b mb awkw lpoint
    m "Oh my-... Everything will be fine, don't worry!"
    show monika base uniform e1a b1a ma nobl rhip ldown
    "Monika looks towards Natsuki."
    show monika base uniform e1a mb rhip ldown
    m "Natsuki?"
    show monika base uniform e1a ma rhip ldown
    show natsuki cross uniform e1a mg b1a nobl
    n "What?"
    show natsuki cross uniform mi b1f
    n "You think I'm going to let you do this just because Yuri changed her mind?"
    show natsuki cross uniform mi b1e blaw
    n "You're dreaming...!"
    "The three of us stare intensely at Natsuki with a disappointed look."
    show sayori base uniform md e1a b1b
    show monika base uniform md e1a b1b
    "Natsuki looks around, starting to feel unsettled."
    show natsuki base uniform rhip lhip mg b1e nobl
    n "Why are you all looking at me like that?"
    show natsuki cross uniform e4a mm b3a nobl
    n "Stop making that face!"
    show natsuki base uniform e1a mg b1f
    n "You are..."
    window hide
    pause 2
    $ nref
    show natsuki base uniform fs e4 b2 m3 n1 at h42
    n "Well okay, okay!"
    $ nref()
    show natsuki cross uniform e4a mi b3a
    n "You're pissing me off, but I changed my mind."
    show monika base uniform e1a b1b ldown
    show natsuki cross uniform e1b mm b1e nobl
    "Natsuki crosses her arms looking away, grinding her teeth."
    show sayori base uniform e4b b1a mc rup lup
    s "Hehehehe~, thanks Natsuki! But you're way too cute when you act like that!"
    show sayori base uniform behind natsuki at t42
    "Sayori slides in behind Natsuki, taking her in her arms."
    show natsuki base uniform fs e4 b2 m3
    n "Stop grabbing me!"
    $ nref()
    show natsuki base uniform e4c ml b1a blaw at h42
    n "And I'm not CUTE!!"
    show natsuki cross uniform e1b b1e md nobl
    show sayori base uniform neut ma rdown ldown at t44
    show monika base uniform neut ma e1a b1a
    m "Great! Now that everything is okay, I can explain how the next few days are going to go!"
    show yuri shy uniform e2 b1 m1
    m "First of all, we'll have to decorate the club room, and for that we'll need someone with a nice handwriting to catch the eye of the guests and also change the atmosphere of the room!"
    m "Yuri, [player] and I agreed that it will be you who's in charge of this activity."
    m "In our eyes, you are the person who has the most capacity for this task."
    $ yref()
    show yuri base uniform e1b b1a mg nobl
    y "The atmosphere... speaking of that..."
    show yuri base uniform e1a b1e mg rup ldown
    y "I love atomosphere!"
    show monika base uniform e4b mb rhip
    show sayori base uniform e1a b1a
    m "Perfect then! It's settled for one."
    show monika base uniform e1a
    m "Natsuki, you mentioned a few days ago that you were good at baking."
    show natsuki base uniform e1a b1a mg rhip
    show yuri base uniform e1a b1a ma rdown ldown
    n "Yeah, my father is a pastry chef in downtown."
    show monika base uniform e4b ma rdown
    m "Perfect then! We'll need about fifteen or twenty cupcakes."
    show monika base uniform e1a me
    m "Of course, since we can't make them in class, we'll have to make them at someone's house."
    show monika base uniform e1a mb lpoint
    m "Do you think your parents would agree if you could make them at home?"
    show natsuki cross uniform mc nobl
    show monika base uniform e1a md ldown
    n "Of course not, I could show off my baking skills to you all!"
    show natsuki base uniform e4b mo b3c rhip
    n "Ha ha ha, you all won't be ready, believe me."
    show natsuki base uniform e1a mc b1a rdown
    show monika base uniform mb rhip
    m "Do you think we could come over and help you or your parents would not accept?"
    show monika base uniform ma
    show natsuki base uniform lhip mg
    n "Mmmh, good question."
    show natsuki base uniform mc ldown
    n "I'll ask them tonight, I'll let you know tomorrow."
    show monika base uniform e4b mb lpoint
    show natsuki base uniform ma
    m "Alright!"
    show monika base uniform e1a ma ldown
    m "Well, now that everyone knows what they're doing-"
    $ sref()
    show sayori base uniform neut mg rup
    s "Say Monika.. what are we doing Thursday?"
    show sayori base uniform neut md
    s "You haven't said anything yet. Shall we write a poem?"
    show sayori base uniform neut ma rdown
    show monika base uniform e4b mb awkw rhip
    m "Oh yes! Thanks for reminding me Sayori!"
    show monika base uniform e1a ma nobl rdown
    m "What we're going to do on Thursday is not going to be writing a poem, we're going to recite one of our poems that we've been writing lately for practice..."
    show monika base uniform lpoint
    m "...but you can write a new poem for Thursday if you're not satisfied with your old ones."
    show monika base uniform ldown
    "Yuri, Natsuki and Sayori nod."
    show monika base uniform mb
    m "We still have a little bit of time left, you can return what you were doing. Thank you all!"
    show monika at thide
    show sayori at thide
    show natsuki at thide
    show yuri at thide
    hide sayori
    hide monika
    hide natsuki
    hide yuri
    "The girls each go back to their corners, returning to what they were doing."
    "I turn to Monika."
    show monika base uniform neut ma at t11
    mc "Well done Monika, you were clear with what you said."
    mc "Yuri didn't really seem ready for this announcement, but at least Sayori was able to convince her."
    show monika lean uniform ma
    m "Ahahaha! That's true."
    show monika base uniform neut lpoint ma b1b
    m "Yuri is very shy and introverted, and it seems it's not a habit of hers to talk with people."
    show monika base uniform neut ldown mb b1a
    m "Even when we shared the poems, she had a hard time looking me straight in the eye, yet she understood very well what my poem was about."
    m "But when we had shared for the second time, the tension was less present in her. I'm sure in a few days she will be more comfortable."
    show monika base uniform neut ldown ma
    mc "She will be, it's just a matter of time."
    mc "I even suggested to her to talk with Natsuki, so they could try to write a poem on the same theme."
    show monika base uniform neut me rhip
    m "Oh really, [player]?"
    show monika base uniform neut ldown md
    mc "Yeah, I think it could be interesting, don't you think?"
    mc "They have two completely different types of writing styles."
    show monika base uniform neut rdown me
    m "I'm not sure,[player]."
    m "I just worry that it's going to start an argument again."
    show monika base uniform neut md
    mc "I don't think they'll argue again, Monika. Yuri took responsibility for what she did, and she's not going to make the same mistake again."
    mc "As for Natsuki, I think her personality is a bit... you know..."
    mc "... It's all about luck."
    show monika base uniform neut me
    m "What do you mean?"
    mc "Well, what I mean is it just depends on her mood."
    mc "I don't really know, but we'll see how it goes."
    show monika lean uniform neut ma
    m "Ahahaha! That's just Natsuki, [player]. She's like that."
    "I just shrug my shoulders."
    mc "I think we'll stop the meeting in a little while."
    show monika base uniform neut me rhip
    m "So early?"
    mc "Yes, we'll give Yuri some time to buy what she needs from the stores for tomorrow."
    mc "If we stop the meeting at the same time as usual, she won't have much time, plus it's a thirty minute walk downtown to there."
    show monika base uniform ma rdown
    m "I don't think so, but I won't change your mind, it's your club after all."
    show monika lean uniform neut ma
    "I flash Monika a smile, and, she flashes me one too."
    show monika at thide
    hide monika
    "I glance around the room."
    "I see Yuri get up from her chair and start to timidly walk towards Natsuki who is still sitting on the floor towards the closet."
    "She kneels down placing herself at her level."
    "I can't hear very well from what she's saying from where I am."
    "I can just see Natsuki nodding with an embarrassed look on her face."
    show monika base uniform neut me rhip at t11
    mc "I think that's a winner."
    "I nod towards Yuri and Natsuki's direction to signal Monika to look over there."
    show monika base uniform b1b ma rdown
    m "Looks like you were right in the end."
    m "I'm glad they're starting to get along."
    mc "Same here."
    "We both stay in silence for a little while."
    s "{i}Monika, come and see something!{/i}"
    show monika base uniform mb b1a rhip
    m "I'll need to leave you for a bit, [player]. Sorry about that!"
    mc "No problem, I'll just read a little."
    show monika at thide
    hide monika
    "Monika walks over to Sayori, and they begin what seems to be a cheerful discussion."
    "..."
    "I sit down on a desk and take out a book from my bag."
    "I look at the cover of the book, giving me a hint."
    mc "This is the book Yuri lent me."
    "I open it and resume my reading from last night."
    "..."
    "..."
    "...."
    "I can't concentrate on the book."
    "I feel like I'm being watched right now."
    "I look to my right."
    "Nothing."
    "I look to my left."
    "I see Yuri quietly watching me from behind her book."
    show yuri base uniform neut mf rup at t11
    "I have the impression that she is reading the same book that she lent me."


    show yuri base uniform e2a mk rup blaw b1b
    "But{nw}{done}as soon as I make eye contact with her, she hides herself again behind her book."
    $ yref()
    show yuri shy uniform b1 m1 e2
    "But as soon{fast} as I make eye contact with her, she hides herself again behind her book."
    "I get up from the chair and walk towards her, the book in hand."
    show yuri base uniform e2b b1b mb rup blaw at s11
    y "Aah...! Sorry to bother you..."
    show yuri base uniform e2b mb rup blaw at t11
    mc "Don't worry Yuri, I just noticed that you were reading the same book as me."
    show yuri base uniform e1b b1a ma rup lup nobl
    y "Ah..."
    show yuri base uniform e1a mb ldown rdown
    y "...Y-Yes, indeed. It's one of my favorite books since I finished it and, from time to time, I start reading it again."
    show yuri base uniform e2b b1b blaw rup
    y "J-Just for fun! There's really no other reason or anything..."
    mc "Mmh, I see. I can tell you that the book you lent me is pretty good. I started reading it last night."
    show yuri base uniform e1a b1a mf nobl rdown
    y "Oh really?"
    mc "Yeah, you were right, the beginning of the book wasn't very relevant or at least... interesting."
    mc "But the rest of it made up for it."
    show yuri base uniform e4a ma b1a rup lup
    y "It relieves me..."
    show yuri base uniform e1a mb rdown ldown
    y "... I'm glad you like the book."
    show yuri shy uniform e1 b1 m1
    y "If you want, [player]..."
    "Yuri delicately closes her book with her hand, I can see a little better that the cover of her book looks newer than the one she lent me."
    mc "Say, Yuri... the book you have next to you, it looks a bit newer than mine, doesn't it?"
    "I take a quick look at the cover of the book I have in my hand."
    "And--indeed, the cover of the book looks a little more battered and dusty compared to her."
    show yuri base uniform mk e2a blaw rup lup
    y "I-...!"
    show yuri shy uniform n2 e2 m1 b1
    y "Well... it's... I..."
    "She can't seem to formulate her sentence completely."
    show yuri shy uniform n5 m2
    "It's obvious that Yuri bought the same examplar last Friday, but I decide not to point it out."
    mc "Sorry Yuri... it had just hit me when I saw that, I didn't mean to imply anything strange."
    show yuri shy uniform n1 m1 e2 b1
    y "..."
    "Yuri rubs part of her hair with both hands turning her face away."
    "Finally, she decides to speak."
    show yuri base uniform e4a mf b1b rup lup
    y "I... I just wanted to... introduce to you a whole new kind of story."
    show yuri base uniform e1b mg b1a
    y "And I like to reread from time to time, not just for fun only..."
    y "... But also, to hear what others think, when they have a constructive opinion..."
    show yuri shy uniform m1 e2 b1
    y "... Especially from someone like you."
    mc "Ahaha... Yuri, don't you think you are exaggerating?"
    show yuri base uniform e1a b1b rup lup
    y "I mean it sincerely and no... I'm not exaggerating."
    show yuri base uniform e1b b1b ldown
    y "You have always been calm, respectful and patient with me..."
    show yuri shy uniform b1 m1 e2
    y "Even though at times I would end up saying stupid things."
    show yuri base uniform e4a b1b rup lup mf
    y "Most people would have ended up laughing at me or just walked away uncomfortable..."
    show yuri base uniform e1a b1b ma ldown rdown
    y "So just thank you... and thank you for starting this club..."
    show yuri base uniform e1b b1b rup lup
    y "... I really feel comfortable here..."
    mc "I... please Yuri, I'm just doing my job as president."
    mc "I try my best to make this club more pleasant."
    "Yuri smiles wistfully."
    mc "I had seen you talking with Natsuki about, what did you talk about?"
    mc "If you don't mind of course..."
    show yuri base uniform e1a mb b1a rdown ldown
    y "I don't mind on the contrary, I had quickly thought about your request earlier when we shared our poems and..."
    show yuri base uniform e1b ma rup lup
    y "... We finally settled on writing a poem on the same theme."
    mc "That's nice, I'm glad you were able to talk to her."
    mc "And what is the theme?"
    show yuri base uniform e1a mg ldown rdown
    y "The beach."
    mc "The beach?"
    mc "That's great!"
    mc "It can only be a happy poem."
    show yuri shy uniform e2 m1 b1
    y "That's... It's true that I tend to write poems that are a little dark."
    show yuri base uniform neut ma
    y "I guess a little change wouldn't hurt?"
    mc "Exactly, you got it all figured out, Yuri."
    mc "I can't wait to see how you do it."
    show yuri base uniform rup lup e1b
    y "If that's the case.."
    show yuri base uniform e1a b1b
    y "I won't let you down, [player]."
    mc "Ah..."
    "How am I supposed to answer that?"
    mc "Well... I think we'll stop the meeting a little early for today."
    mc "So you can buy everything you need for tomorrow."
    show yuri base uniform e1b b1a
    y "Ah yes..."
    show yuri base uniform e1a mb rdown ldown
    y "I already have some ideas for tomorrow."
    show yuri base uniform e4b ma
    "Yuri smiles happily."
    show yuri base uniform e1a ma
    mc "That's perfect then!"
    mc "Ah, Yuri..."
    show yuri base uniform e1a mf rup lup
    y "Ummmh... yes?"
    "I pull my wallet out of my bag, extracting a few bills holding them to Yuri."
    mc "Since I was the one who came up with the idea, along with Monika, I figured it was up to me to give you the money so you could buy the necessities without having to use your own money."
    "To my surprise, Yuri puts her two delicate hands on my wrist and brings it to me."
    show yuri base uniform e1a b1b ma
    y "No [player]..."
    show yuri base uniform e1b
    y "I don't need you to lend me money."
    y "You have already done enough for me..."
    mc "Um... really Yuri, I don't mind."
    "I hold my hand back towards her."
    mc "I prefer that you do not--"
    show yuri base uniform e1a mh b1e rdown ldown
    y "No!!"
    "Suddenly Yuri raises her voice."
    $ yref()
    show yuri base uniform e2a b1b mk rup blaw
    y "I-...!"
    show yuri base uniform e2a b1b ml rup lup
    y "I'm sorry-!"
    y "I'm really sorry!"
    show yuri base uniform e1b mk ldown
    y "I.. didn't mean to raise my voice...!"
    y "..."
    show yuri shy uniform n5 m2
    y "{i}(I am so stupid...){/i}"
    mc "It's okay Yuri, I understand..."
    mc "... I shouldn't have forced it."
    show yuri shy uniform n1 b1 m1 e2
    y "..."
    show yuri base uniform e4a mf b1b
    y "Sorry again..."
    mc "I think you apologize a lot, Yuri."
    $ yref()
    show yuri base uniform e2b b1b mb blaw rup
    y "Ah... you think so?"
    mc "Yes, ahaha."
    show yuri base uniform e2b b1b mb blaw rdown at s11
    y "Uuuh... it's-..."
    show yuri base uniform e2b b1b mb blaw rdown at t11
    y "Well...{w=1}{nw}{done}I'm-!"
    show yuri shy uniform n5 m2 at h11
    y "Well...{fast}I'm-!"
    "Yuri clearly stops in her sentence, understanding her nonsense that she was about to say."
    "I can't help but blow my nose to express this funny situation."
    show yuri base uniform e2b b1b mb blaw rup at s11
    y "You are right, ahaha.."
    mc "Thank you for that conversation, Yuri."
    show yuri base uniform b1a e1a ma blus rdown at t11
    y "Thanks to you too, [player]. It was a pleasure."
    show bg club_day1
    hide yuri
    with wiperight_scene
    mc "Okay everyone!"
    mc "We're going to stop today's meeting a little early."
    show sayori base uniform b1b mg rup at t11
    s "What? Already?"
    show sayori base uniform me at t21
    show monika base uniform neut mb lpoint at t22
    m "Yes Sayori, sorry. But tomorrow the meeting will last a little longer, we promise!"
    show sayori base uniform me at t31
    show monika base uniform neut mb lpoint at t32
    show natsuki base uniform rhip lhip mg at t33
    n "Why are we stopping so early anyway?"
    show sayori base uniform me at t41
    show monika base uniform neut ma ldown at t42
    show natsuki base uniform e1a rhip lhip md at t43
    show yuri shy uniform n1 b1 m1 e2 at t44
    mc "It's so that Yuri has more time so she can buy the necessary supplies tomorrow, and then we already shared our poems."
    show natsuki cross uniform e1b b1e blus mm
    "Natsuki grunts to express her frustration."
    mc "Oh yes, Monika forgot to mention this to you, but since we're going to focus fully on the preparations for the festival, there will be no poem sharing for the next few days!"
    mc "But if you would like to write one and share it to someone in particular, feel free. There's no harm."
    show monika lean uniform neut ma
    m "Thanks, [player]."
    show monika base uniform neut mb ldown
    m "Anyway everyone, the meeting is over for today!"
    m "See you tomorrow, and be in shape!"
    show monika at thide
    show yuri at thide
    show sayori at thide
    show natsuki at thide
    hide monika
    hide yuri
    hide natsuki
    hide sayori
    "Once Natsuki and Yuri bid us farewell, only Monika and Sayori are left in the club room."
    show monika base uniform neut ma at t21
    show sayori base uniform neut at t22
    m "Sayori, do you mind if I walk home with [player] for today?"
    show monika base uniform lpoint b1b
    m "I'd like to talk to him about something."
    "I scratch the back of my head, with my heart rate suddenly accelerating, not being ready for what Monika was going to say."
    mc "..."
    show sayori base uniform neut mb
    s "No no, there's no worries!"
    s "I went home with him on Friday, and I noticed I live not too far from him."
    show monika base uniform e4b mb ldown
    m "Oh, great!"
    show sayori base uniform neut ma rip
    s "I'm going to go now by the way, see you two tomorrow!"
    mc "See you tomorrow, Sayori."
    stop music fadeout 3.0
    show sayori at lhide
    show monika at thide
    hide sayori
    hide monika
    "Sayori packs up her things and heads for the exit."
    "I pack up my things and head for Monika."
    "She already has her bag on her back, ready to go too."
    show bg re2_e
    with wiperight_scene
    play music evening
    show monika base uniform e1a ma rhip at t11:
        matrixcolor TintMatrix ("#eec7a7")
    mc "What did you want to talk to me about Monika?"
    show monika base uniform e1a b1b
    m "You know, [player], I'm just saying this for you, but please, don't take up all your time for the club."
    m "I know there is the festival coming up, but I would hate to see you spending all your free time for your club."
    show monika base uniform e1b mb blaw lpoint
    m "Did I more or less just say the same sentence?"
    mc "Kind of, yes."
    show monika base uniform e4b awkw ldown
    m "Ahahaha... sorry."
    show monika base uniform e1a b1a ma nobl rhip
    mc "But otherwise, I understand what you mean, Monika. Thanks for worrying about me."
    mc "I just want, that everything goes perfectly well."
    show monika lean uniform neut ma
    m "Me too, I also want everything to go smoothly, [player]."
    mc "How do you think it will go tomorrow, Monika?"
    show monika base uniform neut me
    m "Tomorrow? Why do you ask that, [player]?"
    mc "I like to plan things in advance."
    show monika base uniform neut mb rhip
    m "Ah... you don't like to improvise things too much, do you?"
    mc "Well... it really depends on the situation."
    show monika base uniform neut e4b mb rdown
    m "Oh right... I think everything will go as planned!"
    show monika base uniform neut e1a ma rhip
    m "I don't really see what could go wrong."
    m "We're going to do a lot of work, sure, but it will be for the good of the club."
    show monika base uniform neut e4b
    m "I'm sure we'll have good credibility in the eyes of the people at the school."
    show monika base uniform neut e1a mb rdown
    m "What about you, [player]? What do you think?"
    mc "I'm thinking the same thing too, although I am a little stressed about whether Natsuki's parents will accept us coming to their house or not."
    show monika base uniform me rhip
    m "Indeed... That's the only thing that could block us."
    show monika base uniform me lpoint
    m "We have to think of a plan B."
    mc "That's easy, we could-"
    show monika lean uniform neut m1
    m "Yes, we could go to your home."
    mc "Huh?!"
    m "Ahahaha! Why not, [player]?"
    show monika lean uniform neut m2
    m "Are you afraid that four girls will come to your house?"
    show monika lean uniform neut m1
    mc "No! Not at all!"
    mc "But I wasn't thinking about that."
    mc "I'll just have to do some cleaning before you come, I already know in advance the reactions of some of you."
    show monika base uniform neut ma b1b rhip
    m "Ooooh, come on, [player]!"
    show monika base uniform neut ma b1a rdown
    m "Give yourself a little more credit, you're a very clean guy."
    mc "If you say so.."
    m "I mean it."
    "How we came to talk about cleanliness now??"
    mc "But otherwise, I'm glad I could get your opinion about tomorrow."
    show monika lean uniform ma
    "Monika sketches a big smile."
    show bg residential_e
    hide monika
    with wiperight_scene
    "The rest of the walk passes without any other incident in particular."
    "Just like this morning, with Sayori, we talked about various and sundry topics that were each, more or less interesting."
    "We stop once we arrive in front of the gate to my house."
    mc "Here I am."
    "Monika looks at the front of the house."
    show monika base uniform neut ma at t11:
        matrixcolor TintMatrix ("#f5aa87")
    m "Your parents' house looks nice, [player]."
    mc "Thanks, Monika. you don't live too far away?"
    show monika base uniform neut e4b
    m "No, no, don't worry."
    show monika base uniform e1a rhip
    m "I'll see you tomorrow, [player]. Get some rest, because I wouldn't want to find you asleep on a table again."
    show monika lean uniform neut ma at h11
    m "Ehehehe~"
    mc "I already told you that I don't----"
    show monika base uniform neut ma e4b rhip
    m "I know, I know. I'm teasing you, [player]."
    show monika base uniform neut mb e1a rdown
    m "Anyway! I'm going to go, thanks for the walk!"
    show monika at thide
    hide monika
    "Monika crosses the road, heading across the street."
    "She then continues on her way, taking the direction of where we came from."
    "Meanwhile, I open the gate and unlock the door to the house before going inside."
    play sound closet_open
    stop music fadeout 2.0
    show bg kitchen
    with wiperight_scene
    play sound closet_close
    "I take off my shoes and head to my room."
    show bg bedroom
    with wipeleft_scene
    "Once in the room, after putting my things down, I sit down on the desk chair."
    window hide
    $ quick_menu = False
    show bg black
    with dissolve_scene_full
    show text "{=labeltext}{outlinecolor=#ffffff00}{size=40}Thank you for playing the demo of Doki Doki: The Reflection!{/outlinecolor}{/=labeltext}{/size}"
    with Dissolve(1)
    $ pause (3)
    hide text
    with Dissolve(1)
    show text "{=labeltext}{outlinecolor=#ffffff00}{size=40}If you have any suggestions to improve my project, don't hesitate to tell me in the comments.{/outinecolor}{/=labeltext}{/size}"
    with Dissolve(1)
    $ pause (2)
    hide text
    show text "{=labeltext}{outlinecolor=#ffffff00}{size=40}Big thanks to SpiritH0F#1283, DeltaOmega17#2949 & Zaun Aura#6946 for taking their free time to correct a LOT of grammatical errors in my mod due to my bad English.(There are probably still some, but less than before.){/outinecolor}{/=labeltext}{/size}"
    with Dissolve(1)
    $ pause (6)
    hide text
    with Dissolve(1)
    if persistent.secret == True:
        show text "{=monika_text}{outlinecolor=#ffffff00}{color=#0b5311}{size=80}And remember one thing...{/outinecolor}{/color}{/=monika_text}{/size}"
        with Dissolve (1)
        $ pause (1)
        hide text with Dissolve (2)
        show text "{=monika_text}{outlinecolor=#ffffff00}{color=#0b5311}{size=80}I love you.{/outinecolor}{/color}{/=monika_text}{/size}"
        with Dissolve (2)
        $ pause (1)
        hide text with Dissolve (3)
        $ pause (2)
        show text "{=monika_text}{outlinecolor=#ffffff00}{color=#0b5311}{size=100}END{/outinecolor}{/color}{/=monika_text}{/size}"
        with Dissolve (3)
        $ pause (2)
        $ config.name = "Just Monika."
        $ renpy.full_restart()
    $ pause (1)
    show text "{=labeltext}{outlinecolor=#ffffff00}END{/outinecolor}{/=labeltext}"
    with Dissolve (3)
    $ pause (1.5)
    $ renpy.full_restart()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
