label ch2_main:
    stop music fadeout 2.0
    window hide
    show bg black
    with dissolve_scene_full
    pause 5
    show bg bedroom
    with dissolve_scene_full
    play music alarm
    "{b}BIP {w=0.5} BIP {w=0.5} BIP {w=0.5} BIP {w=0.5} BIP{/b}"
    mc "Aaaaaaah..."
    mc "Puñetera alarma..."
    stop music
    "Golpeo la alarma para pararla."
    mc "{i}-suspiro-{/i} Al lío... {w=0.58} comienza un nuevo día."
    "Al levantarme de la cama, me estiro."
    "Echo un buen vistazo a mi habitación mientras lo hago."
    mc "...Hmmmmmmmm... ¿y mi uniforme...?"
    mc "..."
    mc "¡Ah! Ya te veo"
    "Cojo mi uniforme y me lo pongo."
    "Después de coger mi mochila, me dirijo al baño, peinándome rápidamente."
    "Me hago algún que otro ajuste a la corbata y salgo del baño."
    play sound closet_close
    show bg kitchen
    with wiperight_scene
    "Echo un vistazo a mi teléfono."
    "{i}6:40 AM{/i}"
    "Tengo tiempo de sobra para desayunar."
    "Voy a la cocina, saco un bol de cereales y un cartón de leche, y me sirvo una buena cantidad de cereales."
    "Mientras desayuno, hago tiempo leyendo un libro la mayor parte de la mañana."
    show bg kitchen
    with wipeleft_scene
    mc "Creo que ya basta."
    "Cierro el libro con cuidado y lo pongo de vuelta en mi mochila."
    "Saco mi teléfono y miro la hora."
    "{i}7:30 AM{/i}"
    mc "¡Hora de irse!"
    "Voy a la entrada de la casa para ponerme mis zapatos y poner mi mano en el pomo de la puerta."
    mc "Un momento..."
    "Me estoy acordando ahora."
    "Vuelvo a la nevera para llevarme un sándwich que preparé ayer."
    "Hace buen tiempo, creo que me iré a comer a la azotea cuando sea el descanso para el almuerzo."
    "Con el sándwich en mi mochila, me dirijo fuera de mi casa, cerrando la puerta con llave."
    play sound closet_close
    show bg residential_day
    with wiperight_scene
    play music morning
    "Yyyyyyyyyyyyyyyy... comienzo a hacer el mismo recorrido todas las mañanas para ir al colegio."
    show bg re2
    with wiperight
    "Por el camino, no puedo imaginar cómo transcurrirá el día de hoy."
    "Especialmente en el club, con las chicas."
    "Me imagino todas las posibilidades."
    "Y algunas son las peores posibilidades, como que no hayan hecho su poema por un olvido, o por cualquier otra razón, y sea yo el único pringado que haya hecho uno."
    "O puede que... todo vaya bien y quizá esté siendo..."
    "... no sé ni cómo describirme ahora mismo."
    "Estoy emocionado por ver cómo se expresan ellas mismas."
    "Pero, al mismo tiempo, estoy temiendo que llegue ese momento."
    "Bueno..."
    "Quizá solo esté sobrepensando."
    "Llegará a su debido tiempo."
    "..."
    "Por ahora..."
    "... todo lo que tengo que hacer es causarles una buena impresión."
    "Incluso lo dije ayer en la reunión... mi meta es hacer que todo el mundo se lleve bien y estén cómodos en el club."
    "Céntrate en eso, [player]... solo céntrate en eso."
    show bg school_front
    with wiperight_scene
    "I hardly notice it, but I am already in front of the school gate."
    mc "So, here we go for another boring school day..."
    stop music fadeout 2.0    
    show bg class_day
    with dissolve_scene_full
    pause 1    
    play music t3
    "The morning went by very slowly again, with all I did being simple note taking and oral participation."
    play sound bell
    "The bell finally rings, signaling the lunch break."
    "I put my backpack on my back and head for the stairs that lead up to the roof of the building."
    show bg roof
    with wiperight_scene
    stop music fadeout 2.0
    pause 2
    play music evening
    mc "What a splendid view!"
    "I admire the view of the landscape that stretches to the horizon."
    "I sit on a bench, one that's best suited for admiring the view while I eat my lunch."
    mc "Mmmmh, that's strange..."
    "I take a look around."
    "I notice there is no one here, and that I'm the only person here."
    mc "I thought there would be a lot of people."
    "..."
    "A minute passes while the sound of nature lives around me."
    "I can hear heavy footsteps in the distance coming out of the entrance while the door is closed."
    "The footsteps get louder and heavier as the person approaches the door."
    "The door opens and I can see..."
    "... Sayori?"
    show sayori base uniform e1b b1f mf at t41
    s "Ohhh?"
    show sayori base uniform e4b mc rup at h41
    "Sayori notices my presence, coming to throw me a hand gesture to greet me from where she is."
    "I greet her with the same gesture."
    show sayori base uniform ldown rdown ma at t11
    s "Hey, [player]!"
    "Sayori walks slowly towards me."
    mc "Hey Sayori something went wrong in the morning?"
    s 1b "Huh? Why do you say that?"
    show sayori 3a at d11
    "Sayori stands next to me, coming to take out her snack from her bag. It appears to be a common sandwich that you could buy downtown."
    "I do the same, taking out my sandwhich."
    mc "I could hear you stomping loudly with your feet with every step you took."
    s 4r "Ohhhh, not at all!"
    "Sayori lets out a small laugh."
    s 1a "Actually... I like to tap my legs hard every time I take a step haha!"
    s 3x "I think it's funny, I've been doing it since I was a child."
    show sayori base uniform neut ma
    mc "Ah.. I see, it's one of the things we all did when we were kids I guess."
    s base uniform happ "Yeah, ehehehe... there's always a childish spirit in us somewhere, isn't there?"
    mc "I agree with you, like walking only on the white markings when crossing a crosswalk."
    mc "I still do that, haha."
    s 3r "Hehehehe, me too!"
    "We both share a small laugh."
    mc "Otherwise, Sayori.. aren't you eating with Monika this lunch?"
    s 2c "Well, actually, yes!"
    s 1c "But she had to talk about something with a teacher, so she told me she'll join me."
    mc "Oh, right."
    s 2x "To be honest I wasn't expecting you to--{w=0.05}{nw}"
    show sayori base uniform neut rup ml e2a b1a at h11
    m "{i}-Sorry, sorry Sayori for the delay!!! {/i}"
    mc "Ah well, speaking of the wolf.."
    hide sayori
    with wipeleft
    "We can hear Monika screaming from the stairs. Unlike Sayori, she seems to be treading the stairs with very hasty steps."
    show monika base uniform neut awkw ldown rdown mb e4b b1b at l11
    m "...Haaaaah.. {w=0.1} ..Haaaaaah.. {w=0.1} pheeew... I'm sorry Sayori, the teacher wan-{nw}"
    show monika base uniform neut nobl ldown rdown me e1a b1a at h11
    m "Oh! [player]?"
    mc "Hi, Monika."
    show monika lean uniform neut ma
    m "Hey, [player]... I wasn't expecting to see you here."
    mc "I know. It's just that last night I made myself a sandwhich."
    show monika base uniform neut ma e4b
    m "Oh right, I see!"
    show monika base uniform neut mb e1a rhip
    m "Well..."
    show monika lean uniform neut ma
    m "I don't mind you being here."
    m "On the contrary, in fact."
    show monika base uniform neut ma at t22
    show sayori base uniform neut lup at t21
    s "It took you a while Monika, was it something serious?"
    show monika base uniform rhip e4b
    m "Oh no no, don't worry Sayori!"
    show monika base uniform neut ma
    m "It was just to ask her something."
    mc "Uuuh... anyway, Monika and Sayori?"
    show monika base uniform neut me e1a rhip
    show sayori base uniform neut me
    ms "...?"
    "Monika and Sayori are both looking at me with an interogative look."
    mc "Do you eat here often?"
    show sayori base uniform happ ma
    s "Well, you know [player]..."
    show monika base uniform happ ma rhip
    m "Yes, we often eat on the roof of the school!"
    show monika base uniform happ ma e4b
    m "Already from one to admire the beautiful view that is offered to us."
    m "But mainly... we eat almost every day here because we bring our own food every day."
    show sayori base uniform happ lup rup ma e4b
    s "Yes!"
    show sayori base uniform happ lup rup ma
    show sayori tap uniform neut awkw m1 e2 b1 at s21
    s "And the food in the cafeteria is really expensive and it's not good..."
    show sayori tap uniform neut awkw m1 e1 b1
    s "So it's good for my wallet, hehehe.."
    s "And Monika is a vegan, so it's clearly good for her that we eat outside the cafeteria."
    show monika base uniform neut e1a b1c me
    m "Sayori!"
    show sayori base uniform neut rup ml e2a b1a at h21
    "Monika raises her voice slightly."
    show sayori base uniform neut rup lup ml e2a b1a
    s "Uwoooah?"
    mc "..?"
    show monika base uniform awkw mb lpoint e1b b1b
    m "Uuuhh... sorry for yelling suddenly."
    show monika base uniform lpoint awkw ma e1b b1b
    m "It's just that..."
    show monika base uniform neut awkw lpoint rdown mb e1b b1b
    m "I'm not a vegan."
    show monika base uniform neut awkw ma b1b
    m "I'm a vegetarian."
    show sayori tap uniform neut awkw m1 e2 b1 at s21
    s "Hahahah.. {w=0.5} sorry, I just can't quite tell the difference between those two terms hehe.."
    mc "If you want Sayori, to clear your head."
    show monika base uniform neut nobl ma e1a b1b ldown rhip
    mc "Vegan is a person who excludes all meat, but not only that."
    show sayori base uniform neut ma nobl
    mc "It also excludes any product that comes from the animal."
    show sayori base uniform neut ma
    mc "Milk, butter, and also eggs are an example."
    mc "Everything that is of animal origin, for a summary."
    mc "However, the diet of a vegetarian excludes only meat and fish."
    mc "She can still eat the stuff that I quoted earlier.."
    show sayori base uniform neut mb lup e1a
    s "Thanks, [player]!"
    s "Hehehe, you've cleared my head now."
    mc "Now, back to the topic at hand..."
    mc "Why Monika, don't you get meat and fish from the cafeteria?"
    mc "Can't you just take the side dish?"
    show monika base uniform neut b1a lpoint rhip me
    m "It's because they don't charge back for what you don't take."
    show monika base uniform neut ma
    m "It's a fixed price, you know?"
    m "No matter how little you take on your tray, the price will stay the same."
    show monika base uniform neut ldown rdown e1a b1b
    show sayori base uniform neut ma b1b
    m "For others it's nice and beneficial, but for me... not really."
    show monika base uniform neut ma e4b b1a rhip
    show sayori base uniform neut ma b1a
    m "I'd rather make my own food for the next day and know what's on my plate!"
    show monika base uniform neut mb e4b lpoint
    m "It also costs less and tastes good too!"
    show monika base uniform neut e1a ma rhip ldown
    mc "I can only agree with you."
    mc "The food in the cafeteria is really, really bland."
    mc "We have to add a ton of salt to make our palate recognize the flavors."
    show monika base uniform neut e4b mb lpoint
    m "Hahaha, it's true, it's true."
    show monika base uniform neut e1a ma ldown
    mc "Say, Monika... ?"
    show monika base uniform neut me rhip
    m "Yes?"
    mc "Will you come and sit with us?"
    mc "Instead of standing in front of us, ahaha."
    show monika base uniform awkw ma e4b rhip
    m "Oh.. ahahaha!"
    m "Excuse me, I was just carried away in the conversation."
    mc "Don't worry."
    hide monika
    hide sayori
    with wipeleft
    "Monika takes a seat on my left while Sayori sits on my right."
    "Sitting between two such cute girls..."
    "It does something to me honestly."
    "Sayori is still devouring her sandwich, and Monika has already started to take out a small transparent box from her bag."
    mc "What did you bring Monika today?"
    show monika base uniform neut ma at t11
    m "Today I brought something simple."
    mc "And what is that?"
    show monika base uniform neut ma lpoint e4b
    m "A small Caesar Salad but prepared the Monika way!"
    "I quickly look at Monika's dish."
    mc "That looks delicious."
    m "Indeed! When it's perfectly prepared, it can only be delicious."
    "I simply nod and smile at Monika before a small silence settles in but quickly broken by Monika."
    show monika base uniform neut me rhip at t11
    m "So [player], do you have any plans for the festival?"
    mc "No, I haven't thought about it yet, but I'll think about it when I get to the club."
    show monika base uniform neut ma lpoint
    m "I could give you a hand if you want."
    show monika lean uniform neut ma
    m "Since I'm your vice president now."
    mc "That would be my pleasure, Monika."
    show monika base uniform neut ma e4b
    "Monika smiles happily."
    show sayori base uniform neut ml e2a at t21
    show monika base uniform neut ma e4b at t22
    s "Huh? You've become the vice president of the club Monika?"
    show monika base uniform mb e4b lpoint
    m "Yes, ahaha!"
    show monika base uniform mb e1a rhip ldown
    m "[player] asked me yesterday, and I agreed."
    show sayori base uniform mc e4b lup rup at h21
    s "Soooooooooooo cool!"
    s "Ahahaha! This is going to be the best club!"
    show monika base uniform mb e4b
    "The three of us share a laugh."
    hide sayori
    hide monika
    with wipeleft
    pause 0.2
    show bg roof
    with dissolve_scene_full
    "We continue to eat our lunch in silence."
    "Sometimes we break the it time to time by talk about various and sundry topics, like the environment."
    "When we were talking about the environment, Monika explained to us why she became a vegetarian."
    "She clarified that she became a vegetarian after watching a documentary a few years ago explaining why eating meat was a greenhouse gas bomb for the Earth."
    "She seemed to be very serious and took this topic to heart."
    play sound bell
    "The bell rings to signify the end of the lunch break."
    "The three of us sigh mutually."
    "To tell you the truth, I too am frustrated that I have to go back to class."
    "But hey, we don't have much choice..."
    "I'm the first one to get up and turn around to Monika and Sayori to face them."
    mc "Well... thanks for spending lunch with you two."
    mc "It was really nice to have a chat with you."
    mc "I wish we could have spent a little more time together, but we're running out of time I guess.."
    show monika base uniform ma b1b rhip at t11
    m "Me too, I wish we could have talked a little longer, I didn't see the hour go by."
    show sayori base uniform neut ma lup rup at t21
    show monika base uniform ma b1a rhip at t22
    s "That's okay, we'll see you this afternoon at the club, [player]!"
    mc "Someone is very impatient, I see!"
    show sayori base uniform e4b mb at h21
    s "Yeah! We'll have fun, I'm sure of it!"
    mc "Ahahaha, don't get excited Sayori."
    show monika base uniform mb e1a rhip
    m "We'll go soon [player], otherwise we'll be late because our class is at the other end of the building."
    mc "See you two later."
    show sayori base uniform happ ma
    s "See you later!"
    hide monika
    hide sayori
    with wiperight
    show bg corridor
    with wiperight_scene
    stop music fadeout 3.0
    "We briefly say goodbye, before I head to class."
    show bg class_day
    with dissolve_scene_full
    play music t3
    "The afternoon was more than ordinary even though it was very boring for the most part."
    play sound bell
    "The last bell ring, bringing the day to a close."
    show bg corridor
    with wipeleft_scene
    "After putting my things away, I head for the club."
    play sound closet_open
    show bg club_day1
    with wipeleft_scene
    "After entering the club room, I realize that I am the first to arrive."
    mc "Well, I'll just have to wait for them to come."
    "I sit down at a desk and take a sheet of paper and a pen out of my bag."
    mc "Preparing for the festival:"
    "I start writing a line."
    mc "Making new flyers."
    mc "Yeah... logical."
    "I continue to write a few lines describing as best I can."
    "I hear the door open."
    "I lift my head slightly to see that it's Natsuki."
    "I get up from my chair coming towards her."
    show natsuki base uniform neut ma rhip at t11
    mc "Hey, Natsuki!"
    show natsuki base uniform neut mb rhip
    n "Hi, [player]."
    show natsuki base uniform neut md ldown
    mc "If you have any suggestions or recommendations for the club, again, don't hesitate to talk to me or Monika."
    show natsuki cross uniform neut mh
    n "Got it, I'll be sure to see you if I have one."
    "I nod and head back to my desk, focusing on my paper once again."
    show natsuki at rhide
    hide natsuki
    "Natsuki heads for the closet but I don't pay any more attention to her."
    mc "Where was I then..."
    mc "Mmmhh.. What can we get if we need-{w=0.01}{nw}"
    n "[player!u]!!!!!"
    "Natsuki yells from the closet, which makes me startle."
    "I get up from my seat again heading towards her."
    show bg closet
    with wiperight
    mc "What's up?"
    show natsuki cross uniform neut mm b1e at t11
    n "Gnnnnnn-!"
    "Damn, she looks really pissed off."
    mc "Natsu---{w=0.1}{nw}"
    show natsuki base uniform neut mi b1e
    n "Did you move my manga?!"
    show natsuki base uniform neut mm b1e
    mc "A-Ah! Uuuuh.. it was me who moved them, yeah."
    mc "They didn't belong there."
    show natsuki base uniform neut mi lhip rhip b1e
    n "I don't want to know!"
    show natsuki base uniform neut mm b1e
    n "How can I grab my books then?!"
    mc "Well, uh..."
    show natsuki cross uniform neut mi e4a b3a
    n "You asked earlier for suggestions and recommendations for the club, and that's good. Because I have one if you don't mind, Mr. PRESIDENT!"
    show natsuki cross uniform neut mi e1a b1e
    n "And my suggestion is not to move my manga boxes!"
    show natsuki cross uniform neut mm e1a b1e
    n "What do you think, Mr. President?!"
    "Natsuki looks at me with a furious look."
    mc "Natsuki!"
    mc "You can't disregard my words like that!"
    mc "If I moved them it's because there's a good reason behind it!"
    mc "And I won't change my mind."
    mc "I didn't even know about it either."
    show natsuki base uniform neut blaw mm e1a b1e
    n "Kngggg-!"
    show natsuki base uniform neut blaw lhip rhip mi e1a b1e
    n "Ok well you know what?!"
    mc "Natsuki, listen."
    mc "I know you're upset but there's no need to make a big deal out of it!"
    show natsuki base uniform neut blaw lhip rhip md e1a b1d
    mc "It's the teachers who asked me to keep this room the way it has been since I was assigned it."
    mc "If a teacher ever came to check the closet and they found this mess, I'm afraid I'd get in trouble because I'm in charge of the room!"
    show natsuki cross uniform neut blaw md e1a b1b
    mc "Do you understand?"
    "I take a chair not far from me, and put it in front of me."
    mc "Here, why don't you take this chair to get access to your manga that I put on top of the shelf?"
    show natsuki cross uniform neut awkw mg e1b b1a
    n "Well... I wouldn't mind that in itself."
    show natsuki cross uniform neut awkw mg e1a b1a
    n "Thanks, [player]... I guess."
    mc "Well, if we're good then, that's fine with me."
    hide natsuki
    with wipeleft
    "I gently hand the chair to Natsuki who receives it coming to put it inside the closet in the right place to grab her manga collection."
    "She climbs on the chair, but even with the chair giving her a height to be able to grab her books, she is still forced to stand on her tiptoes because of her small size."
    "She glances in my direction."
    show natsuki base uniform neut mh b3c at t11
    n "What are you still doing here?"
    n "Wait... a minute."
    show natsuki base uniform neut e2a b3c
    "Natsuki's eyes widen as a thought just passed through her mind."
    show natsuki base uniform neut blaw ml e4c b1c at h11
    n "You wouldn't do that to try to look up my skirt by any chance?!"
    mc "H-Huh?!"
    mc "N-No, I wouldn't!"
    mc "I'm just trying to find a solution Natsuki!"
    show natsuki base uniform neut blaw ml e4c b1c at h11
    n "Go away pervert! Don't just stand there!"
    show natsuki base uniform neut blaw ml e4c b1c at h11
    n "Get out!"
    show natsuki at thide
    hide natsuki
    "I walk away from the closet."
    show bg club_day
    with wipeleft
    mc "Damn... what a talk."
    "I head back to my desk."
    "I notice that Monika, Sayori and Yuri are already present in the club room."
    "I must not have noticed their arrival during my little altercation with Natsuki."
    "What reassures me is that they don't seem to care too much about what just happened."
    "Yuri is already sitting on a desk already immersed in her reading."
    "As for Monika and Sayori, they are having a discussion that seems to be joyful."
    "I can't help but notice that Monika is glancing in my direction."
    "I decide to send her a small smile. And she immediately does the same."
    mc "-sigh-.. Let's go back to where I left off."
    "I settle back into the chair starting to write again."
    mc "Materials needed..."
    "I place my pen on the next line, but I don't move my hand."
    "I have writer's block, great."
    mc "..."
    mc "Raah... it's messing with my brain all over again."
    "The tip of my pen pressed for a moment on the paper, leave a single black ink stain."
    mc "Great."
    $ y_name = "????"
    y "H-hey, [player]..."
    $ y_name = "Yuri"
    show yuri base uniform neut awkw rup md e2b b1b at t11
    "I raise my head to see Yuri standing in front of me."
    mc "Yes, Yuri? Can I help you?"
    "I can see that her hands are shaking slightly."
    show yuri base uniform neut awkw rup mb e2b b1b
    y "S-Sorry to come and disturb you while you were doing something, but..."
    show yuri base uniform neut awkw rdown mb e2b b1b
    y "I have a small request to ask you if you don't mind.."
    mc "Hey Yuri, relax a little. I'm not going to yell at you or anything."
    show yuri base uniform neut awkw rup mb e1b b1b
    y "Aah.. you're right, sorry.."
    y "I don't know why I'm nervous all of a sudden, ahaha.."
    mc "Take a deep breath and tell me everything you want to say, I'm listening."
    mc "Take your time."
    show yuri base uniform neut lup rup mf e4a b1c nobl at s11
    "Yuri take a breath of air."
    show yuri base uniform neut lup rup mg b1a e1a at t11
    y "Well... you know... I like to read a lot."
    show yuri base uniform neut rup ma e1b b1a
    y "But at home when I read, well... I like to read with a nice hot cup of tea."
    show yuri base uniform neut rup ma e1b b1b
    y "And here at the club... there's no electric kettle."
    y "So I'm just asking you if..."
    show yuri shy uniform happ awkw m1 e2 b1
    y "It was possible to ask permission from the teachers to bring a teapot and some teacups.."
    "After her request, Yuri exhales for a long time as if to release all the stress that had accumulated inside her."
    show yuri shy uniform happ m1 e1 b1 n1
    mc "I will see what I can do for you, Yuri."
    y "T-thank you, [player]."
    show yuri base uniform happ nobl lup rup ma b1a
    mc "I can go now."
    show yuri base uniform happ nobl ldown rdown mh e1a b2c
    y "A-Are you sure...?"
    y "I mean... you were busy and worried a lot about your paper... It was something important I guess."
    mc "You can say it like that.. but it can wait for now... I mean I can always work on it at home."
    mc "For now, what matters is that I take care of my club members."
    show yuri base uniform neut rup ma e1b b1b
    y "That's so sweet.."
    mc "Eh?"
    show yuri shy uniform n5 m2 at h11
    y "S-Sorry...! F-Forget what I just said..."
    y "That wasn't what I meant... it just came out of my mouth..!"
    show yuri base uniform flus awkw lup rup mg e4a
    y "It's just... it's just that sometimes I speak without really thinking when I come out of a reading.."
    y ".. And I end up saying stupid things.."
    mc "Ah.. don't worry Yuri, I can understand."
    mc "Under the moment of stress we say things that we don't mean."
    show yuri base uniform neut lup rup mf e4a b1c nobl at s11
    "Yuri exhales with relief."
    show yuri base uniform flus nobl ldown rdown ma e1d b1b at t11
    y "You are really an understanding person [player]..."
    mc "Ahaha.. that's a quality that all people should have, right?"
    show yuri base uniform flus nobl ldown rdown ma e1b b1b
    y "Yes, it should be..."
    "Yuri remains silent."
    mc "I-I.. I'll go see what I can do, Yuri."
    show yuri base uniform flus nobl lup rup mb e1b b1b
    y "Thanks again."
    show yuri at rhide
    hide yuri
    "Yuri goes back to her desk resuming her reading."
    mc "..."
    mc "Monika!"
    "I decide to call Monika."
    "Immediately after calling her, she pauses her discussion with Sayori and starts walking towards me."
    "While Sayori is alone, she looks around and decides to head towards Yuri."
    show monika base uniform neut mb at t11
    m "Hey [player], is there anything you want to ask me?"
    mc "Yeah. Since you're my vice president, I'm going to ask for something in the staff room."
    mc "I'm asking if it's possible for you to watch the club while I'm gone."
    show monika base uniform neut mb rhip
    m "Okay, I don't mind!"
    show monika base uniform neut me rdown
    m "What are you going to ask if I can be curious?"
    mc "I'm going to ask for permission from the teachers to be able to serve hot drinks within the club."
    mc "You see how dangerous it is because you can get burned and everything. You have to ask them first, you know.."
    m "Who asked that?"
    mc "Yuri asked me."
    mc "I won't be long!"
    mc "But knowing you, you'll be able to handle it well."
    show monika base uniform neut ma b1b
    m "Say, [player]..."
    show monika lean uniform neut ma
    m "Are you underestimating me by any chance?"
    mc "N-Not at all!"
    mc "You even have much more experience than me in running a club!"
    show monika base uniform neut mb e4b rhip
    m "Ahahaha! You are so easy to tease."
    show monika base uniform neut ma e1a b1b
    m "But, you know, you can't judge a book by it's cover?"
    show monika base uniform neut ma b1b lpoint
    m "Actually, I've always had trouble when it comes to handling members. It's not one of my great qualities, I admit."
    mc "Ah... we're about the same level then.."
    show monika base uniform neut ma b1b ldown
    m "I don't think so, [player]. You seem to handle it very well, even better than me."
    show monika base uniform neut ma e1a b1a
    mc "Thanks for the compliment, I guess.."
    mc "When I get back, we'll start sharing poems."
    show monika base uniform neut mb e4b
    m "Okay!"
    show monika base uniform neut mb e1a rhip
    m "Make it quick [player], I'm a little curious to see what you've written."
    show monika lean uniform ma at h11
    m "Ehehehe~"
    mc "M-Me too, Monika.."
    hide monika
    with wiperight
    show bg corridor
    with wiperight
    "Leaving the clubroom, I start to make my way to the staff room downstairs."
    show bg corridor
    with dissolve_scene_full
    "After talking to one of the teachers who were present in the room, I was able to get permission, even though it was a little difficult to convince them."
    "I go back to the clubroom and open the door, seeing the same usual scene that hasn't changed."
    play sound closet_open
    show bg club_day
    with wiperight_scene
    "Sayori and Yuri are talking together while Monika is writing something in a small notebook."
    "And Natsuki is sitting on the floor reading what seems to be one of the mangas that was present in her box."
    "No one seems to have noticed my return."
    "I calmly walk towards Sayori and Yuri."
    mc "Hey Yuri, I have good news for you."
    show yuri base uniform neut nobl ldown rup mg e1d b1a at t11
    y "Y-You could?"
    "I nod in response."
    show yuri base uniform neut nobl ldown rup ma e4b b1c at h11
    y "Thank you so much, [player]."
    mc "Except...they won't lend us the equipment."
    show yuri base uniform curi mf e1a b1a rdown
    y "Oh?"
    show yuri base uniform curi mg b1a
    y "What do you mean?"
    mc "Well, we'll have to bring a teapot in short."
    mc "That goes for the teacups too."
    y "A-Ah.."
    show yuri base uniform curi ma e1b b1a
    y "That's okay. As long as the teachers have given us permission... I don't mind bringing an electric kettle and some teacups."
    mc "Are you sure?"
    show yuri base uniform curi ma e1a b1a
    y "Yes, I'm sure."
    show yuri base uniform curi blus ma e1b b1a
    y "I... I'm a big tea fan, I have a lot of teapots at home."
    show yuri base uniform curi blus ma e1b b1a at t21
    show sayori base uniform neut mb lup at t22
    s "Hey, [player]!"
    mc "Hey Sayori, sorry I didn't say hello earlier."
    show sayori base uniform mb e4b ldown
    s "Hahaha, don't worry!"
    show sayori base uniform ma e1a
    s "By the way [player], Yuri told me that she wanted to give you a book for you!"
    show yuri base uniform neut blaw rup ml e2a b1b
    y "S-Sayori! You shouldn't have told him now!"
    mc "Huh? A book for me?"
    show yuri shy uniform happ bful m2 e2
    y "Uuuh.. N-Not really..."
    show sayori base uniform neut rup me e1a b1b
    s "Aah.. sorry Yuri, that came straight out of my mouth..."
    show sayori base uniform neut me e1b b1b
    s "I'm really sorry..."
    show sayori at thide
    hide sayori
    show yuri shy uniform bful m2 e2 at t11
    mc "Did you really bring a book for me Yuri?"
    show yuri base uniform neut awkw rup ml e2a b1b
    y "Forget about that!"
    show yuri shy uniform happ nobl m2 e2 b2
    y "Sayori made it sound like a huge problem..."
    show yuri 4c
    y "Uuuuuuuhh... what do I do..."
    "Yuri frantically rubs the ends of her long hair turning her face away from looking at me."
    "I think I need to fix this situation..."
    show yuri shy uniform happ nobl m1
    mc "Hey Yuri, I really appreciate the offer."
    mc "No matter what's in the book, it's still so nice coming from you."
    "Even though we've only known each other since Friday..."
    mc "And also, it will expand my collection of books that I have at home!"
    "Yuri inhales and exhales briefly, taking a small breath of air."
    show yuri base uniform happ ma e1a b1b
    y "... If you mean it.."
    "Yuri reaches into her bag, fiddling around inside and pulls out a book."
    show yuri base uniform happ mb b1a
    y "This is the book I mentioned on Friday, which I particularly liked it and finished this weekend."
    show yuri base uniform happ e1b b1b
    y "I hope you'll like it..."
    "Yuri hands me the book, looking slightly away from me."
    "I pick up the book with both hands coming to show a smile of confidence."
    mc "Thank you Yuri! I'll take good care of the book and as soon as I get the chance, I won't hesitate to start reading it."
    mc "I'm sure I'll like it."
    show yuri base uniform happ lup rup mg e4a b2b at s11
    y "Pheww..."
    show yuri base uniform happ lup rup ma e1a b1c at t11
    y "Depending on how fast you read, you can finish it in less than a week if you read it every day."
    show yuri base uniform happ ldown rdown ma b1c
    y "The beginning may not be very interesting, but trust me the deeper you get into the story the more interesting and relevant it will become."
    show yuri base uniform happ lup rup ma e1b b1c
    y "I.. I won't say more."
    y "I don't want to spoil the surprise for you."
    show yuri base uniform happ lup rup ma e1a b1c
    mc "It works, Yuri! I'll think about it when I start reading it."
    show yuri shy uniform happ m1 e2 b2
    y "[player]... if you want..."
    y "When you advanced a bit in the story... or even if you've started reading it.."
    show yuri shy uniform happ m1 e1 b1
    y "W-We could discuss it if you want..."
    mc "With great pleasure, Yuri! I would love to discuss it with you!"
    show yuri base uniform neut lup rup mg e4a at s11
    y "Phew... what a relief."
    show yuri base uniform neut lup rup ma e1b
    "Yuri lets out a small discreet smile."
    hide yuri
    with wipeleft
    "I head to my desk to put the book in my bag."
    "I clear my throat slightly before standing in the center of the room."
    mc "Okay everyone! Come in front of me!"
    "The girls stop what they were doing and walk towards me."
    show monika base uniform neut ma at t44
    show sayori base uniform neut ma at t43
    show natsuki cross uniform neut ma at t42
    show yuri base uniform neut ma at t41
    mc "I am pleased to announce that we can finally begin our first club activity!"
    mc "Did you all write a poem for today?"
    show monika base uniform neut ma e4b
    show sayori base uniform neut mc lup rup e4b
    show yuri shy uniform e2 b2
    show natsuki cross uniform blaw md e1b b1f
    "Sayori and Monika both dynastically nod their heads while Natsuki and Yuri do it shyly."
    mc "Well then, it's time to share our poems!"
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    with wiperight
    "The girls spread out and head for their backpacks."
    "Sayori takes out a single, crumpled sheet of paper, while Monika takes out a small textbook."
    "From where I am, I can see perfectly her impeccable handwriting."
    "As for Yuri and Natsuki, they take out their poems too, but reluctantly."
    stop music fadeout 2.0
    show bg club_day1
    with wiperight_scene
    play music t5
    "Monika seemed impatient to see my poem, so I decide to start with her."
    show bg club_day1
    with wiperight_scene
    show monika base uniform ma at t11
    mc "Hey, Monika!"
    m "Hey, [player]!"
    mc "Ready to share your poem?"
    show monika base uniform mb e4b
    m "I'm ready!"
    mc "Well then, let's get started!"
    "Monika and I share our poems each other."
    call showpoem (poem_m11, img="monika base uniform ma b1a e1a") from _call_showpoem_1
    m "..."
    show monika base uniform mb
    m "So, what do you think?"
    show monika base uniform ma b1a e1a rhip
    mc "I like your poem, Monika."
    mc "Your poem is... very free, I say..."
    show monika lean uniform neut ma
    m "Ahahaha, yes! It's starting to become a bit of a fashion among writers lately, if I may say so."
    mc "I didn't even know about it."
    show monika base uniform ma neut b1b rhip
    m "You're more of a reader than a writer, right [player]?"
    mc "Oh yeah... you have a point there."
    show monika base uniform neut mb b1a rdown
    m "I can always give you writing tips if you're ever interested!"
    mc "I'd rather it be done in private then."
    show monika base uniform neut ma e4b
    m "All right!"
    show monika base uniform neut mb lpoint e1a
    m "Isn't that funny?"
    mc "About what? That you give me writing advice?"
    show monika base uniform neut ma e4b ldown
    m "Yeah! I think it's pretty funny that I'm giving writing advice to my own president who runs a literature club."
    show monika lean uniform neut ma at h11
    m "Ehehehe."
    mc "You say that as if I don't have the ability to give writing advice myself..."
    show monika base uniform neut me rhip b1b
    m "Oh no, I didn't mean it! I'm sorry!"
    show monika base uniform neut ma rhip b1b
    m "Actually, I'm sure you can do it too."
    mc "..."
    mc "In fact, I might do it from time to time when I have something informative to say."
    mc "I favor quality over quantity."
    "A slight silence falls between the two of us, but quickly broken by Monika."
    show monika base uniform neut ma lpoint b1a
    m "Otherwise... I like your poem too, [player]."
    show monika base uniform neut ma ldown e4b b1a
    m "It is very metaphorical!"
    show monika base uniform neut ma ldown e1a
    m "Really amazing."
    mc "Oh thanks... I had a hard time last night when I started writing it."
    show monika base uniform neut mb lpoint
    m "Ahaha! You know [player], you have a block on something whenever your mind focuses solely on a specific goal, which in this case is writing a poem."
    show monika base uniform neut ma lpoint rhip
    m "You might make your pen be pressed against the paper for too long, and end up only making a huge layer of black ink!"
    m "Think of that layer of black ink as a river."
    m "So in order for you to get that river of ink out and make progress on your poem, let your pen follow the flow of this river naturally!"
    show monika base uniform e4b mb
    m "And you'll get through it!"
    mc "..."
    mc "That's funny, it actually happened to me when I was writing notes on my paper earlier."
    show monika lean uniform ma
    m "Ahahaha! What a funny coincidence don't you think, [player]?"
    mc "Clearly. I was stuck on some stuff I was preparing for the next Friday about the festival."
    show monika base uniform me rhip
    m "You started thinking about it?"
    mc "Yeah."
    mc "I'll talk to you about it after the poem sharing."
    show monika base uniform ma e4b rdown
    m "Okay, [player]!"
    mc "Thanks for sharing your poem Monika."
    show monika base uniform mb e4b rhip
    m "You're welcome!"
    "We get our poems back before we part ways."
    show bg club_day1
    hide monika
    with wiperight_scene
    show sayori base uniform neut ma at t11
    mc "Hey, Sayori!"
    show sayori base uniform neut mb lup
    s "Hi, [player]!"
    mc "How's the poem sharing going on your side?"
    show sayori base uniform neut ma lup rup e4b
    s "It's super fun so far!"
    show sayori base uniform neut e2a mh ldown rdown
    s "I shared with Natsuki and she has a very different way of writing than I do!"
    mc "That's great! We all have different writing processes, and that's a good thing for the club!"
    show sayori base uniform neut e1a md
    s "Really? Why would you say that?"
    mc "Well, if we all had the same processes, wouldn't you think it would be a little flat?"
    mc "I mean... we're all human, and we're all different intellectually. It wouldn't be interesting if we had the same processes on writing."
    mc "Don't you think so?"
    show sayori base uniform neut awkw e1b b1b mc lup at s11
    s "Ha ha, well.."
    show sayori base uniform neut nobl e1a b1a ma ldown at t11
    s "You're right, [player]."
    mc "Sorry, I didn't mean to get to the heart of the matter.."
    mc "Would you mind if we started sharing poems?"
    show sayori base uniform neut e1a mb
    s "Ok!"
    "I hand my poem to Sayori."
    show sayori base uniform neut e2a mh b2a lup
    "..."
    show sayori base uniform neut b1a e1a ma ldown
    s "I didn't know you write so well, [player]!"
    show sayori base uniform neut e4b mc lup rup
    s "Your poem is the best one ever!"
    mc "Sayori..."
    mc "I sincerely think that you are exaggerating..."
    mc "Honestly, I didn't even know what I was writing last night."
    show sayori base uniform neut e1a mb rdown ldown
    s "Maybe that's why!"
    show sayori base uniform neut e1a mb rup
    s "Sometimes when you do things without thinking, you can do wonderful things."
    show sayori base uniform neut e4b mc lup rup at h11
    s "Ahahaha!"
    "I don't know if Sayori is serious in what she says or if she's the girl who talks without really thinking..."
    mc "Ah.. thank you, Sayori."
    mc "I'll take that as a compliment."
    mc "Will you share your poem now?"
    show sayori base uniform neut e1a mb rdown ldown
    "Sayori gives back my poem, giving me her poem in the process."
    call showpoem (poem_s11, img="sayori base uniform neut blus e1b b1b ma") from _call_showpoem_2
    mc "..."
    show sayori base uniform neut nobl e1a b1a ma
    mc "Your poem is very good, Sayori."
    mc "You wrote it on Friday, if I am to believe the third line?"
    show sayori base uniform neut e4b mc b1a lup rup
    s "Yes!"
    s "Friday is the best day of the week!"
    show sayori base uniform neut e1a ma ldown rdown
    s "At least I can sleep a lot."
    mc "Uh... okay..."
    show sayori base uniform neut me b2b lup
    s "What? You don't agree with me?"
    mc "Yes, I agree with you!"
    mc "But sleeping a lot is not really a good thing, but anyway!"
    mc "I'm not going to give a moral lesson."
    show sayori base uniform neut mc e4b b1a lup
    s "Hehehe, don't worry [player], next time I will write the best poem in the whole world!"
    mc "Okay Sayori, I can't wait to see if you keep your word."
    show bg club_day1
    hide sayori
    with wiperight_scene
    show yuri base uniform neut ma at t11
    y "Hello, [player]."
    mc "Hey, Yuri!"
    mc "Is everything going well on your end?"
    show yuri base uniform neut ma e1b b1b rup lup
    y "It's okay... I-I'm a little stressed about sharing my writing.."
    mc "Don't worry Yuri, we're all stressed out!"
    mc "It's a little barrier that stands in front of each of us, but I'm sure we'll learn to cross it quickly!"
    mc "It's only a matter of time before we become a little more serene about sharing our writing."
    show yuri base uniform neut ma e1a b1a ldown
    y "Yes, probably."
    mc "How would you like to start sharing our poems?"
    show yuri base uniform neut ma e4b b1a rup lup
    y "I'd like to!"
    "Yuri smiles at me happily while she tend her poem."
    "I catch it and start to read it."
    call showpoem (poem_y1) from _call_showpoem_3
    "..."
    show yuri base uniform neut e1a ldown rdown
    "I like this poem."
    show yuri base uniform neut mh e1a b1b rup lup
    "Monika was right that Yuri would be a good advantage for the club."
    show yuri base uniform neut mh e1a b2c rup lup
    y "... I-I'm sorry for having such a terrible handwriting!"
    mc "Eh?"
    mc "No, no... your handwriting is really beautiful, Yuri."
    show yuri base uniform neut mh e1b b2c rup lup
    y "But it took you a long time to read..."
    mc "Oh, you think so?"
    show yuri base uniform neut mg e1b b1b rup lup at s11
    "Yuri nods her head shyly."
    mc "Sorry... it's just that..."
    mc "I'm not really used to cursive writing."
    mc "But otherwise... your poem is very impressive, I really like it."
    show yuri base uniform neut ma e1a b2a rup ldown at t11
    y "Ah.. thank you, I usually write poems that are a little longer.."
    show yuri base uniform neut mb e1a b1a rup ldown
    y "Since this is the first time I'm sharing my writing, I wanted it to be something a little softer than my usual."
    show yuri base uniform neut mb e1b b1a rup ldown
    y "Something easier to digest, actually."
    mc "Ah okay, Yuri, it's very grateful of you to think of others."
    show yuri shy uniform b1 e1 m1
    mc "But it shouldn't be a barrier either, I mean... don't limit yourself compared to others!"
    show yuri shy uniform b1 e2 m1
    mc "I'm perfectly sure that you have the ability to write beautiful things, Yuri."
    mc "And your poem right now proves it very well!"
    show yuri shy uniform b1 e1 m2
    mc "You can even teach others to write better poems!"
    y "..."
    show yuri shy uniform b1 e2 m1
    y "I-I have a little trouble talking to people..."
    mc "I'm sure you'll be able to get over that little wall one day, Yuri."
    mc "Thank you for sharing your poem."
    show yuri shy uniform e2 b1 m1
    "I give Yuri back her poem with one hand, holding my poem with my other one."
    mc "Here's my poem, tell me what you think!"
    show yuri shy uniform e2 b1 m1
    "Yuri grabs my poem and starts reading it."
    show yuri base uniform neut e1b b1d mf rup
    "..."
    show yuri base uniform neut e1b b1a ma rup lup
    "....."
    show yuri base uniform neut e1b b1d mf rup ldown
    "......."
    "A minute passes in silence."
    "Yuri's eyes are still fixed on my poem, she shows an intense expression on her face."
    mc "Uh.. Yuri?"
    show yuri base uniform neut e2a b1b mk b1b rdown
    y "A-Ah! I haven't spoken yet, have I?"
    mc "Well... yes."
    mc "My handwriting is bad?"
    show yuri base uniform neut e2a ml b1b rup lup blaw
    y "W-What? No!"
    show yuri base uniform neut e2b mk rup ldown
    y "Did I just raise my voice?"
    show yuri shy uniform n5 m2
    y "Uuuuh... I'm so sorry..."
    show yuri shy uniform nobl m2 e2 b1
    mc "Don't worry Yuri, I'm the one who should be sorry, I guess you were still reading my poem.."
    show yuri base uniform e2b b1b awkw mb rup
    y "Oh no... don't apologize..."
    show yuri base uniform e4a b1a mf nobl rup lup at s11
    "Yuri takes a deep breath."
    show yuri base uniform e1a ma rdown ldown at t11
    y "Your poem is very... intriguing."
    show yuri base uniform neut e1a ma rdown
    y "It is very metaphorical and really well crafted."
    mc "Thank you Yuri, it's nice to hear that from someone who is used to reading every day."
    show yuri base uniform neut e1b ma b1b blaw
    y "I-it's nothing, really..."
    show yuri base uniform neut e1a ma b1a nobl
    y "It implies that you are used to writing poems often?"
    mc "Actually... I haven't written poems in a while."
    show yuri base uniform neut e1a mf b1a nobl
    y "Oh?"
    show yuri base uniform neut e1b mf b1a nobl rup
    "Yuri traces her finger, along the sheet."
    show yuri base uniform neut e1b mf b1a nobl rdown
    y "..."
    show yuri base uniform neut e2b mb b1b awkw
    y "Y-Yes..!"
    show yuri base uniform neut e1a ma b1a nobl
    y "Indeed... I noticed some small mistakes, but nothing alarming."
    mc "Ah.. thank you, and what are these small mistakes you speak of?"
    show yuri base uniform neut e2b mk b1b awkw at s11
    y "A-Ah, uh.."
    "Yuri sinks into her chair."
    show yuri shy uniform m1 e2 b1 nobl at t11
    y "I.. You'll take it the wrong way.."
    mc "Ahahaha, why would I take it the wrong way, Yuri?"
    show yuri shy uniform m1 e1 b1
    mc "You're very good at judging our scriptures!"
    show yuri shy uniform m2 e2 b1
    y "Judging...?"
    show yuri base uniform neut e2b b1b mk rup blaw
    y "I will never judge your poems...! I can't..."
    mc "Ah... sorry, I actually meant..."
    mc "You are the right person to make small suggestions to improve our poems."
    show yuri base uniform e2a mk rup lup blaw
    y "Uh... [player]! You're really exaggerating here..."
    show yuri base uniform neut e4a mf nobl rdown ldown nobl
    "Yuri take a breath of air."
    show yuri base uniform neut e1a b1a ma
    y "... But otherwise..."
    show yuri base uniform neut e1b b1b mb
    y "It's just that there are certain writing habits that are very unique to each writer."
    show yuri base uniform neut e1b mb rup
    mc "I agree with you Yuri, I actually talked to Sayori about it while we were exchanging poems."
    mc "Do you think it's a problem?"
    show yuri base uniform neut e1a b1a mf rup
    y "Not really... it just depends on how other people react.."
    show yuri base uniform neut e1b b1d rup lup
    y "I mean some people tend to make fun of other people's writing."
    show yuri shy uniform e2 m1 b2
    y "And I was just a little worried about sharing our own poems..."
    y "Afraid of being judged for what I write because... people tend to mock other people's work because they don't get the message..."
    y "And that's what I was a little afraid of this, to be honest.."
    show yuri base uniform neut e4a b1b mf rup
    y "But in the end my fear was wrong... it went really well with Monika and Sayori, they were very nice.."
    $ yref()
    show yuri shy uniform e1 m1 b1 at s11
    y "And you too..."
    "..."
    show yuri base uniform e2b awkw mb rup b1b at t11
    y "I'm rambling a bit now, aren't I...?"
    mc "Listen Yuri, I will not accept members of my club who judge the work of others."
    show yuri shy uniform e2 m1 b2
    mc "The reason I decided to do this activity is so we can get to know everyone's writing better!"
    "{i}(Even though I actually hadn't really thought about it, it just came to me.){/i}"
    show yuri shy uniform e1 m1 b1
    mc "I'm very glad that you're getting along with the others, you can sympathize a little more and even be friends with them!"
    y "Be-be friends... you said?"
    mc "Yes."
    show yuri base uniform neut e1b b1b ma rup blus
    y "That's... that's one thing I would like to..."
    show yuri shy uniform e1 m1 b1 n1 at s11
    y "To be... friends with you all..."
    mc "Ah..."
    "I think I said a little too much, the discussion might reach a deadline."
    mc "Thanks for reading my poem Yuri, can you give it back to me?"
    show yuri base uniform neut e2b mb b1b rup at t11
    y "A-Ah yes, sorry.."
    "I notice that Yuri crumpled my paper a little while she was holding it in her hand."
    "I'll take it back."
    show yuri shy uniform m1 b2 e2
    y "S-Sorry about your poem... it was the stress."
    mc "That's okay."
    show bg club_day1
    hide yuri
    with wiperight_scene
    show natsuki base uniform neut b1a md at t11
    mc "Hey, Natsuki."
    show natsuki base uniform neut b1a mg
    n "Hi, [player]."
    mc "Ready to share your poem?"
    show natsuki cross uniform neut e1b b1a md awkw
    n "Hmpfff, let's get it over with quickly."
    show natsuki cross uniform neut e1b b1b md nobl
    n "You won't like it."
    mc "But why would you say that?"
    mc "I haven't even read it yet and you're already making up your mind."
    show natsuki base uniform neut fs m3 e4 b2 at h11
    n "Yes, well, enough!"
    "Natsuki hands me her poem furiously."
    mc "Thanks..."
    call showpoem (poem_n1, img="natsuki base uniform rhip lhip e1a b1b mg") from _call_showpoem_4
    n "See, you don't like it."
    mc "I like it."
    show natsuki cross uniform neut e1a b1d mg
    n "Please, stop lying."
    mc "But!"
    mc "Honestly, I like your poem!"
    mc "Why are you hinting to yourself that I don't like your poem?"
    show natsuki base uniform neut fs m3 e4 b2
    n "Because!"
    $ nref()
    show natsuki cross uniform e1b b1d mh awkw
    n "... Because people don't take me seriously."
    n "The only sentence that comes out of most people is that « It's so cute! », or they just say plain « I like it. » just to please me!"
    show natsuki cross uniform neut e1a b1a md
    mc "So just because I said I liked your poem, you think I'm not taking it seriously and that I'm a liar...?"
    show natsuki cross uniform neut e1b b1f md blaw
    n "Hmpff."
    mc "Natsuki... what you wrote proves to me that you did your poem seriously."
    show natsuki base uniform neut mf e1a b1a nobl
    "Natsuki tries to say something but her mouth stays open without a word coming out."
    show natsuki cross uniform neut md e1b b1a
    mc "I don't see why I shouldn't take you seriously."
    show natsuki cross uniform neut mg e1b b1d awkw
    n "Most people I know in this school are all like that. They never take me seriously."
    mc "Well... listen Natsuki, in this club, you'll be taken seriously."
    "What a nice answer, [player]..."
    show natsuki base uniform neut mg e1a b1a nobl rhip
    n "Thanks I guess... in the end you're not such a bad president."
    mc "Because I was until now...?"
    show natsuki cross uniform neut mg e1b b1a
    "Natsuki doesn't answer me."
    "So I decide to give her back her poem."
    mc "Will you read my poem now?"
    show natsuki base uniform neut ma e1a b1a lhip rhip
    n "Sure."
    "I hand her my poem."
    "It takes very little time before she gives it back to me."
    mc "Already?"
    show natsuki cross uniform neut mg e1a b1a
    n "Well listen... I have nothing to say."
    mc "Nothing to say?"
    show natsuki base uniform neut mh e1a b1f
    n "What do you want me to say?"
    show natsuki base uniform neut fs m3 e4 b2 at h11
    n "Your poem is very good, then!"
    $ nref()
    show natsuki cross uniform neut mg e1a b1a
    n "Even if I didn't really understand what it was about."
    "... Okay?"
    mc "Ah.. thank you, I guess."
    show natsuki base uniform neut mg e1a b1a
    n "Yeah, yeah. Here's your poem."
    "She plasters my poem on my chest which makes me wince slightly in pain."
    mc "H-Hey... watch out..!"
    show natsuki base uniform neut e4a mc blaw b3b rhip lhip
    n "Ahaha, what did you think?"
    n "Just because I'm the smallest one here in this club doesn't mean I'm the weakest!"
    mc "I never said that.."
    show natsuki base uniform neut e4b mo b3c rhip ldown nobl
    n "It's okay, it was a little joke!"
    "Natsuki puts on a wide smile."
    "I don't think you can call it a joke, but I'd rather not offend her."
    mc "Yeah... thanks for reading my poem, Natsuki."
    stop music fadeout 2.0
    show bg club_day1
    hide natsuki
    with wiperight_scene
    play music t3
    mc "Phew.. I think I shared with everyone."
    mc "It was a little more stressful than I thought it would be."
    mc "But I think I did okay."
    "I look around."
    "Monika just finished sharing her poem with Yuri."
    "I head towards her."
    show monika base uniform neut ma rhip at t11
    mc "I'm back, Monika!"
    mc "Do you feel like to chatting a bit about plans for the festival?"
    show monika base uniform mb e4b rhip
    m "Sure!"
    show monika base uniform ma e1a rhip
    "Monika and I arrange two desks to stick together."
    mc "So..."
    mc "Wait a minute."
    hide monika
    with wipeleft
    "I walk over to where I left my paper with some notes written on it, and turn to Monika who is already settled in her chair."
    "I sit down too, putting the sheet of paper in the middle on the table so she can get a view."
    "I don't know why I'm doing this, but it helps me to have my little landmark. To keep me from getting lost in my threads of thought."
    show monika base uniform ma rhip at l11
    mc "If I could explain to you what I had planned was to make pamphlet with each of our poems written on them."
    show monika base uniform me rdown
    m "Mmmh, that sounds pretty good, but have you thought of anything else?"
    mc "Well, at the moment I haven't really had time to think about it much longer."
    show monika base uniform me e4a
    "Monika thinks for a moment."
    show monika base uniform mb e1a rhip
    m "I know!"
    mc "Mmh?"
    show monika base uniform ma e1a lpoint
    m "How about a performance poem presentation?"
    mc "You mean reciting in front of a public..?"
    show monika base uniform mb e4b ldown rdown
    m "Yep!"
    show monika base uniform mb e1a rhip
    m "Each of the five of us would pick a poem we wrote ourselves and recite it in public!"
    mc "Uuuuuh..."
    show monika base uniform mb e4b lpoint
    m "But again!"
    show monika base uniform mb e1a rhip ldown
    m "The guests, if they wish, can also recite!"
    "Well, I hadn't really thought about that."
    "But what will the others think?"
    mc "Do you think it's a good idea?"
    show monika base uniform ma e4b ldown rdown
    m "Totally!"
    mc "And what will others think?"
    mc "I mean... It's only been a day since they joined the club."
    mc "This is going to seem very sudden to them, don't you think?"
    show monika base uniform me e1a rhip
    m "Mmmhh... I hadn't really thought about it."
    show monika base uniform mb e1a rhip lpoint
    m "But we can try to reassure them."
    mc "Yeah, you're right."
    mc "Sometimes I think a little too much for no good reason.."
    mc "But I trust you Monika, and I think your idea is great."
    mc "How do we plan to organize all this?"
    show monika base uniform me e1a ldown
    m "What do you mean?"
    mc "Well, for the-{w=0.04}{nw}"
    stop music fadeout 2.0
    n "I hadn't noticed you were so dedicated to trying to impress our president, Yuri."
    mc "Huh?"
    show monika at lhide
    hide monika
    pause 0.1
    show yuri base uniform neut e4a b1a mf rup blus at r21
    show natsuki base uniform neut e4a b3a rhip lhip blaw mc at r22
    "I avert my eyes to Natsuki and Yuri. Natsuki is standing while Yuri is still sitting in her chair."
    play music t7 fadein 2.0
    show yuri base uniform neut e2a b1b mk rup blaw
    y "H-Huh?"
    y "N-No..."
    y "That's not what I'm trying to..."
    show yuri base uniform neut e2b b1b mk rup lup
    y "You.. you're just..."
    show yuri base uniform neut e2b b1b mk rup lup at t31
    show natsuki base uniform neut e4a b3a rhip lhip blaw mc at t32
    show sayori base uniform neut e1b b1b mc blaw rup at r33
    s "Hey..."
    s "Is everything okay----{w=0.02}{nw}"
    show sayori base uniform neut e4c b1b ml blaw rup lup at h33
    pause 0.04
    show sayori at rhide
    hide sayori
    show yuri base uniform neut e2b b1b mk rup lup awkw at t21
    show natsuki base uniform neut e4a b3a rhip lhip blaw mc at t22
    "Yuri suddenly stands up too."
    show yuri base uniform neut e1a b1e mh rup ldown nobl
    y "Maybe you're just jealous that [player] enjoyed my poem more than yours!"
    show natsuki base uniform e2a b1e mm rhip lhip
    n "Gnnn..! {nw}{done}And how do you know he didn't also appreciate my poem too?!"
    show natsuki base uniform neut e1a b1e mi blaw
    n "Gnnn..!{fast} And how do you know he didn't also appreciate my poem too?!"
    show natsuki cross uniform neut e1a b1e mi
    n "Where do you get such confidence from?!"
    show natsuki cross uniform neut e1a b1e mm
    show yuri base uniform e1b b1a rup mh
    y "No.. It's not that I..."
    y "If I had.."
    y "If I had such confidence in myself..."
    "I get up from my chair heading towards Natsuki and Yuri."
    mc "Uh... what's going on----{w=0.02}{nw}"
    show yuri base uniform neut e1a b1e mh rup ldown
    y "I'll have done manners on purpose to try to look super cute!"
    show natsuki base uniform e2a b1e mm blaw rdown ldown
    n "Nnnnnnnn...!"
    show natsuki base uniform e1a b1e mi rhip lhip
    n "You know what?!"
    show natsuki cross uniform e1a b1e mi blaw
    n "I'm not the one who magically saw her boobs get bigger when I joined this fucking club!"
    show natsuki cross uniform e1a b1e mm blaw
    show yuri base uniform e2a ml b1b rup lup blaw at h21
    y "W-What did you say??"
    show natsuki cross uniform e1a b1e mm blaw at t32
    show yuri base uniform e2a ml b1b rup lup at t31
    show sayori base uniform neut e4c b1b ml blaw rup lup at h33s
    s "I don't like fights girls, stop it!"
    show sayori flip at rhide
    hide sayori flip
    show natsuki cross uniform e1a b1e mm blaw at t22
    show yuri base uniform e2a ml b1b rup lup at t21
    $ renpy.music.set_volume(0.3)
    mc "That's enough!"
    mc "What is wrong with you two?!"
    show yuri shy uniform b2 e2 m2 n1
    mc "How did we get there???"
    show natsuki base uniform e1a b1e mi
    n "She's the one who started being mean to me!"
    "Natsuki takes a sour voice to accuse her innocence."
    $ yref()
    show yuri base uniform neut e2a b1b ml rup blaw
    $ renpy.music.set_volume(1.0)
    y "No... that's not true..!"
    show yuri base uniform neut ml lup blaw
    y "[player]! Don't listen to her! She's the one who criticized my writing style in the first place!"
    y "She... She's just trying to make me look bad!"
    show yuri base uniform neut mk e2b b1b rdown ldown
    show natsuki cross uniform neut mi e1a b1e blaw
    n "Are you serious right now?!"
    show natsuki cross uniform neut mm e1a b1e blaw
    n "Do you even listen to yourself when you talk??"
    show natsuki base uniform e2a mi b1e
    show yuri shy uniform n5 m2 awkw
    n "You're the one who criticized in first place, calling my poem cute when it's not cute at all!"
    show natsuki base uniform e4a mi b3a
    n "You didn't understand anything about my poem!"
    y "I was just...{w=0.05}{nw}"
    show natsuki base uniform e2a mi b1e
    n "And you dare say that I'm the one at fault in all this?"
    show natsuki base uniform e4a mi b3a
    n "I can't believe it!"
    show natsuki base uniform e1a b1e mi rhip lhip
    n "You know what would be better?"
    show natsuki base uniform e4a mi b1e
    n "It's to...-{w=0.09}{nw}"
    stop music
    mc "STOP!"
    show natsuki cross uniform md e1a b1f blaw
    mc "Natsuki, you are going too far!"
    show yuri shy uniform n1 b1 e2 m1
    mc "I both like your poems."
    mc "You have two writing styles that have nothing to do with each other certainly."
    mc "And I have one thing to say."
    mc "It doesn't matter if the poem is long or short."
    show yuri shy uniform n1 b1 m1
    mc "What matters most is the words that are used in the poem."
    mc "Yuri."
    show yuri shy uniform n1 b1 e1 m1
    y "...?"
    mc "You are a really talented writer, I admit it."
    $ yref()
    show yuri base uniform e2b b1b mb rup blaw
    y "Well.. it's.."
    $ yref()
    show yuri base uniform e2a b1b md rup blaw
    mc "But, just because a person's writing isn't refined doesn't mean they don't put their emotions into it!"
    mc "That's why Natsuki felt hurt when you called her poem cute."
    show yuri base uniform e2b mg b1b rup lup nobl at s21
    y "Eh... well... I'm sorry... I didn't mean it... really..."
    show yuri shy uniform e2 m2 b1 at t21
    show natsuki base uniform e4a mc b3b blaw rhip lhip
    n "See?"
    n "Finally it was you, Yuri who-"
    mc "Natsuki, it's worth the same to you."
    show natsuki base uniform e1a b1a mh blaw
    n "Huh? But...!"
    mc "You took the case too seriously!"
    mc "If you would have just said what you thought to Yuri without getting angry, calmly, this fight would never have happened!"
    show natsuki base uniform e1a b1e mi
    n "Are you kidding me?"
    show natsuki base uniform e1a b1e mi rdown ldown
    n "That's what I did!"
    show natsuki cross uniform md b1b e1a
    mc "Natsuki. Yuri apologized."
    mc "Don't you think you should do the same?"
    show natsuki base uniform e1a mm b1e
    n "Nnnn...!"
    mc "Natsuki, once again, apologize to Yuri."
    show natsuki base uniform mm e4a b3a
    "Natsuki takes a deep breath before turning to Yuri."
    show natsuki cross uniform e1b b1b md at s22
    n "Listen Yuri.."
    show natsuki cross uniform e1a b1b mg
    n "I'm.."
    show natsuki base uniform e1b b1b md
    n "About what I said to you... you know... I didn't mean it, really."
    show natsuki cross uniform e1b b1b md
    n "I apologize for being rude to you."
    show natsuki cross uniform e1a b1b md
    show yuri base uniform e1b b1b ma awkw
    y "I accept your apology... I'm also sorry for criticizing your writing, I didn't really mean it again.."
    "Natsuki doesn't answer. She just nods her head."
    mc "There you go! I'm glad you were able to settle this out of court."
    mc "I hope I don't have to deal with this kind of thing."
    show yuri at lhide
    show natsuki at rhide
    hide yuri
    hide natsuki
    "Natsuki and Yuri both resume their poems, each dispersing into their own corners."
    "The tense atmosphere that was plunging into the room starts to dissipate and becomes a bit more relaxed."
    play music t8 fadein 4.0
    show monika base uniform neut ma b1b at t11
    "I turn around to face Monika who has a small smile on her lips."
    show monika base uniform neut mb b1b
    m "You know, [player]... I'm glad you were able to handle that fight."
    show monika base uniform neut mb e4b awkw rhip
    m "I may have been vice president of the debate club and good at organizing things, but I have a weakness for handling any altercations with club members."
    show monika base uniform neut ma e1b b1b blaw
    m "I can't imagine if you wouldn't have been there, haha."
    mc "Don't worry Monika, I'm not very good at organizing things."
    mc "Each it's own own talent, I'd say."
    mc "Shall we go back?"
    show monika base uniform neut mb e1a b1a nobl
    m "Let's go!"
    show monika at thide
    hide monika
    stop music fadeout 2.0
    show bg club_day1
    with dissolve_scene_full
    play music t3 fadein 3.0
    "The rest of the meeting passes without any remarkable events."
    "Monika and I worked very well on the sketch of the flyers for the festival."
    "Even though I had some uncertainties, she was able to present me good arguments."
    "She told me that she would think about the organization later."
    "..."
    mc "Sounds perfect to me..."
    "I put my paper back in my bag."
    show monika base uniform neut mb rhip at t11
    m "I think we can end the meeting now."
    "I look at the time on my phone."
    "{i}6:05 PM{/i}"
    mc "Yep."
    mc "It was nice working with you Monika."
    show monika lean uniform neut ma at face(y=750)
    with Dissolve(0.10)
    "Monika suddenly approaches my ear coming to whisper something to me."
    m "{i}And honestly, we're going to work together more and more often if that's okay with you.{/i}"
    show monika base uniform e1f ma at t11
    "Monika pulls away from me displaying a sweet smile that knots my stomach and makes all my blood flow up in my head."
    show monika base uniform e4b ma
    mc "S-Same with you, Monika..."
    show monika at lhide
    hide monika
    "I get up from the seat, a little unsettled."
    show sayori base uniform neut ma at t41
    show monika base uniform neut ma e4b rhip at t42
    show yuri base uniform neut ma at t43
    show natsuki cross uniform ma at t44
    mc "Okay everyone! Come here!"
    mc "What did you think of-"
    show natsuki cross uniform mg b1a
    n "Say [player]... why is your face all flushed?"
    mc "Huh... what are you talking about Natsuki?"
    "I can't help but let out a little stressed laugh."
    mc "Ahaha... it's just stress really, it's nothing."
    show natsuki base uniform mc
    n "Don't be silly."
    show natsuki base uniform e4b mo b3c rhip
    n "You can tell us everything!"
    show sayori base uniform e4b mc rup lup
    s "Ehehehe, you're as red as a tomato [player]!"
    mc "..."
    mc "... I'm just hot."
    show natsuki cross uniform e1a mc b1a
    n "Not an impressive excuse [player]."
    "I'm starting to get caught up in a dead-end argument and I need to change the subject as soon as possible."
    mc "... Well...!"
    mc "... Otherwise...!"
    mc "What did you think of this poem sharing?"
    mc "Monika?"
    show monika base uniform mb e1a b1a
    m "It was a pretty cool activity."
    show monika base uniform rdown
    m "It was fun to discover each other's writing style."
    show monika base uniform ma
    mc "Sayori?"
    show sayori base uniform e1a b1a mb lup rdown
    s "It was great! I really liked it."
    mc "Yuri?"
    show yuri base uniform e1a b1a mb rup ldown
    y "It was pretty good overall."
    show yuri base uniform e1b b1a ma rup ldown
    mc "Natsuki?"
    show natsuki base uniform e1a b1a mg
    n "Yeah, it was pretty good if I can say it like that."
    mc "Great! I suggest we do this again for Monday!"
    mc "You've learned a bit more about writing between you all! I'm sure your poems will be ten times better next time and you'll try something new!"
    mc "We can finally finish the meeting, have a great evening everyone and we'll see you on Monday!"
    show natsuki at rhide
    show yuri at rhide
    show monika at lhide
    show sayori at lhide
    hide monika
    hide yuri
    hide natsuki
    hide sayori
    "Everyone disperses, each of them going about their business."
    "I head to my bag to put my things away too."
    "Suddenly I feel a hand gently resting on my shoulder, startling me slightly."
    m "Say, [player]?"
    mc "Ah! {w=0.5}Yes Monika?"
    show monika base uniform neut ma rhip at t11
    m "I wanted to know if I could have your phone number?"
    show monika base uniform lpoint
    m "That way we can communicate by message or call when we're not in the clubroom."
    m "I think it's important that we have a way to reach each other."
    show monika base uniform neut mb e1b rhip ldown
    m "About the festival you know..."
    show monika base uniform neut ma e1a rhip ldown
    mc "Sure, wait a minute."
    "I pull my phone out of my bag heading into my « Contacts » so I can find my personal phone number."
    "I use my phone very very rarely to be honest. My parents bought me one at the beginning of the year since they started to be away from home more and more often because of their work."
    mc "Do you have your phone on you?"
    show monika base uniform neut me rdown
    m "Uuh.. no. Hold on, I'm going to look for it in my bag, give me five seconds."
    show monika at rhide
    hide monika
    pause 5
    show monika base uniform mb rhip at r11
    m "Ok! I'm back! Can you tell me your number?"
    mc "Okay..."
    "I dictate my number to her while she, in sync, taps her fingers on the touch screen of her phone."
    show monika base uniform ma rdown
    m "I think that's it. Let me send you an S.M.S. to be sure."
    pause 1
    play sound phone
    "{i}DING!{/i}"
    mc "Great, I got your message."
    "As I am talking, I'm saving Monika's number in my Contacts."
    m "Great! I'll send you a message when I get a chance, [player]."
    mc "Okay, Monika."
    show monika at lhide
    hide monika
    "Monika leaves to collect her things."
    "I wait patiently for everyone to leave the room."
    show bg club_day1
    stop music fadeout 2.0
    with dissolve_scene_full
    "Once everyone is gone I lock the door, and I start to leave the school."
    show bg school_front_e
    with wipeleft
    play music evening fadein 3.0
    "When I get to the front door of the school, I start to take out my phone and my headphones."
    $ s_name = "??????"
    s "[player]! Wait!"
    mc "Huh...?"
    $ s_name = "Sayori"
    "I turn around to see Sayori running towards me."
    "I discreetly put away my phone and my headphones."
    show sayori base uniform neut e4c rup lup ml blaw at t11:
        matrixcolor TintMatrix("#f5c7ad")
    mc "Yes, Sayori?"
    mc "You didn't have to run by the way, I was going to wait for you when you called me."
    show sayori base uniform neut e4c lup rdown ml blaw at s11
    s "...Haaah... Haaah.."
    show sayori base uniform neut e1a mh rup lup nobl at t11
    s "I saw you take out your phone so I thought you were already leaving!"
    mc "Ah, sorry. It's just that I'm used to going home alone."
    show sayori base uniform neut e2a b2a mf
    s "Oh?"
    show sayori base uniform neut e1a b1a mb ldown rdown
    s "I saw you this morning when you were going to school!"
    s "We don't live too far, it seems."
    show sayori base uniform neut e1a b1a ma ldown rdown
    mc "Huh?"
    mc "Then how come I've never seen you before?"
    show sayori base uniform neut e1b b1b mc at s11
    s "Ah... I don't know hehe... that's a good question."
    mc "..."
    show sayori base uniform e1a b1a mb lup at t11
    s "So, do you want to walk home together?"
    mc "Aren't you walking home with Monika, Sayori?"
    show sayori base uniform md
    s "Not today, she told me she had things to do."
    mc "Oh right, well, yeah, if you want we can walk home together."
    show sayori base uniform mc e4b lup rup at h11
    s "Yaaay! Let's go!"
    show sayori at lhide
    hide sayori
    $ pause (0.2)
    show bg re2_e
    with wiperight_scene
    "Sayori and I start to make our way home."
    "There wasn't really any in-depth discussion with me and her, which made the walk a bit awkward and very quiet."
    "The only sounds were the exhaust pipes of cars on the roads and the chirping of the birds flying overhead..."
    "... Only one question comes to mind."
    show sayori base uniform neut md at t11:
        matrixcolor TintMatrix("#f5c7ad")
    mc "Sayori, how long have you known Monika?"
    show sayori base uniform neut mb
    s "Monika? We have known each other since the beginning of this year."
    s "We're in the same class, and we became best friends quickly!"
    show sayori base uniform neut ma
    mc "Oh right, thanks for your answer."
    show sayori base uniform neut mb
    s "What about you, [player]?"
    show sayori base uniform neut ma
    mc "I've known her since last year, we were in the same class and we worked together a lot."
    mc "But since the beginning of this school year, we talked less and less. Mainly because she became very busy since she became vice president of the debate club."
    mc "And since then, we would occasionally talk to each other when we ran into each other but nothing more."
    show sayori base uniform b1b ma rdown
    s "Oh.. okay, I'm glad you're talking again then."
    mc "Yeah, I guess."
    show sayori at thide:
        matrixcolor TintMatrix("#f5c7ad")
    hide sayori
    "The discussion ends there, and we continue walking in silence until I get to my alley."
    show bg residential_e
    with wiperight_scene
    "..."
    mc "The path ends here for me."
    mc "My house is right there."
    "I point vaguely in the direction of my house."
    show sayori base uniform neut ma lup at t11:
        matrixcolor TintMatrix("#f7b792")
    s "Alright, thanks for agreeing to go back together, [player]! My house is a few blocks over there, it's about a five minute walk."
    mc "My pleasure, Sayori. See you Monday."
    show sayori base uniform neut mc e4b rdown
    s "See you Monday!"
    show sayori at thide:
        matrixcolor TintMatrix("#f5c7ad")
    hide sayori
    "Sayori continues on her way while I open the gate and head for the door of my house."
    play sound closet_open
    show bg kitchen
    with wipeleft_scene
    $ pause (0.2)
    play sound closet_close
    stop music fadeout 2.0
    "Once unlocked and inside the house, I take off my shoes at the entrance and go straight to my room."
    show bg bedroom
    with wipeleft_scene
    mc "I don't think I'll be going out again today."
    mc "I might as well get comfortable."
    "I drop my bag on the floor, removing myself from my uniform afterwards and dressing in simple pajamas."
    "I collapse on my bed, staring at the ceiling."
    play sound phone
    "{i}DING!{/i}"
    mc "Huh?"
    "A notification rings out from the pants pocket of my uniform."
    "I head for the pants pocket extirpating to see a notification from Monika."
    play music t3 fadein 3.0

    call _phone_register from _call__phone_register

    $ phone.discussion(mc_monika)

    $ phone.date(4, 21, 2023, 19, 31)

    $ phone.message("mc", _("Hey Monika, doing nothing right now. just got home actually"))

    $ phone.message("m", _("Okay! Do u mind if i call u rn ?"))

    $ phone.message("mc", _("yeah if u want, what is it for ??"))

    $ phone.message("m", _("On the way home, I thought about how we could organize all this, before the festival! :D"))

    $ phone.message("mc", _("Yeah sure, I would love to know ur idea."))

    $ phone.message ("m", _("Great {}! Calling you rn :)".format(player)))

    $ phone.end_discussion()

    "As soon as Monika sends me her last message I see the call already in front of my eyes."
    "I pick up."

    $ renpy.music.set_volume(volume=0.4)

    $ phone.call("m")


    phone_mc "Hey, Monika!"

    phone_m "Hey, [player]!"

    phone_mc "I'm listening to you, Monika!"
    phone_m "You see, Natsuki said she likes making pastry at home, right?"
    phone_mc "Yeah, indeed."
    phone_m "Well, I thought she could make cakes to attract people to the room!"
    phone_m "I think that's a really good way to do so."
    phone_mc "Yeah, you're right!"
    phone_mc "Very good idea, Monika."
    phone_mc "Do you think she'll be okay with that?"
    phone_m "Yes, I'm sure!"
    phone_mc "Alirght. Got any other ideas?"
    phone_m "Yep! I remember you put on your sheet that you were going to make flyers, didn't you?"
    phone_mc "Exactly, and what do you want to do with them?"
    phone_m "Well, I suggest I make them this weekend, I know my way around Canva or even Photoshop."
    phone_mc "Without me?"
    phone_m "Yeah, don't worry, [player]. I'll put them up Monday morning."
    phone_mc "It works."
    phone_m "Did you get any new ideas on your own or not?"
    phone_mc "I have one that just popped into my head."
    phone_m "And what is it?"
    phone_mc "How about decorating the clubroom?"
    phone_m "What do you mean?"
    phone_mc "Well, we could decorate the club room with a banner that says « Welcome to the Literature Club! » on it."
    phone_mc "We could also put some kind of long ribbon at the entrance to make like a curtain."
    phone_mc "And maybe change the curtains to a slightly softer color if we're allowed to?"
    phone_mc "To put the room in a special atmosphere like in a theater, don't you think?"
    phone_m "[player]..."
    phone_mc "You don't like my idea?"
    phone_m "On the contrary! I love your idea!"
    phone_m "But we shouldn't put too much work on ourselves."
    phone_m "How about giving this task to someone in particular?"
    phone_mc "Yes, I agree, but to whom... ?"
    phone_m "Mmmh..."
    phone_mc "..."
    phone_mc "I think I know who."
    phone_m "Who?"
    phone_mc "Yuri."
    phone_mc "Her handwriting is beautiful don't you think?"
    phone_m "Yes, I agree with you."
    phone_m "Do you want to give her this task?"
    phone_mc "Yes."
    phone_mc "Natsuki will be in charge of the cupcakes."
    phone_mc "Yuri will be in charge of the atmosphere and the decoration of the room."
    phone_mc "So they will have a little responsibility too!"
    phone_m "Great! I like the idea of giving small responsibilities to the club members."
    phone_mc "But back to my fear that I had earlier."
    phone_mc "That is, how do we plan to organize all this?"
    phone_m "Well, I know how to do it."
    phone_mc "Explain it to me."
    phone_m "Instead of sharing poems, we're going to put it on hold until the day of the Festival."
    phone_m "No, wait, I meant..."
    phone_m "We're pausing them until Thursday, because the Festival is on a Friday, it's less convenient. We could have had the whole weekend to prepare it if the Festival was on a Monday, but oh well."
    phone_m "We have to adapt, I guess."
    phone_m "So this Monday, we continue the sharing of the poems and after we have shared the poems, we announce to them the organization of the club for the next few days until the day of the Festival."
    phone_m "On Tuesday, we will take care of the decoration and the atmosphere of the club room."
    phone_m "And on Wednesday, we'll take care of the cupcakes."
    phone_m "What do you think?"
    phone_mc "I like the idea, but for the cupcakes, how do we plan to do it?"
    phone_mc "We don't have a cook in the club, ahahaha."
    phone_mc "And I highly doubt that the school will accept that we use the refectory's kitchen."
    phone_m "I know!"
    phone_m "Since we only have classes in the morning, we could go to Natsuki's house to help her prepare the cakes in the afternoon."
    phone_m "And if we're done sooner than planned, maybe we could take a walk around town together to relax a bit."
    phone_mc "Mmmhh.."
    phone_mc "Sounds good to me."
    phone_m "Is that all good?"
    phone_mc "Let's do it like this!"
    phone_m "Great then!"
    phone_mc "Thank you, Monika. You're a great help!"
    phone_m "Don't say that... you are a great help too."
    phone_mc "Ahahaha, well thanks again. I'm going to go eat."
    phone_m "Same here, enjoy your meal! We'll talk to each other by message."
    phone_mc "It works, so we'll do it like that. Enjoy your meal too!"
    stop music fadeout 4.0
    "Suddenly, a thought comes to mind."
    "I remember Monika putting on a sad face when she said she had left the debate club on Friday."
    phone_mc "Wait, Monika. Actually, I wanted to know what happened that made you leave the debate club?"
    phone_m "[player]...why are you asking me this?"
    phone_m "You don't need to know, because it's not important. Anyway, have a good evening!"

    $ phone.end_call()

    "Suddenly, Monika hangs up on me with a dry voice."

    "I sigh, putting my phone on the desk."
    mc "Great..."
    play sound closet_open
    show bg kitchen
    with wiperight_scene
    "I head for the kitchen."
    "Once I get to the kitchen I look in the fridge to see what's left."
    mc "I'm as hungry as a wolf.."
    mc "..."
    mc "Nothing interesting.."
    mc "Well, I guess I'm going to make some pasta today."
    show bg bedroom
    with dissolve_scene_full
    "After eating and cleaning the dishes, I go back to my room."
    mc "So..."
    "I stand in front of my closet where my books are stored."
    "..."
    "I remember that Yuri lent me a book."
    mc "Maybe I could start reading it..."
    "I take the book out of my bag."
    mc "« Portrait of Marakov »..."
    "I put the book on my desk, opening the first page and begins to read it."
    show bg bedroom_n
    with dissolve_scene_full
    stop music fadeout 2.0
    "I close the book putting it back in my bag."
    "It was pretty good I'd say."
    "Yuri was right about the beginning. It wasn't very interesting, but as I got further into the story it got more and more intriguing."
    "I get up and walk out of my room to start my evening routine."
    pause 2
    mc "{i}-yawn-...{/i}"
    mc "Well, it's time to go to sleep."
    "I slide under my blanket, and my eyelids, which are rather heavy because of the fatigue accumulated throughout this day, close by themselves."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
