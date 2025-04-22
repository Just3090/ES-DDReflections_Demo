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
    mc "¡Ah, genial!"
    mc "Así que, de nuevo, gracias a las dos por haberos unido a mi club, me hace muy feliz, más de lo que podéis imaginar."
    mc "Aunque me habría gustado que las cosas fueran un poco {i}diferentes.{/i} {w=0.3} Ajajajaja."
    show sayori base uniform neut mb rup
    s "No te preocupes, soy mejor que tú cuando se trata de dormir. ¡Estoy segura que hasta podría sustituirte!"
    mc "¿Sustituirme...?"
    mc "¿De qué hablas?"
    show sayori base uniform e1b b1b mc blaw
    s "Emmmm..."
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
    "¿Su mejor amiga?"
    "Estoy sorprendido. Llevamos años conociéndonos y nunca me había hablado de ella antes..."
    m "Siempre se esfuerza al máximo en las cosas que hace y que realmente le importan, [player]."
    m "Es como un rayo de sol andante."

    show sayori base uniform neut blaw rup mc e1b b2c

    s "No digas eso, Monika... ¡Solo quiero hacer que todo el mundo sea feliz!"
    mc "Supongo que podría escucharte con los ojos cerrados, Monika."
    mc "Después de todo, tienes experiencia en los clubes."
    mc "Sé que ahora el club está empezando y parece obvio lo que te estoy contando."
    mc "Pero lo que quiero decir es que, de momento, no tenemos actividades planeadas para el club. ¡Cuando seamos más, empezaré a pensar en ello!"

    show sayori base uniform happ lup e1a b1a ma rdown nobl

    m "No te preocupes, [player]."
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
    mc "Ah... vale, de acuerdo..."
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

    "Después de mi primer intento, que llamaría inusual, decido acercarme a unos estudiantes de secundaria que encuentro deambulando por el pasillo, pero todos terminan diciendo 'no'."
    "Apuesto a que probablemente sea lo mismo para Monika y Sayori."

    show bg corridor
    with dissolve_scene_full

    "Supongo que volveré al club. Creo que Monika y Sayori deben haber vuelto."
    mc "¿Qué?"
    "Cuando llego frente al club, veo una cara nueva."
    "Puedo ver a una chica alta con el pelo largo y púrpura leyendo un libro en un escritorio junto a la ventana con Sayori."
    "Sayori se da cuenta de mi presencia detrás de la ventana y pone su sonrisa más grande, puedo empezar a oírla gritar y resoplar desde el pasillo."
    s "{i}¡¡CHICOS, EL PRESIDENTE ESTÁ AQUÍ!!{/i}"

    stop music fadeout 3.0

    mc "Joder... ¿Por qué tiene que gritar así?"
    "Tomo un largo suspiro antes de abrir la puerta y entrar al club."

    play sound closet_open
    show bg club_day
    with wipeleft_scene
    play music t3

    "Monika se dirige hacia mí sin más preámbulos."

    show monika base uniform happ rhip at l11

    m "¡Ah, [player]!"

    $ renpy.music.set_pause(True, channel="music")

    show monika base uniform neut ldown rdown me

    m "¿Por qué has tardado tanto?"

    $ renpy.music.set_pause(False, channel="music")
    m "Ya pensábamos que te había pasado algo."
    mc "Lo siento mucho."
    mc "No me fijé en la hora al salir."
    mc "Solo estaba... atareado, si así se le puede decir."

    show monika lean uniform neut m1

    m "No te preocupes. Ahora que estás aquí, ¡podemos empezar las presentaciones!"
    "La chica alta con el pelo largo y púrpura se levanta de su silla tímidamente, caminando hacia nosotros."

    show monika base uniform happ at t21
    show yuri base uniform happ at t22
    y "¿Eres [player], el presidente del club?"
    "Asiento con brevedad."
    mc "Así es."
    y "Es un placer conocerte."
    mc "El gusto es mío."
    "No la había notado al entrar, pero una figura enana sale del armario y se une al resto del grupo."
    "¿Qué hacía ella en el armario?"

    show monika base uniform happ at t31
    show yuri base uniform happ at t32
    show natsuki base uniform b1d mi rhip lhip at f33

    n "¿En serio? ¡¿El presidente es un chico?!"
    n "¡Pensé que era un club 'exclusivo' de chicas!"
    n "El ambiente será pésimo en este club."
    mc "Emm... Gracias."

    show natsuki base uniform md rdown ldown at t43
    show sayori base uniform e1b b1b mc at t44
    show monika base uniform happ at t41
    show yuri base uniform happ at t42

    s "Natsuki..."

    show sayori base uniform e1b b1b mc at t44
    show yuri base uniform neut rup lup mf e4a b1c

    y "Así que eres Natsuki..."

    $ n_name = "Natsuki"

    show monika at thide
    show sayori at thide
    show yuri at thide
    hide monika
    hide yuri
    hide sayori
    show natsuki cross uniform neut fta at t11

    n "Hm."
    "La chica con la actitud agria parece llamarse Natsuki, según Sayori."
    "Sayori se acerca a mi oído y me susurra algo."
    s "{i}No te preocupes, ignórala cuando se pone así.{/i}"

    show natsuki cross uniform neut fta at t22
    show sayori base uniform happ rup ldown at t21

    s "¡Aún así!"
    s "[player], ¡esta es Natsuki, una chica que siempre está llena de energía!"

    show natsuki 1g at t32
    show monika base uniform happ rhip at t33
    show sayori base uniform rup ldown at t31

    m "Y por último, os presento a Yuri."
    m "La encontramos con Sayori en la biblioteca del instituto, así que creedme: será un valioso activo para el Club de Literatura."

    $ y_name = "Yuri"
    show natsuki 1g at t42
    show monika base uniform happ rhip at t43
    show sayori base uniform rup ldown at t41
    show yuri shy uniform happ m1 e2 b2 at t44

    y "No digas... esas cosas..."
    "Yuri mira a otro lado, y puedo hacerme una idea de que es una persona bastante tímida."
    mc "..."
    "Estoy atónito."
    "Mi club está lleno de..."
    "¿Chicas?"
    "No sé si es casualidad o algo, pero no me voy a quejar..."
    "...¡porque es que son muy mo--!{w=0.02}{nw}"

    show yuri at thide
    show monika at thide
    show sayori at thide
    hide yuri
    hide monika
    hide sayori
    show natsuki base uniform neut mg b1a at t11

    n "¿Por qué nos miras de esa manera?"

    show natsuki cross uniform neut mi b1d

    n "Si quieres decir algo, adelante."
    mc "... Perdón..."

    show natsuki at thide
    hide natsuki

    "Bueno... ha sido bastante directa."
    "Volviendo al tema, tomo un pequeño respiro."

    show monika base uniform happ rhip at t44
    show yuri base uniform happ at t43
    show sayori base uniform happ at t42
    show natsuki base uniform neut at t41

    mc "¡Vale, compis!"
    mc "Como tenemos dos nuevos miembros, propongo que nos acomodemos y nos conozcamos un poco mejor."
    "Con la ayuda de todas las chicas, estamos reorganizando las mesas que movimos anteriormente, para que ahora formen una mesa más grande."

    show yuri at thide
    show natsuki at thide
    show monika at thide
    show sayori at thide
    hide natsuki
    hide yuri
    hide monika
    hide sayori

    "Antes de sentarnos, Sayori, con una mirada emocionada, dice algo en alto."

    show sayori base uniform neut lup rup mc e4b at t21

    s "¡Voy a por los cupcakes!"

    show natsuki base uniform neut lhip mi b1d at t22

    n "¡Oye! ¡Yo los compré, así que los traigo yo!"

    show sayori 5a at s21

    s "Perdón, me emocioné por un momento, jejeje..."
    s 5b "Y tengo mucha hambre también..."

    show sayori at thide
    hide sayori

    mc "¿Qué, cupcakes?"

    show natsuki base uniform neut rhip mh b1c at t11

    n "Sí, ¿pasa algo?"
    mc "Claro que no, pero ten cuidado de no ensuciarlo todo. Soy el responsable de mantener este aula lo más limpia posible."

    show natsuki at thide
    hide natsuki
    show monika base uniform happ rhip at t11

    m "Si quieres, [player], te puedo ayudar a limpiar el club el final de cada reunión."
    mc "¿No te importaría, Monika?"
    mc "No es de mi agrado robarte tu tiempo libre."
    m happ e4b "¡No no! ¡No te preocupes, no me importa!"
    mc "Muy bien, entonces... muchísimas gracias."

    show monika at thide
    hide monika

    "Durante nuestra pequeña charla, Natsuki regresa a la mesa con una bandeja cubierta con papel de aluminio."
    "Coloca la bandeja en la mesa, manteniendo una mano en el papel, lista para quitarlo."

    show natsuki base uniform neut rhip mo e4b at t32

    n "¿Estáis listos?"
    "Asentimos en señal de acuerdo"
    n "¡Tacháaaaaaaaaan!"

    show monika base uniform neut me at t31
    show sayori base uniform neut nobl lup rup ml e2a b1a at t33

    ms "¡Halaaaaaa!"
    "Al quitar el papel de aluminio, vemos unos diez pastelitos de chocolate."
    "Están decorados con glaseado blanco y algunas chispas de colores que le dan un efecto arcoíris."

    show natsuki cross uniform e1a mc

    n "¿A qué esperáis? ¡Coged uno!"
    show natsuki cross uniform ma
    "Sayori es la primera en ir a por un cupcake. Monika y Yuri le siguen poco después. Yo soy el último en coger uno."

    show sayori base uniform neut lup rup mc e4b

    s "¡Eshtá bueníshimooooooooooo~!"
    "Sayori ya está hablando con la boca llena, y en poco tiempo, tiene todo el glaseado alrededor de la misma."
    "Sin darse cuenta, ha ensuciado la mesa con sus dedos llenos de glaseado."
    show monika base uniform neut ma rhip
    show natsuki base uniform mc rhip

    n "Jajaja, es una lástima que no los haya hecho yo, habrían sido diez veces mejores."
    n "Los hicieron en la pastelería de la escuela."
    mc "¿En serio? ¿Te gusta hornear, Natsuki?"
    show natsuki cross uniform neut mc

    n "¡Claro! Es una tradición familiar."
    show natsuki cross uniform ma
    mc "Ah, es genial."
    "Giro el pastelito entre mis dedos, buscando un buen ángulo para darle un bocado sin ensuciarme."

    show sayori at thide
    show monika at thide
    hide monika
    hide sayori
    show natsuki base uniform neut mg b1a at t11

    "No puedo evitar notar que Natsuki me observa todo el rato."
    "¿Está esperando a que me decida a probarlo?"
    "FInalmente, decido darle un mordisco."
    "!!!"
    "No me lo esperaba, pero el pastelito está muy bueno."
    "La base chocolateada es muy dulce y combina perfectamente con el glaseado, que supongo es de vainilla, logrando un equilibrio perfecto entre ambos sabores."
    mc "¡Está muy bueno!"
    mc "Gracias por traerlos, Natsuki."

    show natsuki cross uniform neut mh b1f

    n "¿Por qué me das las gracias?"

    show natsuki cross uniform neut blaw mh e1b b1d at s11

    n "No los traje especialmente para ti y tu club... idiota..."
    mc "¿Eh?"
    mc "Pero, ¿no dijiste que los habías comprado para--?{w=0.10}{nw}"

    show natsuki base uniform neut ldown fs m3 e4 b2 at h11

    n "¡Bueno, puede!"
    n "¡Puede que los comprara para esta ocasión!"

    show natsuki 5q

    n "Pero no para... tú... {w=0.4} el club... idiota."
    mc "Emmm... vale, vale..."

    show natsuki at thide
    hide natsuki

    "Decido no intentar comprender la extraña lógica de Natsuki."

    show yuri base uniform happ at t11

    y "Por cierto, [player]... ¿Qué te gusta leer?"
    mc "Ah... bueno..."
    "Hace mucho que no me preguntan esto."
    "Considerando cuánto ha crecido mi colección de libros en los últimos años, temo que si digo todo, podríamos quedarnos aquí hasta mañana."
    mc "... Leo un poco de todo... pero el pasado fin de semana empecé a leer un pequeño libro de terror."

    show yuri base uniform happ ma e1b b1b rup

    y "Ya veo, un gran y sabio lector como yo..."
    mc "Puede ser."
    "Noto a Yuri sonreír discretamente."

    show yuri base uniform happ ma e1b b1b rdown at t21
    show monika base uniform happ lpoint ma e1a b1a at t22

    m "Ah, yo también empecé hace poco un libro de terror."
    mc "¿En serio, Monika?"
    mc "Me sorprende mucho viniendo de ti."

    show monika base uniform happ lpoint rhip e4b

    m "Ajajaja, es cierto que parezco alguien que no se interesa en esos géneros."

    show monika base uniform happ ldown e1a rhip

    m "Pero eso fue hace algunos años, y he tenido ganas de probar cosas nuevas."


    show monika lean uniform happ ma

    m "Después de todo, ¿la vida no sería un poco aburrida si todos los días fueran iguales?"
    "Monika me sonríe dulcemente."



    mc "Ah, sí... tienes razón."
    show monika at thide
    hide monika
    show yuri base uniform b1a e1a ma at t11
    mc "Entonces, Yuri... ¿qué te gusta leer?"
    show yuri 1e
    y "¿A mí? Veamos..."
    y 2g "Generalmente, me gusta leer novelas que cuentan una historia compleja y muy profunda de fantasía."
    y 2l "El nivel de creatividad y calidad de las historias es sorprendente..."
    y 1b "Pero ya sabes, también me gusta leer un poco de todo."
    y 1a "Empecé hace unas semanas a leer libros de terror."
    y 2a "Ahora estoy leyendo un libro llamado «Retrato de Markov»."
    mc "No he oído hablar de él..."
    y 1a "El autor del libro tampoco es que sea muy conocido."
    mc "¿De qué va la historia?"
    y 3i "En pocas palabras... es la historia de una chica de secundaria que se muda a la casa de su hermana perdida hace mucho tiempo..."
    y 3f "Pero tan pronto como se muda, su vida da un giro radical y empieza a volverse completamente extraña."
    y "De repente es perseguida por personas que han escapado de una prisión donde se realizan experimentos humanos."
    y "Sin embargo, mientras su vida está en peligro, desesperadamente busca credibilidad, pero sin importar lo que haga, sus relaciones siempre terminan desmoronándose."
    mc "Ah, pues sí, es una historia bastante inusual, pero suena interesante."
    show yuri 3f at t22
    show natsuki cross uniform neut mg e1b b1e at t21
    n "Aghhh... odio el horror."
    y 2e "¿Por qué?"
    n "Porque..."
    show natsuki cross uniform awkw b1a e1a
    "Natsuki me mira brevemente, como si se contuviera de decir algo."
    n cross uniform neut mg e1b b1e "... Déjalo."
    show yuri at t32
    show natsuki at t31
    show monika base uniform happ rhip at t33
    m "A ti te gusta más escribir sobre cosas monas, ¿no, Natsuki?"
    show natsuki base uniform neut blaw ldown rdown mm e2a b1e at h31
    n "Aghhh... ¡¿Qué?!"
    n "¿¿Qué te hace decirlo??"
    m "Bueno, cuando íbamos al club después de conocerte, se te cayó un papel de tu mochila, específicamente un poema llamado..."
    show natsuki base uniform neut blaw ldown rdown mi b1d at h31
    n "¡Ni se te ocurra abrir la boca!"
    show natsuki base uniform neut blaw ldown rdown ml e4c b1d at h31
    n "¡Y devuélvemelo!"
    show monika base uniform neut ldown rhip ma e4b b1a
    m "Vale, vale~"
    show yuri at thide
    show monika at thide
    show natsuki at thide
    hide monika
    hide yuri
    hide natsuki
    "Monika saca con discreción un pequeño papelito del bolsillo de su chaqueta, lo dobla de tal manera que no podamos ver lo que hay escrito y se lo da a Natsuki."
    "Natsuki se lo arrebata de las manos y lo pone en un lugar seguro."

    mc "Natsuki, ¿escribes poemas?"
    show natsuki 5h at t11
    n "Digamos que sí..."
    n "¿Por qué lo preguntas?"
    mc "Bueno, ¡porque creo que es increíble!"
    mc "¿Por qué no te ha dado por compartirlos con todos los miembros?"
    mc "Estaría bien qu--"
    show natsuki 1o at h11
    n "¡No! ...¡No!"
    "Asustada, Natsuki aparta brevemente la mirada para evitar cualquier contacto visual."
    mc "¿Por qué?"
    show natsuki 5s at s11
    n "A vosotros... no os gustarían..."
    mc "Ah... por lo que veo, no confías en compartirlos, ¿verdad?"
    show natsuki 5s at t21
    show yuri base uniform neut lup rdown mf e4a b1c at t22
    y "Entiendo lo que siente..."
    y "Compartir tu propia escritura es un desafío muy grande..."
    y "Si escribimos, es básicamente para describir algo nuestro, algo personal."
    show yuri base uniform neut lup rup mf e4a b1c
    y "Compartir nuestro trabajo es un desafío real para uno mismo, ya que conlleva acatar las críticas de los demás."
    y "Abrirte a otros, exponer tus debilidades e incluso mostrar las profundidades de tu corazón..."
    mc "¿Tienes experiencia escribiendo, Yuri?"
    mc "Quizá puedas compartir lo que escribas a Natsuki para darle un poco más de confianza para compartir poemas, ¿no crees?"
    show yuri 2o at s22
    y "Ah... eh... yo..."
    show natsuki 5s at t31
    show yuri at t32
    show monika base uniform neut awkw lpoint ma e1b b2c at t33
    m "Creo que con Yuri pasa lo mismo..."
    show natsuki 5s at t41
    show yuri at t42
    show monika base uniform neut awkw lpoint ma e1b b2c at t43
    show sayori base uniform neut e1b b1b md at t44
    s "Joooo... quería leer vuestros poemas..."
    show natsuki at thide
    show yuri at thide
    show monika at thide
    show sayori at thide
    hide natsuki
    hide yuri
    hide monika
    hide sayori
    "Nos quedamos en silencio un rato."
    "Leer los poemas de las demás..."
    "Creo que tengo una pequeña idea de la que puede ser la primera actividad del club."
    mc "¡Vale, compis!"
    mc "Tengo una idea."
    show natsuki base uniform neut nobl mg e1a at t21
    show yuri 2e at t22
    ny "¿...?"
    "Natsuki y Yuri me miran de forma interrogante."
    mc "¡Después de esta pequeña charla, que ha sido agradable de escuchar, para la primera actividad del club he propuesto que todos nos vayamos a casa..."
    mc "... y que todo el mundo escriba sus propios poemas y que los compartamos mañana en la siguiente reunión del club!"
    mc "¡Así estamos todos en igualdad de condiciones!"
    show natsuki cross uniform e1b b1d neut md awkw at t31
    show yuri base uniform flus awkw rup at t32
    show sayori base uniform happ nobl lup rup mc e4b b1a at h33
    s "¡Síiiiii! ¡Vamos a hacer eso!"
    show sayori base uniform happ nobl lup rup mc e4b b1a at t43
    show monika base uniform happ rhip at t44
    show natsuki cross uniform e1b b1d neut md awkw at t41
    show yuri base uniform flus awkw mk rup at t42
    m "¡Es una buena decisión, [player]!"
    n "Eh..."
    y "Yo..."
    mc "Y ahora disponemos de cinco miembros... ¡creo que esta actividad será la indicada para aprender sobre vosotros mismos y también aprender una pizca sobre los demás miembros!"
    mc "Creo que ahora podemos-...{w=0.08}{nw}"
    show yuri at thide
    show monika at thide
    show sayori at thide
    hide yuri
    hide monika
    hide sayori
    show natsuki base uniform e4c b1a ml blaw at h11
    n "¡Espera un minuto!"
    mc "¿...?"
    show natsuki cross uniform neut n3 mg e1b b1d nobl
    n "¡No me uní para hacer esto!"
    show natsuki base uniform neut n3 mg e1a b1d
    n "Aunque comprase cupcakes, no dije de unirme para compartir-..."
    "De forma inintencionada, interrumpo a Natsuki mientras hablaba."
    mc "Pero... pero..."
    "¿Por qué creí que sería una buena idea?"
    show natsuki at t11
    show yuri 1w at t41
    y "Perdona, no pretendí..."
    show natsuki at t42
    show sayori 3k at t43
    show monika 1f at t44
    ms "Natsuki..."
    show natsuki cross uniform neut awkw mg e1a b1f at s42
    n "Tú..."
    "Con la guardia baja, Natsuki nos mira a los cuatro."
    show natsuki cross uniform neut awkw mg e1b b1f
    n "Yo..."
    show natsuki 4x at t42
    n "¡Vale, vale, vale!"
    n "He cambiado de opinión, me uno al club."
    show natsuki cross uniform e1b mm b1e blaw at s42
    show monika base uniform happ b1b
    show sayori base uniform happ lup b1b
    show yuri base uniform happ b1b
    "Los cuatro miramos a Natsuki, aliviados."
    show sayori 4r at h43
    s "¡Bieeeeeeeeen! ¡Eres la mejor, Natsuki!"
    show sayori 4r behind natsuki at t42
    show yuri base uniform happ b1a
    "Levantándose de la silla de repente y yendo tras de Natsuki, Sayori la envuelve en sus brazos, sando saltitos."
    show natsuki base uniform neut fs m3 e4 b2
    show yuri base uniform e4b mb
    show monika base uniform e4b b1a mb
    n "¡Lo pillo, lo pillo! ¡Buagh!"
    show sayori base uniform happ at t43
    show yuri base uniform e1a ma
    show monika base uniform happ b1a e1a
    m "Por un momento me habías asustado, Natsuki..."
    mc "¡Entonces es oficial!"
    show natsuki 1g
    mc "¡Bienvenida al club, Natsuki!"
    mc "Y a ti también. Bienvenida, Yuri."
    show yuri shy uniform happ e2 m1
    y "G- gracias..."
    show monika at thide
    show sayori at thide
    show yuri at thide
    show natsuki at thide
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    mc "Para finalizar, ¡creo que podemos acabar la primera reunión oficial con buena nota!"
    mc "Como presidente, es mi deber hacer todo lo posible para asegurarme de que todos os llevéis bien en el club."
    mc "No toleraré malas formas si, por desgracia, llegase a suceder lo contrario."
    mc "Por otra parte..."
    mc "Si tenéis alguna sugerencia para mejorar el club o incluso peticiones para el mismo, ¡no dudéis en decírmelas!"
    mc "Me lo apuntaré y haré todo lo posible para que se haga."
    mc "Sin miedo..."
    mc "... que no muerdo."
    show monika lean uniform neut m1 at t11
    m "Vaya, vaya, [player]. ¡Estás hecho todo un diplomático! Estoooy impresionaaada."
    "Joder, Monika... deja de molestarme, vas a acabar avergonzándome si sigues haciéndolo."
    show monika at thide
    hide monika
    mc "Ajajajaja... ¡e- estoy muy feliz por el rumbo que está llevando el club hoy!"
    show monika base uniform happ at t21
    show sayori base uniform happ at t22
    mc "Por cierto, Monika y Sayori, me gustaría hablar con vosotras un momentillo de nada, si es posible."
    show monika base uniform happ at t41
    show sayori base uniform happ at t42
    show natsuki base uniform at t43
    show yuri shy uniform happ m1 e2 at t44
    mc "¿Recordáis los deberes para mañana?"
    mc "¡Traer un poema para compartirlo mañana!"
    mc "Con eso recordado, la sesión queda cerrada. ¡Podéis iros a casa!"
    mc "Pasad una buena tarde, chicas, ¡nos vemos mañana!"
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    with wiperight
    "Natsuki y Yuri se levantan de sus respectivas sillas y recogen sus cosas."
    show yuri base uniform neut ma at t11
    y "Pues bien, creo que me iré ya... la biblioteca cerrará ya mismo porque se está haciendo tarde..."
    y "Mejor me doy prisa, no quisiera llegar tarde."
    y "Os veo mañana."
    mc "¡Hasta mañana, Yuri!"
    show yuri base uniform neut lup rup ma e4b
    y "Hasta mañana, [player]."
    "Yuri me sonríe felizmente mientras empieza a irse."
    show yuri at lhide
    hide yuri
    "..."
    show natsuki base uniform happ lhip at t11
    n "¡Que sí, que yo me voy también! ¡Hasta mañana, pringados!"
    mc "Hasta mañana, Natsuki."
    "Natsuki se va, cerrando la puerta violentamente."
    show natsuki at lhide
    hide natsuki
    stop music fadeout 2.0
    "Un leve silencio abunda en la sala del club, con Sayori y Monika aún dentro."
    show monika base uniform neut rhip me at t11
    m "Así que... ¿[player]?"
    m "¿Qué querías hablar con nosotras?"
    mc "Ah, sí..."
    mc "Bueno... gracias a ambas."
    mc "Gracias por lo que habéis hecho en tan poco tiempo."
    show monika base uniform neut ma b1b
    m "Ah, no te preocupes, [player]... nos complace ayudarte."
    mc "¡Lo sé! Pero lo que quiero decir es que... no hace más de 4 horas, más o menos, estaba completamente solo... y ahora aquí estamos."
    mc "Así que gracias por todo, no os defraudaré. Confiad en mí."
    "Monika deja escapar una pequeña sonrisa."
    show sayori base uniform happ lup at t22
    show monika base uniform happ b1a mb at t21
    s "¡Estoy segura de que serás un gran presidente, [player]!"
    mc "Ajajajaja. Gracias, Sayori. Haré todo lo que esté en mi mano para hacer de este club lo mejorcito."
    mc "Por cierto, siento lo de antes."
    s "¿Por qué? ¿Qué debo perdonar?"
    mc "El haber sido duro contigo al haberte preguntado tu motivación en respecto a la literatura."
    show sayori base uniform happ b1b
    s "No te juzgo, [player], no te preocupes por eso. Es normal que pensases de esa manera."
    mc "Ah, gracias... eso me tranquiliza."
    mc "Gracias a ambas por escucharme, podéis iros. Ordenaré y limpiaré la habitación para dejarla decente después de la cata de los cupcakes."
    show monika base uniform neut ma rdown
    m "Te ayudo, [player], recuerda lo que te dije."
    mc "Ah, sí. Casi me olvido, fallo mío."
    s "¿Os puedo ayudar yo también?"
    mc "¡Claro!"
    show sayori base uniform neut lup rup mc e4b b1a
    s "¡Bieeeeeeeeeeen!"
    mc "En mi vida he visto a alguien tan contento por limpiar una habitación."
    mc "¡Al lío, cuanto antes terminemos, antes nos vamos a casa!"
    show monika at thide
    show sayori at thide
    hide monika
    hide sayori
    "Sayori, Monika y yo comenzamos poniendo las mesas en sus lugares de procedencia."
    "Al ser tres, terminamos de limpiar el aula del club en un abrir y cerrar de ojos."
    show bg club_day1
    with wiperight_scene
    "Después de unos cinco o seis minutos de limpieza, el aula del club está como los chorros del oro."
    mc "Gracias a ambas. Habéis sido de mucha ayuda."
    mc "Sin vosotras, hubiera tardado una eternidad, ajajajaja."
    show sayori base uniform happ lup ma at t11
    s "Monika, esperaré fuera mientras hablas con [player]."
    s "¡Hasta mañana, [player]!"
    mc "¡Hasta mañana, Sayori!"
    show sayori at lhide
    hide sayori
    "Sayori se coloca la mochila en su espalda y se va del aula del club."
    play sound closet_close
    play music her
    "Cierra la puerta con cuidado tras de sí."
    mc "Así que Monika..."
    show monika base uniform neut ma at t11
    m "Te escucho, [player], ¿Qué quieres preguntarme?"
    mc "Verás, sé que esto va a sonar repentino, pero..."
    mc "Sé que te fuiste del club de debate hace poco, y quizás estás harta de tantas responsabilidades, pero es que--{w=0.40}{nw}"
    show monika base uniform neut me b1b at t11
    m "Espera un minuto, [player]."
    "Monika me interrumpe de repente."
    m "No querrás preguntarme, de casualidad, el ser tu vicepresidenta, ¿no?"
    mc "¡Emmmm...!"
    "Me rasco la cabeza con nervios, no puedo evitar reírme."
    mc "¡Algo así!"
    mc "Si... si no quieres, lo entenderé y no te juzgaré..."
    mc "Entonces..."
    show monika base uniform neut rhip me b1b at t11
    m "[player]..."
    m "Ya sabes que..."
    show monika base uniform neut awkw ldown rhip mb e1b b1b at s11
    m "Bueno..."
    mc "..."
    "Vale, creo que conozco ya la respuesta."
    "Además, ¿qué clase de persona soy pensando que ella aceptaría?"
    show monika base uniform neut rhip ma e4b b1a
    m "Es que... ¡Acepto ser tu vicepresidenta!"
    "¿Lo he escuchado bien?"
    mc "¿Qué? ¿En serio?"
    show monika 1a
    m "Totalmente."
    mc "Ajajajaja... por un momento, me estabas asustando."
    mc "Cuando te vi cambiar de expresión de repente, pensé que se había acabado todo..."
    show monika 5a
    m "Ejejeje, soy una buena actriz, ¿eh?"
    show monika base uniform neut ma e4b
    m "Todo sea dicho, ¡tu cara era un poema, ha sido desternillante! ¡Ajajajajaja!"
    m "No me arrepiento de haberte puesto en duda."
    mc "Bla, bla, bla. Quien ríe último, ríe mejor, Monika."
    show monika lean uniform m2
    m "Oooooh, ¿me has amenazado?"
    mc "Ajajaja, claro, obviamente."
    show monika base uniform anno rhip ma e1d b1c
    m "No te preocupes, me preparo para cualquier posible ataque tuyo, [player]~"
    show monika base uniform neut ma e4b b1a
    "Ambos echamos unas risas."
    mc "Ya en serio, estoy orgulloso de tenerte como mi vicepresidenta, Monika."
    mc "Tú y yo podremos darle al Club de Literatura un buen sitio en el colegio."
    show monika base uniform e1a mb b1a
    m "¡Está claro que lo haremos!"
    mc "Vamos, puedes irte, Monika. Gracias por esta pequeña charla."
    mc "Te veo mañana."
    show monika lean uniform ma
    m "Igualmente, [player]. ¡Hasta mañana!"
    hide monika
    with wipeleft
    "Monika recoge sus cosas antes de irse con Sayori, quien la espera fuera del aula."
    play sound closet_close
    stop music fadeout 2.0
    "No pasa mucho hasta que el aula vuelve a estar en completo silencio."
    "Pero no es cualquier silencio."
    "No es el mismo silencio que me ha acompañado estos días."
    "Cuando estaba solo en el club."
    "Me siento en una de las sillas, descansando mi cabeza en la mesa."
    mc "-suspiro- Qué día tan genial."
    "Miro mi teléfono."
    "{i}6:10 PM{/i}"
    "Hora de irse."
    "Cojo mi mochila, deslizándola en mi espalda."
    mc "¿Eh?"
    "Veo los folletos abandonados encima de la mesa."
    "Suspiro."
    mc "No los necesito más."
    "Cojo los folletos, arrugándolos con ambas manos hasta hacer una pelota de papel, para seguidamente tirarlos a la basura."
    "Me dirijo a la puerta, poniendo un pie fuera del club, cuando algo pasa por mi cabeza de repente."
    mc "Eh, un minuto..."
    "Recuerdo que Natsuki estaba en el armario cuando volví."
    show bg closet
    with wipeleft_scene
    "No puedo evitar ser curioso, así que me dirijo al armario."
    "Abro la puerta y echo un vistazo dentro."
    mc "¿¿¿Eh???"
    "Veo tres colecciones de manga en la estantería, lo que hace del armario un buen desorden."
    mc "¿Qué coño hace esto aquí?"
    "Saco un libro completamente aleatorio."
    mc "¿'Parfait Girls' tomo 2...?"
    "La portada muestra cuatro chicas con poses exageradas en ropajes muy coloridos, que puedo deducir como heroínas."
    mc "..."
    mc "¡Pero es manga!"
    mc "No es mi género favorito, pero hay algunos interesantes para leer."
    mc "{i}-suspiro-{/i}... esto no va aquí, de todas maneras."
    "Miro en lo alto de la estantería, dándome una idea."
    mc "Hmmm, podría ponerlos allí. No molestarían mucho."
    "Pongo el libro de vuelta a su lugar, levantando la caja de cartón por ambos lados."
    "Deslizo la caja con facilidad, colocándola en lo alto de la estantería."
    "Mi altura, que es algo decente comparada con la altura de la estantería, me fuerza a ponerme de puntillas."
    "Hago lo mismo con las dos cajas restantes."
    "..."
    "..."
    mc "Buf... ya está hecho."
    mc "Ahora me toca recoger este desastre que ha causado Natsuki, supongo..."
    "Empiezo a colocar los libros en su sitio, intentando dejar la estantería tan ordenada como si nadie la hubiera tocado."
    "Al final, tras un rato, consigo dejarla como nueva."
    mc "¡Perfecto!"
    show bg club_day1
    with wiperight_scene
    play sound closet_close
    "Cierro las puertas del armario y me dirijo hacia la salida del club."
    show bg corridor_e
    with wiperight_scene
    "Cierro la puerta con llave y empiezo a caminar hacia la salida del instituto."
    mc "Ahora, a casa a escribir un poema."
    show bg kitchen
    with dissolve_scene_full
    "Al llegar a casa, voy directo a mi habitación."
    show bg bedroom
    with wiperight_scene
    mc "Bueno, vamos allá..."
    "Es hora de escribir un poema."
    "Me siento en mi silla, cojo un bolígrafo y empiezo a escribir."
    show bg black
    with dissolve_scene_full
    pause 0.5
    show text "Quince minutos después..."
    pause 2
    hide text
    show bg bedroom
    with dissolve_scene_full
    mc "¡Ah! {w=0.75} No..."
    "Dejo a un lado el papel, cojo otra hoja y lo intento de nuevo."
    show bg bedroom
    stop music fadeout 2.0
    with dissolve_scene_full
    pause 1
    call showpoem (poem_p1, music=False) from _call_showpoem
    mc "Uf. Hacía tiempo que no escribía un poema, pero creo que este no está mal."
    mc "Tengo curiosidad por ver qué les parecerá mañana."
    "Con una pequeña sonrisa en los labios, guardo el poema en mi mochila."
    mc "Eh... {i}-bostezo-{/i}... ¿Qué hora es...?"
    "Miro la hora en el despertador digital que hay en la mesilla de noche."
    "{i}10:10 PM{/i}"
    mc "Todavía tengo tiempo de darme una ducha rápida y comer algo."
    show bg bedroom_n
    with dissolve_scene_full
    "Después de terminar mi rutina nocturna, me desplomo en la cama."
    mc "Se siente bien estar tumbado en esta cama..."
    mc "... Mañana será un día importante."
    "Poco a poco, me dejo llevar por el sueño, cayendo en los brazos de Morfeo."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
