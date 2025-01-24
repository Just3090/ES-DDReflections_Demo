label ch1_main:
    stop music fadeout 3.0
    scene bg black
    with dissolve_scene_full
    show text "2 DÍAS DESPUÉS\n\n\n\n\n\n\n\n20 de abril de 2023"
    with dissolve
    pause 3
    hide text
    show bg class_day
    with dissolve_scene_full
    play music t3
    "Es jueves, el penúltimo día de clases antes de que comience el fin de semana."
    "El día ha sido más que ordinario, y las clases siempre son más o menos aburridas."
    play sound bell
    "Una vez que suena la campana, recojo mis cosas antes de dirigirme al aula del club."
    show bg corridor
    with wipeleft_scene
    "Tomo aire mientras me planto frente a la puerta."
    play sound closet_open
    show bg club_day
    with wipeleft_scene
    "Finalmente, entro en el aula del club y saludo a los miembros del club."
    mc "¡Hola, compis!"
    mc "¿Está todo el mundo aquí?"
    mc "¡Genial! ¡Podemos comenzar la reunión!"
    stop music fadeout 2.0
    mc "..."
    "Estoy de pie frente al aula del club, vacía."
    play music dccpa
    "Suspiro largamente antes de dejarme caer sobre un pupitre."
    "Es muy difícil empezar un club nuevo."
    "¿No son mis folletos lo suficientemente buenos...?"
    "Estoy hojeando los folletos desperdigados sobre el pupitre."
    "Esos que no repartí el martes."
    mc "{i}-suspiro-...{/i}¿Estaban mal hechos después de todo?"
    mc "No lo sé..."
    "Apoyo la cabeza en mis brazos, descansando sobre el pupitre."
    window hide
    show bg black
    with close_eyes
    "Los últimos tres días han sido más ansiosos de lo que esperaba."
    "¿He sido demasiado optimista y ambicioso al pensar que la literatura era un tema interesante para desarrollar?"
    mc "Mierda..."
    "La falta de sueño acumulada durante los últimos dos días empieza a manifestarse."
    "Mis pensamientos se empiezan a nublar, y el cansancio comienza a apoderarse de mí."
    mc "Supongo que una pequeña siesta no me hará daño..."
    "Con mis pensamientos disolviéndose lentamente, empiezo a quedarme dormido."
    stop music fadeout 3.0
    window hide
    pause 4.5
    $ m_name = "??????"
    m "Eh, {w=0.75}¿[player]?"
    scene bg club_day1
    with open_eyes
    "Sorprendido por un repentino subidón de adrenalina, salto del pupitre."
    mc "¡¡AAA-!!"
    "Miro hacia la puerta y veo a dos chicas de instituto paradas."
    "Reconozco a una de ellas como nadie más que..."
    "¿Monika?"
    show monika 1d at t21
    play music encounter 
    "La otra chica no la conozco, pero si está con Monika, eso me dice que probablemente es su amiga."
    show sayori 2q at t22
    "Ella ríe, adoptando un tono burlón."
    s 2r "Jejejejeje... ¿Este es el club de las siestas?"
    mc "¿Qu- qué? ¡No, no!"
    show monika base uniform neut awkw rhip n2 mb e4b at f21
    show sayori 2q at f22
    "{i}Ella{/i} y Monika se ríen."
    "Pensándolo rápidamente, es cierto que me pillaron echándome una siesta. ¡Pero no es así, en realidad!"
    "Hago todo lo posible por calmarme antes de echar un vistazo más serio."
    show monika 1a at t21
    show sayori 1a at t22
    mc "Es cierto, me pillásteis en {i}un mal momento{/i}."
    mc "Pero volviendo al tema, este es el Club de Literatura."
    mc "Dios mío...{w=0.5} Ojalá no me hubiera quedado dormido para mostrar un lado más profesional..."
    "Río nerviosamente."
    show sayori base uniform happ
    s "¡No pasa nada! Estaba bromeando."
    "Finalmente, Monika decide intervenir."
    $ m_name = "Monika"
    show monika base uniform me e1a
    m "Así que tú eres quien lleva el Club de Literatura, ¿no?"
    "Asiento con la cabeza mostrando una pequeña sonrisa."
    mc "¡Exacto!"
    mc "Soy el presidente del club."
    show monika base uniform neut mb e4b
    m "¡Eso está genial!"
    pause 0.5
    show monika base uniform neut ma e1b
    pause 0.5
    show monika base uniform neut ma e1c
    pause 0.5
    "Monika echa un vistazo por el aula."
    "Yo hago lo mismo, notando cómo se acelera mi corazón."
    show monika base uniform neut mb e1a
    m "¿Dónde están los demás miembros?"
    show monika base uniform neut ma
    mc "Ajaja...{w=0.5} bueno...{w=0.4} ya 'estáis' aquí."
    "Me encojo de hombros, avergonzado."
    show monika 1d
    m "¿Eh?"
    "Monika levanta las cejas, como si fuera a decir algo, pero se contiene rápidamente."
    mc "Ajajajaja... No sabía que abrir un club sería tan difícil."
    mc "Hice lo mejor que pude para reclutar gente, pero fue en vano."
    show sayori base uniform mg e1a b1a
    s "Si solo estás tú... eso significa..."
    show sayori base uniform e4b mc rup lup at h22
    s "... ¡Que somos tus dos primeros miembros!"
    show monika base uniform happ lpoint e4b
    m "Ajajaja, cierto."
    mc "¿Qué?"
    "¿Es eso lo que he escuchado?"
    "Pero ¿no está Monika en el club de debate?"
    "Quizás me he perdido algo..."
    mc "Pero, Monika... ¿no estabas en el club de debate?"
    show sayori at thide
    hide sayori
    show monika base uniform happ lpoint e4b at t11
    "Monika se ríe nerviosamente."
    show monika base uniform e1b b1b mb rhip
    m "Jajajaja.. bueno... dejé el club de debate hace poco."
    show monika base uniform e1b b1b ma rhip ldown
    mc "¿Y eso?"
    show monika base uniform e1b rdown
    m "Bueno... ¿Recuerdas aquella actividad que te mencioné el martes?"
    show monika base uniform e1b md
    mc "Claro."
    show monika base uniform e4b mb awkw
    m "Digamos que... fue un desastre y el ambiente quedó por los suelos..."
    show monika e1a b1b ma lpoint
    m "Prefiero no entrar en detalles, ya da igual."
    m "Vamos a centrarnos en el 'ahora', ¿vale, [player]?"
    show monika lean uniform neut ma n1 at h11
    "Esa condenada sonrisa... siempre dejándome con el corazón en la boca."
    mc "Eeehhh... Sí..."
    show monika base uniform e1b b1b me rdown ldown at t21
    show sayori base uniform mg rup at t22
    s "Parece que os conocéis."
    mc "Exacto, ya nos conocemos."
    "Me giro un poco hacia la otra chica."
    mc "Por cierto, ¿cómo te llamas?"
    mc "No te lo he preguntado y creo que es algo importante."
    show monika base uniform ma e1a b1a rhip
    show sayori base uniform e1a mb lup
    $ s_name = "Sayori"
    s "¡Me llamo Sayori!"
    show sayori base uniform neut mb ldown
    s "¿Y tú?"
    show sayori base uniform neut ma
    mc "¡Encantado de conocerte, Sayori! Me llamo [player]."
    "Le sonrío felizmente."
    show sayori base uniform neut mb lup
    s "El gusto es mío."
    s "Todavía me sorprende que nadie se haya unido a tu club aún."
    show sayori base uniform neut ma ldown
    mc "Bueno, si lo piensas, creo que sé por qué no hay nadie aquí..."
    mc "A primera vista, la literatura puede parecer poco interesante o incluso aburrida."
    mc "Lo cual puedo entender."
    mc "Pero yo no lo veo así en absoluto.{w=0.5} Es algo muy amplio..."
    mc "Hay muchas formas de expresarla, ya sea mediante libros, {w=0.5} poesía o incluso teatro."
    show sayori base uniform e1b b1b mc blaw at s22
    show monika base uniform e1c me rdown
    "Noto que Sayori desvía la mirada de Monika, y se le dibuja una sonrisa en los labios que no sé cómo describir."
    mc "Ah... perdón, no quería sonar aburrido."
    show monika base uniform e1a md
    show sayori base uniform e1a b1c mg rup nobl at t22
    s "¿Eh? ¡No!"
    show sayori base uniform e1b b1b mc
    s "Es solo que... ¡parece que le pones mucha pasión, jeje!"
    mc "Puede ser, pero también me gusta hacer otras cosas."
    show sayori base uniform neut md e1a b1a nobl
    show monika base uniform neut ma e1a b1a nobl
    mc "No soy alguien que solo se centra en libros o novelas."
    mc "Es solo que es mi hobby principal, si lo podemos llamar así..."
    mc "Bueno... así que..."
    "Aclaro mi garganta, cambiando a una voz firme y diplomática."
    mc "Monika y Sayori, si no cambiáis de opinión... puedo decir con orgullo como presidente..."
    mc "¡Bienvenidas al Club de Literatura!"
    show sayori base uniform e4b mc rup lup at h22
    s "¡Bieeeeeeeeeeeeeen!"
    show monika lean uniform neut ma
    m "Gracias, [player]."
    show monika base uniform neut ma
    mc "Dicho esto... No quiero sonar pesimista ni nada."
    mc "Pero... para que pueda declarar oficialmente mi club y que pueda participar en las actividades anuales organizadas por la escuela, necesitamos tener un mínimo de cinco miembros..."
    show monika base uniform neut mb rhip
    m "No te preocupes [player], encontraremos a los dos miembros restantes en un abrir y cerrar de ojos."

    "No puedo evitar sonreír estúpidamente."
    "Incluso tengo la sensación de que Monika es más optimista que yo."
    "Sé que Monika tiene mucha confianza en lo que hace."
    "Pero, ¿cómo vamos a encontrar a dos personas más?"
    "Tardé toda una semana de clases en conseguir solo a dos personas."
    "Y lo peor es que ni siquiera logré que vinieran."
    "¡Han venido por su cuenta!"
    "Como Monika fue vicepresidenta del club de debate, seguramente pueda..."
    "¿Pedirle que sea mi vicepresidenta?"
    "Siento un nudo en la garganta al pensarlo, ¿no es un poco directo?"
    "¿Pensará que quiero aprovecharme de su popularidad para darle al club la mayor credibilidad posible?"
    "Además, dejó claro que hace poco dejó el club de debate."
    "La mejor manera de saberlo es preguntarle."
    mc "Monika, sé que esto puede parecer repentino, pero..."
    mc "Me gustaría preguntarte algo, si puedo."
    show monika base uniform neut me rdown
    m "¿Eh?"
    show monika base uniform neut md
    m "¿Qué quieres preguntarme?"
    mc "¡D- d- después te lo pregunto!"
    show monika base uniform neut me rhip
    m "Ehhh... ¿vale?"
    m "Haz lo que quieras."
    show sayori base uniform e1a mb rup ldown
    s "Jejejeje, ¡se te quiere declarar, Monika!"
    show sayori base uniform e4b mc rup lup
    s "¡Qué monooooooo~!"
    show monika base uniform e4b b1b blaw ma rdown ldown
    mc "¡¿Qu- qué?!"
    mc "¡Ni siquiera estaba pensando en eso!"
    "Es imposible no sentirme incómodo."
    "Esta chica es impredecible, te lo juro."
    "En cuanto a Monika, lo noto brevemente, pero parece estar un poco avergonzada por lo que acaba de decir Sayori."
    show sayori base uniform e1a mb rup ldown
    s "Jejejeje, estoy bromeando. No te preocupes."
    s "Tu reacción ha sido muy mona, es muy fácil ponerte nervioso, ¡me gusta!"
    mc "Bueno... eso no era realmente lo que estaba pensando..."
    mc "Y... espera un momento, ¿acabas de decir que mi reacción ha sido-?"
    show sayori base uniform e1a mb rdown
    s "¡No has escuchado nada!"
    show sayori base uniform e1a ma
    show monika base uniform e4b mb awkw lpoint
    m "Ajajajaja... Vamos, Sayori. Sé un poco más seria delante de tu presidente."
    show monika base uniform e1a ma awkw ldown
    show sayori tap uniform m2 e2 b2
    s "Pffffff... no tienes gracia, Monika."
    mc "Sigo entendiendo lo que dices, Sayori..."
    show sayori base uniform e4b mc rup lup
    show monika base uniform e4b b1a nobl mb rhip
    "Ambas se ríen."
    "Pongo los ojos en blanco y respiro profundamente."
    mc "¡Bueno!"
    mc "¿Qué os parece si nos tranquilizamos un poco?"
    show sayori base uniform e1a b1a mb rdown ldown
    s "¡Vale!"
    show monika base uniform e1a ma
    "Monika asiente brevemente en respuesta a mi petición."
    show monika at thide
    show sayori at thide
    hide monika
    hide sayori
    "Y así, por primera vez desde que empezó la semana, mi club tiene dos nuevos miembros."
    show monika 1a at t11
    "Monika."
    show monika 1a at t21
    show sayori 1a at t22
    "... Y Sayori."
    show monika 1a at thide
    show sayori 1a at thide
    hide monika
    hide sayori
    "Es como si me hubieran quitado un peso de encima; se siente genial."
    show bg club_day1
    with wiperight_scene
    "Monika, Sayori y yo organizamos algunas mesas antes de sentarnos."
    show sayori base uniform neut ma at t21
    show monika base uniform neut ma at t22
    mc "¡Ah, bien!"
    mc "Quiero repetirlo de nuevo: gracias a las dos por haberos unido a mi club, me hace muy feliz, más de lo que podéis imaginar."
    mc "Aunque me habría gustado que las cosas fueran un poco {i}diferentes.{/i} {w=0.3} Ajajajaja."
    show sayori base uniform neut mb rup
    s "No te preocupes, soy mejor que tú cuando se trata de echarme siestas. ¡Estoy segura que hasta puedo sustituirte!"
    mc "¿Sustituirme...?"
    mc "¿De qué hablas?"
    show sayori base uniform e1b b1b mc blaw
    s "..."
    show sayori base uniform nobl at s21
    s "Yo... Tú... eh... qué es lo que..."
    show sayori base uniform e4c ml b1b rdown at h21
    s "Bah, ¡olvídalo!"
    mc "¿Eh...?"
    show sayori base uniform neut mc e1b b1b blaw at s21
    "Sayori se hunde un poco más en su silla, luchando contra su incomodidad."
    "Finalmente, desisto de tratar de entender su comportamiento inexplicable."
    "Monika suspira y toma las riendas de la situación."
    show monika base uniform rhip mb
    m "De todas formas, [player], creo que hay algo importante que debo decirte."
    show monika base uniform ma
    mc "¿Sí...?"
    show monika lean uniform ma
    m "Me has robado la idea, ¿sabes?"

    mc "¿De qué estás hablando?"

    show monika base uniform happ lpoint b1b
    show sayori base uniform e1a ma b1a nobl

    m "Pues..."
    m "No te lo dije, pero también había pensado en fundar un Club de Literatura."
    mc "¿En serio?"
    mc "Nunca lo mencionaste."

    show monika happ rhip

    m "¡Lo sé!"
    m "Me lo reservaba mientras estaba en el club de debate."

    show monika lean uniform happ

    m "Jejejeje, pero parece que tuvimos la misma idea."
    m "Debe haber alguna conexión entre nosotros, ¿eh?"
    mc "¿Qu- qué?"
    "De repente, siento mi corazón acelerándose."


    show monika base uniform happ rhip mb e4b

    m "¡Madre mía, vaya cara pones, [player], ajajajaja!"

    show sayori base uniform happ lup rup mc e4b b1a nobl

    s "¡Ajajaja! ¡Es muy monoooooo!"
    "¡¿Cómo no vas a poner una cara así cuando la chica popular de tu antigua clase te dice algo como eso?!"
    "Respiro profundamente, tratando con todas mis fuerzas de recuperar la seriedad."

    show monika base uniform neut ma e1a rdown
    show sayori base uniform neut ma e1a rdown ldown

    mc "Ajajaja... bueno, para ser honesto, pensé en esto el fin de semana."
    mc "Pensé que iba a ser un rollo fundar el club, pero parece que todo ha ido como la seda."
    mc "Solo tuve que imprimir unos folletos y rellenar unos papeles administrativos. Lo más complicado ya está hecho."
    mc "Ahora lo que falta es encontrar gente interesada en la literatura."
    "Miro brevemente a Sayori mientras lo digo."

    show sayori base uniform neut rup mh b2c

    s "Eh... ¿por qué me miras así de repente?"
    mc "Bueno... quería saber si realmente te interesa la literatura, Sayori. Solo era una pregunta inocente..."

    show sayori base uniform neut rup b2b

    s "¡Pues claro que me gusta la literatura!"

    show sayori base uniform neut lup rdown mg b1d

    mc "¿Y qué géneros literarios son tus favoritos, Sayori?"

    show sayori base uniform happ lup rup mc e4b b1a

    s "¡Me encanta escribir poemas!"
    mc "¿Poemas?"
    mc "Es cierto que forman parte de la literatura y son un género literario."
    mc "Perdona, tenía mis dudas contigo, Sayori."

    show sayori base uniform neut ma e1b b1b lup rdown
    show monika base uniform neut ma rhip

    m "No te preocupes, [player]."
    m "Sayori es mi mejor amiga, la conozco mejor que nadie."
    "¿Su mejor amiga?
    "Estoy sorprendido. Llevamos años conociéndonos y nunca me había hablado de ella antes..."
    m "Siempre se esfuerza al máximo en lo que hace y se preocupa por [player]."
    m "Es como un rayo de sol andante."

    show sayori base uniform neut blaw rup mc e1b b2c

    s "No digas eso, Monika... ¡Solo quiero hacer que todo el mundo sea feliz!"
    mc "Supongo que podría escucharte con los ojos cerrados, Monika."
    mc "Después de todo, tienes experiencia en los clubes."
    mc "Sé que ahora el club está empezando y parece obvio lo que te estoy contando."
    mc "Pero lo que quiero decir es que, de momento, no tenemos actividades planeadas para el club. ¡Cuando seamos más, empezaré a pensar en ello!"

    show sayori base uniform happ lup e1a b1a ma rdown nobl

    m "No te preocupes, [player]"
    m "Puedes tomarte tu tiempo, no hay prisa."
    mc "Monika, sabes que el festival es el próximo viernes, ¿no?"

    show monika base uniform neut ldown me

    m "¿Eh?"

    show monika base uniform neut me

    m "Sí, claro que lo sé, [player]. Pero, ¿por qué lo mencionas?"
    mc "Bueno, para participar, el club tiene que tener al menos cinco miembros."
    show sayori base uniform neut e1a mb rdown
    s "Entonces, ¿por qué no empezamos a buscarlos ya?"
    mc "¿Ahora?"
    show sayori base uniform neut rup e4b mc
    s "¡Claro!"
    mc "Emmm... vale."
    mc "¿Qué dices, Monika? ¿Te apuntas?"
    show monika base uniform neut ma rdown
    m "¡Por supuesto!"

    show sayori base uniform neut rup mb e4b at h21

    s "¡Vamos allá!"
    mc "Sí, vamos allá."
    mc "Podéis coger uno de los folletos que hay en la mesa de allí."
    "Señalo con el dedo un escritorio, donde está la pila de folletos que me sobró."

    show monika base uniform happ b2c

    m "Tranquilo, no te preocupes. Soy bastante persuasiva."
    s 1b "Hmmmmmmmm..."

    show sayori base uniform neut ma

    s "¡Yo también me las apañaré!"
    mc "Ah... vale, de acuerdo.."
    mc "¿Qué tal si nos dividimos para que sea más fácil?"

    show sayori tap uniform nerv awkw m1

    s "Eh... [player]... no es por ti, pero..."
    s "Preferiría ir con Monika si es posible."
    mc "Está bien, no pasa nada."
    "Los tres salimos del aula del club."

    show sayori at thide
    show monika at thide
    hide sayori
    hide monika
    show bg corridor
    with wiperight_scene
    show sayori base uniform happ at t21
    show monika base uniform happ rhip at t22

    s "¡Jejejejeje, que gane el mejor, [player]!"
    mc "Emmmm... sí, que gane el mejor, Sayori."

    show sayori base uniform neut lup rup mc e4b b1a

    s "¡Jejejeje, es como una competición!"
    s "¡Hace que tenga aún más ganas de buscar gente!"

    show sayori at thide
    show monika at thide
    hide sayori
    hide monika

    "Por dentro, me parece una tontería."
    "Pero para no hacerla sentir mal ni ahuyentarla, decido seguirle el juego."
    "Al fin y al cabo, ¿es una competición de verdad?"
    "¡Si no hay nada que ganar!"
    "Bueno... ganaríamos miembros para el club, pero eso no es un trofeo."
    mc "Suerte a las dos, nos vemos en el club en media hora, ¿os parece bien?"

    show monika base uniform happ at t11

    m "Suerte para ti también, [player]."

    show monika at thide
    hide monika
    show bg corridor
    with wipeleft_scene

    "Finalmente, nos separamos, y cada uno sigue su camino."
    "Deambulo por los pasillos desiertos del instituto."
    "Solo escucho voces apagadas de algunas clases, lo que me hace suponer que son otros clubes en sus actividades extraescolares."
    "..."
    "Veo a una chica sentada en un banco del pasillo, mirando su móvil."
    "Decido acercarme para hablar con ella."
    mc "Eh... hola, ¿puedo--{w=0.20}{nw}"
    stu "Tengo novio, no me interesa."
    "Estupendo."
    mc "¡Pero si ni siquiera he llegado a preguntarte algo!"
    stu "HE DICHO."
    stu "QUE TENGO."
    stu "NOVIO."
    stu "¿Es que no lo entiendes o quieres que te dé una patada en los huevos?"
    mc "Ehmmm... no, gracias, estoy bien."
    stu "Joder..."
    stu "Los tíos sois todos iguales."
    "Decido seguir mi camino y no mirar atrás."

    show bg corridor
    with wiperight_scene

    "After my first attempt, which I'll call unusual, I decide to approach some high school students I find wandering the hallway, who all end up saying no."
    "I bet it's probably the same on Monika and Sayori's side."

    show bg corridor
    with dissolve_scene_full

    "I guess I'll go back to the club. I think Monika and Sayori must be back already."
    mc "Huh?"
    "When I arrive in front of the club, I can see a new face."
    "I can see a tall girl with long purple hair reading a book on a desk next to the window with Sayori."
    "Sayori notices me behind the window putting on her biggest smile, I can start hear her screaming and snorting from the hallway."
    s "{i}Guys, the president is here!!{/i}"

    stop music fadeout 3.0

    mc "Geez... Why does she have to scream like that?"
    "I take a long sigh before opening the door going inside the club."

    play sound closet_open
    show bg club_day
    with wipeleft_scene
    play music t3

    "Monika is heading towards me without further ado."

    show monika base uniform happ rhip at l11

    m "Ah, [player]!"

    $ renpy.music.set_pause(True, channel="music")

    show monika base uniform neut ldown rdown me

    m "What took you so long?"

    $ renpy.music.set_pause(False, channel="music")
    m "We were beginning to wonder if something had happened to you."
    mc "I'm so sorry!"
    mc "I didn't check the time when we left!"
    mc "I was just... busy, if you can call it that."

    show monika lean uniform neut m1

    m "Don't worry. Now that you're here, we can start the introductions!"
    "The tall girl with long purple hair gets up from her chair shyly, walking towards us."

    show monika base uniform happ at t21
    show yuri base uniform happ at t22
    y "So you're [player], the club president?"
    "I nod briefly."
    mc "That's right."
    y "A pleasure to meet you."
    mc "Nice to meet you too."
    "I didn't notice her on the way in, but a much smaller figure comes out of the closet, joining the rest of the group."
    "What was she doing in the closet?"

    show monika base uniform happ at t31
    show yuri base uniform happ at t32
    show natsuki base uniform b1d mi rhip lhip at f33

    n "Seriously, the president is a boy?!"
    n "I thought this was a girls-only club!"
    n "The atmosphere will be really bad in this club."
    mc "Ah... Thanks."

    show natsuki base uniform md rdown ldown at t43
    show sayori base uniform e1b b1b mc at t44
    show monika base uniform happ at t41
    show yuri base uniform happ at t42

    s "Natsuki..."

    show sayori base uniform e1b b1b mc at t44
    show yuri base uniform neut rup lup mf e4a b1c

    y "So you're Natsuki..."

    $ n_name = "Natsuki"

    show monika at thide
    show sayori at thide
    show yuri at thide
    hide monika
    hide yuri
    hide sayori
    show natsuki cross uniform neut fta at t11

    n "Hmpff."
    "The girl with the sour demeanor seems to be called Natsuki, according to Sayori."
    "Sayori approaches my ear whispering something to me."
    s "{i}Don't worry, just ignore her when she gets like this.{/i}"

    show natsuki cross uniform neut fta at t22
    show sayori base uniform happ rup ldown at t21

    s "Anyway!"
    s "[player], here's Natsuki, a girl who is always full of energy!"

    show natsuki 1g at t32
    show monika base uniform happ rhip at t33
    show sayori base uniform rup ldown at t31

    m "And for finish, let's me introduce you Yuri."
    m "We found her with Sayori at the school library, and believe me, she will be a valuable asset for the Literature Club."

    $ y_name = "Yuri"
    show natsuki 1g at t42
    show monika base uniform happ rhip at t43
    show sayori base uniform rup ldown at t41
    show yuri shy uniform happ m1 e2 b2 at t44

    y "Don't... say such things like that..."
    "Yuri looks away, and I can already get an idea that she's a person who seems quite shy."
    mc "..."
    "I'm speechless."
    "My club is full of..."
    "Girls?"
    "I don't know if it's a coincidence, but I'm not going to complain about it..."
    "...because they are all--!{w=0.02}{nw}"

    show yuri at thide
    show monika at thide
    show sayori at thide
    hide yuri
    hide monika
    hide sayori
    show natsuki base uniform neut mg b1a at t11

    n "Why are you staring at us like that?"

    show natsuki cross uniform neut mi b1d

    n "If you want to say something out, go ahead."
    mc "... Excuse me..."

    show natsuki at thide
    hide natsuki

    "Well... that's pretty blunt."
    "Getting back on track, I take a short breath."

    show monika base uniform happ rhip at t44
    show yuri base uniform happ at t43
    show sayori base uniform happ at t42
    show natsuki base uniform neut at t41

    mc "Okay everyone!"
    mc "Since we have two new members, I propose that we go settle in and get to know each other a little better!"
    "With the help of all the girls, we're rearranging the few tables we moved earlier, so that it become a bigger table."

    show yuri at thide
    show natsuki at thide
    show monika at thide
    show sayori at thide
    hide natsuki
    hide yuri
    hide monika
    hide sayori

    "Before we settle down, Sayori, with an excited look speak up."

    show sayori base uniform neut lup rup mc e4b at t21

    s "I'll go get the cupcakes!"

    show natsuki base uniform neut lhip mi b1d at t22

    n "Hey! I bought them, so I gonna get them!"

    show sayori 5a at s21

    s "I'm sorry, I just got a little excited for a moment ehehe..."
    s 5b "And I'm hungry too..."

    show sayori at thide
    hide sayori

    mc "Eh, cupcakes?"

    show natsuki base uniform neut rhip mh b1c at t11

    n "Yeah, is that a problem?"
    mc "Oh no, just be careful not to get it everywhere, I hold the responsibility of keeping this room as clean as possible."

    show natsuki at thide
    hide natsuki
    show monika base uniform happ rhip at t11

    m "If you want [player], I could help you clean up the clubroom at the end of each session."
    mc "Would you mind, Monika?"
    mc "I wouldn't really like to borrow any of your free time."
    m happ e4b "No no! Don't worry, I don't mind!"
    mc "Very well, then thanks to you."

    show monika at thide
    hide monika

    "During our little chat, Natsuki proudly returns to the table with a tray covered with a foil wrapping the top of the tray in her hands."
    "She sets the tray on the table, still keeping one hand on the foil, ready to remove it."

    show natsuki base uniform neut rhip mo e4b at t32

    n "Are you all ready?"
    "We all nod in agreement."
    n "Tadaaaaaaaaaaaaa!"

    show monika base uniform neut me at t31
    show sayori base uniform neut nobl lup rup ml e2a b1a at t33

    ms "Woooaaahh!"
    "Removing the foil, we can see about ten chocolate cupcakes, iced with white frosting."
    "There is a slight decoration done on the frosting which is made with little sprinkles of different colors to give a rainbow effect."

    show natsuki cross uniform e1a mc

    n "What are you waiting for? Get some!"
    show natsuki cross uniform ma
    "Sayori is the first one to take a cupcake. Followed by Monika and Yuri. I'm the last one to serve myself."

    show sayori base uniform neut lup rup mc e4b

    s "Schoooooooooooooooo goooood~!"
    "Sayori is already talking with her mouth full, in a short time, she has already stuffed a lot of frosting around her mouth."
    "Without noticing it, she has already messed up the table with her fingers full of icing."
    show monika base uniform neut ma rhip
    show natsuki base uniform mc rhip

    n "Hehehe, it's too bad for the club that I didn't make these, otherwise they would have been ten times better than these."
    n "They were made by the school bakery."
    mc "Really? You like to bake Natsuki?"
    show natsuki cross uniform neut mc

    n "Of course, it's a tradition in my family."
    show natsuki cross uniform ma
    mc "Oh right, that's really nice."
    "I twirl the cupcake around my fingers, looking for a good angle to take a bite without getting it all over myself."

    show sayori at thide
    show monika at thide
    hide monika
    hide sayori
    show natsuki base uniform neut mg b1a at t11

    "I can't help but notice that Natsuki keeps glancing at me over and over."
    "Is she waiting for me to decide to take a bite?"
    "Finally, I decide to take a bite."
    "!!!"
    "I didn't think so, but the cupcake is actually delicious."
    "The chocolate cupcake base is very sweet and combines with the flavor of the frosting, which is vanilla I would assume, gives a perfect balance between the two flavors."
    mc "This is damn good!"
    mc "Thank you for bought these cupcakes Natsuki."

    show natsuki cross uniform neut mh b1f

    n "Why are you thanking me?"

    show natsuki cross uniform neut blaw mh e1b b1d at s11

    n "It's not like I bought them for you and your club.. dummy.."
    mc "Huh?"
    mc "But didn't you say you bought them for--{w=0.10}{nw}"

    show natsuki base uniform neut ldown fs m3 e4 b2 at h11

    n "Well, maybe!"
    n "I probably bought them for this occasion!"

    show natsuki 5q

    n "But not for... you.. {w=0.4} the club... dummy."
    mc "Ummh.. okay, okay..."

    show natsuki at thide
    hide natsuki

    "I decide to give up falling on Natsuki's strange logic."

    show yuri base uniform happ at t11

    y "Otherwise [player]... What do you like to read?"
    mc "Ah.. well.."
    "I haven't been asked that question in a while."
    "Considering how much my book collection in my room has grown in the last few years, I'm afraid if I say everything, we can stay here until tomorrow morning."
    mc "... I read a little bit of everything... but last weekend I started reading a little horror book."

    show yuri base uniform happ ma e1b b1b rup

    y "A great and wise reader like myself I see..."
    mc "Yes, you can say it like that."
    "I notice Yuri smiles discreetly."

    show yuri base uniform happ ma e1b b1b rdown at t21
    show monika base uniform happ lpoint ma e1a b1a at t22

    m "Ah, I have started reading a horror book lately, too."
    mc "Really, Monika?"
    mc "That surprises me a lot coming from you."

    show monika base uniform happ lpoint rhip e4b

    m "Ahahaha, it's true that I look like someone who doesn't read those genres."

    show monika base uniform happ ldown e1a rhip

    m "But that was a few years ago, and I've had an urge to try new things."


    show monika lean uniform happ ma

    m "After all, wouldn't life be a little boring if every day was the same thing?"
    "Monika smiles at me sweetly."



    mc "Oh well yeah... you're right about that."
    show monika at thide
    hide monika
    show yuri base uniform b1a e1a ma at t11
    mc "So Yuri, what do you like to read?"
    show yuri 1e
    y "Me? Let's see..."
    y 2g "Usually, I like to read novels that tell a complex and very deep fantasy story everyday."
    y 2l "The level of creativity and quality of the written stories always impresses me.."
    y 1b "But you know, I like to read a little bit of everything too."
    y 1a "I also started few weeks ago reading horror books, too."
    y 2a "Now I'm on a book called « Portrait of Marakov »."
    mc "I've never heard of it..."
    y 1a "The author of this book is not well known around the world either."
    mc "What is the story about?"
    y 3i "In a nutshell... this is the story of a high school girl who moves in to the home of her long-lost sister..."
    y 3f "But as soon as she moves in, her life suddenly turns upside down and starts to become completely strange."
    y "She is suddenly targeted by people who have escaped from a prison where human experiments are taking place inside."
    y "However, while her life is in danger, she is desperate to be trusted, but no matter what she does, her relationships always end up falling apart."
    mc "Ah yes, it's a rather unusual story, but it still sounds interesting."
    show yuri 3f at t22
    show natsuki cross uniform neut mg e1b b1e at t21
    n "Ughh... I hate horror."
    y 2e "Oh why's that?"
    n "It's because..."
    show natsuki cross uniform awkw b1a e1a
    "Natsuki looks at me briefly, holding back from saying something."
    n cross uniform neut mg e1b b1e "... Nevermind."
    show yuri at t32
    show natsuki at t31
    show monika base uniform happ rhip at t33
    m "It's true that you prefer to write cute things, isn't it Natsuki?"
    show natsuki base uniform neut blaw ldown rdown mm e2a b1e at h31
    n "Uuugh... What?!"
    n "What makes you say that??"
    m "Well, when we were going to the club after we met you, you dropped a piece of paper from your bag, specifically a poem called..."
    show natsuki base uniform neut blaw ldown rdown mi b1d at h31
    n "Don't say another word!"
    show natsuki base uniform neut blaw ldown rdown ml e4c b1d at h31
    n "And give it back to me!"
    show monika base uniform neut ldown rhip ma e4b b1a
    m "Very well~"
    show yuri at thide
    show monika at thide
    show natsuki at thide
    hide monika
    hide yuri
    hide natsuki
    "Monika discreetly slips a small paper she took out of her blazer's pocket, she folds it in a way that we can't see the text written on it and hands it to Natsuki."
    "Natsuki takes it and puts it in a safe place."

    mc "Natsuki, you write poems?"
    show natsuki 5h at t11
    n "Well, let's say I do..."
    n "Why do you ask?"
    mc "Well, I think it's completely incredible!"
    mc "Why not share them with everyone here?"
    mc "It might be nice to--"
    show natsuki 1o at h11
    n "No! ..No!"
    "In fright, Natsuki briefly avert her eyes to avoid any eye contact."
    mc "Why?"
    show natsuki 5s at s11
    n "You... you wouldn't like them..."
    mc "Ah.. you don't trust sharing them I see?"
    show natsuki 5s at t21
    show yuri base uniform neut lup rdown mf e4a b1c at t22
    y "I understand her fear..."
    y "Sharing your own writing is a real challenge..."
    y "If we write, it is basically to describe something personal about ourselves."
    show yuri base uniform neut lup rup mf e4a b1c
    y "Sharing one's own work is a real test to oneself, it means accepting criticism from other people."
    y "To open yourself to others, to expose your weaknesses and even to show the deepest recesses of your heart.."
    mc "Do you also have experience in writing?"
    mc "Maybe you can share your writing with Natsuki to give Natsuki a little more confidence to share her poem, don't you think?"
    show yuri 2o at s22
    y "Ah... uh... I..."
    show natsuki 5s at t31
    show yuri at t32
    show monika base uniform neut awkw lpoint ma e1b b2c at t33
    m "I think it's the same for Yuri.."
    show natsuki 5s at t41
    show yuri at t42
    show monika base uniform neut awkw lpoint ma e1b b2c at t43
    show sayori base uniform neut e1b b1b md at t44
    s "Awwww... I wanted to read everyone's poems.."
    show natsuki at thide
    show yuri at thide
    show monika at thide
    show sayori at thide
    hide natsuki
    hide yuri
    hide monika
    hide sayori
    "We stay in silence for a while."
    "Reading everyone's poems..."
    "I think I have a little good idea for the first club activity."
    mc "Okay everyone!"
    mc "I have an idea."
    show natsuki base uniform neut nobl mg e1a at t21
    show yuri 2e at t22
    ny "...?"
    "Natsuki and Yuri look at me with an interogative look."
    mc "After this little discussion which was very nice to listen to, for the first activity of the club, I propose that we all go home:"
    mc "And that everyone writes their poem under their own pen and that we all share them tomorrow for the next club meeting!"
    mc "That way everyone is on equal footing!"
    show natsuki cross uniform e1b b1d neut md awkw at t31
    show yuri base uniform flus awkw rup at t32
    show sayori base uniform happ nobl lup rup mc e4b b1a at h33
    s "Yaaaay! Let's do that!"
    show sayori base uniform happ nobl lup rup mc e4b b1a at t43
    show monika base uniform happ rhip at t44
    show natsuki cross uniform e1b b1d neut md awkw at t41
    show yuri base uniform flus awkw mk rup at t42
    m "That's a very good decision, [player]!"
    n "Um..."
    y "I..."
    mc "And that now we have five members... I think it will be a very good activity to learn about yourselves and also learn a little bit about each other!"
    mc "I think now we can-..{w=0.08}{nw}"
    show yuri at thide
    show monika at thide
    show sayori at thide
    hide yuri
    hide monika
    hide sayori
    show natsuki base uniform e4c b1a ml blaw at h11
    n "Wait a minute!"
    mc "...?"
    show natsuki cross uniform neut n3 mg e1b b1d nobl
    n "I didn't sign up for this!"
    show natsuki base uniform neut n3 mg e1a b1d
    n "Even though I bought cupcakes, I didn't want to join to share-.."
    "I unintentionally cut off Natsuki's talk."
    mc "But.. but..."
    "Why did I think it was a good idea?"
    show natsuki at t11
    show yuri 1w at t41
    y "Sorry, I didn't mean to..."
    show natsuki at t42
    show sayori 3k at t43
    show monika 1f at t44
    ms "Natsuki..."
    show natsuki cross uniform neut awkw mg e1a b1f at s42
    n "You..."
    "Caught off guard Natsuki, looks at the four of us."
    show natsuki cross uniform neut awkw mg e1b b1f
    n "I..."
    show natsuki 4x at t42
    n "Okay, okay, okay!"
    n "I've changed my mind, I'm joining the club."
    show natsuki cross uniform e1b mm b1e blaw at s42
    show monika base uniform happ b1b
    show sayori base uniform happ lup b1b
    show yuri base uniform happ b1b
    "All four of us look at Natsuki with a relieved face."
    show sayori 4r at h43
    s "Yaaaaaaaaaay! You're the best Natsuki!"
    show sayori 4r behind natsuki at t42
    show yuri base uniform happ b1a
    "Sayori suddenly gets up from her chair to come and stand behind Natsuki, wrapping her in her arms, hopping."
    show natsuki base uniform neut fs m3 e4 b2
    show yuri base uniform e4b mb
    show monika base uniform e4b b1a mb
    n "I get it, I get it, raah!"
    show sayori base uniform happ at t43
    show yuri base uniform e1a ma
    show monika base uniform happ b1a e1a
    m "You had really scared me for a while Natsuki..."
    mc "Then it's official!"
    show natsuki 1g
    mc "Welcome to the club Natsuki!"
    mc "And welcome to you too, Yuri."
    show yuri shy uniform happ e2 m1
    y "T-Thank you..."
    show monika at thide
    show sayori at thide
    show yuri at thide
    show natsuki at thide
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    mc "So to resume, I think we can end the first and official meeting on a good note!"
    mc "As president, it is my duty to do everything I can to make sure that everyone gets along well at the club!"
    mc "I would not tolerate the single deviation if by misfortune it if would happen."
    mc "On the other hand..."
    mc "If you have any suggestions for improvement or even requests for the club, please feel free to ask!"
    mc "I will take note of it and will do my best that it can be done!"
    mc "Please don't hesitate..."
    mc "I don't bite."
    show monika lean uniform neut m1 at t11
    m "My, my [player]. What a diplomatic man! I am truly impressed."
    "Damn it Monika... please stop teasing me like that, I'll end up red-faced if you continue."
    show monika at thide
    hide monika
    mc "Ahaha... I-I am really happy, the way the club is turning out for today!"
    show monika base uniform happ at t21
    show sayori base uniform happ at t22
    mc "By the way Monika and Sayori, I'd like to talk to you for a few moments if possible."
    show monika base uniform happ at t41
    show sayori base uniform happ at t42
    show natsuki base uniform at t43
    show yuri shy uniform happ m1 e2 at t44
    mc "Everyone remember the assignment for tomorrow?"
    mc "Bring back a poem for tomorrow so we can share them!"
    mc "On that note, I can close the session, you can all go home!"
    mc "Have a good evening everyone, hope to see you tomorrow!"
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    with wiperight
    "Natsuki and Yuri get up from their chairs to pick up their things."
    show yuri base uniform neut ma at t11
    y "Alright, I think I'll go.. the library will close soon because it's already getting late..."
    y "I better hurry up or I'll be too late."
    y "See you all tomorrow."
    mc "See you tomorrow, Yuri!"
    show yuri base uniform neut lup rup ma e4b
    y "See you tomorrow, [player]."
    "Yuri smiles happily at me before she starts to leave."
    show yuri at lhide
    hide yuri
    "..."
    show natsuki base uniform happ lhip at t11
    n "Come on, I'm going too, see you tomorrow, losers!"
    mc "See you tomorrow Natsuki."
    "Natsuki leaves the room, closing the door violently."
    show natsuki at lhide
    hide natsuki
    stop music fadeout 2.0
    "A slight silence settles in the club room, with Sayori and Monika still inside."
    show monika base uniform neut rhip me at t11
    m "So, [player]?"
    m "What did you want to talk to us about?"
    mc "Oh yeah.."
    mc "Well... thanks to the both of you."
    mc "Thank you for what you did in such a short time."
    show monika base uniform neut ma b1b
    m "Oh, don't worry [player]... we're happy to help you."
    mc "Yes! But I mean... not even four hours ago, more or less, I was alone... and now here we are."
    mc "So thank you for everything, I won't let you down believe me."
    "Monika lets out a small smile."
    show sayori base uniform happ lup at t22
    show monika base uniform happ b1a mb at t21
    s "I'm sure you'll be a good president [player]!"
    mc "Ahahaha thank you Sayori, I will do my best to make this club the best I can."
    mc "By the way, I am sorry about earlier."
    s "Oh sorry for what?"
    mc "For being a little sour to you about my questioning your motivation for literature."
    show sayori base uniform happ b1b
    s "I don't blame you [player], don't worry about it, it's okay that you were thinking about that."
    mc "Ah thank you...that's a relief to me."
    mc "Thank you for listening to me, now you can leave, I will tidy up and clean up the room to get it in shape after this cupcake tasting."
    show monika base uniform neut ma rdown
    m "I'll help you [player], remember what I said."
    mc "Oh yeah, I almost forgot, my bad."
    s "Can I come and help you too?"
    mc "Sure Sayori!"
    show sayori base uniform neut lup rup mc e4b b1a
    s "Yaaaaaay!"
    mc "I've never seen someone so happy to clean a room."
    mc "Come on, let's get to work so we can all go home!"
    show monika at thide
    show sayori at thide
    hide monika
    hide sayori
    "Sayori, Monika and I, start putting the desks back in their original places."
    "Since it's the three of us, the cleaning of the room goes by pretty fast."
    show bg club_day1
    with wiperight_scene
    "After about five or six minutes of cleaning, the clubroom looks like new."
    mc "Thank you so much both of you. You were a great help."
    mc "If you weren't there, it would have taken me longer, ahaha."
    show sayori base uniform happ lup ma at t11
    s "Monika, I'll wait for you outside while you talk quickly with [player]."
    s "See you tomorrow, [player]!"
    mc "See you tomorrow, Sayori!"
    show sayori at lhide
    hide sayori
    "Sayori puts her bag on her back and leaves the clubroom."
    play sound closet_close
    play music her
    "She gently closes the door behind her."
    mc "So Monika..."
    show monika base uniform neut ma at t11
    m "I'm listening [player], what did you want to ask me?"
    mc "Look, I know this is going to sound sudden but..."
    mc "I know you left the debate club recently, and maybe you're tired of having responsibilities but is it--{w=0.40}{nw}"
    show monika base uniform neut me b1b at t11
    m "Wait a minute, [player]."
    "Monika suddenly cuts me off from my speech."
    m "You wouldn't by any chance ask me to be your vice president?"
    mc "Ummm!"
    "I'm scratching my head nervously, I can't help but laugh nervously."
    mc "Sort of!"
    mc "If... if you don't want to, I'll understand and I won't blame you.."
    mc "And then..."
    show monika base uniform neut rhip me b1b at t11
    m "[player]..."
    m "You know that..."
    show monika base uniform neut awkw ldown rhip mb e1b b1b at s11
    m "Well..."
    mc "..."
    "Well, I think I know the answer."
    "Also what kind of person am I to have thought she would accept?"
    show monika base uniform neut rhip ma e4b b1a
    m "That... I'm agreeing to be your vice president!"
    "Did I hear that right?"
    mc "What, really?"
    show monika 1a
    m "Really."
    mc "Ahahaha... you really scared me for a moment."
    mc "When I saw your expression change all of a sudden I thought it was over.."
    show monika 5a
    m "Ehehehe, I'm a good actress aren't I?"
    show monika base uniform neut ma e4b
    m "That said, the look on your face was funny to see, ahaha!"
    m "I don't regret putting you in doubt."
    mc "Blah, blah, blah. Who's goung to be laughing last, Monika?"
    show monika lean uniform m2
    m "Ohhh, is that a little threat?"
    mc "Ahaha, yeah, clearly."
    show monika base uniform anno rhip ma e1d b1c
    m "Don't worry, I'm preparing for any possible attack from you, [player]~"
    show monika base uniform neut ma e4b b1a
    "We both share a laugh."
    mc "But seriously, I'm proud to have you as my vice president, Monika."
    mc "You and I, I'm sure we can give the literature club a good place in the school."
    show monika base uniform e1a mb b1a
    m "I'm sure, we will too!"
    mc "Come on, you can go Monika, thanks for this little talk."
    mc "I'll see you tomorrow."
    show monika lean uniform ma
    m "Same here, [player]. See you tomorrow!"
    hide monika
    with wipeleft
    "Monika collects her things before going to join Sayori, who is waiting for her outside."
    play sound closet_close
    stop music fadeout 2.0
    "It doesn't take long before the room is plunged into silence again."
    "But now it's not just any silence."
    "It's not the same silence I've known for the past few days."
    "When I was alone in the club."
    "I sit down on a chair, resting my head on the desk."
    mc "-sigh- What a great day."
    "I look at my phone."
    "{i}6:10 PM{/i}"
    "It's time to go."
    "I pick up my bag, slipping it onto my back."
    mc "Mmmmh?"
    "I see the abandoned flyers on the table."
    "I sigh."
    mc "I don't really need them anymore."
    "I pick up the flyers, crushing them with both hands to form a paper ball, and throwing them at the trash."
    "I head for the door, place one foot outside the club when suddenly a thought pops into my head."
    mc "Oh, wait a minute..."
    "I remember that Natsuki was in the closet when I came back."
    show bg closet
    with wipeleft_scene
    "I can't help but be curious but I decide to head to the closet."
    "I open the closet door coming to look everywhere inside."
    mc "Eh???"
    "I see three manga collection boxes on the shelf, which made a good mess in the closet."
    mc "What the hell is this doing here?"
    "I pull out a random book."
    mc "Parfait Girls Volume 2...?"
    "The cover shows four girls with exaggerated positions dressed in very colorful clothes that can be likened to heroines."
    mc "..."
    mc "But it's manga!"
    mc "It's not really my favorite genre but there are some that are very good to read."
    mc "{i}-sigh-{/i}... this doesn't belong there though."
    "I look up at the top of the shelf giving me an idea."
    mc "Mmmh, I could put them up there, it shouldn't bother too much."
    "I put the book back in its place, taking the cardboard on both sides."
    "I easily lift the box coming to put it on top of the shelf."
    "My height, which is quite decent compared to the height of the shelf, forces me to stand on my toes."
    "And I repeat the same operation for the other two boxes."
    "..."
    "..."
    mc "Phew... that's now done."
    mc "Now I just have to put away this mess caused by Natsuki, I guess..."
    "I start to put the books back in their original place, I try my best to put the shelf back in order as if it had never been touched."
    "Finally, after a little while, I manage to rearrange the shelf."
    mc "Perfect!"
    show bg club_day1
    with wiperight_scene
    play sound closet_close
    "I close the closet doors, heading for the club door."
    show bg corridor_e
    with wiperight_scene
    "I lock the door and start walking outside the school."
    mc "Now time to go home and write a poem."
    show bg kitchen
    with dissolve_scene_full
    "Once I get home, I head straight to my room."
    show bg bedroom
    with wiperight_scene
    mc "Well then..."
    "It's time to write a poem."
    "I sit down in my chair, taking a pen and start to write."
    show bg black
    with dissolve_scene_full
    pause 0.5
    show text "Fifteen minutes later..."
    pause 2
    hide text
    show bg bedroom
    with dissolve_scene_full
    mc "Ah! {w=0.75} No..."
    "I set the paper aside and grab another sheet and try again."
    show bg bedroom
    stop music fadeout 2.0
    with dissolve_scene_full
    pause 1
    call showpoem (poem_p1, music=False) from _call_showpoem
    mc "Phew. It's been a long time since I've written any poems, but I think this is decent."
    mc "I can't wait to see what they think about it tomorrow."
    "With a small smile on the corner of my lip, I put my poem in my bag."
    mc "Eh... {i}-yawn-{/i}... What time is it now..?"
    "I'm looking at the time displayed digitally on the electronic alarm clock sitting on the nightstand."
    "{i}10:10 PM{/i}"
    mc "It's okay, I still have time to take a shower and eat something quickly."
    show bg bedroom_n
    with dissolve_scene_full
    "After I finish my evening routine, I land in my bed."
    mc "It feels good to be lying in this bed..."
    mc "... Tomorrow is going to be a big day."
    "I slowly let myself fall asleep getting caught in the arms of morpheus."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
