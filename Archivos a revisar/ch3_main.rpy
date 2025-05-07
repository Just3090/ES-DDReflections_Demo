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
    s "¡Eeeyyy, [player], espérame!"
    mc "Huh?"
    $ s_name = "Sayori"
    play music t2 fadein 3.0
    "Me doy la vuelta para ver a Sayori corriendo en mi dirección, agitando los brazos en el aire."
    "Decido detenerme para que pueda alcanzarme."
    show sayori base uniform neut ml e4c awkw rup lup at t11
    s "Aaah... Aaah..."
    show sayori base uniform neut mb e1a rdown ldown
    s "[player], ¿eres un dormilón como yo también?"
    mc "¿Un dormilón?"
    mc "No, la verdad es que no. He estado despierto desde las seis y media."
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
    s "¿Eeeh?"
    show sayori base uniform neut e1a b1a mb
    s "¡Pensé que te lo había dado el viernes!"
    mc "Bueno... pues no."
    mc "De todos modos, deberíamos irnos o llegaremos tarde."
    show sayori base uniform e2a ml rup lup at rhide
    s "¡Aaah! ¡Sí, vamos rápido, [player]!"
    $ pause (0.4)
    hide sayori
    "Sayori sale corriendo sin decirme nada."
    mc "¡Eeeyyy, espérame!"
    "Acelero el paso para alcanzarla."
    show bg re2
    with wiperight_scene
    "De camino a la escuela, Sayori y yo intercambiamos rápidamente nuestros números de teléfono."
    "Charlamos un poco sobre cómo estuvo el fin de semana, pero no profundizamos mucho en el tema."
    show bg school_front
    with wiperight_scene
    "Llegando justo a tiempo antes de que sonara la campana de la escuela, nos despedimos mientras nos dirigíamos a nuestras clases."
    mc "Vamos a terminar con este día..."
    stop music fadeout 2.0
    show bg class_day
    with dissolve_scene_full
    play music t3
    play sound bell
    "La campana suena, señalando el fin de las clases y el comienzo del receso para el almuerzo."
    "Recojo mis cosas y me dirijo a la azotea."
    scene bg roof
    with wiperight_scene
    stop music fadeout 2.0
    "Después de abrir la puerta, veo a Monika de pie en la barandilla, contemplando las vistas."
    play music evening
    show monika base uniform neut e4a at t11
    "Pongo mi mochila en el banco y me acerco a ella discretamente."
    "Me coloco a su derecha, mirando al frente."
    "Hay un silencio entre nosotros."
    "Lo único que se llega a escuchar es el viento soplar y el sonido de la naturaleza."
    "Decido cortarlo."
    mc "Preciosas vistas, ¿eh, Monika?"
    "Monika asiente con la cabeza."
    show monika base uniform neut e1c me
    m "En efecto. Son preciosas, [player]."
    show monika base uniform neut e1c md
    mc "¿No está Sayori comiendo en la azotea?"
    show monika base uniform neut e1c me
    m "No vendrá por un rato, tuvo que hablar con uno de los profesores."
    show monika base uniform neut e1c md
    "Eso significa que habrá un poco de tiempo a solas entre Monika y yo..."
    "Tal vez pueda indagar un poco más para descubrir qué pasó cuando ella dejó el club de debate."
    "Aún tengo un poco de miedo de su reacción, sin embargo, ha sido bastante vaga y fría cada vez que le he hecho esa pregunta por mensaje de texto."
    mc "Ey, Monika, tengo que preguntarte algo..."
    show monika base uniform neut e1a me b1c
    m "¿Vas a hacérmela otra vez?"
    show monika base uniform neut e1a me rhip
    m "[player], ¿sabes que eres muy pesado?"
    show monika base uniform neut e1a me rdown
    m "¿Cuántas veces te lo he dicho por mensaje?"
    show monika base uniform neut e1c md rhip
    "Monika me interrumpe secamente, mirándome directamente a los ojos."
    mc "Monika, sé que sueno como si estuviera exagerando, pero escucha..."
    show monika base uniform neut e1a me rdown
    m "Sí, estás exagerando."
    m "¿Recuerdas lo que te dije?"
    show monika base uniform neut e1a me lpoint
    m "Es mejor centrarse en el presente en lugar de en el pasado."
    show monika base uniform neut e1a me ldown
    m "¿Qué no entiendes de eso, [player]?"
    show monika base uniform neut e4a b3b me
    "Siento la molestia salir en la voz de Monika, lo que me ha desestabilizado un poco, haciéndome perder en mis pensamientos."
    "Hay un pequeño momento de silencio antes de que decida romperlo."
    show monika base uniform neut e1a b1c md
    mc "Tienes toda la razón, Monika, debemos concentrarnos en el presente y no quedarnos atrapados en el pasado."
    mc "Pero escucha, sé que algo pasó y quieres ocultarlo."
    show monika base uniform e4a b2b me
    mc "¿Sabes, Monika? Me gustas mucho y quiero que lo sepas."
    mc "Pero el hecho de que no quieras decírmelo es prueba de que aún no confías completamente en mí."
    show monika base uniform e1a b1b
    mc "Sin embargo... ¿recuerdas el año pasado cuando estábamos en la misma clase?"
    mc "¿Cómo trabajamos juntos?"
    show monika base uniform e1c me
    mc "Nos confiábamos el uno al otro, al menos eso pensé."
    show monika base uniform e4a md
    m "..."
    mc "¿Sayori, tu mejor amiga, sabe sobre esto?"
    show monika base uniform e1c me
    m "No, ella no sabe la historia."
    show monika base uniform e4a me
    m "Solo me da vergüenza."
    mc "¿Vergüenza de qué?"
    show monika base uniform e1c md
    m "Vergüenza de decirlo, eso es todo."
    mc "Monika, puedes decírmelo. En serio."
    mc "Será algo que quede entre nosotros dos. Créeme, por favor."
    show monika base uniform e4a me
    mc "Nadie más que yo sabrá este secreto..."
    $ renpy.music.set_volume(0.8, delay=3)
    m "..."
    "Monika inhala brevemente, cerrando los ojos."
    play channel1("<loop 06.058>mod_assets/bgm/piano.ogg") volume 0.1
    show monika base uniform e1c me
    m "Es solo que he estado pensando en una nueva actividad para el club de debate."
    show monika base uniform e1b mi
    m "Quería salir de este ciclo vicioso desde que asumí el cargo de vicepresidenta."
    show monika base uniform e4a lpoint mh b2a
    m "¡Era optimista!"
    show monika base uniform e1b me ldown b1b
    m "Pensé que era una gran idea, divertida de hacer."
    show monika base uniform e4d md b1a
    m "Pero si tan solo hubiera sabido lo que iba a suceder..."
    mc "¿Qué pasó, Monika?"
    "Monika toma una bocanada de aire."
    show monika base uniform e1c b1b me
    m "Fue una pesadilla."
    show monika base uniform e1g
    m "Nadie encontró mi actividad interesante."
    show monika base uniform e4d mj
    m "Naide."
    show monika base uniform e4d mj
    m "No solo había perdido el tiempo trabajando en todo esto para nada, sino que..."
    m "...Sino que destruyeron todo lo que había hecho."
    show monika base uniform e1h mk
    m "Todo lo que había planeado para que el club organizara el festival..."
    show monika base uniform e4e ml
    m "...Rasgaron los carteles que había planeado y preparado para el festival."
    show monika base uniform e1h ml
    m "Me tomó mucho tiempo hacer todo..."
    show monika base uniform e1h mk
    m "¡Me tomó casi dos semanas enteras!"
    show monika base uniform e4e ml
    m "¡Dos semanas completas en las que estuve sacrificando mi tiempo libre para poder hacer avanzar el club!"
    show monika base uniform e4e mm
    m "...Me dijeron que era una porquería, que era un trabajo descuidado..."
    show monika at thide
    hide monika
    "Monika entierra su cabeza en mi hombro, sollozando."
    "La tomo del brazo."
    "Un torrente de lágrimas recorre su cara y manchan mi chaqueta al mismo tiempo."
    m "¡Todo se fue a la mierda!..."
    m "En cuestión de segundos..."
    "Siento cómo Monika me aprieta el antebrazo."
    "Lo único que se escucha son sus sollozos."
    "Monika, siento muchísimo que hayas tenido que pasar por esto."
    mc "Son unos capullos, unos gilipollas, y lo digo de corazón. No se merecen a alguien con tanto talento como tú."
    "Hay un silencio muy breve antes de volver a hablar."
    mc "Escúchame bien, Monika..."
    mc "En mi club se te va a respetar."
    mc "Se te va a escuchar."
    mc "Y, por encima de todo..."
    mc "Vas a recibir cariño De mí y del resto."
    mc "Nadie tiene derecho a tratarte así."
    mc "Las ideas que me contaste el viernes eran geniales, créeme."
    mc "Estoy seguro de que Sayori, Natsuki y Yuri pensarán lo mismo."
    "Por fin, los sollozos de Monika empiezan a cesar. Pero sigue con la cabeza apoyada en mi hombro."
    "Escucho pasos provenientes de las escaleras."
    "¿Será Sayori?"
    "Probablemente sí, aunque nunca se sabe"
    "Le suelto el brazo a Monika."
    s "{i}Perdón por la tardanza, el profe me ha echado la bronca por un examen que me salté...{/i}{w=0.04}{nw}"
    show sayori base uniform e4b mc at l21
    show monika base uniform e4d mj at t22
    s "Tengo unas ganas locas de...{w=0.02}{nw}"
    show sayori base uniform e2a mi rup lup
    s "¡¿Monika, estás bien?!"
    show sayori base uniform e1a b1c md rdown ldown
    "Miro a Sayori, que tiene una expresión de preocupación en la cara y se va acercando poco a poco a nosotras."
    show monika base uniform e1b me
    m "Tranquila, Sayori... Es solo que..."
    show monika base uniform e4d mj
    "Monika tiene dificultades para terminar la frase."
    "Me acerco a ella y le susurro al oído, para que Sayori no nos escuche."
    mc "{i}¿Quieres contarle tú misma lo que me dijiste, Monika?{/i}"
    "..."
    "No responde."
    "Solo lanza miradas, a mí y a Sayori."
    show sayori base uniform e1a b1b mh rup
    s "¿Qué le has dicho, [player]?"
    mc "Eeeh... Yo..."
    "Mis pensamientos se desordenan al instante. ¡Pero si Monika ni siquiera me ha dicho si podía contárselo o no!"
    "¿Debería decírselo o no?"
    "..."
    "..."
    "Le prometí que no lo haría."
    "Si Sayori quiere saberlo, tendrá que hablar con Monika."
    "Por respeto a ella."
    show monika base uniform e1c b1b me
    m "Sayori... es una larga historia."
    show monika base uniform e4e b1b me
    show sayori base uniform rup lup b1b md
    s "¿Puedo darte un abrazo?..."
    show sayori behind monika at t22s
    "Monika no responde, pero Sayori se le acerca y la abraza."
    show sayori base uniform e4a md ldown b1b
    "Sayori cierra los ojos y le habla con un tono suave."
    show sayori base uniform e4a me lup b1a
    s "Puedes contarme lo que sea. Soy tu amiga."
    show sayori base uniform e4a mg ldown b1b
    s "Y una amiga... escucha todo lo que llevas dentro."
    s "No me gusta verte así de triste."
    show sayori base uniform e4a me rup b1a
    s "Cuéntame lo que guardas en el corazón."
    m "..."
    "Al final, Monika empieza a contarle a Sayori todo lo que me dijo a mí."
    "Yo no hago más que quedarme ahí plantado, como si fuera una farola."
    window hide
    stop channel1 fadeout 2.0
    stop music fadeout 2.0
    show bg roof_r
    show sayori base uniform neut b1b ma rup
    show monika base uniform neut e1c md b1b
    with dissolve_scene_full
    "Da la sensación de que Sayori ha conseguido calmar un poco el ambiente, aunque no tengo ni idea de cómo."
    "..."
    show monika base uniform neut e1a me b1b
    m "Yo solo..."
    show sayori base uniform e1a b1b at t21
    show monika base uniform neut e1a md b1b
    m "¿Prometéis que esto quedará entre nosotros?"
    mc "Te lo prometo, Monika."
    "Hago el gesto de cerrar la boca con una cremallera."
    show sayori base uniform b1b e1a lup rup
    s "Esto se queda entre los tres, Monika. Puedes confiar en nosotros."
    show monika base uniform e1a b1b ma
    m "Muchas gracias. Sois unos amigos increíbles."
    mc "No te preocupes, Monika. Si necesitas hablar, aquí estamos Sayori y yo."
    s "¡Sí! Y además..."
    show sayori base uniform e4b b1a mc rup lup
    s "Eres muy lista y guapa, Monika."
    show monika base uniform e1c b1b lpoint blaw mb
    m "Ja, ja... ¿Cuántas veces me has dicho eso ya, Sayori?"
    show monika base uniform e1c b1b lpoint blaw ma
    show sayori base uniform e2a b1a mf rup at h21
    s "¡Ah! Eh... ¡ni idea! ¡No llevo la cuenta!"
    show sayori base uniform neut e4b mc rup lup
    s "¡Pero lo digo de corazón!"
    show sayori base uniform neut e1a mb rdown lup
    s "¡Y lo repetiré las veces que haga falta!"
    show sayori base uniform neut e4b ma rup lup at face
    s "¡Y gracias a ti también, [player], por ser el mejor presidente!"
    show monika base uniform e4b awkw mb b1a
    "De repente, Sayori me abraza con fuerza."
    "Para ser sinceros, me pilla un poco por sorpresa."
    mc "¡Eh, eh!"
    show sayori base uniform neut mb rup ldown at t21
    s "Ja, ja, ja. ¡Perdón, es que soy una doña abracitos!"
    show monika base uniform neut ma e1a rhip nobl
    m "Que no te sorprenda, [player]. Así es Sayori normalmente."
    mc "Lo noté desde que se unió al club. No te preocupes, Monika."
    show monika base uniform ma e4b rdown ldown
    "Monika sonríe con ternura."
    show monika base uniform me b1a rhip e1a
    show sayori tap m1 e2 blaw b1 at s21
    "El estómago de Sayori ruge con mucha fuerza."
    show sayori tap m1 e1 nobl at t21
    s "Je, je, je... ¿Y si... vamos a comer algo?"
    show sayori base uniform e1b b1b mc
    show monika base uniform ma b1a rhip
    s "¡El señor barrigón empieza a protestar!"
    mc "¿El señor barrigón?"
    mc "¿Le has puesto un mote a tu estómago, Sayori?"
    show sayori base uniform e4b b1a rup lup mc
    s "¡Síii!"
    mc "Y..., ¿de dónde ha salido?"
    show sayori base uniform e2a mf b1f
    "Sayori muestra una mirada enreversada mientras piensa durante un rato."
    show sayori base uniform e1a mb b1a
    s "Lo vi en Internet y pensé que el nombre era divertido y cuqui al mismo tiempo."
    show monika base uniform e4b mb rdown
    "Monika y yo reímos."
    show sayori tap m2 e1 b1 awkw at s21
    s "¡Oyeee! ¡No os riais de mí!"
    show monika base uniform neut ma
    show sayori tap m2 e2 b1 awkw at t21
    mc "¡Ja, ja, ja! No te preocupes, Sayori, que no nos estamos riendo de ti."
    mc "En fin, deberíamos disfrutar de la comida el tiempo que nos queda."
    show sayori base uniform neut e4b mc b1a at h21
    s "¡Porfiii, que tengo hambreee!"
    show sayori at rhide
    $ pause (0.01)
    hide sayori
    "Sayori va corriendo hacia el banco y se sienta justo en medio."
    show monika at thide
    hide monika
    "Monika y yo la seguimos."
    "Sacamos la comida y empezamos a comer."
    stop music fadeout 2.0
    show bg corridor
    with dissolve_scene_full
    "El resto del almuerzo en la azotea fue bastante ordinario."
    "Estuvimos hablando de varios temas comunes."
    play sound bell
    "Tras el sonido de la campana, que quiere decir que siguen las clases y se termina el descanso para almorzar, Sayori y Monika van a la misma clase, despidiéndonos al unísono."
    show bg class_day
    with dissolve_scene_full
    pause 1
    play music t3
    "El resto de las clases de tarde fueron más que anodinas."
    "Escribí rápidamente un poema dedicado a Monika mientras me aburría."
    call showpoem (poem_p11, music=False) from _call_showpoem_18
    stop music
    pause 1
    play sound bell
    "Tras una interminable espera, el timbre suena."
    "Recojo mis cosas y me levanto de la silla."
    t "Espera un minuto, [player]. Hoy te toca limpiar la clase."
    mc "Pero, ¿por qué?"
    t "El personal de limpieza está de baja hoy, así que tengo que asignar a un alumno al azar para que se encargue."
    t "Son órdenes de los de arriba."
    "¡¿Qué putísimo sentido tiene eso?!"
    "Es decir, ¡¿no existe un sustituto o yo-qué-sé-quién al que asignarle la tarea en lugar de preguntarle a alguien que ni siquiera ha pedido hacerlo?!"
    "Esto no es justo, joder."
    "Por dentro, me hallo mascullando."
    mc "Vale..."
    "Los estudiantes que quedan en la clase ya han salido con el profesor, dejándome únicamente a mí."
    mc "Qué guay, acabemos con esto de una puta vez."
    pause 5
    "Después de limpiar con vagueza hasta dejarla a mi gusto, consigo salir del aula."
    show bg corridor
    with wiperight_scene
    "Subo por las escaleras hasta llegar al club."
    mc "Genia, voy tarde..."
    play sound closet_open
    show bg club_day
    with wipeleft_scene
    play music t3
    "Una vez llegué al club, Monika se acerca directamente a mí."
    show monika base uniform neut me rhip at r11
    m "¡[player]! ¿A qué se viene el retraso?"
    mc "Ah, perdona... Me han encargado limpiar mi clase..."
    mc "por alguna razón que ni yo mismo quiero mencionar."
    show monika base uniform neut mb rdown
    m "Mmm... Vale. ¡Bueno, mientras hayas llegado, eso es lo que cuenta!"
    mc "¿Me he perdido algo en mi ausencia?"
    show monika base uniform neut md rhip
    m "Qué va."
    show monika base uniform mb ldown
    m "Solo Yuri, que ha traído su tetera eléctrica y algunas tacitas de té. Dice que quiere hacer un poco."
    show monika base uniform e4b ma rhip
    m "Parece muy aliviada."
    show monika base uniform e1a ma rhip
    mc "Me alegro por ella."
    show monika at thide
    hide monika
    "Echo un vistazo al aula."
    "Veo una bandeja sobre una mesa, con unas bolsitas de té y un hervidor eléctrico, tal y como había dicho Monika."
    "Natsuki y Sayori están sentadas en el suelo, frente al armario, leyendo juntas un manga."
    "Y Yuri está inmersa en su libro con una taza de té en su mano derecha."
    "Miro a Monika de nuevo."
    show monika base uniform neut ma at t11
    mc "Hablaremos más tarde del festival junto a los demás. Primero debemos compartir los poemas con el resto."
    show monika base uniform neut me rhip
    m "Claro, les comento eso, [player]."
    show monika base uniform neut ma rdown
    m "Sé cómo hacerlo."
    mc "No te preocupes, Monika. Te creo."
    show monika base uniform neut e4b
    "Monika sonríe felizmente."
    show monika base uniform neut e1a mb
    m "Estaré escribiendo cosas en mi libreta."
    mc "Claro, Monika."
    show monika at rhide
    hide monika
    "..."
    "Me derrumbo en el escritorio, observando alrededor y..."
    "y sin hacer nada, la verdad."
    "Podría empezar a compartir los poemas, pero creo que aún es muy temprano."
    "Podría trabajar más en los preparativos del festival, pero no es justo para Monika ya que ella está ayudándome,"
    "y parece que le hacía ilusión decírselo a los miembros del club."
    "Echo otro vistazo al aula."
    "Sayori y Natsuki parecen hablar sobre el manga que estaban leyendo. Apoyo la cabeza en mis brazos mientras estoy tumbado en el escritorio, escuchando la conversación con cierta vagueza."
    show natsuki cross uniform happ at t22
    show sayori base uniform ma at t21
    n "Así que... ¿Qué piensas del primer capítulo, Sayori?"
    show sayori base uniform mb rup
    s "¡Ha estado genial!"
    show natsuki base uniform rhip lhip
    n "Si quieres, la próxima vez seguimos leyendo el siguiente capítulo."
    show natsuki base uniform e4b mo rhip ldown
    n "No quiero destriparte nada, ¡pero la historia mejorará por momentos!"
    show sayori tap m1 n2 at s21
    s "Je, je, je... Oye, Natsuki, verás... La sesión de lectura qur acabamos de tener me ha hecho despertar hambre. ¿Quieres ir conmigo a comprar algo a la máquina expendedora?"
    show natsuki base uniform mh e1a rdown
    show sayori tap m1 e1
    n "¿Qué?"
    show natsuki e1a mi b1e blaw at h22
    n "Espera, no me digas que te has puesto a leer conmigo... ¡solo para preguntarme eso!"
    show sayori tap m1 e2
    s "Je, je, no... O bueno, puede que sí... ¡¡Pero ha sido el señor barrigón el que me lo ha dicho!!"
    show natsuki e1a mi rhip lhip b1f
    n "¡Me podrías haber dicho desde un principio que no querías leer conmigo, Sayori!"
    show natsuki e1a md rhip lhip b1f
    show sayori base uniform e1a b1b mg
    s "¿Eh? Pero ¡sí que quería!"
    show sayori base uniform e4b b1a mc rup nobl at h21
    s "¡Porfiiiii, Natsuki!"
    show natsuki base uniform e4a b3b mi
    n "¡No, no, y no!"
    show natsuki cross uniform e1a b1c mh
    n "Sayori, ni de coña cambiaré de parecer."
    show sayori base uniform e4b mc b1a rup lup
    s "¡Porfiiiiiiii!"
    $ AutofocusStore.disable_zoom()
    $ AutofocusStore.disable_zorder()
    show sayori behind natsuki at t22s
    "Sayori rodea con sus brazos a Natsuki y la abraza con fuerza."
    show natsuki base uniform fs e4 m3 b2 n1
    n "Aaarg, ¡para, por favor!"
    show sayori at h22s
    s "¡Porfiiiiiiiiii, Natsukiiiiiiii!"
    $ nref()
    show natsuki cross uniform e4a mm b3b blaw
    n "{i}-suspiro-{/i} ¡Vale, vale!... ¡Lo pillo, lo pillo!"
    n "¡Has ganado...!"
    $ sref()
    show sayori base uniform e4b mc rup lup nobl at t21
    s "¡Sííí!"
    "Cierro los ojos lentamente."
    $ AutofocusStore.enable_zoom()
    $ AutofocusStore.enable_zorder()
    scene black with close_eyes
    hide natsuki
    hide sayori
    pause 3
    "No sé por qué, pero siento que alguien se encuentra por encima mía."
    "En un acto reflejo, abro los ojos con extrema rapidez y levanto la cabeza."
    show bg club_day
    show monika lean uniform at face (y=750)
    "De repente, veo a Monika ocupando absolutamente todo mi campo de visión."
    "Doy un salto desde la silla, con el corazón a mil."
    mc "¡¿Monika?!"
    show monika base uniform e4b mb awkw at t11
    m "¡Ja. ja, ja! Perdona, no podía evitar hacerlo."
    show monika lean uniform ma nobl
    m "¿No hemos descansado ya bastante esta noche, presidente?"
    mc "No te creas, ¡tenía mucho que pensar y estaba descansando la cabeza!"
    show monika base uniform lpoint ma
    m "Venga ya, [player], tómate el club con más seriedad..."
    show monika base uniform ldown mb
    m "No deberías estar tumbado en la mesa..."
    show monika lean uniform ma
    m "Eso no es muy propio de un presidente, [player]..."
    mc "¿No exageras demasiado, Monika?..."
    show monika base uniform e4b ma
    "Monika ríe con mucha fuerza."
    show monika base uniform e1a mb
    m "¡Que estoy de coña!"
    show monika base uniform me lpoint
    m "Aun así..."
    show monika base uniform mb ldown
    m "Deberíamos empezar a compartir los poemas. Puede que, si acabamos a tiempo, podamos hablar de los preparativos del festival."
    mc "Ya, tienes razón. Vamos, no hay tiempo que perder."
    show monika at thide
    hide monika
    "Me levanto de la silla para colocarme en la parte frontal de la clase."
    mc "¡Vale, compis!"
    mc "¡Vamos a compartir los poemas, si os parece!"
    stop music fadeout 2.0
    show bg club_day1
    with wiperight_scene
    play music t5
    show sayori base uniform rup mb at t11
    s "¡Hola, [player]!"
    mc "Hola, Sayori."
    mc "¿Cómo te va en el club?"
    show sayori base uniform e4b mc rup lup
    s "¡Genial!"
    mc "¡Me alegro!"
    show sayori base uniform e1a ma rdown ldown
    mc "Si es así, a mí me alegras el día."
    show sayori base uniform e4b mc
    "Sayori sonríe felizmente."
    show sayori base uniform e1a ma
    mc "¿Lista para compartir tu poema, Sayori?"
    show sayori base uniform e1a mb
    s "¡Síp!"
    show sayori base uniform e4b mc rup
    s "¡Verás que mi poema es el mejor que he escrito!"
    mc "Lo espero con ansias."
    "Sayori me da su poema con una sonrisa de oreja a oreja. Lo cojo y empiezo a leerlo."
    call showpoem (poem_s2, img="sayori base uniform neut e1b b1b ma blaw lup rup") from _call_showpoem_19
    show sayori base uniform neut e1a b1a ma nobl rdown ldown
    mc "Dios mío..."
    mc "Sayori, si tuviese que opinar con una sola palabra..."
    mc "Impresionante."
    show sayori base uniform e4b mc rup
    s "Je, je, je. ¡Te dije que escribiría el mejor poema hasta la fecha!
    show sayori base uniform e1a ma
    mc "No estabas de coña..."
    mc "Tu poema es impresionante, Sayori. Muy bien."
    show sayori base uniform e4b mc rup at h11
    s "¡Bieeen! ¡Me ha felicitado el presidente!"
    mc "Sayo..."
    show sayori base uniform e4b mc rup at h11
    s "¡Eso significa que es el mejor poema que has visto el día de hoy!"
    mc "Sayori... esto no es una competición."
    show sayori tap uniform e2 m2 b1 awkw at s11
    s "Baaah, no te diviertes un poco, ¿eh, [player]?"
    mc "¡Pero...!"
    mc "Vale, está bien... Felicidades, Sayori, has quedado en primer puesto."
    show sayori base uniform e4b mc rup at h11
    s "¡Tomaaa!"
    show sayori base uniform e4b mc rup lup nobl at h11r
    "Me aguanto las ganas de reírme, solo dejo entrever una sonrisita."
    show sayori base uniform neut e1a ma at t11
    mc "¿Quieres leer ahora mi poema...?"
    show sayori base uniform mb
    s "¡Claro!"
    show sayori base uniform e2a b1f rdown ldown mf
    s "..."
    show sayori base uniform e1a b1a lup mb
    s "¡Tu poema es excelente, [player]!"
    show sayori base uniform e4b mc rup lup
    s "¡Aunque no tan excelente como el mío!"
    mc "Eh... ¿A qué te refieres?"
    show sayori base uniform e1a mb rdown
    s "¡Estoy de coña!"
    show sayori base uniform e4b mc rup lup
    s "¡Ja, ja, ja! Se te da increíble escribir poemas, ¿eh?"
    show sayori base uniform e2a b1f mf ldown rdown
    s "Aunque no haya entendido ni papa..."
    mc "Eh... Gracias, supongo."
    show sayori base uniform e4b ma b1a
    "No me sorprende. Sayori tiende a escribir cosas un tanto simples. Eso de escribir poemas con vocabulario extenso no es su punto más fuerte."
    "Pero puedo decir que tiene un don y se esfuerza de verdad por escribir cosas maravillosas."
    "No me arrepiento de tenerla en mi club."
    mc "Gracias por compartirlo, Sayori."
    show sayori base uniform e1a mb lup
    s "¡Gracias a ti!"
    show bg club_day1
    hide sayori
    with wiperight_scene
    show monika base uniform neut ma at t11
    mc "¡Hola, Monika!"
    show monika base uniform neut mb
    m "¡Eh, [player]!"
    mc "¿Cómo estás?"
    show monika base uniform neut e4b mb rhip
    m "¡Pues mucho mejor! Gracias por preguntar."
    show monika lean uniform ma
    m "¿Cómo estás tú? No mucha gente pregunta si tú estás bien, ¿eh?"
    mc "Estoy genial, si es que puede decirse así."
    mc "¿Lista para compartir, Monika?"
    show monika base uniform neut ma
    m "¡Síp!"
    "Le doy a Monika mi poema especial."
    "..."
    show monika base uniform e2a md
    m "¡Mmm...!"
    "Los ojos de Monika se hacen cada vez más grandes."
    show monika base uniform e1a b1b rhip ma
    m "[player]... ¿has escrito tú esto?"
    mc "Claro, lo escribí especialmente para ti."
    show monika base uniform e1a b1b rdown ma
    m "Oye, [player]... Lo siento muchísimo por estar tan ocupada por esas mierdas del club de debate."
    m "A partir de ahora, podremos volver a construir nuestra amistad."
    "Monika me lanza una sonrisa de sinceridad, que va entre el poema y yo."
    mc "Monika... si quieres, puedes quedártelo..."
    show monika base uniform e1a b1b rhip ma
    m "Lo cierto es que lo voy a hacer."
    show monika base uniform e1a b1b rdown mb
    m "Eso me demostrará cada día lo sincero que eres."
    m "Estoy muy feliz de poder estar aquí."
    mc "Y yo, Monika."
    show monika lean uniform ma
    m "Bueno, ¿quieres leer mi poema?"
    show monika base uniform mb
    m "He querido probar algo nuevo."
    "Monika me da su porma y lo cojo con la mano derecha."
    mc "Muy bien, veamos..."
    call showpoem (poem_m12, img="monika base uniform neut ma b1b") from _call_showpoem_20
    mc "..."
    show monika base uniform neut ma b1a
    mc "Hala... Monika, ¿has escrito tú esto?"
    mc "Me impresionas cada vez más."
    show monika lean uniform ma
    m "¡Ja, ja, ja! Muchísimas gracias, [player]."
    show monika base uniform neut mb lpoint
    m "Como dije, quise probar algo nuevo."
    show monika base uniform neut e4b ma ldown
    m "Y lo escribí esta mañana. Me sentí... muy inspirada."
    mc "¿Trata sobre aquellos días que viviste?"
    show monika base uniform neut e1a md rhip
    m "Mmm..."
    show monika base uniform neut mb rdown
    m "Sí, podría decirse que sí."
    m "Hasta que dejé el club de debate, con más exactitud."
    show monika base uniform b1b ma rhip
    m "Y no me gustaría hablar otra vez de ello porque lo he dicho todo en la hora del almuerzo."
    mc "Sí, tienes razón. Ahora que sé lo que ha ocurrido, es mejor olvidarse del tema."
    mc "Gracias por compartirlo conmigo, Monika."
    mc "Ha sido una lectura bastante inspiradora, la he disfrutado muchísimo."
    show monika base uniform b1a e4b mb
    m "¡Gracias a ti también!"
    "Monika se me acerca, susurrando."
    show monika lean uniform ma
    m "{i}Y... gracias de nuevo por tu poema...{/i}"
    m "{i}Lo cuidaré muchísimo.{/i}"
    m "{i}Te lo prometo.{/i}"
    mc "A-Ah... Eh... Gracias..."
    "No sé qué decir, mi corazón está empezando a acelerarse."
    show monika at thide
    hide monika
    "No hay tiempo que perder, Monika ya ha ido a compartir su poema con otra persona."
    "Suspiro con pesadez."
    show bg club_day1
    with wiperight_scene
    show natsuki base uniform rhip ma at t11
    mc "¡Oye, Natsuki!"
    show natsuki base uniform rdown mc
    n "Hola, Señor Presidente."
    mc "Por favor, Natsuki, deja de llamarme así."
    show natsuki base uniform rhip lhip mb
    n "Ja, ja, ja. ¿Por qué no, Señor Presidente?"
    show natsuki base uniform e4a b3c mc
    n "¿Odias que la gente te llame Señor Presidente?"
    mc "..."
    show natsuki base uniform b1a e4b mo rhip ldown
    n "Señoooooooooor... PRESIDENTEEEEEEEE."
    mc "Vale. A ver, niña bonita, deberíamos empezar a compartir nuestros poemas."
    show natsuki base uniform e2a b1a mi
    n "¡¿No vas a reírte de mí?!"
    mc "Has empezado tú."
    show natsuki e1d mh rhip lhip
    n "Bueno, vale. ¡Vale, lo pillo!"
    show natsuki e1a md b1d ldown
    n "Dame tu puñetero poema."
    "Me río para mis adentros, dándole mi poema."
    show natsuki cross uniform md b1a
    "..."
    show natsuki cross uniform mg b1a
    n "Está bien."
    show natsuki base uniform mh
    n "Mejor que el de ayer, imagino."
    mc "Ah, pues gracias."
    mc "Aprecio tu... honestidad."
    mc "Quería probar con algo diferente."
    show natsuki base uniform lhip
    n "Veenga ya, ¿en serio? No me he dado cuenta, en serio."
    n "Hasta Monika ha probado algo nuevo, idiota."
    show natsuki base uniform rhip
    n "¿Os conectáis al escribir? ¿O qué?"
    mc "¿Eh?"
    mc "No, pero ¡quizá el haber compartido poemas ayer haya influido en nuestra escritura!"
    mc "¿Quién sabe?"
    show natsuki cross uniform mg
    n "Ya, genial. A mí no me influye en nada."
    mc "Es genial saberlo, Natsuki..."
    mc "¿Vas a compartir mi poema conmigo?"
    show natsuki base uniform ma
    n "Claro."
    show natsuki cross uniform mc
    n "Te aviso de que es más largo que el del viernes."
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
    show text "{=labeltext}{outlinecolor=#ffffff00}{size=40}¡Gracias por jugar a la versión de demostración de Doki Doki: The Reflection!{/outlinecolor}{/=labeltext}{/size}"
    with Dissolve(1)
    $ pause (3)
    hide text
    with Dissolve(1)
    show text "{=labeltext}{outlinecolor=#ffffff00}{size=40}Si tienes alguna sugerencia o consejo para mejorar mi proyecto, no dudes en decírmelo en los comentarios.{/outinecolor}{/=labeltext}{/size}"
    with Dissolve(1)
    $ pause (2)
    hide text
    show text "{=labeltext}{outlinecolor=#ffffff00}{size=40}Mil gracias a SpiritH0F#1283, DeltaOmega17#2949 y Zaun Aura#6946 por usar su tiempo libre en corregir los CIENTOS de errores gramaticales en mi mod debido al mal nivel de inglés que tengo.(Y seguirán habiendo, pero muchísimos menos que antes.){/outinecolor}{/=labeltext}{/size}"
    with Dissolve(1)
    $ pause (6)
    hide text
    with Dissolve(1)
    if persistent.secret == True:
        show text "{=monika_text}{outlinecolor=#ffffff00}{color=#0b5311}{size=80}Y recuerda una cosita...{/outinecolor}{/color}{/=monika_text}{/size}"
        with Dissolve (1)
        $ pause (1)
        hide text with Dissolve (2)
        show text "{=monika_text}{outlinecolor=#ffffff00}{color=#0b5311}{size=80}Te amo.{/outinecolor}{/color}{/=monika_text}{/size}"
        with Dissolve (2)
        $ pause (1)
        hide text with Dissolve (3)
        $ pause (2)
        show text "{=monika_text}{outlinecolor=#ffffff00}{color=#0b5311}{size=100}FIN{/outinecolor}{/color}{/=monika_text}{/size}"
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
