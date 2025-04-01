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
    "Tardé en darme cuenta, pero ya estoy frente a la entrada del instituto."
    mc "Así que nada, al lío con otro aburrido día de colegio."
    stop music fadeout 2.0    
    show bg class_day
    with dissolve_scene_full
    pause 1    
    play music t3
    "La mañana transcurrió bastante lenta, y todo lo que hice fue simplemente hacerme apuntes y participar oralmente."
    play sound bell
    "El timbre suena al fin, marcando el descanso para el almuerzo."
    "Me coloco la mochila en la espalda y me dirijo a las escaleras que conducen al tejado del edificio."
    show bg roof
    with wiperight_scene
    stop music fadeout 2.0
    pause 2
    play music evening
    mc "¡Menudas vistas más espléndidas!"
    "Me quedo admirando las vistas del paisaje, extendiéndose hasta el horizonte."
    "Me siento en un banco, en el que mejor se admiran las vistas mientras me como el almuerzo."
    mc "Hmmmmm, es extraño..."
    "Echo un vistazo alrededor."
    "Me percato que no hay nadie aquí y soy el único."
    mc "Creí que habría más gente."
    "..."
    "Un minuto transcurre mientras que los sonidos de la naturaleza me atrapan."
    "En la distancia, alcanzo a oír pisadas fuertes viniendo de la entrada, mientras la puerta se mantiene cerrada."
    "Las pisadas se hacen más notorias y más fuertes a medida que la persona se acerca a la puerta."
    "La puerta se abre y alcanzo a ver..."
    "... ¿a Sayori?"
    show sayori base uniform e1b b1f mf at t41
    s "¿Ehhh?"
    show sayori base uniform e4b mc rup at h41
    "Sayori se percata de mi presencia, levantando la mano para hacer un gesto de saludo desde su posición."
    "La saludo con el mismo gesto."
    show sayori base uniform ldown rdown ma at t11
    s "¡Hola, [player]!"
    "Sayori camina despacio hacia mí."
    mc "¡Hola, Sayori! ¿Ha pasado algo esta mañana?"
    s 1b "¿Qué? ¿Por qué lo preguntas?"
    show sayori 3a at d11
    "Sayori está de pie justo al lado mía, sacando su tentempié de la mochila. Parece un simple sándwich que puedes comprar en el centro de la ciudad."
    "Hago lo mismo, sacando mi sándwich."
    mc "Noté que estabas pisando muy fuerte."
    s 4r "Aaahhhh, ¡no es así!"
    "A Sayori se le escapa una pequeña risa."
    s 1a "En realidad... ¡me gusta golpearme las piernas con fuerza cada vez que doy un paso, jajajajaja!"
    s 3x "Creo que es divertido, llevo haciéndolo desde que era niña."
    show sayori base uniform neut ma
    mc "Ah.. ya veo, es una de esas cosas que todos hemos hechos de niños, supongo yo."
    s base uniform happ "Sí, ejejejeje... todos tenemos nuestro lado infantil en algún lado, ¿no?"
    mc "Claro, como andar únicamente por las líneas blancas al cruzar un paso de peatones."
    mc "Aún lo sigo haciendo, jajajajaja."
    s 3r "Jejejejeje, ¡yo también lo sigo haciendo!"
    "Compartimos una pequeña pequeña risa."
    mc "Por cierto, Sayori... ¿no estás hoy comiendo con Monika?"
    s 2c "Bueno, en realidad, ¡debería!"
    s 1c "Pero tenía que hablar algo con una profe, así que me dijo que vendría más tarde a comer conmigo."
    mc "Ah, vale."
    s 2x "Siendo honesta, no me esperaba que tú--{w=0.05}{nw}"
    show sayori base uniform neut rup ml e2a b1a at h11
    m "{i}-¡¡¡PERDÓN, PERDÓN POR EL RETRASO, SAYORI!!! {/i}"
    mc "Ah, bueno, hablando de la reina de Roma..."
    hide sayori
    with wipeleft
    "Podíamos oír a Monika gritando desde las escaleras. A diferencia de Sayori, parece subir las escaleras con pasos muy apresurados."
    show monika base uniform neut awkw ldown rdown mb e4b b1b at l11
    m "...Aaaaaah.. {w=0.1} ..Aaaaaaah.. {w=0.1} bufffff... perdóname, Sayori, la profesora que-{nw}"
    show monika base uniform neut nobl ldown rdown me e1a b1a at h11
    m "¡Ah! ¿[player]?"
    mc "Hola, Monika."
    show monika lean uniform neut ma
    m "Hola, [player]... no esperaba verte aquí."
    mc "Lo sé. Es que anoche me hice un sándwich."
    show monika base uniform neut ma e4b
    m "¡Es verdad, ya veo!"
    show monika base uniform neut mb e1a rhip
    m "Bueno..."
    show monika lean uniform neut ma
    m "No me importa que estés aquí."
    m "En realidad, es al contrario."
    show monika base uniform neut ma at t22
    show sayori base uniform neut lup at t21
    s "Te has pegado un rato hablando, Monika. ¿Era algo grave?"
    show monika base uniform rhip e4b
    m "¡Oh, no, no, no! No te preocupes, Sayori."
    show monika base uniform neut ma
    m "Solo quería preguntarle algo."
    mc "Ehhh... de todas formas, ¿Sayori? ¿Monika?"
    show monika base uniform neut me e1a rhip
    show sayori base uniform neut me
    ms "¿...?"
    "Ambas me miran de manera interrogante."
    mc "¿Venís aquí con frecuencia?"
    show sayori base uniform happ ma
    s "Bueno, ya sabes, [player]..."
    show monika base uniform happ ma rhip
    m "Claro, ¡normalmente comemos en la azotea de la escuela!"
    show monika base uniform happ ma e4b
    m "De primeras, para admirar las preciosas vistas que nos ofrece."
    m "Pero principalmente... casi todos los días comemos aquí porque nos traemos nuestra propia comida."
    show sayori base uniform happ lup rup ma e4b
    s "¡Claro!"
    show sayori base uniform happ lup rup ma
    show sayori tap uniform neut awkw m1 e2 b1 at s21
    s "Además de que la comida de la cafetería es muy cara y no está muy buena, que digamos..."
    show sayori tap uniform neut awkw m1 e1 b1
    s "Así que... mejor para mi cartera. Jejejejeje..."
    s "Y Monika es vegana, así que es mejor para ella comer fuera de la cafetería."
    show monika base uniform neut e1a b1c me
    m "¡Sayori!"
    show sayori base uniform neut rup ml e2a b1a at h21
    "Monika alza la voz ligeramente."
    show sayori base uniform neut rup lup ml e2a b1a
    s "Aiiiiiii."
    mc "¿...?"
    show monika base uniform awkw mb lpoint e1b b1b
    m "Emmmm... perdón por gritar de repente."
    show monika base uniform lpoint awkw ma e1b b1b
    m "Es que..."
    show monika base uniform neut awkw lpoint rdown mb e1b b1b
    m "No soy vegana."
    show monika base uniform neut awkw ma b1b
    m "Soy 'vegetariana'."
    show sayori tap uniform neut awkw m1 e2 b1 at s21
    s "Jajajaja... {w=0.5} perdón, es que no sé diferenciar esos dos términos, jejeje..."
    mc "Si quieres, Sayori, para que salgas de dudas..."
    show monika base uniform neut nobl ma e1a b1b ldown rhip
    mc "... ser vegano te hace excluir toda la carne, pero no es solamente eso."
    show sayori base uniform neut ma nobl
    mc "Excluyes también cualquier producto de procedencia animal."
    show sayori base uniform neut ma
    mc "Por ejemplo: la leche, la mantequilla o incluso los huevos."
    mc "En resumen, todo lo que sea de origen animal."
    mc "Sin embargo, la dieta de un vegetariano excluye únicamente la carne y el pescado."
    mc "Monika puede comer las cosas que mencioné anteriormente..."
    show sayori base uniform neut mb lup e1a
    s "¡Gracias, [player]!"
    s "Jejejeje, me has resuelto la duda."
    mc "Ahora, volviendo a lo que nos ocupa..."
    mc "¿Por qué no compras un menú combinado de carne y pescado de la cafetería, Monika?"
    mc "¿No te conviene desechar el plato principal e ir directamente al segundo plato?"
    show monika base uniform neut b1a lpoint rhip me
    m "Es que no te devuelven el dinero de la comida que no quieres."
    show monika base uniform neut ma
    m "Es un precio fijo, ¿sabes?"
    m "No importa cuán pequeña sea la cantidad que consigas agenciarte, el precio es el mismo."
    show monika base uniform neut ldown rdown e1a b1b
    show sayori base uniform neut ma b1b
    m "Para los demás está bien y les beneficia, pero para mí... no lo es tanto."
    show monika base uniform neut ma e4b b1a rhip
    show sayori base uniform neut ma b1a
    m "¡Prefiero hacerme la comida para el día siguiente, que así sé qué contiene!"
    show monika base uniform neut mb e4b lpoint
    m "Además, ¡cuesta menos y sabe mejor!"
    show monika base uniform neut e1a ma rhip ldown
    mc "Debo decirte que estoy de acuerdo."
    mc "La comida de cafetería está muy, pero que muy sosa."
    mc "Tendríamos que añadir toneladas de sal para que nuestras papilas gustativas reconozcan los sabores."
    show monika base uniform neut e4b mb lpoint
    m "Jajajaja, es cierto, es cierto."
    show monika base uniform neut e1a ma ldown
    mc "Dime, Monika..."
    show monika base uniform neut me rhip
    m "¿Qué?"
    mc "¿Vas a sentarte con nosotros..."
    mc "... en lugar de estar ahí de pie en frente nuestra? Ajajajaja."
    show monika base uniform awkw ma e4b rhip
    m "Ah... ¡Ajajajaja!"
    m "Perdóname, me he dejado llevar hablando."
    mc "No te preocupes."
    hide monika
    hide sayori
    with wipeleft
    "Monika se sienta a mi izquierda, y Sayori a mi derecha."
    "Estar sentado entre estás dos chicas tan monas..."
    "Me hace sentir algo, siendo sinceros."
    "Sayori sigue devorando su sándwich, y Monika acaba de sacar una cajita transparente de su mochila."
    mc "¿Qué has traído hoy, Monika?"
    show monika base uniform neut ma at t11
    m "Algo simple."
    mc "¿Qué es?"
    show monika base uniform neut ma lpoint e4b
    m "Una ensalada César pequeña, ¡pero preparada al más puro estilo de Monika!"
    "Echo un vistazo rápido a la comida de Monika."
    mc "Parece delicioso."
    m "¡Lo es! Cuando se prepara de una forma tan perfecta, solo puede catalogarse como 'delicioso'."
    "Asiento y sonrío en dirección a Monika antes de que se forme un pequeño silencio que Monika rompe rápidamente."
    show monika base uniform neut me rhip at t11
    m "Por cierto, [player], ¿tienes planes para el festival?"
    mc "Qué va, no he pensado aún en ello, pero pensaré algo cuando lleguemos al club."
    show monika base uniform neut ma lpoint
    m "Podría echarte una mano, si quieres."
    show monika lean uniform neut ma
    m "Porque ahora soy tu vicepresidenta."
    mc "Sería un placer, Monika."
    show monika base uniform neut ma e4b
    "Monika sonríe con felicidad."
    show sayori base uniform neut ml e2a at t21
    show monika base uniform neut ma e4b at t22
    s "¿Qué? ¿Ahora eres la vicepresidenta del club, Monika?"
    show monika base uniform mb e4b lpoint
    m "¡Sí! Ajajajaja."
    show monika base uniform mb e1a rhip ldown
    m "[player] me preguntó ayer, y estuve de acuerdo."
    show sayori base uniform mc e4b lup rup at h21
    s "¡Quéeeeeeeeeeee guaaaaaaayyyyyyy!"
    s "¡Ajajajajaja! ¡Será el mejor club!"
    show monika base uniform mb e4b
    "Los tres reímos."
    hide sayori
    hide monika
    with wipeleft
    pause 0.2
    show bg roof
    with dissolve_scene_full
    "Seguimos comiendo en completo silencio."
    "De vez en cuando lo rompíamos para hablar de algunos temas variados, como el tiempo que hace."
    "Cuando estábamos hablando del tiempo, Monika nos explicó por qué se hizo vegetariana."
    "Recalcó que fue por un documental que vio hace unos años que explicaba cómo comer carne era una bomba de gases de efecto invernadero para el planeta."
    "Parecía tomárselo en serio y el tema le afectó muchísimo."
    play sound bell
    "Suena el timbre, señal de que el descanso para el almuerzo ha tocado su final."
    "Los tres suspiramos al unísono."
    "Si te soy sincero, me frustra tener que volver a clase."
    "Pero... oye, no es que tengamos más opciones que escoger, ¿no?"
    "Soy el primero en levantarse, me doy la vuelta para encontrarme a Monika y a Sayori de cara."
    mc "Bueno... gracias a las dos por pasar el almuerzo conmigo."
    mc "Ha estado genial poder charlar con vosotras."
    mc "Ojalá poder pasar más rato juntos, pero nos quedamos cortos de tiempo, supongo..."
    show monika base uniform ma b1b rhip at t11
    m "Igualmente, ojalá poder hablar un poco más, se me va el tiempo volando."
    show sayori base uniform neut ma lup rup at t21
    show monika base uniform ma b1a rhip at t22
    s "¡No pasa nada, te veremos por la tarde en el club, [player]!"
    mc "¡Alguien está impaciente, por lo que veo!"
    show sayori base uniform e4b mb at h21
    s "¡Claro! Nos lo pasaremos bien, ¡estoy segura!"
    mc "AJajajaja, no te emociones aún, Sayori."
    show monika base uniform mb e1a rhip
    m "Nos vamos ya, [player]. De todas maneras, vamos a llegar tarde... porque nuestra clase está en la otra punta del edificio."
    mc "Nos vemos después."
    show sayori base uniform happ ma
    s "¡Hasta luego!"
    hide monika
    hide sayori
    with wiperight
    show bg corridor
    with wiperight_scene
    stop music fadeout 3.0
    "Nos despedimos, antes de dirigirme a clases."
    show bg class_day
    with dissolve_scene_full
    play music t3
    "La tarde fue más de lo mismo, aunque la mayor parte del tiempo fue bastante aburrida."
    play sound bell
    "Suena el último timbre, poniendo punto y final al día."
    show bg corridor
    with wipeleft_scene
    "Después de recoger mis cosas, me dirijo al club."
    play sound closet_open
    show bg club_day1
    with wipeleft_scene
    "Al entrar en la sala del club, me doy cuenta de que soy el primero en llegar."
    mc "Bueno, tocará esperar a que lleguen las chicas."
    "Me siento en un escritorio y saco una hoja de papel y un bolígrafo de mi mochila."
    mc "Preparativos para el festival:"
    "Empiezo a escribir una línea."
    mc "Hacer nuevos folletos."
    mc "Sí... es lógico."
    "Sigo escribiendo unas cuantas líneas, describiendo lo mejor que puedo."
    "Oigo que se abre la puerta."
    "Levanto un poco la cabeza y veo que es Natsuki."
    "Me levanto de la silla y me acerco a ella."
    show natsuki base uniform neut ma rhip at t11
    mc "¡Hola, Natsuki!"
    show natsuki base uniform neut mb rhip
    n "Hola, [player]."
    show natsuki base uniform neut md ldown
    mc "Si tienes alguna sugerencia o recomendación para el club, ya sabes, no dudes en decírmelo a mí o a Monika."
    show natsuki cross uniform neut mh
    n "Vale, si se me ocurre algo, yo te aviso."
    "Asiento con la cabeza y vuelvo a mi escritorio, centrándome de nuevo en el papel."
    show natsuki at rhide
    hide natsuki
    "Natsuki se dirige al armario, pero ya no le presto más atención."
    mc "¿Por dónde iba yo...?"
    mc "Hmmmmm... ¿Qué podemos conseguir si necesitamos...?{w=0.01}{nw}"
    n "¡¡¡¡¡[player!u]!!!!!"
    "Natsuki grita desde el armario, lo que hace que me quede mirando fijamente."
    "Me levanto, de nuevo, para acercarme a ella."
    show bg closet
    with wiperight
    mc "¿Qué pasa?"
    show natsuki cross uniform neut mm b1e at t11
    n "¡Aaaahhhh-!"
    "Joder, parece muy enfadada."
    mc "Natsu---{w=0.1}{nw}"
    show natsuki base uniform neut mi b1e
    n "¡¿HAS MOVIDO MIS MANGAS DE SITIO?!"
    show natsuki base uniform neut mm b1e
    mc "¡A-Ah! Eeeeh.. sí, los moví yo, claro."
    mc "Ahí estaban mal puestos."
    show natsuki base uniform neut mi lhip rhip b1e
    n "¡Me la suda!"
    show natsuki base uniform neut mm b1e
    n "¡¿Cómo pretendes que coja los tomos?!"
    mc "Bueno, eh..."
    show natsuki cross uniform neut mi e4a b3a
    n "Me preguntaste antes sobre las sugerencias y recomendaciones del club, y es genial, ¿sabes? Porque tengo una que hacerte si no es de mucha importancia, SEÑOR PRESIDENTE."
    show natsuki cross uniform neut mi e1a b1e
    n "¡No muevas mis cajas de manga!"
    show natsuki cross uniform neut mm e1a b1e
    n "¡¿Qué piensas, Señor Presidente?!"
    "Natsuki me mira, enfurecida."
    mc "¡Natsuki!"
    mc "¡¡No puedes despreciarme de esa manera!!"
    mc "¡Si los moví, fue por una buena razón!"
    mc "¡Y no voy a cambiar de parecer!"
    mc "Además, yo tampoco sabía nada de que habían 'ahí' cajas de manga."
    show natsuki base uniform neut blaw mm e1a b1e
    n "¡Grrrrr-!"
    show natsuki base uniform neut blaw lhip rhip mi e1a b1e
    n "¡Vale, ¿sabes qué?!"
    mc "Natsuki, haz el favor de escucharme."
    mc "Sé que estás muy enfadada, ¡pero no hace falta montar un numerito por todo esto!"
    show natsuki base uniform neut blaw lhip rhip md e1a b1d
    mc "Son los profesores los que me pidieron mantener este aula como estaba desde que me la asignaron."
    mc "Si un profesor se acerca al armario y encuentra este desastre, ¡me temo... que estaré metido en un buen lío porque 'estoy a cargo de la habitación'!"
    show natsuki cross uniform neut blaw md e1a b1b
    mc "¿Me estás entendiendo?"
    "Cojo una silla que está cerca y la pongo en frente mía."
    mc "Toma, ¿por qué no usas esta silla para alcanzarlos?"
    show natsuki cross uniform neut awkw mg e1b b1a
    n "Bueno... no me importaría, en realidad."
    show natsuki cross uniform neut awkw mg e1a b1a
    n "Gracias, [player]... supongo."
    mc "Bueno, si con eso estamos en paz, me quedo tranquilo."
    hide natsuki
    with wipeleft
    "Le paso la silla a Natsuki con cuidado, y ella la coloca en el armario en el lugar adecuado para coger su colección de mangas."
    "Se sube a la silla, pero incluso con la altura que le da, tiene que ponerse de puntillas por lo pequeña que es."
    "Me mira de reojo."
    show natsuki base uniform neut mh b3c at t11
    n "¿Qué haces todavía aquí?"
    n "Un... minuto."
    show natsuki base uniform neut e2a b3c
    "Los ojos de Natsuki se abren como platos cuando una idea cruza su mente."
    show natsuki base uniform neut blaw ml e4c b1c at h11
    n "¡¿No estarás aquí para mirarme bajo la falda, verdad?!"
    mc "¿¡E-Eh!?"
    mc "¡Pues claro que no!"
    mc "¡Trato de encontrar una solución, Natsuki!"
    show natsuki base uniform neut blaw ml e4c b1c at h11
    n "¡Largo, pervertido! ¡No te quedes ahí parado!"
    show natsuki base uniform neut blaw ml e4c b1c at h11
    n "¡Fuera!"
    show natsuki at thide
    hide natsuki
    "Me alejo del armario."
    show bg club_day
    with wipeleft
    mc "Joder... vaya conversación de la que acabo de ser partícipe."
    "Vuelvo a mi escritorio."
    "Me doy cuenta de que Monika, Sayori y Yuri ya están en la sala del club."
    "Debo de no haberme percatado de su llegada durante mi pequeño altercado con Natsuki."
    "Lo que me tranquiliza es que no parecen haberle dado mucha importancia a lo que acaba de pasar."
    "Yuri ya está sentada en un escritorio, completamente inmersa en su lectura."
    "En cuanto a Monika y Sayori, están teniendo una conversación que parece bastante animada."
    "No puedo evitar notar que Monika me lanza una mirada de reojo."
    "Decido lanzarle una sonrisa, y ella hace lo mismo al momento de yo hacerlo."
    mc "-suspiro-... Volvamos a lo que estaba haciendo."
    "Me siento de nuevo en la silla y retomo la escritura."
    mc "Materiales necesarios..."
    "Coloco el bolígrafo en la siguiente línea, pero no muevo la mano."
    "Genial, padezco del bloqueo del escritor."
    mc "..."
    mc "Jodeeeer... la cabeza me da vueltas otra vez."
    "La punta del bolígrafo presiona el folio por un momento, dejando una minúscula mancha de tinta oscura."
    mc "Qué bien."
    $ y_name = "????"
    y "O- oye, [player]..."
    $ y_name = "Yuri"
    show yuri base uniform neut awkw rup md e2b b1b at t11
    "Levanto la cabeza y veo a Yuri de pie en frente mía."
    mc "Dime, Yuri, ¿en qué puedo ayudarte?"
    "Veo que sus manos tiemblan con ligereza."
    show yuri base uniform neut awkw rup mb e2b b1b
    y "Pe- perdón por molestarte mientras estás ocupado, pero..."
    show yuri base uniform neut awkw rdown mb e2b b1b
    y "Tengo una pequeña petición que hacerte, si no te importa..."
    mc "Oye, Yuri, relájate. Tranquila, ni que te fuera a gritar o algo así."
    show yuri base uniform neut awkw rup mb e1b b1b
    y "Ajaja... tienes razón, perdona..."
    y "No sé a qué vienen estos nervios repentinos, ajajaja..."
    mc "Respira hondo y dime, te escucho."
    mc "Sin prisa."
    show yuri base uniform neut lup rup mf e4a b1c nobl at s11
    "Yuri coge aire."
    show yuri base uniform neut lup rup mg b1a e1a at t11
    y "Bueno... ya sabes... que me encanta leer mucho."
    show yuri base uniform neut rup ma e1b b1a
    y "Pero cuando leo en casa, en fin... me gusta leer con una buena taza de té calentito."
    show yuri base uniform neut rup ma e1b b1b
    y "Y aquí en el club... no hay teteras eléctricas."
    y "Así que me gustaría saber..."
    show yuri shy uniform happ awkw m1 e2 b1
    y "... si fuese posible pedir permiso a los profesores para traer una tetera con tazas de té..."
    "Después de esa petición, Yuri expulsa aire durante un largo tiempo, como si estuviese liberando todo el estrés acumulado dentro suya."
    show yuri shy uniform happ m1 e1 b1 n1
    mc "Veré lo que puedo hacer por ti, Yuri."
    y "Gra- gracias, [player]."
    show yuri base uniform happ nobl lup rup ma b1a
    mc "Puedo acercarme ahora, si quieres."
    show yuri base uniform happ nobl ldown rdown mh e1a b2c
    y "¿E- estás seguro...?"
    y "Me refiero, estabas ocupado y muy preocupado por lo que sea que tuviese tu papel... así que creo que era algo importante."
    mc "Podría decirse que sí lo es... pero eso puede esperar... me refiero, que esto lo puedo seguir en casa sin problemas."
    mc "Por ahora, lo que importa es encargarme de mis miembros."
    show yuri base uniform neut rup ma e1b b1b
    y "Eso es muy dulce de tu parte..."
    mc "¿Qué?"
    show yuri shy uniform n5 m2 at h11
    y "¡P- perdón...! O- olvida lo que acabo de decir..."
    y "No quería decir eso... ¡simplemente salió de mi boca...!"
    show yuri base uniform flus awkw lup rup mg e4a
    y "Solo... es que, a veces, hablo sin pensar cuando vengo de leer un rato..."
    y ".. y termino diciendo estupideces..."
    mc "Ah.. no te preocupes, Yuri, lo entiendo."
    mc "En momentos estresantes, acabamos diciendo cosas que no queremos."
    show yuri base uniform neut lup rup mf e4a b1c nobl at s11
    "Yuri exhala con alivio."
    show yuri base uniform flus nobl ldown rdown ma e1d b1b at t11
    y "Eres una persona muy considerada, [player]..."
    mc "Ajajaja... es una cualidad que todo el mundo debería tener, ¿no?"
    show yuri base uniform flus nobl ldown rdown ma e1b b1b
    y "Deberían..."
    "Yuri se queda en completo silencio."
    mc "I- Iré... iré a ver lo que puedo hacer, Yuri."
    show yuri base uniform flus nobl lup rup mb e1b b1b
    y "Gracias, de nuevo."
    show yuri at rhide
    hide yuri
    "Yuri vuelve a su mesa, dando continuación a su lectura."
    mc "..."
    mc "¡Monika!"
    "Decido llamarla."
    "Inmediatamente después de hacerlo, deja de hablar con Sayori y empieza a caminar hacia mí."
    "Cuando Sayori se queda sola, empieza a mirar alrededor y decide ir con Yuri."
    show monika base uniform neut mb at t11
    m "Hola, [player], ¿hay algo que quieras preguntarme?"
    mc "Claro. Voy a pedir una cosilla en la sala de profesores."
    mc "Así que, como eres mi vice presidenta, preguntaba si es posible que vigiles el club mientras no estoy."
    show monika base uniform neut mb rhip
    m "¡Claro, no me importa!"
    show monika base uniform neut me rdown
    m "¿Qué vas a pedir, si puedo preguntarte?"
    mc "Pues... pedir permiso para servir bebidas calientes dentro del club."
    mc "Como es peligroso por los riesgos de quemarte y demás, tienes que preguntar antes, ya sabes..."
    m "¿Quién te lo ha pedido?"
    mc "Yuri."
    mc "¡No tardaré!"
    mc "Aunque conociéndote, serás capaz de manejar esta situación con excelencia."
    show monika base uniform neut ma b1b
    m "Dime una cosa, [player]..."
    show monika lean uniform neut ma
    m "¿Me estás subestimando?"
    mc "¡Qu- qué va!"
    mc "¡TIenes mucha más experiencia que yo llevando un club!"
    show monika base uniform neut mb e4b rhip
    m "¡Ajajajajajaja! Es que es muy fácil molestarte."
    show monika base uniform neut ma e1a b1b
    m "Pero, ¿sabes... que no puedes juzgar un libro por su portada?"
    show monika base uniform neut ma b1b lpoint
    m "En realidad, siempre he tenido problemas cuando se trata de gestionar a los miembros. Admito que no es un punto fuerte por mi parte."
    mc "Anda... entonces estamos en el mismo nivel..."
    show monika base uniform neut ma b1b ldown
    m "Qué va, [player]. Parece que te las apañas muy bien, incluso mejor que yo."
    show monika base uniform neut ma e1a b1a
    mc "Gracias por el cumplido, supongo..."
    mc "Cuando vuelva, empezaremos a compartir poemas."
    show monika base uniform neut mb e4b
    m "¡Vale!"
    show monika base uniform neut mb e1a rhip
    m "Date prisa, [player], tengo algo de curiosidad por ver lo que has escrito."
    show monika lean uniform ma at h11
    m "Ejejeje~"
    mc "Y- y yo, Monika..."
    hide monika
    with wiperight
    show bg corridor
    with wiperight
    "Dejando la sala del club, me dirijo a la sala de profesores escaleras abajo."
    show bg corridor
    with dissolve_scene_full
    "Después de hablar con uno de los profesores allí presentes, pude pedir permiso, aunque fue algo difícil convencerles."
    "Vuelvo al club y abro la puerta, viendo la misma escena que había cuando me fui."
    play sound closet_open
    show bg club_day
    with wiperight_scene
    "Sayori y Yuri están hablando, mientras Monika escribe algo en una pequeña libreta."
    "Natsuki está sentada en el suelo leyendo lo que parece ser uno de los mangas que estaban en una de las cajas."
    "No parecen haber notado mi regreso."
    "Me acerco con cuidado a Sayori y Yuri."
    mc "Oye, Yuri, tengo buenas noticias para ti."
    show yuri base uniform neut nobl ldown rup mg e1d b1a at t11
    y "¿Ha- has podido?"
    "Asiento a modo de respuesta."
    show yuri base uniform neut nobl ldown rup ma e4b b1c at h11
    y "Muchísimas gracias, [player]."
    mc "Lo único malo... es que no nos conceden el equipo necesario."
    show yuri base uniform curi mf e1a b1a rdown
    y "¿Eh?"
    show yuri base uniform curi mg b1a
    y "¿A qué te refieres?"
    mc "A ver, que tendremos que traer nosotros una tetera."
    mc "Y más de lo mismo con las tazas."
    y "A-Ah.."
    show yuri base uniform curi ma e1b b1a
    y "Está bien. Mientras que nos hayan dejado... no me importa traer una tetera eléctrica y algunas tazas."
    mc "¿Segura?"
    show yuri base uniform curi ma e1a b1a
    y "Claro."
    show yuri base uniform curi blus ma e1b b1a
    y "Soy... soy una fánatica del té, tengo muchas tacitas en casa."
    show yuri base uniform curi blus ma e1b b1a at t21
    show sayori base uniform neut mb lup at t22
    s "¡Hola, [player]!"
    mc "Hola, Sayori, siento no haber saludado antes."
    show sayori base uniform mb e4b ldown
    s "Jajajaja, ¡no te preocupes!"
    show sayori base uniform ma e1a
    s "Por cierto, [player], ¡Yuri me dijo que quería darte un libro!"
    show yuri base uniform neut blaw rup ml e2a b1b
    y "¡Sa-Sayori! ¡No se lo deberías haber dicho justo ahora!"
    mc "¿Eh? ¿Un libro para mí?"
    show yuri shy uniform happ bful m2 e2
    y "Eeeehhh... e- en realidad no..."
    show sayori base uniform neut rup me e1a b1b
    s "Ay... perdóname Yuri, se me escapó..."
    show sayori base uniform neut me e1b b1b
    s "Lo siento muchísimo..."
    show sayori at thide
    hide sayori
    show yuri shy uniform bful m2 e2 at t11
    mc "¿Es verdad que me has traído un libro, Yuri?"
    show yuri base uniform neut awkw rup ml e2a b1b
    y "¡Olvídalo!"
    show yuri shy uniform happ nobl m2 e2 b2
    y "Sayori lo hizo parecer demasiado..."
    show yuri 4c
    y "Uuuuuuuu... qué hago ahora..."
    "Yuri frota con nerviosismo los mechones de su cabello largo y púrpura mientras aparta su mirada de mí."
    "Debería arreglar esta situación..."
    show yuri shy uniform happ nobl m1
    mc "Oye, Yuri, aprecio el regalo, en serio."
    mc "No importa de qué sea el libro, es genial saber que viene de ti."
    "Incluso sabiendo que nos conocemos desde el viernes..."
    mc "Y bueno, ¡ayudará a expandir la colección de libros que tengo en casa!"
    "Yuri inhala y exhala brevemente, tomando un poco de aire."
    show yuri base uniform happ ma e1a b1b
    y "... Si tú lo dices..."
    "Yuri mete la mano en su mochila, rebuscando un poco y sacando un libro."
    show yuri base uniform happ mb b1a
    y "Este es el libro que mencioné el viernes, que particularmente me gusta, y lo acabé este mismo fin de semana."
    show yuri base uniform happ e1b b1b
    y "Espero que te guste..."
    "Yuri me da el libro, mirando ligeramente a otro lado."
    "Cojo el libro con ambas manos y le devuelvo una sonrisa de confianza."
    mc "¡Gracias, Yuri! Me encargaré del libro tan pronto como pueda, no dudaré en empezar a leerlo."
    mc "Estoy seguro de que me encantará."
    show yuri base uniform happ lup rup mg e4a b2b at s11
    y "Uffff..."
    show yuri base uniform happ lup rup ma e1a b1c at t11
    y "Dependiendo de cuán rápido leas, te lo acabas en menos una semana si lees cada día."
    show yuri base uniform happ ldown rdown ma b1c
    y "El inicio puede no ser tan interesante, pero créeme que, cuanto más profundices en la historia, más interesante y relevante se vuelve."
    show yuri base uniform happ lup rup ma e1b b1c
    y "No... no diré más."
    y "No quiero destriparte la sorpresa."
    show yuri base uniform happ lup rup ma e1a b1c
    mc "¡Vale, Yuri! Lo tendré en cuenta cuando empiece a leerlo."
    show yuri shy uniform happ m1 e2 b2
    y "[player]... si quieres..."
    y "Cuando avances algo en la historia... o cuando empieces a leer..."
    show yuri shy uniform happ m1 e1 b1
    y "Po- podríamos hablar sobre el libro si quieres..."
    mc "¡Sería un gran placer, Yuri! ¡Me encantaría hablarlo contigo!"
    show yuri base uniform neut lup rup mg e4a at s11
    y "Ufff... qué alivio."
    show yuri base uniform neut lup rup ma e1b
    "Yuri sonríe discretamente."
    hide yuri
    with wipeleft
    "Voy a mi escritorio para poner el libro en mi mochila."
    "Me aclaro la garganta ligeramente antes de plantarme en medio de la habitación."
    mc "¡Vale, compis! ¡Poneos en frente mía!"
    "Las chicas dejan de hacer lo que estaban haciendo y caminan hacia mí."
    show monika base uniform neut ma at t44
    show sayori base uniform neut ma at t43
    show natsuki cross uniform neut ma at t42
    show yuri base uniform neut ma at t41
    mc "¡Tengo el placer de anunciar que podemos, finalmente, empezar nuestra primera actividad del club!"
    mc "¿Habéis escrito un poema para hoy?"
    show monika base uniform neut ma e4b
    show sayori base uniform neut mc lup rup e4b
    show yuri shy uniform e2 b2
    show natsuki cross uniform blaw md e1b b1f
    "Sayori y Monika asienten ambas con energía, mientras que Natsuki y Yuri lo hacen avergonzadas."
    mc "¡Genial! Entonces... ¡es hora de compartir poemas!"
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    with wiperight
    "Las chicas se dirigen a sus mochilas."
    "Sayori tiene una hoja arrugada en su mano, y Monika saca de su mochila una libretita."
    "Desde mi posición, puedo vislumbrar su perfecta y refinada escritura."
    "En cuanto a Yuri y Natsuki, sacan sus poemas con cierta reticencia."
    stop music fadeout 2.0
    show bg club_day1
    with wiperight_scene
    play music t5
    "Monika parecía impaciente por ver mi poema, así que decido empezar con ella."
    show bg club_day1
    with wiperight_scene
    show monika base uniform ma at t11
    mc "¡Hola, Monika!"
    m "¡Hola, [player]!"
    mc "¿Lista para compartir tu poema?"
    show monika base uniform mb e4b
    m "¡Por supuesto!"
    mc "Entonces, ¡empecemos!"
    "Hicimos un intercambio: su poema por mi poema y viceversa."
    call showpoem (poem_m11, img="monika base uniform ma b1a e1a") from _call_showpoem_1
    m "..."
    show monika base uniform mb
    m "Bueno, ¿qué opinas?"
    show monika base uniform ma b1a e1a rhip
    mc "Me gusta, Monika."
    mc "Mmmmm... Tiene un estilo muy... improvisado, creo que se llama."
    show monika lean uniform neut ma
    m "¡Ajajajaja, no pasa nada! Esa clase de estilo se ha puesto muy de moda últimamente."
    mc "Pues no lo sabía."
    show monika base uniform ma neut b1b rhip
    m "Tú eres más de leer que de escribir, ¿no, [player]?"
    mc "Ehhh... sí, lo has clavado."
    show monika base uniform neut mb b1a rdown
    m "¡Puedo darte pequeños consejos de escritura si estás interesado!"
    mc "Eso sería mejor hacerlo en privado."
    show monika base uniform neut ma e4b
    m "¡Muy bien!"
    show monika base uniform neut mb lpoint e1a
    m "¿No es divertido?"
    mc "¿El qué? ¿Que me des consejos de escritura?"
    show monika base uniform neut ma e4b ldown
    m "¡Claro! Creo que es bastante gracioso que le vaya a dar consejos de escritura a mi propio presidente, que precisamente, dirige un club de literatura."
    show monika lean uniform neut ma at h11
    m "Ejejejeje."
    mc "Lo dices como si yo no fuera capaz de aconsejar sobre literatura..."
    show monika base uniform neut me rhip b1b
    m "¡Ay, no, no quería decir eso! ¡Perdóname!"
    show monika base uniform neut ma rhip b1b
    m "En realidad, estoy segura de que podrías."
    mc "..."
    mc "De hecho, podría hacerlo de vez en cuando, cuando tenga algo interesante que comentar."
    mc "Prefiero calidad por encima de la cantidad."
    "Un breve silencio se cierne sobre nosotros, que es interrumpido por Monika."
    show monika base uniform neut ma lpoint b1a
    m "De todas formas... me gusta tu poema también, [player]."
    show monika base uniform neut ma ldown e4b b1a
    m "¡Es muy metafórico!"
    show monika base uniform neut ma ldown e1a
    m "Muy impresionante."
    mc "Ah, gracias... anoche me costó bastante empezarlo."
    show monika base uniform neut mb lpoint
    m "¡Ajajaja! ¿Sabes, [player]? Siempre te bloqueas cuando te concentras demasiado en un objetivo concreto, como en este caso, escribir un poema."
    show monika base uniform neut ma lpoint rhip
    m "¡Puede que presiones tanto el bolígrafo sobre el papel... que acabes con una mancha grande de tinta!"
    m "Piensa en esa mancha enorme como un río."
    m "Para que ese río de tinta fluya y avances con tu poema, ¡deja que el bolígrafo siga la corriente naturalmente!"
    show monika base uniform e4b mb
    m "¡Y verás como lo consigues!"
    mc "..."
    mc "Es curioso, porque eso mismo me ha pasado antes, mientras apuntaba unas cosas en un papel."
    show monika lean uniform ma
    m "¡Ajajaja! ¿No crees que ha sido una coincidencia bastante graciosa, [player]?"
    mc "Pues sí. Estaba liado con algunas cosillas que quiero preparar para el festival que hay el viernes que viene."
    show monika base uniform me rhip
    m "¿Ya has empezado a plantearlo?"
    mc "Claro."
    mc "Hablaré contigo sobre ello después de que todos hayamos visto nuestros poemas."
    show monika base uniform ma e4b rdown
    m "¡Vale, [player]!"
    mc "Gracias por enseñarme tu poema, Monika."
    show monika base uniform mb e4b rhip
    m "¡Gracias a ti!"
    "Nos los devolvemos antes de separarnos."
    show bg club_day1
    hide monika
    with wiperight_scene
    show sayori base uniform neut ma at t11
    mc "¡Hola, Sayori!"
    show sayori base uniform neut mb lup
    s "¡Ey, [player]!"
    mc "¿Cómo va eso de enseñar tu poema?"
    show sayori base uniform neut ma lup rup e4b
    s "¡Es súper divertido!"
    show sayori base uniform neut e2a mh ldown rdown
    s "¡Lo he intercambiado con el de Natsuki y tiene una manera de redactar muy diferente en comparación con la mía!"
    mc "¡Anda, eso es genial! Todos tenemos diferentes estilos de escritura, ¡y eso viene muy bien para el club!"
    show sayori base uniform neut e1a md
    s "¿En serio? ¿Y eso por qué?"
    mc "Bueno, si todos escribiésemos igual, ¿no sería un poco aburrido?"
    mc "Es decir... somos humanos, y somos diferentes intelectualmente. No sería interesante si tuviésemos el mismo estilo de escritura."
    mc "¿No crees?"
    show sayori base uniform neut awkw e1b b1b mc lup at s11
    s "Ja ja, bueno..."
    show sayori base uniform neut nobl e1a b1a ma ldown at t11
    s "Tienes razón, [player]."
    mc "Perdona, no quería sonar muy profundo..."
    mc "¿Te importaría si intercambiamos poemas?"
    show sayori base uniform neut e1a mb
    s "¡Claro que no!"
    "Le doy mi poema a Sayori."
    show sayori base uniform neut e2a mh b2a lup
    "..."
    show sayori base uniform neut b1a e1a ma ldown
    s "Vaya, ¡no sabía que escribías tan bien, [player]!"
    show sayori base uniform neut e4b mc lup rup
    s "¡Tu poema es el mejor!"
    mc "Sayori..."
    mc "Creo, sinceramente, que estás exagerando..."
    mc "En realidad, ni siquiera sabía lo que estaba escribiendo anoche."
    show sayori base uniform neut e1a mb rdown ldown
    s "¡Pues será por eso!"
    show sayori base uniform neut e1a mb rup
    s "Hay veces en las que, haciendo las cosas sin pensar, acaban saliendo verdaderas maravillas."
    show sayori base uniform neut e4b mc lup rup at h11
    s "¡Ajajaja!"
    "No sé si iba en serio... o es que es la típica que habla sin pensar..."
    mc "Ehh... gracias, Sayori."
    mc "Consideraré eso como un cumplido."
    mc "¿Quieres darme el tuyo ahora?"
    show sayori base uniform neut e1a mb rdown ldown
    "Sayori me devuelve el poema, dándome ella el suyo al mismo tiempo."
    call showpoem (poem_s11, img="sayori base uniform neut blus e1b b1b ma") from _call_showpoem_2
    mc "..."
    show sayori base uniform neut nobl e1a b1a ma
    mc "Es muy bueno, Sayori."
    mc "Lo escribiste un viernes, como dices en la tercera línea, ¿no?"
    show sayori base uniform neut e4b mc b1a lup rup
    s "¡Pues sí!"
    s "¡El viernes es el mejor día de la semana!"
    show sayori base uniform neut e1a ma ldown rdown
    s "Al menos puedo dormir un montón."
    mc "Emmm... sí..."
    show sayori base uniform neut me b2b lup
    s "¿Qué? ¿No estás de acuerdo conmigo?"
    mc "¡Pues sí, estoy de acuerdo contigo!"
    mc "Dormir mucho no es muy bueno, que digamos. Pero aún así..."
    mc "No soy quién para dar lecciones morales."
    show sayori base uniform neut mc e4b b1a lup
    s "Jejejeje, no te preocupes, [player], ¡la próxima vez escribiré el mejor poema del mundo entero!"
    mc "Excelente, Sayori. Estoy impaciente por ver si has mantenido tu palabra en pie."
    show bg club_day1
    hide sayori
    with wiperight_scene
    show yuri base uniform neut ma at t11
    y "Hola, [player]."
    mc "¡Hola, Yuri!"
    mc "¿Va todo bien?"
    show yuri base uniform neut ma e1b b1b rup lup
    y "Sí... E- es que me da algo de nervios eso de compartir poemas..."
    mc "¡No pasa nada, Yuri! Todos estamos con los nervios."
    mc "Es una pequeña barrera que se interpone ante cada uno de nosotros, ¡pero estoy seguro de que aprenderemos a cruzarla con efectividad!"
    mc "Es cuestión de tiempo coger confianza y adoptar más tranquilidad a la hora de compartir poemas con las demás."
    show yuri base uniform neut ma e1a b1a ldown
    y "Sí, lo más probable es que acabe siendo así."
    mc "¿Qué tal si empezamos intercambiando los nuestros?"
    show yuri base uniform neut ma e4b b1a rup lup
    y "¡Sí, por favor!"
    "Yuri me sonríe con felicidad mientras me ofrece su poema."
    "Lo cojo y comienzo a leerlo."
    call showpoem (poem_y1) from _call_showpoem_3
    "..."
    show yuri base uniform neut e1a ldown rdown
    "Me gusta, Yuri."
    show yuri base uniform neut mh e1a b1b rup lup
    "Monika estaba en lo cierto cuando dijo que Yuri sería un gran activo para el club."
    show yuri base uniform neut mh e1a b2c rup lup
    y "... Y- yo... ¡pido disculpas por tener una letra tan sumamente horrible!"
    mc "¿Qué?"
    mc "No, no... pero si tu letra es muy bonita, Yuri."
    show yuri base uniform neut mh e1b b2c rup lup
    y "Pero es que te has pegado un buen rato leyéndolo..."
    mc "¿Sí? ¿Eso crees?"
    show yuri base uniform neut mg e1b b1b rup lup at s11
    "Yuri asiente, avergonzada."
    mc "Perdona, es que..."
    mc "No me acostumbro a la letra cursiva."
    mc "Pero, dejando eso de lado... tu poema ha sido impresionante, me gusta."
    show yuri base uniform neut ma e1a b2a rup ldown at t11
    y "Ah.. gracias, normalmente escribo poemas algo más largos..."
    show yuri base uniform neut mb e1a b1a rup ldown
    y "Como es la primera vez que intercambio un poema con alguien, quería que fuese una lectura más suave."
    show yuri base uniform neut mb e1b b1a rup ldown
    y "Algo fácil de digerir."
    mc "Anda, Yuri, es muy generoso de tu parte haber pensado en los demás."
    show yuri shy uniform b1 e1 m1
    mc "Pero no te pongas barreras por delante. Quiero decir, ¡no limites tus acciones comparándote con las demás!"
    show yuri shy uniform b1 e2 m1
    mc "Estoy muy seguro de que tienes la habilidad para escribir cosas maravillosas, Yuri."
    mc "¡Y tu poema lo demuestra a la perfección!"
    show yuri shy uniform b1 e1 m2
    mc "¡Incluso podrías enseñarle a la gente cómo escribir mejores poemas!"
    y "..."
    show yuri shy uniform b1 e2 m1
    y "T- tengo algunas dificultades hablando con las personas..."
    mc "Estoy seguro de que podrás lidiar con esa pequeña barrera algún día, Yuri."
    mc "Gracias por compartirlo conmigo."
    show yuri shy uniform e2 b1 m1
    "Le devuelvo a Yuri su poema con una mano, mientras con la otra le doy el mío."
    mc "Toma, ¡dime qué tal!"
    show yuri shy uniform e2 b1 m1
    "Yuri sostiene mi poema y comienza su lectura."
    show yuri base uniform neut e1b b1d mf rup
    "..."
    show yuri base uniform neut e1b b1a ma rup lup
    "....."
    show yuri base uniform neut e1b b1d mf rup ldown
    "......."
    "Pasa un minuto entero en total silencio."
    "Los ojos de Yuri siguen fijos en mi poema. Su cara muestra una expresión muy intensa."
    mc "Eh... ¿Yuri?"
    show yuri base uniform neut e2a b1b mk b1b rdown
    y "¡A-AY! Aún no he dicho nada, ¿verdad?"
    mc "Emmm... sí."
    mc "¿Tengo mala letra?"
    show yuri base uniform neut e2a ml b1b rup lup blaw
    y "¿Qu- qué? ¡No!"
    show yuri base uniform neut e2b mk rup ldown
    y "¿He alzado la voz?"
    show yuri shy uniform n5 m2
    y "Uuuu... lo siento muchísimo..."
    show yuri shy uniform nobl m2 e2 b1
    mc "Tranquila, Yuri, soy yo el que debe disculparse. No imaginaba que siguieses leyendo mi poema..."
    show yuri base uniform e2b b1b awkw mb rup
    y "Ah, no... no te disculpes..."
    show yuri base uniform e4a b1a mf nobl rup lup at s11
    "Yuri respira hondo."
    show yuri base uniform e1a ma rdown ldown at t11
    y "Tu poema es muy... intrigante."
    show yuri base uniform neut e1a ma rdown
    y "Está bien montado, y es muy metafórico."
    mc "Gracias, Yuri, es genial escuchar eso de alguien que está acostumbrada a leer prácticamente cada día."
    show yuri base uniform neut e1b ma b1b blaw
    y "N- no es nada, en serio..."
    show yuri base uniform neut e1a ma b1a nobl
    y "¿Quiere eso decir que escribes poemas con frecuencia?"
    mc "Bueno, en realidad... hace tiempo que no escribía uno."
    show yuri base uniform neut e1a mf b1a nobl
    y "¿Qué?"
    show yuri base uniform neut e1b mf b1a nobl rup
    "Yuri pasa su dedo por el folio."
    show yuri base uniform neut e1b mf b1a nobl rdown
    y "..."
    show yuri base uniform neut e2b mb b1b awkw
    y "¡Y- ya, es que..!"
    show yuri base uniform neut e1a ma b1a nobl
    y "Ejem, a ver... me he dado cuenta de que habían algunos errores, pero nada alarmante."
    mc "Ah... gracias, y, ¿cuáles son esos errores de los que hablabas?"
    show yuri base uniform neut e2b mk b1b awkw at s11
    y "A-Ah, emmm..."
    "Yuri se hunde en su silla."
    show yuri shy uniform m1 e2 b1 nobl at t11
    y "Yo... a ver, lo vas a entender de la manera incorrecta..."
    mc "Ajajajaja, ¿por qué tendría que entenderlo de otra manera que no sea la que quieres darme a entender, Yuri?"
    show yuri shy uniform m1 e1 b1
    mc "¡Eres muy buena criticando nuestra manera de escribir!"
    show yuri shy uniform m2 e2 b1
    y "¿Criticando...?"
    show yuri base uniform neut e2b b1b mk rup blaw
    y "¡Nunca criticaría vuestros poemas...! No puedo..."
    mc "Ah... perdona, quería decir que..."
    mc "... eres la persona a la que hay que acudir para poder mejorar nuestros poemas."
    show yuri base uniform e2a mk rup lup blaw
    y "Eh... [player], estás siendo un poco exagerado..."
    show yuri base uniform neut e4a mf nobl rdown ldown nobl
    "Yuri respira hondo."
    show yuri base uniform neut e1a b1a ma
    y "... Aún así..."
    show yuri base uniform neut e1b b1b mb
    y "Es que hay ciertos hábitos de escritura que desarrolla cada escritor de forma exclusiva."
    show yuri base uniform neut e1b mb rup
    mc "Y concuerdo contigo, Yuri. Hace nada hablé con Sayori acerca de este mismo tema, mientras estábamos intercambiando poemas."
    mc "¿Crees que eso es un problema?"
    show yuri base uniform neut e1a b1a mf rup
    y "En realidad no... solo que depende de cómo reaccionen los demás..."
    show yuri base uniform neut e1b b1d rup lup
    y "Es decir, hay gente que se dedica a cachondearse de la escritura de otras personas."
    show yuri shy uniform e2 m1 b2
    y "Y no te voy a mentir, estaba un poco preocupada sobre eso de intercambiar poemas y tal..."
    y "Tenía miedo de ser criticada por lo que escribo, y solo porque... la gente suele burlarse del trabajo de los demás solo por no entender el mensaje..."
    y "Y es por eso que tenía tanto miedo, para ser honesta..."
    show yuri base uniform neut e4a b1b mf rup
    y "Al final, mi miedo era infundado... porque con Monika y Sayori fue genial, eran muy amables..."
    $ yref()
    show yuri shy uniform e1 m1 b1 at s11
    y "Y contigo también..."
    "..."
    show yuri base uniform e2b awkw mb rup b1b at t11
    y "Ya estoy empezando a divagar, ¿verdad...?"
    mc "Escúchame, Yuri, no consideraré miembros en mi club que se dediquen a criticar a malas el trabajo de los demás."
    show yuri shy uniform e2 m1 b2
    mc "¡La razón por la cual decidí hacer esta actividad es para que todos los miembros conozcan la escritura de sus compañeros de club!"
    "{i}(Aunque ni siquiera haya pensado así al crearla, se me ha ocurrido decir eso.){/i}"
    show yuri shy uniform e1 m1 b1
    mc "¡Me enorgullece que estés soltándote con las demás! ¡Quizás, si sigues simpatizando y estrechando lazos, puedas hacerte amiga de ellas!"
    y "¿A- ami- amigas...?"
    mc "Claro."
    show yuri base uniform neut e1b b1b ma rup blus
    y "Eso... es algo que me encantaría..."
    show yuri shy uniform e1 m1 b1 n1 at s11
    y "Ser... amiga de todos los miembros..."
    mc "Ah..."
    "Creo que dije de más, esta charla ha llegado a un extremo un tanto frágil."
    mc "Gracias por leer mi poema, Yuri. ¿Me lo devuelves?"
    show yuri base uniform neut e2b mb b1b rup at t11
    y "A-Ah, sí, perdona..."
    "Noto que Yuri, mientras sostiene mi poema en su mano, lo arruga un poco."
    "Se lo quito."
    show yuri shy uniform m1 b2 e2
    y "Pe- perdón por lo de tu poema... fue el estrés de la situación."
    mc "No pasa nada."
    show bg club_day1
    hide yuri
    with wiperight_scene
    show natsuki base uniform neut b1a md at t11
    mc "Hola, Natsuki."
    show natsuki base uniform neut b1a mg
    n "Hola, [player]."
    mc "¿Lista para enseñarme tu poema?"
    show natsuki cross uniform neut e1b b1a md awkw
    n "Hmmmm, acabemos rapidito, espabila."
    show natsuki cross uniform neut e1b b1b md nobl
    n "Aunque no te va a gustar."
    mc "¿Por?"
    mc "Ni lo he leído y ya estás diciéndome lo que pueda o no pensar."
    show natsuki base uniform neut fs m3 e4 b2 at h11
    n "¡Sí, sí, lo que tú digas!"
    "Natsuki me da su poema con mucha furia."
    mc "Gracias, supongo..."
    call showpoem (poem_n1, img="natsuki base uniform rhip lhip e1a b1b mg") from _call_showpoem_4
    n "¿Ves? Lo que dije antes, no te gusta."
    mc "Pues es todo lo contrario."
    show natsuki cross uniform neut e1a b1d mg
    n "Si eres tan amable, deja de mentirme en la cara."
    mc "¡Oye!"
    mc "¡Si es que 'me gusta' tu poema, no es mentira!"
    mc "¿Por qué te estás interiorizando de que 'no' me gusta tu poema?"
    show natsuki base uniform neut fs m3 e4 b2
    n "¡Pues...!"
    $ nref()
    show natsuki cross uniform e1b b1d mh awkw
    n "... Porque la gente no me toma en serio."
    n "Lo único que sale de la boca de la gente es « ¡Qué monaaaa! », o simplemente dicen « Me gusta. » sin ningún tipo de sentimiento. ¡Parece que lo hacen para quitarme de en medio!"
    show natsuki cross uniform neut e1a b1a md
    mc "Entonces, déjame que lo entienda... ¿solo porque he dicho que 'me gusta tu poema', ya piensas que soy un mentiroso y no te estoy tomando ni a 'ti' ni a 'tu poema' en serio...?"
    show natsuki cross uniform neut e1b b1f md blaw
    n "Hum."
    mc "Natsuki... lo que has escrito demuestra que te tomaste el poema en serio."
    show natsuki base uniform neut mf e1a b1a nobl
    "Natsuki trata de decir algo, pero se queda boquiabierta sin decir una sola palabra."
    show natsuki cross uniform neut md e1b b1a
    mc "No entiendo por qué no debería tomarte en serio."
    show natsuki cross uniform neut mg e1b b1d awkw
    n "Casi todos los que conozco en este antro son así. Nunca me toman en serio."
    mc "A ver... escucha, Natsuki, en este club, serás tomada completamente en serio."
    "Qué respuesta más elaborada, [player]..."
    show natsuki base uniform neut mg e1a b1a nobl rhip
    n "Gracias, supongo... que al final no eres mal presidente."
    mc "Ah, bueno, ¿lo era hasta hace un momento...?"
    show natsuki cross uniform neut mg e1b b1a
    "Natsuki no me responde..."
    "... así que decido devolverle el poema."
    mc "¿Vas a leer mi poema?"
    show natsuki base uniform neut ma e1a b1a lhip rhip
    n "Sí."
    "Le doy mi poema."
    "Pasa un ratito antes de que Natsuki me lo devuelva."
    mc "¿Ya lo has leído?"
    show natsuki cross uniform neut mg e1a b1a
    n "Escucha... no tengo nada que decirte."
    mc "¿Nada?"
    show natsuki base uniform neut mh e1a b1f
    n "¿Qué quieres que te diga?"
    show natsuki base uniform neut fs m3 e4 b2 at h11
    n "¡Tu poema es muy bueno, joder!"
    $ nref()
    show natsuki cross uniform neut mg e1a b1a
    n "Aunque no haya entendido una mierda."
    "... Vale."
    mc "Ah... gracias, supongo."
    show natsuki base uniform neut mg e1a b1a
    n "Que sí, que sí. Toma tu poema."
    "Me incrusta el poema en el pecho, lo que hace que retroceda con un poco de dolor."
    mc "¡O- Oye... cuidado con lo que haces..!"
    show natsuki base uniform neut e4a mc blaw b3b rhip lhip
    n "Ajajajaja, ¿qué crees?"
    n "¡Solo porque sea la más enana, no quiere decir que sea la más enclenque!"
    mc "No he dicho eso..."
    show natsuki base uniform neut e4b mo b3c rhip ldown nobl
    n "¡Ya está, que era una bromita, coño!"
    "Natsuki puts on a wide smile."
    "No creo que eso sea 'una bromita', pero preferiría no ofenderla."
    mc "Sí, ya... gracias por leer mi poema, Natsuki."
    stop music fadeout 2.0
    show bg club_day1
    hide natsuki
    with wiperight_scene
    play music t3
    mc "Uffff... creo que ya están todas."
    mc "Ha sido un poco más estresante de lo que creía."
    mc "Pero creo que lo he hecho bien."
    "Echo un vistazo alrededor."
    "Monika acaba de compartir su poema con Yuri."
    "Me dirijo hacia ella."
    show monika base uniform neut ma rhip at t11
    mc "¡Estoy de vuelta, Monika!"
    mc "¿Te apetece hablar un rato sobre los planes que tenemos que hacer para el festival?"
    show monika base uniform mb e4b rhip
    m "¡Claro!"
    show monika base uniform ma e1a rhip
    "Monika y yo unimos dos escritorios."
    mc "Entonces..."
    mc "Un minuto."
    hide monika
    with wipeleft
    "Vuelvo hacia el lugar en el que dejé mi papel con algunas cosas escritas, y vuelvo con Monika, que está ya sentada en su silla."
    "Me siento también, poniendo el folio en medio de las mesas, lo que le permite verlo con claridad."
    "No sé por qué estoy haciendo esto, pero siento que me ayuda a dejar un pequeño marcapáginas. Ya sabes, para evitar perderme en mis pensamientos."
    show monika base uniform ma rhip at l11
    mc "Para darte una explicación concisa de lo que tenía pensado, quería hacer folletos impresos con cada uno de nuestros poemas."
    show monika base uniform me rdown
    m "Hmmmmm, eso pinta bien, ¿tienes alguna idea más?"
    mc "A ver, no he tenido mucho tiempo para pensar en ello."
    show monika base uniform me e4a
    "Monika se queda pensativa por un momento."
    show monika base uniform mb e1a rhip
    m "¡Tengo una idea!"
    mc "¿Sí?"
    show monika base uniform ma e1a lpoint
    m "¿Cómo suena hacer un recital de poemas?"
    mc "¿Te refieres a redactarlos en frente de un público...?"
    show monika base uniform mb e4b ldown rdown
    m "¡Síp!"
    show monika base uniform mb e1a rhip
    m "¡Cada una escogerá un poema que hayamos escrito anteriormente y lo recitaremos en público!"
    mc "Uuuuu..."
    show monika base uniform mb e4b lpoint
    m "¡Aún así!"
    show monika base uniform mb e1a rhip ldown
    m "¡Los invitados, si desean, también podrán participar en el recital!"
    "La verdad es que... no tengo mucha fé en que alguien del público quiera salir."
    "¿Qué pensarán las demás chicas?"
    mc "¿Crees que es una buena idea?"
    show monika base uniform ma e4b ldown rdown
    m "¡Absolutamente!"
    mc "Y, ¿qué pensarán las demás?"
    mc "Me refiero... no han pasado ni dos días desde que se unieron al club."
    mc "Puede que les sea algo repentino, ¿no?"
    show monika base uniform me e1a rhip
    m "Hmmmm... la verdad es que tienes razón, no había pensado en ello."
    show monika base uniform mb e1a rhip lpoint
    m "Pero podemos intentar llevarlas a nuestro terreno, tranquilizarlas un poco."
    mc "Ya, es cierto."
    mc "A veces, me como la cabeza demasiado y sin buenas razones para ello..."
    mc "Pero confío en ti, Monika, y creo que tu idea es genial."
    mc "¿Cómo vamos a organizar todo esto?"
    show monika base uniform me e1a ldown
    m "¿A qué te refieres?"
    mc "Bueno, para-{w=0.04}{nw}"
    stop music fadeout 2.0
    n "No me he percatado de que tenías tanta dedicación en darle buenas impresiones a nuestro presi, Yuri."
    mc "¿Eh?"
    show monika at lhide
    hide monika
    pause 0.1
    show yuri base uniform neut e4a b1a mf rup blus at r21
    show natsuki base uniform neut e4a b3a rhip lhip blaw mc at r22
    "Dirijo mis ojos a Natsuki y Yuri. Natsuki está de pie mientras que Yuri está sentada en su silla."
    play music t7 fadein 2.0
    show yuri base uniform neut e2a b1b mk rup blaw
    y "¿Qu- Qué?"
    y "N-No..."
    y "No trato de..."
    show yuri base uniform neut e2b b1b mk rup lup
    y "Tú... solo tratas..."
    show yuri base uniform neut e2b b1b mk rup lup at t31
    show natsuki base uniform neut e4a b3a rhip lhip blaw mc at t32
    show sayori base uniform neut e1b b1b mc blaw rup at r33
    s "Ey..."
    s "¿Va todo guay----?{w=0.02}{nw}"
    show sayori base uniform neut e4c b1b ml blaw rup lup at h33
    pause 0.04
    show sayori at rhide
    hide sayori
    show yuri base uniform neut e2b b1b mk rup lup awkw at t21
    show natsuki base uniform neut e4a b3a rhip lhip blaw mc at t22
    "De pronto, Yuri se levanta."
    show yuri base uniform neut e1a b1e mh rup ldown nobl
    y "¡Quizá estás celosa de que [player] haya disfrutado de mi poema mucho más que con el tuyo!"
    show natsuki base uniform e2a b1e mm rhip lhip
    n "¡Grrrr..! {nw}{done}¡¿Cómo sabes que no ha disfrutado mi poema y el tuyo SÍ?!"
    show natsuki base uniform neut e1a b1e mi blaw
    n "¡Grrrr..!{fast} ¡¿Cómo sabes que no ha disfrutado mi poema y el tuyo SÍ?!"
    show natsuki cross uniform neut e1a b1e mi
    n "¡¿De dónde has sacado tantas confianzas?!"
    show natsuki cross uniform neut e1a b1e mm
    show yuri base uniform e1b b1a rup mh
    y "No... no es lo que yo..."
    y "Si tuviese..."
    y "Si tuviese tanta confianza en mí misma..."
    "Me levanto de mi silla y pongo rumbo a Natsuki y Yuri."
    mc "Eh... qué ocurre----{w=0.02}{nw}"
    show yuri base uniform neut e1a b1e mh rup ldown
    y "¡Buscaría cualquier manera para parecer súper mona a propósito!"
    show natsuki base uniform e2a b1e mm blaw rdown ldown
    n "¡Mmmmmmmmm...!"
    show natsuki base uniform e1a b1e mi rhip lhip
    n "¡¿SABES QUÉ?!"
    show natsuki cross uniform e1a b1e mi blaw
    n "¡¡NO SOY A LA QUE LE HAN CRECIDO LAS TETAS POR ARTE DE MAGIA CUANDO SE UNIÓ A ESTE PUTO CLUB!!"
    show natsuki cross uniform e1a b1e mm blaw
    show yuri base uniform e2a ml b1b rup lup blaw at h21
    y "¿¿Qu- Qué has dicho??"
    show natsuki cross uniform e1a b1e mm blaw at t32
    show yuri base uniform e2a ml b1b rup lup at t31
    show sayori base uniform neut e4c b1b ml blaw rup lup at h33s
    s "¡No me gustan las confrontaciones! ¡Parad ya, chicas!"
    show sayori flip at rhide
    hide sayori flip
    show natsuki cross uniform e1a b1e mm blaw at t22
    show yuri base uniform e2a ml b1b rup lup at t21
    $ renpy.music.set_volume(0.3)
    mc "¡SUFICIENTE!"
    mc "¡¿Qué coño pasa con vosotras dos?!"
    show yuri shy uniform b2 e2 m2 n1
    mc "¿¿¿Cómo hemos llegado a este punto de la pelea???"
    show natsuki base uniform e1a b1e mi
    n "¡Ha sido ella la que empezó a molestarme!"
    "Natsuki adopta una voz agria para defender su inocencia."
    $ yref()
    show yuri base uniform neut e2a b1b ml rup blaw
    $ renpy.music.set_volume(1.0)
    y "No... ¡no es cierto...!"
    show yuri base uniform neut ml lup blaw
    y "¡[player]! ¡No la escuches! ¡Ella es la que ha empezado a criticar mi estilo de escritura en primer lugar!"
    y "Ella... ¡Solo quiere hacerme ver como la mala del cuento!"
    show yuri base uniform neut mk e2b b1b rdown ldown
    show natsuki cross uniform neut mi e1a b1e blaw
    n "¡¿Estás de coña?!"
    show natsuki cross uniform neut mm e1a b1e blaw
    n "¿¿Te estás escuchando al hablar??"
    show natsuki base uniform e2a mi b1e
    show yuri shy uniform n5 m2 awkw
    n "¡Has sido tú la que me ha criticado en primer lugar, diciendo que mi poema es una monada cuando, obviamente, no lo es!"
    show natsuki base uniform e4a mi b3a
    n "¡No has entendido absolutamente nada del poema!"
    y "Yo solo...{w=0.05}{nw}"
    show natsuki base uniform e2a mi b1e
    n "¿Y tienes los cojones de decir que tengo yo la culpa?"
    show natsuki base uniform e4a mi b3a
    n "¡Es inaceptable!"
    show natsuki base uniform e1a b1e mi rhip lhip
    n "¿Sabes lo que sería mejor?"
    show natsuki base uniform e4a mi b1e
    n "¡Es...-!{w=0.09}{nw}"
    stop music
    mc "¡PARAD DE UNA PUTA VEZ!"
    show natsuki cross uniform md e1a b1f blaw
    mc "Natsuki, ¡estás cruzando un punto de no retorno!"
    show yuri shy uniform n1 b1 e2 m1
    mc "Me ha gustado el poema de ambas."
    mc "Tenéis dos estilos de escritura que no tienen nada que ver entre sí, eso es cierto."
    mc "Y algo tengo que decir."
    mc "Me da igual si el poema es corto o largo."
    show yuri shy uniform n1 b1 m1
    mc "Lo que importa son las palabras impuestas en el poema."
    mc "Yuri."
    show yuri shy uniform n1 b1 e1 m1
    y "¿...?"
    mc "Eres una escritora con talento, lo admito."
    $ yref()
    show yuri base uniform e2b b1b mb rup blaw
    y "Bueno... es que..."
    $ yref()
    show yuri base uniform e2a b1b md rup blaw
    mc "Pero, no porque la escritura de otra persona sea poco refinada, ¡no quiere decir que no ponga sus emociones al hacerlo!"
    mc "Por eso Natsuki se sintió ofendida cuando dijiste que su poema es mono."
    show yuri base uniform e2b mg b1b rup lup nobl at s21
    y "Eh... a ver... lo siento... no quería... en serio..."
    show yuri shy uniform e2 m2 b1 at t21
    show natsuki base uniform e4a mc b3b blaw rhip lhip
    n "¿Ves?"
    n "Al final eras tú la que-"
    mc "Natsuki, lo mismo va por ti."
    show natsuki base uniform e1a b1a mh blaw
    n "¿Qué? ¡Pero...!"
    mc "¡Te has tomado el comentario demasiado a pecho!"
    mc "¡Si le hubieras dicho tus pensamientos a Yuri sin enfadarte, y con calma, esta pelea absurda nunca hubiera ocurrido!"
    show natsuki base uniform e1a b1e mi
    n "¿Estás de coña?"
    show natsuki base uniform e1a b1e mi rdown ldown
    n "¡Es que eso fue lo que hice!"
    show natsuki cross uniform md b1b e1a
    mc "Natsuki. Yuri se ha disculpado."
    mc "¿No crees que deberías disculparte con ella también? Vamos, hazlo."
    show natsuki base uniform e1a mm b1e
    n "¡Grrrrr...!"
    mc "Natsuki, te lo repito una vez más, discúlpate con Yuri."
    show natsuki base uniform mm e4a b3a
    "Natsuki respira hondo antes de darse la vuelta."
    show natsuki cross uniform e1b b1b md at s22
    n "Escucha, Yuri..."
    show natsuki cross uniform e1a b1b mg
    n "Yo..."
    show natsuki base uniform e1b b1b md
    n "Sobre lo que te dije... ya sabes... no quería decir eso, en serio."
    show natsuki cross uniform e1b b1b md
    n "Perdón por ser tan bruta."
    show natsuki cross uniform e1a b1b md
    show yuri base uniform e1b b1b ma awkw
    y "Acepto tus disculpas... yo también lo siento por criticar tu estilo de escritura, no quería decir eso... otra vez."
    "Natsuki no responde, solo asiente con la cabeza."
    mc "¡Muy bien! Me alegro de que hayáis podido zanjar esto fuera de la corte."
    mc "Espero que no tenga que volver a lidiar con esta clase de cosas."
    show yuri at lhide
    show natsuki at rhide
    hide yuri
    hide natsuki
    "Natsuki y Yuri siguen con sus poemas, cada una dispersa en sus propias esquinas."
    "La pesada atmósfera que estaba atada a la habitación del club empieza a disiparse y se vuelve algo más relajada."
    play music t8 fadein 4.0
    show monika base uniform neut ma b1b at t11
    "Me giro hacia Monika, que tiene una pequeña sonrisa en sus labios."
    show monika base uniform neut mb b1b
    m "¿Sabes, [player]...? Me alegro de que hayas podido con esta pelea."
    show monika base uniform neut mb e4b awkw rhip
    m "Puedo haber sido vice presidenta del club de debate y ser buena planeando cosas, pero tengo una debilidad con esto de los altercados con los miembros del club."
    show monika base uniform neut ma e1b b1b blaw
    m "No me imagino si hubieses estado ausente, jajaja."
    mc "No te preocupes, Monika. No soy muy bueno planeando cosas."
    mc "Cada cual tiene su buen talento, digo yo."
    mc "¿Seguimos?"
    show monika base uniform neut mb e1a b1a nobl
    m "¡Claro, vamos!"
    show monika at thide
    hide monika
    stop music fadeout 2.0
    show bg club_day1
    with dissolve_scene_full
    play music t3 fadein 3.0
    "El resto de la reunión transcurre sin ningún suceso importante."
    "Monika y yo trabajamos en unísono haciendo el boceto de los folletos del festival."
    "Aunque me surgieron algunas dudas en el proceso, pero ella fue capaz de resolverlas a base de buena argumentación."
    "Me dijo que pensaría en la organización más tarde."
    "..."
    mc "Me parece perfecto..."
    "Pongo el papel de vuelta en mi mochila."
    show monika base uniform neut mb rhip at t11
    m "Creo que podemos dar esta reunión por finalizada."
    "Miro la hora en mi móvil."
    "{i}6:05 PM{/i}"
    mc "Síp."
    mc "Ha sido genial poder trabajar contigo, Monika."
    show monika lean uniform neut ma at face(y=750)
    with Dissolve(0.10)
    "De pronto, Monika se acerca a mi oído, susurrándome."
    m "{i}Y... en realidad, trabajaremos mucho mucho más juntos, si es que eso te parece bien.{/i}"
    show monika base uniform e1f ma at t11
    "Monika se aleja de mí sonriendo, lo que hace que sienta un nudo en el estómago, que provoca que toda la sangre suba a mi cabeza del tirón."
    show monika base uniform e4b ma
    mc "I- Igualmente, Monika..."
    show monika at lhide
    hide monika
    "Me levanto de la silla, un poco descolocado."
    show sayori base uniform neut ma at t41
    show monika base uniform neut ma e4b rhip at t42
    show yuri base uniform neut ma at t43
    show natsuki cross uniform ma at t44
    mc "¡Vale, compis! ¡Venid si podéis!"
    mc "Qué pensáis de-"
    show natsuki cross uniform mg b1a
    n "Una cosilla te quiero preguntar, [player]... ¿por qué tienes la cara colorada?"
    mc "Emmm... ¿de qué hablas, Natsuki?"
    "No puedo evitar soltar una pequeña y estresada risita."
    mc "Ajajaja... solo es un poco de estrés, no es nada."
    show natsuki base uniform mc
    n "No seas tonto."
    show natsuki base uniform e4b mo b3c rhip
    n "¡Nos lo puedes estar contando!"
    show sayori base uniform e4b mc rup lup
    s "Ejejejeje, ¡estás más rojo que un tomate, [player]!"
    mc "..."
    mc "... Es que tengo calor."
    show natsuki cross uniform e1a mc b1a
    n "No te creas que eso es una excusa muy impresionante, [player]."
    "Me estoy quedando atrapado en un callejón argumentativo sin salida y necesito cambiar el tema de conversación tan pronto como sea posible."
    mc "... ¡A ver...!"
    mc "... ¡De todas maneras...!"
    mc "¿Qué tal ha estado esta actividad poemil?"
    mc "¿Monika?"
    show monika base uniform mb e1a b1a
    m "La verdad es que ha sido una actividad muy divertida."
    show monika base uniform rdown
    m "Me refiero, ha sido divertido descubrir el estilo de escritura de las chicas."
    show monika base uniform ma
    mc "¿Sayori?"
    show sayori base uniform e1a b1a mb lup rdown
    s "¡Ha estado muy guay! Me ha encantado."
    mc "¿Yuri?"
    show yuri base uniform e1a b1a mb rup ldown
    y "Ha estado muy bien, por encima de todo."
    show yuri base uniform e1b b1a ma rup ldown
    mc "¿Natsuki?"
    show natsuki base uniform e1a b1a mg
    n "Sí, ha estado muy bien, si es que se puede considerar así."
    mc "¡Genial! ¡Sugiero, entonces, que hagamos esto otra vez el lunes!"
    mc "¡Habéis aprendido un poco más de vuestro estilo de escritura! ¡Estoy seguro de que vuestros poemas serán diez veces mejor la próxima vez, y querréis probar algo nuevo!"
    mc "¡Podemos finalizar la reunión del club! ¡Pasad un genial resto del día y nos vemos el lunes!"
    show natsuki at rhide
    show yuri at rhide
    show monika at lhide
    show sayori at lhide
    hide monika
    hide yuri
    hide natsuki
    hide sayori
    "Todas se dispersan, yendo cada una a ocuparse de sus asuntos."
    "Me dirijo a mi mochila para guardar las cosas también."
    "De pronto, siento una mano amiga posada en mi hombro, asustándome un poco."
    m "Una cosa, [player]..."
    mc "¡Ay! {w=0.5}¿Qué pasa, Monika?"
    show monika base uniform neut ma rhip at t11
    m "Quería saber si podrías darme tu número de teléfono."
    show monika base uniform lpoint
    m "De esta manera, podremos comunicarnos por mensaje o por llamada mientras no estemos en el club."
    m "Creo que es importante tener alguna manera de contactarnos mútuamente."
    show monika base uniform neut mb e1b rhip ldown
    m "Para el festival, ya sabes..."
    show monika base uniform neut ma e1a rhip ldown
    mc "Claro, un minuto."
    "Saco mi móvil de mi maleta dirigiéndome a la pestaña « Contactos », para así encontrar mi número de teléfono."
    "A decir verdad, uso mi teléfono muy muy muy poco. Mis padres me lo compraron a principios de curso porque empezaron a estar cada vez menos y menos en casa por trabajo."
    mc "¿Tienes el móvil encima?"
    show monika base uniform neut me rdown
    m "Eh... no, espera. Voy a buscarlo en mi bolso, dame 5 segundillos."
    show monika at rhide
    hide monika
    pause 5
    show monika base uniform mb rhip at r11
    m "¡Vale, he vuelto! ¿Me dictas tu número?"
    mc "Vale..."
    "Le dicto mi número de teléfono mientras, en perfecta sincronía, pulsa la pantalla de su móvil con los dedos."
    show monika base uniform ma rdown
    m "Creo que ya está, déjame enviarte un mensaje para asegurarme."
    pause 1
    play sound phone
    "{i}¡DING!{/i}"
    mc "Genial, me ha llegado."
    "Tal y como digo eso, guardo el número de teléfono de Monika en 'Mis contactos'."
    m "¡Bien! ¡Te enviaré un mensaje cuando pueda, [player]!"
    mc "Muy bien, Monika."
    show monika at lhide
    hide monika
    "Monika se dirije a recoger sus cosas."
    "Espero pacientemente a que todo el mundo salga del aula."
    show bg club_day1
    stop music fadeout 2.0
    with dissolve_scene_full
    "Una vez que ya no hay nadie, cierro la puerta con llave y comienzo mi caminata a casa."
    show bg school_front_e
    with wipeleft
    play music evening fadein 3.0
    "Cuando estoy en la puerta de entrada del instituto, saco mis auriculares y mi teléfono."
    $ s_name = "??????"
    s "¡[player]! ¡Espera!"
    mc "¿Qué...?"
    $ s_name = "Sayori"
    "Me giro y veo a Sayori corriendo en mi dirección."
    "Guardo discretamente mis auriculares y mi teléfono."
    show sayori base uniform neut e4c rup lup ml blaw at t11:
        matrixcolor TintMatrix("#f5c7ad")
    mc "¿Qué ocurre, Sayori?"
    mc "No tienes que correr de esa manera, me había parado cuando me llamaste."
    show sayori base uniform neut e4c lup rdown ml blaw at s11
    s "...Aaaaaaah... Aaaaaaaah.."
    show sayori base uniform neut e1a mh rup lup nobl at t11
    s "¡Es que te vi sacando el móvil y pensé que ya te ibas!"
    mc "Ah, perdona. Es que suelo irme solo a casa."
    show sayori base uniform neut e2a b2a mf
    s "Ah, ¿sí?"
    show sayori base uniform neut e1a b1a mb ldown rdown
    s "¡Pues te vi esta mañana haciendo tu caminata al insti!"
    s "Parece que no vivimos tan lejos, ¿eh?"
    show sayori base uniform neut e1a b1a ma ldown rdown
    mc "¿Qué?"
    mc "Entonces, ¿cómo es que nunca te he visto antes?"
    show sayori base uniform neut e1b b1b mc at s11
    s "Ah... pues no lo sé... es una buena pregunta. Ejejejeje."
    mc "..."
    show sayori base uniform e1a b1a mb lup at t11
    s "Pues... ¿quieres que vayamos andando juntos a casa?"
    mc "¿No ibas a hacer eso mismo con Monika, Sayori?"
    show sayori base uniform md
    s "Hoy no, me dijo antes que tenía cosas que hacer."
    mc "Ah, bueno, pues si no es molestia, vamos andando a casa juntos."
    show sayori base uniform mc e4b lup rup at h11
    s "¡Bieeen! ¡Pues vámonos!"
    show sayori at lhide
    hide sayori
    $ pause (0.2)
    show bg re2_e
    with wiperight_scene
    "Sayori y yo empezamos a caminar a casa."
    "No hubieron conversaciones muy profundas entre ella y yo, lo que hizo la caminata un poco incómoda y en silencio."
    "Lo único que sonaba eran las bocinas de los coches en la carretera y el cantar de los pájaros en el cielo..."
    "... y una única pregunta aparece en mi cabeza."
    show sayori base uniform neut md at t11:
        matrixcolor TintMatrix("#f5c7ad")
    mc "Sayori, ¿hace cuánto conoces a Monika?"
    show sayori base uniform neut mb
    s "¿A Monika? Pues desde el inicio de este curso."
    s "Caímos en la misma clase, ¡y os hicimos súper amigas muy rápido!"
    show sayori base uniform neut ma
    mc "Ah, genial, gracias por responderme."
    show sayori base uniform neut mb
    s "¿Qué hay de ti, [player]?"
    show sayori base uniform neut ma
    mc "La conozco desde el año pasado, estuvimos en la misma clase y trabajábamos juntos un montón de veces."
    mc "Desde el inicio de este curso, empezamos a distanciarnos principalmente porque era vicepresidenta del club de debate."
    mc "Y bueno, ahora hablamos de vez en cuando, pero porque nos encontramos casualmente. A partir de ahí, nada más."
    show sayori base uniform b1b ma rdown
    s "Ah... bueno, entonces me alegro de que vuelvas a hablar con ella."
    mc "Sí, supongo."
    show sayori at thide:
        matrixcolor TintMatrix("#f5c7ad")
    hide sayori
    "La charla termina ahí, y el resto de la caminata fue en completo silencio hasta llegar a mi calle."
    show bg residential_e
    with wiperight_scene
    "..."
    mc "Pues el camino ha llegado a su fin para mí."
    mc "De hecho, mi casa está por ahí."
    "Dirijo mi dedo vagamente en dirección a mi casa."
    show sayori base uniform neut ma lup at t11:
        matrixcolor TintMatrix("#f7b792")
    s "¡Genial, pues gracias por aceptar volver juntos a casa, [player]! Mi casa está a algunos bloques de distancia, así que me espera una caminata de unos cinco minutos."
    mc "Ha sido un placer, Sayori. Nos vemos el lunes."
    show sayori base uniform neut mc e4b rdown
    s "¡Nos vemos el lunes!"
    show sayori at thide:
        matrixcolor TintMatrix("#f5c7ad")
    hide sayori
    "Sayori continúa caminando mientras abro la verja y me dirijo a la puerta de entrada de mi casa."
    play sound closet_open
    show bg kitchen
    with wipeleft_scene
    $ pause (0.2)
    play sound closet_close
    stop music fadeout 2.0
    "Una vez abierta la puerta, entro a casa, me quito los zapatos y voy directo a mi habitación."
    show bg bedroom
    with wipeleft_scene
    mc "Por hoy, no creo que salga otra vez a la calle."
    mc "Debería ponerme cómodo."
    "Suelto mi mochila en el suelo, quitándome el uniforme y poniéndome un pijama de diseño simple."
    "Caigo en mi cama, mirando al techo."
    play sound phone
    "{i}¡DING!{/i}"
    mc "¿Qué?"
    "Desde los bolsillos de mi uniforme, suena una notificación proveniente de mi móvil."
    "De los pantalones, cojo el móvil esperando ver un mensaje de Monika."
    play music t3 fadein 3.0

    call _phone_register from _call__phone_register

    $ phone.discussion(mc_monika)

    $ phone.date(4, 21, 2023, 19, 31)

    $ phone.message("mc", _("Hola, Monika, estoy aburrido. Acabo de llegar a casa."))

    $ phone.message("m", _("Genial! Te importa si te llamo ahora?"))

    $ phone.message("mc", _("Si quieres, por supuesto. ¿De qué se trata la llamada?"))

    $ phone.message("m", _("De camino a casa, he pensado cómo podemos organizar todo esto antes del festival! :D"))

    $ phone.message("mc", _("Claro, genial, me gustaría saber qué piensas."))

    $ phone.message ("m", _("Vale {}! Te llamo ahora mismo :)".format(player)))

    $ phone.end_discussion()

    "Tan pronto como Monika me manda ese último mensake, veo la notificación de la llamada frente a mis ojos."
    "Le cojo la llamada."

    $ renpy.music.set_volume(volume=0.4)

    $ phone.call("m")


    phone_mc "¡Hola, Monika!"

    phone_m "¡Holi, [player]!"

    phone_mc "¡Se te escucha bien, Monika!"
    phone_m "Verás, Natsuki dijo que le encanta hacer cosas de repostería en su casa, ¿no?"
    phone_mc "Pues sí, eso dijo."
    phone_m "Verás, ¡he pensado que podría hacer pastelillos para atraer a más personas al club!"
    phone_m "Creo que estaría bien hacerlo."
    phone_mc "¡Estoy de acuerdo!"
    phone_mc "Has tenido una buena idea, Monika."
    phone_mc "¿Crees que estará de acuerdo con esto?"
    phone_m "¡Estoy segura!"
    phone_mc "Bien entonces. ¿Alguna otra idea?"
    phone_m "¡Síp! Creo recordar que pusiste en esa hoja que ibas a hacer folletos, ¿no?"
    phone_mc "Claro, ¿qué quieres hacer con ellos?"
    phone_m "Bueno, pues sugiero que los hagamos este finde. Me manejo bien con Canva o Photoshop."
    phone_mc "¿...sin mí?"
    phone_m "Sí, no te preocupes, [player]. Te los traigo el lunes por la mañana."
    phone_mc "Me vale."
    phone_m "¿Se te ha ocurrido algo entonces?"
    phone_mc "Se me acaba de ocurrir algo ahora mismo."
    phone_m "Y es..."
    phone_mc "¿Decorar el club?"
    phone_m "¿A qué te refieres?"
    phone_mc "Podríamos decorarlo con una pancarta que ponga « ¡Bienvenido/a al club de literatura! » escrito en grande."
    phone_mc "Podemos poner en la puerta un lazo enorme que haga de cortina."
    phone_mc "Y, ¿puede que cambiar el color de las cortinas a uno más suave? Si se nos permite hacerlo, claro."
    phone_mc "Con eso, se pondría el ambiente un poco más teatral, ¿no crees?"
    phone_m "[player]..."
    phone_mc "¿No te gusta mi idea?"
    phone_m "¡Todo lo contrario! ¡Me encanta!"
    phone_m "Pero no deberíamos cargarnos todo a las espaldas."
    phone_m "¿Cómo suena darle esa tarea decorativa a alguien en particular?"
    phone_mc "Claro, estoy de acuerdo, pero... ¿a quién?"
    phone_m "Mmm..."
    phone_mc "..."
    phone_mc "Creo que sé de alguien."
    phone_m "¿Quién?"
    phone_mc "Yuri."
    phone_mc "Su escritura es preciosa, ¿no crees?"
    phone_m "Por supuesto, concuerdo contigo."
    phone_m "¿Le quieres encargar eso?"
    phone_mc "Sí."
    phone_mc "Natsuki estará a cargo de los cupcakes."
    phone_mc "Yuri, a cargo de la decoración y la atmósfera del club."
    phone_mc "¡Así también tendrá algo de trabajo!"
    phone_m "¡Me gusta la idea de encargarles pequeños trabajillos a los miembros del club!"
    phone_mc "Pero... volviendo a mi preocupación de antes."
    phone_mc "¿Cómo vamos a organizar todo esto?"
    phone_m "Bueno, sé cómo hacerlo."
    phone_mc "Vale, pues explícamelo."
    phone_m "En lugar de compartir poemas, lo pospondremos hasta el día del festival."
    phone_m "Ay, no, espera. El día del festival no."
    phone_m "Lo pospondremos hasta el jueves, porque el festival es el viernes y conviene menos. Podríamos prepararlo correctamente si el festival fuese un lunes, ya que tendríamos todo el fin de semana. En fin..."
    phone_m "Tendremos que adaptarnos, supongo yo..."
    phone_m "Así que este lunes continuaremos compartiendo poemas y, una vez hecho, anunciamos en el club cómo nos organizaremos los días restantes hasta el festival."
    phone_m "El martes nos encargamos de la decoración y la ambientación."
    phone_m "Y el miercoles... de los cupcakes."
    phone_m "¿Cómo lo ves?"
    phone_mc "Me atrae la idea, pero no me queda claro cómo haremos los cupcakes."
    phone_mc "No tenemos cocina en el club, ajajaja."
    phone_mc "Y dudo muchísimo que nos dejen usar la cocina de la cafetería."
    phone_m "¡Tengo una idea!"
    phone_m "Como tenemos clase por la mañana, ¿cómo suena ir a casa de Natsuki por la tarde para ayudarla a preparar los cupcakes?"
    phone_m "Y si terminamos antes de lo previsto, podemos dar un paseíllo juntos por la ciudad para relajarnos un poco."
    phone_mc "Mmm.."
    phone_mc "Suena bien."
    phone_m "¿Todo correcto entonces?"
    phone_mc "¡Hagámoslo así!"
    phone_m "¡Genial!"
    phone_mc "Muchas gracias, Monika. ¡Has sido de gran ayuda!"
    phone_m "No digas eso... tú también has sido una gran ayuda."
    phone_mc "Ajajajaja. Gracias de nuevo, Monika. Voy a comer algo."
    phone_m "Yo haré lo mismo, ¡que te aproveche! Podemos hablarnos por mensajes también."
    phone_mc "¡Eso haré, no te preocupes! ¡Que te aproveche a ti también!"
    stop music fadeout 4.0
    "De repente, un pensamiento cruza a una velocidad abrumadora."
    "Recuerdo que, el viernes, Monika puso una cara algo tristona cuando me dijo que abandonó el club de debate."
    phone_mc "Espera, Monika. Querría saber qué te hizo abandonar el club de debate."
    phone_m "[player]... ¿a qué viene esta pregunta tan repentina?"
    phone_m "No es necesario que lo sepas, no es algo importante. Bueno, ¡pasa una buena tarde!"

    $ phone.end_call()

    "En un instante, Monika me cuelga el teléfono con un tono muy seco en su voz."

    "Suspiro, poniendo mi teléfono en la mesa."
    mc "Qué bien, [player]..."
    play sound closet_open
    show bg kitchen
    with wiperight_scene
    "Voy a la cocina."
    "Una vez en la cocina, abro la nevera para ver si hay algo con lo que pueda alimentarme."
    mc "Tengo un hambre de perros..."
    mc "..."
    mc "Nada que llame mi atención..."
    mc "Pues nada, supongo que la única opción viable es hacerme algo de pasta..."
    show bg bedroom
    with dissolve_scene_full
    "Tras comer y limpiar los platos, vuelvo a mi habitación."
    mc "Pues..."
    "Me pongo de pie frente a mi armario, donde tengo mis libros bien colocados."
    "..."
    "Recuerdo que Yuri me dio un libro."
    mc "Podría empezar a leerlo..."
    "I take the book out of my bag."
    mc "« Retrato de Markov »..."
    "Pongo el libro en mi mesa, abriendo la primera página y comenzando a leerla."
    show bg bedroom_n
    with dissolve_scene_full
    stop music fadeout 2.0
    "Cierro el libro y lo coloco de nuevo en mi mochila."
    "He de decir que no ha estado nada mal."
    "Yuri tenía razón con el comienzo del libro. No era muy interesante, pero al avanzar se pone más y más intrigante."
    "Me levanto y camino a mi habitación, comenzando mi rutina."
    pause 2
    mc "{i}-bostezo-...{/i}"
    mc "En fin, es hora de ir a dormir."
    "Me deslizo bajo la manta y, mis párpados, que ya pesan por la fatiga del día, se cierran por sí solos."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
