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
    mc "¿Eh?"
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
    s "¡Aaah! ¡Sí, vamos tirando, [player]!"
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
    "No sé por qué, pero siento que alguien está por encima mía."
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
    mc "Vale. A ver, bonita de cara, deberíamos empezar a compartir nuestros poemas, que ya es hora."
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
    mc "Vale, veamos si es cierto..."
    call showpoem (poem_n2, img="natsuki base uniform rhip lhip neut ma") from _call_showpoem_21
    "Me voy a hacer el idiota."
    mc "Oye, Natsuki... ¿No te gustan las arañas?"
    show natsuki base uniform e1a b1d mg
    n "¿Cómo?"
    show natsuki base uniform e1a b1d mi
    n "¡¿Estás de coña?!"
    mc "¿Me puedes responder a la pregunta que te he hecho?"
    show natsuki cross uniform e1a b1d mm blaw
    n "¡¿Y no quieres mejor una patada en los cojones para relajarte?!"
    mc "¡Oye, oye! Que sí, que sí, que estaba de coña, Natsuki..."
    show natsuki cross uniform e1b b1f mh nobl at s11
    n "{i}-suspiro-...{/i} Idiota."
    show natsuki cross uniform e1a b1f md at t11
    mc "Fuera de bromas ya, ¿tu poema habla sobre los hobbies raros que tiene la gente?"
    show natsuki base uniform e1a b1a mh rhip lhip
    n "Pues sí, y no."
    show natsuki base uniform e1a b1a mg ldown
    n "Mi poema trata sobre las aficiones extrañas o raras que algunas personas pueden tener."
    "{i}(¿¿No es eso lo mismo que he dicho yo??...){/i}"
    show natsuki cross uniform mh
    n "Mi poema se pone en la perspectiva de una persona que quiere entablar amistad con Amy, pero Amy tiene un trauma muy grande hacia las arañas."
    show natsuki base uniform blaw mi b1e rhip lhip
    n "A ver, mientras no le haga daño a nadie, ¡la gente no debe criticar los gustos de los demás!"
    show natsuki base uniform mg nobl rdown ldown b1a
    n "En fin, volviendo a lo que decía... Amy no quería ser amiga de ella porque a ella le encantaban las arañas."
    show natsuki cross uniform mc
    n "Y ahí es donde entra mi poema y su mensaje interior."
    show natsuki base uniform ma rhip
    mc "Guau, pues... es un mensaje bastante fuerte para ser un poema de pocas palabras."
    mc "Esa tal 'Amy', ¿es una amiga tuya, o quizás tú misma...?"
    show natsuki base uniform e2a b1f mi blaw rhip at h11
    n "¡No!"
    show natsuki cross uniform e1b b1b mf
    n "Es... es así, ya está."
    show natsuki cross uniform e1a b1a mg
    n "¿Por qué lo preguntas?"
    mc "Porque es así."
    mc "La mayoría de tus poemas que he leído hasta ahora trataban sobre lo que estamos viviendo, lo que hemos pasado o algún pensamiento que se nos cruza por la cabeza."
    "... ¿Creo?"
    show natsuki cross uniform e4a mc b3c
    n "¡Ja, ja, ja!"
    show natsuki base uniform e4b mo b3c rhip nobl
    n "Destaco dentro del club. Impresionante viniendo de mí, ¿no crees?"
    mc "Eh... sí, si tú lo dices."
    "Natsuki se pone de pie por sí sola, adoptando una pose exageradamente teatral."
    "Decido devolverle su poema."
    mc "Gracias por compartir tu poema conmigo, Natsuki."
    show bg club_day1
    hide natsuki
    with wiperight_scene
    show yuri base uniform neut md at t11
    mc "¡Hola, Yuri!"
    mc "¿Cómo estás?"
    show yuri base uniform neut mb
    y "Hola, [player]. Estoy muy bien, gracias."
    mc "¡Genial! ¿Quieres que empecemos a compartir nuestros poemas?"
    show yuri base uniform rup lup e1b
    y "Sería un placer ver el tuyo primero. Me gustaría ver lo que has escrito hoy."
    show yuri base uniform e4b ma
    "Yuri sonríe feliz mientras le entrego mi poema."
    show yuri base uniform e1b rdown ldown mf
    "..."
    show yuri base uniform rup lup b1b e1b ma
    "Cuanto más lee Yuri mi poema, su sonrisa alegre se va entristeciendo."
    "Al final, deja mi poema sobre el escritorio."
    show yuri shy uniform b1 e2 m1
    y "Y-Yo... lo siento por cómo me comporté el viernes, [player]..."
    show yuri shy uniform b1 e1 m2
    y "Probablemente me odies..."
    show yuri shy uniform b1 e2
    y "Debe ser por eso que tu poema es completamente diferente al del viernes..."
    show yuri shy uniform n5 m2
    y "Qué persona tan horrible soy..."
    "Yuri esconde la cara entre su melena, apartando su mirada."
    mc "¿Eh? ¡No! ¡En absoluto, Yuri!"
    mc "Oye, hablo en serio. No te odio."
    mc "No podría odiaros a ninguna de vosotras. Jamás."
    mc "Al final te disculpaste y todo ha vuelto a la normalidad."
    show yuri shy uniform n1 e1 m1
    mc "Simplemente cambié mi estilo de escritura por probar algo distinto."
    mc "Y me he dado cuenta de que no es lo mío, así que creo que volveré al estilo de antes."
    show yuri base uniform e4a b2b mf rup lup at s11
    y "E-Es un gran alivio."
    show yuri base uniform e1b ma at t11
    y "Quizá le di demasiadas vueltas a todo..."
    show yuri base uniform e1b ma rdown ldown
    "Yuri sonríe débilmente para sí misma."
    "Recupero mi poema en silencio y con cuidado."
    mc "¿Puedo ver tu poema, Yuri?"
    show yuri base uniform e1a b1a mb
    y "Será un placer."
    show yuri base uniform e4b ma rup lup
    y "He cambiado un poco la forma de mis versos, ¡pero espero que aún así te guste!"
    "Yuri me entrega su poema, y en cuanto lo tengo en las manos empiezo a leerlo..."
    call showpoem (poem_y12, img="yuri shy uniform e1 b1 m1") from _call_showpoem_22
    mc "Veo que te has inspirado un poco en mí, Yuri."
    show yuri base uniform e1a mb rup
    y "Sí, así es."
    show yuri shy uniform b1 e2 m1
    y "Tu poema fue..."
    show yuri shy uniform e1 m1
    y "... fue impresionante, así que me inspiré un poco..."
    show yuri base uniform e1a rup lup ma
    y "y había empezado a escribir el principio poco después de que compartiéramos nuestros poemas... {nw}{done}así que... eh..."
    show yuri base uniform e2b b1b mk blaw ldown
    y "y había empezado a escribir el principio poco después de que compartiéramos nuestros poemas... {fast}así que... eh..."
    show yuri base uniform rdown at s11
    y "Y-Yo.."
    "Yuri se queda a medias en su frase. Decido intervenir."
    mc "Me alegro mucho, Yuri. Buen trabajo."
    mc "Me reconforta que estés probando cosas nuevas."
    show yuri base uniform e1a b1a md rup lup nobl at t11
    mc "Quizá, algún día, podrías hablar con Natsuki para escribir algo juntas."
    mc "Sé que vuestros estilos de escritura son muy diferentes..."
    mc "pero tengo mucha curiosidad por ver qué saldrá de ahí."
    show yuri base uniform e2a b1b rup ml awkw
    y "¡Ah...!"
    mc "Ah... perdona, no quería que te sintieses obligada a hacer algo que no quieres..."
    show yuri base uniform e2b b1b rup mk blaw
    mc "Solo... era una sugerencia."
    show yuri base uniform e2b mb ldown b1b awkw at s11
    y "Eh... ya veré qué hacer."
    show yuri shy uniform e2 b1 m1 n1 at t11
    y "Me encantaría ponerme al día con Natsuki, ya que me he dado cuenta de que nuestra pelea no tuvo sentido alguno y fue algo muy estúpido..."
    mc "Yo..."
    "Sin tiempo para responder, Yuri sigue hablando."
    show yuri shy uniform
    y "Intentaré... Intentaré hablar con ella..."
    show yuri shy uniform e1
    mc "Cuento contigo, Yuri. Sé que puedes."
    mc "Gracias por compartir tu poema conmigo."
    show yuri base uniform e1a mb rup nobl
    y "Gracias a ti también."
    stop music fadeout 2.0
    show bg club_day
    hide yuri
    with wiperight_scene
    play music t3
    mc "¡Vale, compis! Venid al frente, a Monika le encantaría comentaros algo."
    show natsuki base uniform neut mg rhip at t22
    show monika base uniform neut ma at t21
    n "Supongo que es sobre el festival, ¿me equivoco?"
    show monika base uniform e4b mb rhip
    m "¡En absoluto, Natsuki!"
    show monika base uniform neut e1a ma lpoint
    m "El finde pasado, [player] y yo estuvimos en llamada telefónica organizando los días previos al festival de este viernes."
    show natsuki cross uniform neut mh
    show monika base uniform neut ldown me
    n "Uuuh..., ¿es necesario que hagamos todo esto?"
    show natsuki base uniform neut lhip mg
    n "Me refiero a que solo quedan tres días hasta el viernes."
    n "En tres días no nos da tiempo a nada y será una humillación. Vamos directos a ser el hazmerreír del instituto."
    $ yref()
    show yuri base uniform e1a rup lup mg at t33
    show natsuki base uniform neut lhip mg at t32
    show monika base uniform b1b at t31
    y "E-Estoy de acuerdo."
    show yuri base uniform e1b rdown ldown b1b mg awkw
    y "Suele pasar que las cosas no salen bien cuando se improvisan a última hora..."
    mc "Chicas, me gustaría... que dejéis a Monika expresarse. Cuando acabe, hablaremos sobre qué hacer."
    show monika base uniform b1a e1a mb rhip
    m "Pues bien, como sabéis, ¡el festival está al caer!"
    show monika base uniform e1a ma lpoint
    m "Con [player], queremos demostrar que la literatura, aunque a muchos en este instituto les parezca aburrida... ¡puede ser algo muy apasionante, si me me permite decirlo!"
    show monika base uniform e4b ma rdown ldown
    m "¡Es por ello que hemos decidido hacer un recital en público!"
    show monika base uniform e1a
    show natsuki base uniform md
    show yuri base uniform e2a b1b rup ml
    y "¿¿¿Q-Qué???"
    show yuri base uniform mk
    y "¿¿Un recital??"
    show yuri base uniform e2b mk lup blaw
    "Yuri coloca ambas manos en su pecho, y puedo ver que su cara va pasando de color carne a color rojo tomate."
    show monika base uniform e4b mb
    m "¡Claro!"
    show monika base uniform e1a ma rhip
    m "Hicimos los folletos y los hemos colocado hoy en los pasillos antes de que empezase la reunión del club."
    show monika base uniform e1a md rdown
    show yuri base uniform e2a ml ldown
    y "¡Monika...!"
    show yuri base uniform mk rdown
    y "¡E-Esto es demasiado repentino!"
    show monika base uniform e1a b1b md rdown
    show yuri shy uniform b1 m1 e2 n2
    y "N-No podría hacer algo así."
    show natsuki cross uniform mi e1a b1f
    n "¡Ni yo!"
    show natsuki base uniform mh e1b blaw rhip
    n "¡Ni siquiera nos has pedido opinión!"
    show monika base uniform e1a b1b me rhip
    m "¿Es que es una mala idea?"
    show monika base uniform e1a b1b ma rdown
    mc "No, Monika, es una gran idea."
    mc "Pero en una cosa tienen razón: debimos haberles dicho esto antes del fin de semana."
    mc "Culpa mía. Perdonadme."
    ny "..."
    "Natsuki y Yuri se quedan en completo silencio."
    show monika base uniform e1a b1b ma rdown at t41
    show natsuki base uniform at t42
    show yuri shy uniform b1 m1 e2 n2 at t43
    show sayori base uniform rup b1b mb at t44
    s "Chicas, por favor. Se nota que Monika y [player] han trabajado mucho durante el finde."
    show sayori base uniform lup
    s "Monika y yo sabemos cuánto se preocupa [player] por su club."
    show sayori base uniform e4b b1a mc at h44
    s "Y gracias a él... ¡he podido hacerme amiga vuestra!"
    show sayori base uniform e1a b1b ldown mb
    s "Ya es hora de que le devolvamos el favor..."
    show sayori base uniform e1a b1b mb
    s "y lo menos que podemos hacer es aportar nuestro granito de arena participando."
    show sayori base uniform e1a b1b ma
    show yuri base uniform e4a b2b mg rup lup at s43
    y "-suspiro-... Yo..."
    show yuri shy uniform b1 m1 e1 n1 at t43
    "Yuri me mira de reojo."
    window hide
    pause 2
    show yuri shy uniform e2
    y "He... cambiado de opinión. Apoyo hacer el recital."
    show sayori base uniform e4b b1a mc at h44
    s "¡Bieeen! ¡Gracias, Yuri, eres la mejor!"
    "Sayori is hopping on the spot."
    show yuri e5 b2
    y "-suspiro- Este club va a acabar conmigo..."
    show monika base uniform e4b b1b mb awkw lpoint
    m "Ay, madre... ¡Que no pasa nada, todo irá genial!"
    show monika base uniform e1a b1a ma nobl rhip ldown
    "Monika está esperando a Natsuki."
    show monika base uniform e1a mb rhip ldown
    m "¿Natsuki?"
    show monika base uniform e1a ma rhip ldown
    show natsuki cross uniform e1a mg b1a nobl
    n "Qué pasa."
    show natsuki cross uniform mi b1f
    n "A ver si te crees que te voy a dejar tranquila solo porque Yuri ha cambiado de parecer."
    show natsuki cross uniform mi b1e blaw
    n "¡Ni lo sueñes...!"
    "Nos quedamos mirando a Natsuki totalmente decepcionados."
    show sayori base uniform md e1a b1b
    show monika base uniform md e1a b1b
    "Ella nos mira, totalmente incómoda."
    show natsuki base uniform rhip lhip mg b1e nobl
    n "¿Por qué me miráis así?"
    show natsuki cross uniform e4a mm b3a nobl
    n "¡Parad de ponerme esa cara!"
    show natsuki base uniform e1a mg b1f
    n "Es que sois..."
    window hide
    pause 2
    $ nref
    show natsuki base uniform fs e4 b2 m3 n1 at h42
    n "¡Bueno, vale ya!"
    $ nref()
    show natsuki cross uniform e4a mi b3a
    n "Me estáis tocando las narices, pero he cambiado de parecer."
    show monika base uniform e1a b1b ldown
    show natsuki cross uniform e1b mm b1e nobl
    "Natsuki se cruza de brazos y mira hacia otro lado, apretando sus dientes."
    show sayori base uniform e4b b1a mc rup lup
    s "Je, je, je... ¡Gracias, Natsuki! ¡Eres incluso más cuqui cuando te pones así!"
    show sayori base uniform behind natsuki at t42
    "Sayori se desliza por detrás de Natsuki y la abraza."
    show natsuki base uniform fs e4 b2 m3
    n "¡Quítate de encima mía!"
    $ nref()
    show natsuki base uniform e4c ml b1a blaw at h42
    n "¡¡Y no soy CUQUI!!"
    show natsuki cross uniform e1b b1e md nobl
    show sayori base uniform neut ma rdown ldown at t44
    show monika base uniform neut ma e1a b1a
    m "¡Pues genial! Ahora que todos estamos de acuerdo, ¡me encargaré de explicar cómo procederemos durante estos días!"
    show yuri shy uniform e2 b1 m1
    m "Antes de nada, hemos de decorar el aula, y necesitamos a alguien con una letra preciosa que también sepa cambiar la atmósfera del lugar."
    m "Yuri, [player] y yo estamos de acuerdo en que tú eres la más indicada para esto."
    m "Para nosotros, eres la más capacitada."
    $ yref()
    show yuri base uniform e1b b1a mg nobl
    y "Hablando de atmósfera..."
    show yuri base uniform e1a b1e mg rup ldown
    y "¡Me encanta la atmósfera!"
    show monika base uniform e4b mb rhip
    show sayori base uniform e1a b1a
    m "Entonces mejor."
    show monika base uniform e1a
    m "Natsuki, hace unos días mencionaste lo buena que eres horneando."
    show natsuki base uniform e1a b1a mg rhip
    show yuri base uniform e1a b1a ma rdown ldown
    n "Claro, mi padre es un pastelero profesional en el centro de la ciudad."
    show monika base uniform e4b ma rdown
    m "¡Me vale! Necesitaremos como quince o veinte cupcakes."
    show monika base uniform e1a me
    m "Claro, como no podemos hacerlos en clase, tendremos que hacerlos en casa de alguien."
    show monika base uniform e1a mb lpoint
    m "¿Crees que tus padres accederán a hacerlos en tu casa?"
    show natsuki cross uniform mc nobl
    show monika base uniform e1a md ldown
    n "Pues claro que no, ¡podría enseñaros mis habilidades horneadas!"
    show natsuki base uniform e4b mo b3c rhip
    n "Ja, ja, ja. Ha sido un chiste malo, pero no estáis preparados, creedme."
    show natsuki base uniform e1a mc b1a rdown
    show monika base uniform mb rhip
    m "¿Crees que podríamos ayudarte con los cupcakes? ¿O tus padres no te dejan?"
    show monika base uniform ma
    show natsuki base uniform lhip mg
    n "Mmm..., buena pregunta."
    show natsuki base uniform mc ldown
    n "Les pregunto esta noche y mañana os lo digo."
    show monika base uniform e4b mb lpoint
    show natsuki base uniform ma
    m "¡Genial!"
    show monika base uniform e1a ma ldown
    m "Ahora que todos tenemos algo que hacer..."
    $ sref()
    show sayori base uniform neut mg rup
    s "Pero, ¿qué vamos a hacer el jueves?"
    show sayori base uniform neut md
    s "Aún no has dicho nada. ¿Escribimos poemas?"
    show sayori base uniform neut ma rdown
    show monika base uniform e4b mb awkw rhip
    m "¡Ah, sí! ¡Gracias por recordármelo, Sayori!"
    show monika base uniform e1a ma nobl rdown
    m "El jueves no escribiremos poemas..., ya que haremos un recital de prácticas en el que cada uno escoge uno de sus poemas ya escritos anteriormente,"
    show monika base uniform lpoint
    m "aunque podéis escribir uno nuevo si no os gustan los que ya habéis escrito."
    show monika base uniform ldown
    "Yuri, Natsuki y Sayori asienten."
    show monika base uniform mb
    m "Nos queda algo de tiempo, así que podéis volver a lo que hacíais antes. ¡Gracias, compis!"
    show monika at thide
    show sayori at thide
    show natsuki at thide
    show yuri at thide
    hide sayori
    hide monika
    hide natsuki
    hide yuri
    "Las chicas vuelven a sus respectivos sitios a seguir con lo que hacían antes."
    "Miro a Monika."
    show monika base uniform neut ma at t11
    mc "Muy bien, Monika. Has hablado alto y claro."
    mc "Aunque Yuri no parecía estar muy convencida, Sayori pudo ser capaz de hacer que entre en razón."
    show monika lean uniform ma
    m "¡Ja, ja, ja! Pues sí."
    show monika base uniform neut lpoint ma b1b
    m "Yuri es muy vergonzosa e introvertida, y parece que eso de hablar con la gente... no es muy típico en ella."
    show monika base uniform neut ldown mb b1a
    m "Aunque hayamos compartido nuestros poemas, estuvo un buen rato mirándome fijamente hasta que entendió a la perfección de qué iba mi poema."
    m "Cuando compartimos poemas la segunda vez, había menos tensión en ella. En unos días, estará como un pececillo en el agua."
    show monika base uniform neut ldown ma
    mc "Pues sí, es cuestión de tiempo."
    mc "Incluso le sugerí que hablase con Natsuki para que ambas escriban un poema con la misma temática."
    show monika base uniform neut me rhip
    m "Ah, ¿sí, [player]?"
    show monika base uniform neut ldown md
    mc "Claro. ¿No crees que sería interesante verlo?"
    mc "Sus estilos de escritura son completamente diferentes."
    show monika base uniform neut rdown me
    m "No estoy muy segura de ello, [player]."
    m "Me preocupa que vuelvan a discutir."
    show monika base uniform neut md
    mc "No creo que discutan, Monika. Yuri se responsabilizó de lo que hizo y no creo que tropiece dos veces con la misma piedra."
    mc "Por la parte de Natsuki, es un poco..., ya sabes...,As for Natsuki, I think her personality is a bit... you know..."
    mc "cuestión de suerte."
    show monika base uniform neut me
    m "¿Suerte?"
    mc "A ver, depende del ánimo que tenga en ese momento."
    mc "No tengo ni idea, pero quiero ver qué tal."
    show monika lean uniform neut ma
    m "¡Ja, ja, ja! Es que así es Natsuki, [player]. No hay más."
    "Me encojo de hombros."
    mc "Creo que falta poco para que acabe la reunión."
    show monika base uniform neut me rhip
    m "¿Ya?"
    mc "Claro. Dejaremos que Yuri tenga suficiente tiempo para comprar lo que necesita para mañana."
    mc "Si acabamos a la hora de siempre, no tendrá casi nada de tiempo, y añade ese poco tiempo a la caminata de 30 minutos que se va a pegar."
    show monika base uniform ma rdown
    m "No creo que tenga tan poco tiempo, pero no voy a decirte qué hacer y qué no. Es tu club, después de todo."
    show monika lean uniform neut ma
    "Le sonrío a Monika y me sonríe al mismo tiempo."
    show monika at thide
    hide monika
    "Echo un vistazo al aula."
    "Veo a Yuri levantarse y andar con mucha timidez hacia Natsuki, que sigue sentada en el suelo, justo al lado del armario."
    "Se arrodilla, poniéndose a la misma altura."
    "No puedo oír con claridad lo que dice..."
    "Lo único que puedo ver desde aquí es a Natsuki asintiendo con vergüenza."
    show monika base uniform neut me rhip at t11
    mc "Creo que es un punto para mí."
    "Hago señas con la cabeza a Monika en dirección a esas dos."
    show monika base uniform b1b ma rdown
    m "Pues es un punto merecido, tenías razón al final."
    m "Me alegra que empiecen a llevarse bien."
    mc "Y a mí."
    "Nos quedamos en silencio un ratito."
    s "{i}¡Monika, ven un momentito, que tengo que enseñarte algo!{/i}"
    show monika base uniform mb b1a rhip
    m "Te dejo, [player]. ¡Perdóname!"
    mc "No pasa nada, me quedaré aquí leyendo un poco."
    show monika at thide
    hide monika
    "Monika va a ver qué quiere Sayori, y parece que están hablando de algo divertido."
    "..."
    "Me siento en uno de los escritorios y saco un libro de mi mochila."
    "Observo con atención la portada, dándome una pista de su procedencia."
    mc "Este es el libro que me dio Yuri."
    "Lo abro y sigo leyendo desde donde lo dejé anoche."
    "..."
    "..."
    "...."
    "No puedo concentrarme en la lectura."
    "Es que siento como si me estuviesen poniendo el ojo encima."
    "Miro a mi derecha."
    "Nada."
    "Miro a mi izquierda."
    "Veo a Yuri, observándome cautelosamente cubierta con su libro."
    show yuri base uniform neut mf rup at t11
    "Tengo la sensación de que está leyendo lo mismo que estoy leyendo yo..."


    show yuri base uniform e2a mk rup blaw b1b
    "Tan pronto{nw}{done}como hago contacto visual con ella, se cubre la cara con el libro."
    $ yref()
    show yuri shy uniform b1 m1 e2
    "Tan pronto como{fast} hago contacto visual con ella, se cubre la cara con el libro."
    "Me levanto y voy hacia ella, libro en mano."
    show yuri base uniform e2b b1b mb rup blaw at s11
    y "¡Aaah! Perdona, no quería molestarte..."
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
    m "Sé que se acerca el festival, pero odio tener que verte dedicando todo tu tiempo libre al club."
    show monika base uniform e1b mb blaw lpoint
    m "¿Acabo de decir lo mismo dos veces?"
    mc "Más o menos, sí."
    show monika base uniform e4b awkw ldown
    m "Ja, ja, ja... Perdóname."
    show monika base uniform e1a b1a ma nobl rhip
    mc "But otherwise, I understand what you mean, Monika. Thanks for worrying about me."
    mc "Lo único que quiero es que todo vaya sobre ruedas."
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
    m "Valórate un poco más. Eres un tío bastante ordenadito."
    mc "Si tú lo dices..."
    m "Que sí, que sí, que voy en serio."
    "¿¿Cómo hemos acabado hablando de limpieza??"
    mc "En fin, me ha encantado saber tu opinión sobre lo de mañana."
    show monika lean uniform ma
    "Monika sonríe."
    show bg residential_e
    hide monika
    with wiperight_scene
    "El resto del camino ocurre sin ningún incidente en particular."
    "Como esta mañana, con Sayori, estuvimos hablando de varios temas, que fueron más o menos interesantes."
    "Nos paramos justo al llegar a la puerta de mi casa."
    mc "Aquí te tengo que abandonar."
    "Monika mira la parte frontal de la casa con bastante interés."
    show monika base uniform neut ma at t11:
        matrixcolor TintMatrix ("#f5aa87")
    m "La casa de tus padres está guay, [player]."
    mc "Gracias, Monika. Oye, ¿no te va a pillar un poquito lejos?"
    show monika base uniform neut e4b
    m "No, no, no te preocupes."
    show monika base uniform e1a rhip
    m "Te veré mañana, [player]. Descansa mucho, que no quiero encontrarte en la mesa otra vez con medio litro de baba fuera."
    show monika lean uniform neut ma at h11
    m "Je, je, je, je, je..."
    mc "Ya te he dicho que no..."
    show monika base uniform neut ma e4b rhip
    m "Que sí, que sí, que estoy de coña contigo, [player]."
    show monika base uniform neut mb e1a rdown
    m "¡En fin, me voy ya! ¡Gracias por la caminata!"
    show monika at thide
    hide monika
    "Monika cruza la carretera."
    "Se despide con la mano y continúa su camino yendo por donde hemos venido."
    "De mientras, voy abriendo la puerta de mi casa."
    play sound closet_open
    stop music fadeout 2.0
    show bg kitchen
    with wiperight_scene
    play sound closet_close
    "Me quito los zapatos y voy hacia mi habitación.I take off my shoes and head to my room."
    show bg bedroom
    with wipeleft_scene
    "Ya en la habitación, y después de dejar mis cosas, me siento en mi escritorio."
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
    show text "{=labeltext}{outlinecolor=#ffffff00}{size=40}Mil gracias a SpiritH0F#1283, DeltaOmega17#2949 y Zaun Aura#6946 por usar su tiempo libre en corregir los CIENTOS de errores gramaticales en mi mod debido al mal nivel de inglés que tengo. (Y seguirán habiendo, pero muchísimos menos que antes.){/outinecolor}{/=labeltext}{/size}"
    with Dissolve(1)
    $ pause (6)
    hide text
    with Dissolve(1)
    if persistent.secret == True:
        show text "{=monika_text}{outlinecolor=#ffffff00}{color=#0b5311}{size=80}Y recuerda una cosita...{/outinecolor}{/color}{/=monika_text}{/size}"
        with Dissolve (1)
        $ pause (1)
        hide text with Dissolve (2)
        show text "{=monika_text}{outlinecolor=#ffffff00}{color=#0b5311}{size=80}Te quiero.{/outinecolor}{/color}{/=monika_text}{/size}"
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
