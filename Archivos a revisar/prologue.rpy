label prologue:
    stop music fadeout 3.0
    scene bg black
    with dissolve_scene_full
    $ quick_menu = False
    pause 1
    play music alarm
    "{i}BIP BIP BIP BIP BIP BIP{/i}"
    mc "Uf... Aquí vamos otra vez con otra semana aburrida de clases."
    show bg bedroom
    with open_eyes
    "Abro lentamente los ojos, mirando al techo."
    $ quick_menu = True
    mc "Ojalá pudiera haberme quedado un poco más en la cama, pero..."
    "Miro hacia mi escritorio y veo una hoja de papel con algunas notas que escribí ayer."
    "Desde el viernes, he estado pensando en formar un club."
    "Un club de literatura."
    play music alarm2
    "{i}BIP BIP BIP BIP BIP BIP BIP BIP BIP BIP BIP BIP BIP BIP BIP BIP{/i}{fast}"
    mc "¡Eh, cállate!"
    stop music
    play sound slap
    "{b}{i}¡PLAF!{/i}{/b}"
    mc "{i}-suspiro-{/i} Hay algo mal con esta puta alarma, tengo que pensar en cambiarla."
    "Me levanto de la cama y voy al baño para comenzar mi rutina matutina."
    show bg kitchen
    with wiperight_scene
    "Después de cepillarme el pelo, lavarme los dientes y ponerme el uniforme, voy a la cocina."
    "Abro uno de los armarios, saco un bol y una caja de cereales, y los vierto en el bol."
    "Luego abro la nevera, sacando un cartón de leche y virtiéndolo también."
    window hide
    scene bg residential_day
    with dissolve_scene_full
    play music morning
    "Tras desayunar y lavar los platos, comienzo mi camino a la escuela."
    "Como todos los días, camino solo."
    "En el camino, pensé en preguntar durante el almuerzo los procedimientos para abrir un club."
    "Escuché que hay que preguntarlo en la sala de profesores."
    show bg school_front
    with wiperight_scene
    "Before I know it, I come across the front gate of the school."
    mc "Vamos... terminemos con este día."
    scene bg class_day
    stop music fadeout 3.0
    with dissolve_scene_full
    pause 1
    play music t3
    "Haata ahora, la mañana ha sido increíblemente ordinaria y aburrida."
    "Estuve jugando con mi bolígrafo en la mesa todo el tiempo mientras miraba por la ventana."
    play sound bell
    "Al cabo de un rato, suena la campana de la escuela, marcando el fin de las clases matutinas y el inicio del almuerzo."
    "Recojo mis cosas y salgo al pasillo."
    scene bg corridor
    with wiperight_scene
    stop music fadeout 3.0
    "Una vez llego a la sala de profesores, golpeo suavemente la puerta."
    "No pasa mucho tiempo antes de que un profesor aparezca."
    t "Hola, ¿en qué puedo ayudarte?"
    mc "Hi, my name's [player]! I wanted to ask what the requirements were for opening up a club?"
    t "Well, you've come to the right place, [player]."
    t "All you have to do is ask, and we'll lead you through the process."
    t "Now, tell me. What kind of club are you looking to make?"
    mc "You see, I would like to start a club based on literature."
    t "A literature club?"
    mc "Yes, a literature club."
    t "Uh huh... {w}Well, it looks like you're in luck."
    mc "How so?"
    t "Well... A few years ago, there was another person who started a literature club too."
    t "But just last week the club was dissolved because all of their members left."
    mc "O-Oh, alright...{w} So that's a no?"
    t "Of course not! We always encourage students to go out and start new clubs!"
    t "If you'd like, we have a spare classroom on the third floor that opened up just recently. We could lend you it, if you'd like."
    mc "Really? Wow, thank you."
    t "Heh, of course! Let me get the keys for you, I'll be right back."
    $ quick_menu = False
    pause 2
    $ quick_menu = True
    "He comes back out with a set of keys in his right hand."
    t "Shall we go? I'll show you to your clubroom and explain some of the rules of living, of course."
    mc "Alright."
    "He goes in front of me, leading me down the hall."
    window hide
    scene bg corridor
    with dissolve_scene_full
    window show
    "After a minute or so of walking, we reach the third floor of the building, a part of the school that I rarely visit."
    "We pass by a couple doors before eventually coming to a stop just outside one."
    t "Here we are, this will be your clubroom."
    "He hands over a spare set of keys, motioning over to the door."
    t "...I'll give {i}you{/i} the honor of opening the door."
    "I push the key into the lock, gently turning it until the door opens enough for myself and the teacher to enter."
    play sound closet_open
    scene bg club_day1
    with wiperight_scene
    play music ts 
    "Once inside, I take a look around the room."
    "The tables are more or less dusty, but that's not a big deal in itself."
    t "Let me explain you, something right quick."
    mc "I'm listening."
    t "You'll be in charge of the room from now on."
    t "That means you’ll be responsible for keeping the room clean and undamaged, or at least until you decide to return the keys back to us."
    t "And... here's the paperwork you'll have to fill out. It's nothing hard, just enter some information about your club."
    t "Once you’re done, you can come back to the staff’s room."
    mc "Alright sir, I'll take care of the room, you can trust me."
    t "Wonderful. I’ll be heading back to the staff room now."
    t "If you have any further questions, feel free to come down at any time!"
    mc "Okay, I’ll get started on it right away, then."
    t "O-Oh yeah, I almost forgot again..."
    t "As you know, the school sets up a festival with activities organized by all the official clubs of the school, each year."
    t "This year’s festival is going to be on the Friday of next week."
    t "In order for your club to be an {i}official{/i} club, and to be to able to organize a festival activity of your own, you will need to have a minimum of five members."
    t "--Otherwise you won't be able to organize a festival activity of your own."
    t "...You got all that?"
    "I nod, with a determined look."
    t "Alright, then. That should be everything…"
    t "I have to head back to the staff room, now. Have a great afternoon, [player]!"
    mc "Thanks, you too!"
    "Once the teacher leaves the room, I sit down at the teacher's desk where some administrative papers he mentioned are located."
    mc "Okay, here we go..."
    window hide
    scene bg corridor
    with dissolve_scene_full
    play music dccpa
    window show
    "Once I had filled out the necessary administrative papers, I went to the staff's room."
    "Afterwards, I continued my day as usual..."
    show bg class_day
    with wiperight_scene
    "The afternoon goes by and I simply did what I usually do."
    "Take notes and pretend to listen to the teacher while she's up at the board."
    play sound bell
    "Soon enough the bell rings, signaling the end of the school day."
    "I pack my things and start walking home."
    stop music fadeout 2.0
    window hide
    scene bg bedroom
    with dissolve_scene_full
    window show 
    "Once I get to my room, I put my things down and take off my uniform."
    play music pc 
    "After slipping into a more casual outfit, I sit down at my desk and turn on the computer."
    "I look down at the paper I left on top of my desk this morning."
    mc "Open a club... it's finally done..."
    mc "..."
    mc "...Now it's time to make flyers so I can promote it."
    "Once the computer is booted up, I head to the CANVA website and begin to edit."
    stop music fadeout 3.0
    window hide
    scene bg black
    with dissolve_scene_full
    show text "3 hours later..."
    with dissolve
    pause 2
    hide text
    show bg bedroom
    with dissolve_scene_full
    play music pc
    "I move the mouse cursor to the « PRINT » button."
    play sound click
    "{i}CLICK{/i}"
    "A few moments later, the printer starts up."
    "One by one, about forty flyers printed onto A4 sheets come out of the printer."
    "I stack the flyers as they come out before putting them all into my bag."
    mc "Well now, it's time to read a little."
    "I get up from my chair and head over to my own little library."
    "I pull out a random book and begin to read it."
    stop music fadeout 3.0
    window hide
    show bg black
    with dissolve_scene_full
    show text "The next day....\n\n\n\nApril, 18th 2023"
    with dissolve
    pause 3
    hide text
    with dissolve

    show bg school_front
    with dissolve_scene_full
    play music morning
    "I stand in front of the school gate, my flyers in my bag."
    "I look at the time on my phone."
    "{i}7:58 AM{/i}"
    "Class starts in just two minutes, I'm lucky I didn't wake up too late this morning..."
    "I had originally planned to set up the flyers this morning, but unfortunately I don't think I'll have the time."
    stop music fadeout 2.0
    "Upon reaching the main door, something catches my attention."

    m "Heeeeeey, [player]!"

    $ m_name = "Monika"

    "I hear a voice come from behind me, calling my name."
    "I immediately recognize this voice that can only be---"
    play music her
    "Monika."
    "Monika...{w=0.8} we were in the same class together last year, she was the most popular girl in the school."
    "We had developed a strong friendship between me and her..."
    "In fact, we often worked together in class whether in pairs or in group work."
    "I had started to develop a crush on her, but I never had the courage to confess to her..."
    "But since the beginning of this school year, that friendship started to fade every day."
    "The first was simply because we weren't in the same class anymore, and the second was that she decided to join the debate club..."
    "She also managed to be promoted to vice president within a month, even telling me how the previous vice president left the club soon after."
    "Which doesn't really help our situation, to be honest..."
    "As a result, for the past few months, we'd been talking quickly whenever we ran into each other."
    "And, it seems this is one of those times..."
    "While I was lost in my thoughts, Monika somehow managed to sneak in front of me."
    show monika 2l at l11
    m "...Haaaaaaaaaahhh... ..Haaaaaahhh.."
    "She places her right hand on her hip, catching her breath."
    "Did she run all the way to school...?"
    mc "Did you oversleep Monika?"
    show monika 1h at h11
    "Monika straightens up, glaring at me."
    show monika 2a
    "I giggle nervously."
    mc "Ahaha.. forget what I said.."
    "Monika giggles."
    show monika 5a at h11
    m "You're so easy to fluster, [player]."
    m "Ehehehe~"
    m 1l "I was just...{w=0.4} let's say...{w=0.4} really {i}busy{/i} with new activities for the debate club."
    mc "Is that what you mean?"
    "I point to Monika's left hand, where she holds a roll of paper."
    show monika 2a at t11
    m "Ehehe, yeah exactly..."
    show monika 3b at t11
    m "I think they'll like it!"
    show monika 1a at t11
    mc "I bet you're right about that, Monika. Even though I'm not in that club, I know you've always had great ideas!"
    show monika 1j at t11
    m "Thanks [player]!"
    show monika 1b
    m "...We should go inside or else we might get in trouble."
    mc "O-Oh, yeah. You're right..."
    show monika at thide
    hide monika
    "...It's just as I predicted."
    "Only a minute or so of talking before we're already heading our seperate ways..."
    "{i}-sigh-{/i}"

    window hide
    show bg class_day
    stop music fadeout 2.0
    with dissolve_scene_full
    play music dccpa
    "It's already the end of the morning."
    "Time passed by a little faster than I thought..."
    play sound bell
    "Soon enough, the bell rings to signify the beginning of our lunch break."
    "I grab my bag and heads for the entrance."
    show bg locker
    with wiperight_scene
    pause 0.80
    scene bg locker with dissolve:

        zoom 1.5
    "I pull out a roll of scotch that I brought from home, along with a flyer from my bag."
    mc "Sooo..."
    "I take a long look at the corkboard in front of me."
    "Flyers from other clubs are already posted."
    "I can't help but compare them to mine for a moment..."
    "There's a small difference in the design quality compared to the others, but I say it still looks decent."
    "I place the flyer against the cork board, taping it up and down."
    "When finished, I step back to admire the result."
    scene bg locker with dissolve
    mc "Not bad!"
    "I retrieve the flyers from my bag, taking them with both hands."
    mc "Now... It's time for a flyer distribution."
    stop music fadeout 2.0
    show bg courtyard
    with wiperight_scene
    pause 0.50 
    play music morning
    "I head to the courtyard."
    "The weather is perfect. There's few clouds in the sky and the sun is shining brightly, making lunch breaks outside enjoyable."
    "A lot of students are having lunch on the benches... I call out to each of them nicely, trying to be as diplomatic as possible."
    show bg black
    stop music fadeout 2.0
    with dissolve_scene_full
    "{i}25 minutes later...{/i}"
    show bg courtyard
    with dissolve_scene_full
    pause 0.50
    play music morning
    mc "{i}Whew...{/i} That was harder than I thought..."
    "I take a quick look around the courtyard."
    "I was able to hand out about thirty flyers, which isn't bad."
    "I still have about nine flyers on hand that I haven't been able to distribute, but I won't complain..."
    mc "Now it's just a matter of waiting until the people come to check out the club."
    "I go back to get my bag that was left on the floor at the entrance."
    show bg locker
    with wipeleft
    "I put away the remaining flyers into my bag before heading back outside."
    show bg courtyard
    with wiperight
    "I decide to take a seat on one of the benches in the courtyard to enjoy some of the sunshine."
    "Dipping my hand back into my bag, I look for my snack."
    mc "Ah, perfect! I deserve a good break..."
    "I pull out a {i}jambon-beurre{/i} sandwich."
    "My mom has made it a tradition to make me this kind of sandwich ever since she traveled to France on a business trip two years ago."
    "She tasted different French traditions, and she was very seduced by this type of sandwich."
    "Since then, every Tuesday morning before she goes to work, she makes me this sandwich."
    "..."
    play sound bell
    "As soon as I finish, the bell rings to signify the end of the lunch break as usual."
    mc "{i}-sigh-{/i} Let's go. More endless hours of class await me."
    window hide
    show bg class_day
    stop music fadeout 1.5
    with dissolve_scene_full
    play music dccpa
    play sound bell
    "The bell rings bringing the day to a close."
    "I put my things in my bag before leaving the room."
    show bg corridor
    with wiperight_scene
    "Once in the hallway, I head straight for my club room."
    "I eventually reach the third floor and quickly head inside the club room."
    show bg club_day1
    with wipeleft_scene
    mc "Ahh, finally."
    "I set down my bag, hanging nearby one of the desks."
    "People should be arriving soon, I should find something to do while I wait..."
    "I pace around the room, eventually heading over to the open closet."
    show bg closet
    with wiperight
    "Mindlessly looking around, I can see a large, vacant spot at the top of the closet."
    "I also see some filing cabinets and some huge books tucked away that appear to be textbooks belonging to the school."
    "Nothing really that {i}notable{/i}, though..."
    "I eventually decide to close up the closet and head back over to where I dropped off my stuff, earlier."
    play sound closet_close
    show bg club_day1
    with wipeleft
    "I contemplate the flyers that lie on the table."
    "And then I look in the direction of the door..."
    mc "Just have to keep waiting..."
    window hide
    show bg club_day1
    with dissolve_scene_full
    "...The next two hours were silent."
    "No one showed up at the club."
    "Only the sound of doors shutting and footsteps of which I would assume are from other students in the hallway were audible to my ears."
    mc "Well... let's go home, I guess."
    show bg corridor_e
    with wipeleft_scene
    "I leave the clubroom, locking the door behind me."
    "I then start to walk home."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
