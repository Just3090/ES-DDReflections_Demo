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
    "Antes de que lo supiese, me encuentro en la entrada principal de la escuela."
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
    mc "Hola, me llamo [player]. Quería preguntar cuáles son los requisitos para abrir un club."
    t "Bueno, has venido al lugar indicado, [player]."
    t "Todo lo que tienes que hacer es pedirlo, y te guiaremos durante el proceso."
    t "Ahora dime, ¿qué tipo de club te gustaría crear?"
    mc "Verá, me gustaría empezar un club de literatura."
    t "¿Un club de literatura?"
    mc "Sí, un club de literatura."
    t "Ajá... {w}Bueno, parece que tienes suerte."
    mc "¿En serio? ¿Por qué?"
    t "Bueno... Hace algunos años, alguien más fundó un club de literatura también."
    t "Pero la semana pasada se disolvió porque todos sus miembros lo abandonaron."
    mc "A-ah... de acuerdo...{w} ¿Eso significa que no puedo hacerlo?"
    t "¡Por supuesto que no! Siempre animamos a los estudiantes a formar nuevos clubes."
    t "Si quieres, tenemos un aula libre en el tercer piso que se acaba de desocupar. Podríamos prestártela, si te interesa."
    mc "¿De verdad? Vaya, muchas gracias."
    t "Jeje, ¡por supuesto! Déjame buscar las llaves, vuelvo enseguida."
    $ quick_menu = False
    pause 2
    $ quick_menu = True
    "El profesor vuelve, al cabo de unos minutos, con un juego de llaves en la mano derecha."
    t "¿Vamos? Te mostraré tu aula del club y te explicaré algunas reglas básicas."
    mc "De acuerdo."
    "El profesor camina delante de mí, guiándome por el pasillo."
    window hide
    scene bg corridor
    with dissolve_scene_full
    window show
    "Después de un minuto caminando, llegamos al tercer piso del edificio, una parte de la escuela que rara vez visito."
    "Pasamos junto a algunas puertas antes de detenernos frente a una."
    t "Aquí estamos. Este será tu aula del club."
    "Me entrega un juego de llaves de repuesto, señalando la puerta."
    t "...{i}Te{/i} daré el honor de abrir la puerta."
    "Inserto la llave en la cerradura, girándola suavemente hasta que la puerta se abre lo suficiente como para entrar junto con el profesor."
    play sound closet_open
    scene bg club_day1
    with wiperight_scene
    play music ts 
    "Una vez dentro, echo un vistazo al aula."
    "Las mesas están algo polvorientas, pero no es un gran problema en sí."
    t "Déjame explicarte algo rápidamente."
    mc "Te escucho."
    t "A partir de ahora, estarás a cargo del aula."
    t "Eso significa que serás responsable de mantenerla limpia y en buen estado, al menos hasta que decidas devolvernos las llaves."
    t "Y... aquí tienes el papeleo que tendrás que rellenar. No es nada complicado, solo necesitas ingresar información sobre tu club."
    t "Cuando termines, puedes volver a la sala de profesores."
    mc "De acuerdo, señor. Me encargaré del aula, puede confiar en mí."
    t "Excelente. Volveré a la sala de profesores ahora."
    t "Si tienes más preguntas, no dudes en venir en cualquier momento."
    mc "Entendido. Me pondré manos a la obra de inmediato."
    t "A-ah, sí, casi se me olvida..."
    t "Como sabes, la escuela organiza un festival anual con actividades de todos los clubes oficiales."
    t "El festival de este año será el viernes de la semana que viene."
    t "Para que tu club sea considerado {i}oficial{/i} y puedas participar en el festival, necesitas tener al menos cinco miembros."
    t "... De todas maneras, no serías capaz de organizar una actividad de festival tú solo."
    t "... ¿Ha quedado todo claro?"
    "Asiento con determinación."
    t "Muy bien, eso sería todo entonces."
    t "Tengo que volver a la sala de profesores. ¡Qué tengas una excelente tarde, [player]!"
    mc "Gracias, igualmente."
    "Una vez que el profesor deja el aula, me siento en el escritorio del profesor, donde están los papeles administrativos que mencionó."
    mc "Bien, manos a la obra..."
    window hide
    scene bg corridor
    with dissolve_scene_full
    play music dccpa
    window show
    "Después de rellenar los papeles administrativos necesarios, voy a la sala de profesores."
    "Luego, continúo mi día como siempre..."
    show bg class_day
    with wiperight_scene
    "La tarde pasa, y simplemente hago lo que suelo hacer."
    "Tomo notas y finjo escuchar a la profesora mientras escribe en la pizarra."
    play sound bell
    "Pronto suena la campana, señalando el final del día escolar."
    "Recojo mis cosas y comienzo a caminar de regreso a casa."
    stop music fadeout 2.0
    window hide
    scene bg bedroom
    with dissolve_scene_full
    window show 
    "Una vez en mi habitación, dejo mis cosas y me quito el uniforme."
    play music pc 
    "Después de ponerme algo más cómodo, me siento en mi escritorio y enciendo el ordenador."
    "Miro el papel que dejé esta mañana encima del escritorio."
    mc "Abrir un club... finalmente está hecho..."
    mc "..."
    mc "... Ahora es momento de crear folletos para promocionarlo."
    "Cuando el ordenador se inicia, accedo a la página de CANVA y empiezo a editar."
    stop music fadeout 3.0
    window hide
    scene bg black
    with dissolve_scene_full
    show text "3 horas después..."
    with dissolve
    pause 2
    hide text
    show bg bedroom
    with dissolve_scene_full
    play music pc
    "Muevo el cursor hasta el botón « IMPRIMIR »."
    play sound click
    "{i}CLIC{/i}"
    "Poco después, la impresora comienza a funcionar."
    "Uno a uno, los cuarenta folletos en hojas A4 salen de la impresora."
    "Apilo los folletos a medida que salen y los guardo en mi mochila."
    mc "Bueno, ahora es momento de leer un poco."
    "Me levanto de la silla y me acerco a mi pequeña biblioteca."
    "Saco un libro al azar y comienzo a leer."
    stop music fadeout 3.0
    window hide
    show bg black
    with dissolve_scene_full
    show text "Al día siguiente....\n\n\n\nn18 de abril de 2023."
    with dissolve
    pause 3
    hide text
    with dissolve

    show bg school_front
    with dissolve_scene_full
    play music morning
    "Estoy frente a la puerta de la escuela, con los folletos en mi mochila."
    "Miro la hora en mi teléfono."
    "{i}7:58 AM{/i}"
    "Las clases empiezan en dos minutos... Menos mal que no me desperté tarde hoy."
    "Tenía planeado colocar los folletos esta mañana, pero desgraciadamente no creo que tenga tiempo."
    stop music fadeout 2.0
    "Al llegar a la entrada principal, algo llama mi atención."

    m "¡Eeeeeeeeey, [player]!"

    $ m_name = "Monika"

    "Una voz familiar llama mi nombre desde atrás."
    "Reconozco de inmediato esa voz. No podría ser otra que..."
    play music her
    "Monika."
    "Monika...{w=0.8} estuvimos en la misma clase el año pasado, era la chica más popular del instituto."
    "Hemos desarrollado una amistad muy fuerte entre ella y yo..."
    "De hecho, solíamos trabajar juntos en clase, ya fuese en parejas o en trabajos grupales."
    "Con el tiempo, empecé a desarrollar sentimientos hacia ella... pero nunca tuve el valor de confesárselos."
    "Sin embargo, desde que comenzó este curso escolar, esa amistad se ha ido desvaneciendo poco a poco."
    "Primero, porque ya no estábamos en la misma clase, y segundo, porque decidió unirse al club de debate..."
    "No solo eso, sino que en menos de un mes consiguió ser promovida a vicepresidenta del club. Recuerdo que me contó cómo el antiguo vicepresidente había dejado el club poco después."
    "Todo esto no ha ayudado precisamente a que mantengamos el contacto..."
    "En los últimos meses, solo hemos intercambiado unas pocas palabras cuando nos cruzamos por casualidad."
    "Y parece que hoy es uno de esos momentos..."
    "Mientras estoy absorto en mis pensamientos, Monika aparece frente a mí."
    show monika 2l at l11
    m "...Aaaaaaaahhhhh... ...Aaaaaahhhhh..."
    "Monika jadea, con la mano en la cadera, mientras recupera el aliento."
    "¿Ha corrido todo el camino hacia la escuela...?"
    mc "¿Dormiste más de la cuenta, Monika?"
    show monika 1h at h11
    "Monika se endereza y me mira con seriedad."
    show monika 2a
    "Río nerviosamente."
    mc "Ajaja... olvida lo que dije."
    "Monika ríe también."
    show monika 5a at h11
    m "Es muy fácil ponerte nervioso, [player]."
    m "Jejejeje~"
    m 1l "Solo...{w=0.4} digamos que estuve...{w=0.4} muy {i}ocupada{/i} con nuevas actividades para el club de debate."
    mc "¿Te refieres a eso?"
    "Señalo el rollo de papel que sostiene con la mano izquierda."
    show monika 2a at t11
    m "Jejeje, exactamente..."
    show monika 3b at t11
    m "Creo que les encantará."
    show monika 1a at t11
    mc "Estoy seguro de eso, Monika. Aunque no esté en tu club, sé que siempre tienes ideas geniales."
    show monika 1j at t11
    m "¡Gracias, [player]!"
    show monika 1b
    m "... Será mejor que entremos, o nos meteremos en problemas."
    mc "A-ah, sí. Tienes razón..."
    show monika at thide
    hide monika
    "... Es tal y como lo predije."
    "Solo unos minutos hablando y ya vamos por caminos separados..."
    "{i}-suspiro-{/i}"

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
