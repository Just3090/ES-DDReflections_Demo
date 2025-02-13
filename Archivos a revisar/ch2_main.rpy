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
    mc "Es cuestión de tiempo coger confianza y adoptar más tranquilidad a la hora de compartir nuestros poemas con las demás."
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
