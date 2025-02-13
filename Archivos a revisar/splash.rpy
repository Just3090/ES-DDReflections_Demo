








init python:

    splash_message_default = [
        "Bienvenido, Señor Presidente.\n",
        "Mil gracias a u/GanstaKingofSA por crear la plantilla del mod.\n",
        "¡Vale, compis~!\n"
    ]









    def recolorize(path, blackCol="#ffbde1", whiteCol="#ffe6f4", contr=1.29):
        return im.MatrixColor(im.MatrixColor(im.MatrixColor(path, im.matrix.desaturate() * im.matrix.contrast(contr)), im.matrix.colorize("#00f", "#fff")
            * im.matrix.saturation(120)), im.matrix.desaturate() * im.matrix.colorize(blackCol, whiteCol))

    def process_check(stream_list):
        if not renpy.windows:
            for index, process in enumerate(stream_list):
                stream_list[index] = process.replace(".exe", "")
        
        for x in stream_list:
            for y in process_list:
                if re.match(r"^" + x + r"\b", y):
                    return True
        return False


image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)






image menu_logo:
    "/mod_assets/DDLCModTemplateLogo.png"

    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_logo2:
    "/mod_assets/DDLCLogoGlitch.png"

    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move


image menu_bg:
    topleft
    "mod_assets/gui/menu_bg.png"

    menu_bg_move

image menu_bg_glitch:
    topleft
    "mod_assets/gui/menu_bg_glitch.png"

    menu_bg_move1

image menu_bg2:
    topleft
    "mod_assets/gui/menu_bg.png"
    pause 10
    "mod_assets/gui/menu_bg_glitch.png"
    pause 0.5

    menu_bg_move




image game_menu_bg:
    topleft
    "mod_assets/gui/menu_bg.png"

    menu_bg_loop




image menu_fade:
    "white"
    menu_fadeout


image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)


image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_m_glitch:
    subpixel True
    "mod_assets/gui/menu_art_m_glitch.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)
    block:
        "mod_assets/gui/menu_art_m_glitch.png"
        10
        "mod_assets/gui/menu_art_m_glitch1.png"
        0.0999
        repeat






image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)


image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)


image menu_nav:
    "mod_assets/gui/main_menu.png"

    menu_nav_move

image menu_nav_glitch:
    "mod_assets/gui/main_menu_glitch.png"

    menu_nav_move








image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout


transform particle_fadeout:
    easeout 1.5 alpha 0


transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_move1:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500
        4
        xoffset 640
        linear 0.1 yoffset -720
        0.99999





transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat


transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0


transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0


transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0



transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0



image intro:
    truecenter
    "green"
    0.5
    "mod_assets/gui/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "green" with Dissolve(0.5, alpha=True)
    0.5


image intro_glitch:
    truecenter
    "mod_assets/gui/splash_glitch1.png"
    pause 0.05666
    "mod_assets/gui/splash_glitch2.png"
    pause 0.05666
    repeat




image warning:
    truecenter
    "green"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "green" with Dissolve(0.5, alpha=True)
    0.5






image tos = "mod_assets/gui/warning.png"
image tos2 = "mod_assets/gui/warning2.png"
image tos3 = "mod_assets/gui/JUST_MONIKA.jpg"
image tos4 = "mod_assets/gui/warning3.jpg"


default persistent.has_chosen_language = False


default persistent.first_run = False


default persistent.lockdown_warning = False



label splashscreen:

    python:
        process_list = []
        currentuser = ""

        if renpy.windows:
            try: process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except subprocess.CalledProcessError:
                try:
                    process_list = subprocess.check_output("powershell (Get-Process).ProcessName", shell=True).lower().replace("\r", "").split("\n") 
                    
                    for x in enumerate(process_list):
                        process_list[x] += ".exe"
                except subprocess.CalledProcessError: pass            


        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = os.environ.get(name)
            if user:
                currentuser = user




    if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
        $ quick_menu = False
        scene black

        menu:
            "Se ha encontrado un archivo de guardado existente. ¿Te gustaría eliminarlo y empezar de nuevo?"
            "Sí, borrar mis datos de guardado.":
                "Borrando datos de guardado...{nw}"
                python:
                    delete_all_saves()
                    renpy.loadsave.location.unlink_persistent()
                    renpy.persistent.should_save_persistent = False
                    renpy.utter_restart()
            "No, continuar desde donde lo dejé.":
                $ restore_relevant_characters()

    if not persistent.lockdown_warning:
        if config.developer:
            call lockdown_check from _call_lockdown_check
        else:
            $ persistent.lockdown_warning = True

    if not persistent.first_run:
        pass


        if not persistent.has_chosen_language and translations:

            if _preferences.language is None:
                call choose_language from _call_choose_language

        $ persistent.has_chosen_language = True





    if persistent.secret_unlocked == True:
        $ persistent.monika = False
        pass
    else:
        pass

    if persistent.monika == True:
        pass
    elif persistent.seen_monika == False:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "[config.name] es un fan mod de Doki Doki Literature Club que no está afiliado con Team Salvato."
        "Se ha diseñado con el propósito de ser jugado después de haber completado el juego original, por lo que contiene destripes del mismo."
        "Los archivos de DDLC necesarios para jugar se pueden encontrar (de forma gratuita) en https://ddlc.moe o en Steam."
        menu:
            "Jugando [config.name] aceptas que has finalizado Doki Doki Literature Club y consideras cualquier destripe que pueda contener."
            "Acepto.":
                scene tos2
                with Dissolve (1.5)
                pause 1.0
                $ persistent.seen_monika = True
                $ persistent.first_run = True
                pass
            "Solo Monika." if persistent.monika == False:
                $ persistent.monika = True
                $ persistent.secret_unlocked = False
                $ persistent.first_run = True
                call screen dialog(message="Solo Monika.", ok_action=Return())
                menu:
                    "M":
                        pass
                    "O":
                        pass
                    "N":
                        pass
                    "I":
                        pass
                    "K":
                        pass
                    "A":
                        pass
                scene tos3
                $ delete_character("yuri")
                $ delete_character("sayori")
                $ delete_character("natsuki")
                pause 1.0
                pass

    if persistent.secret_unlocked == True:
        label secret_unlocked:
            $ quick_menu = False
            scene white
            pause 0.5
            scene tos
            with Dissolve(1.0)
            pause 1.0
            "[config.name] es un fan mod de Doki Doki Literature Club que no está afiliado con Team Salvato."
            "Se ha diseñado con el propósito de ser jugado después de haber completado el juego original, por lo que contiene destripes del mismo."
            "Los archivos de DDLC necesarios para jugar{nw}{done} se pueden encontrar (de forma gratuita) en https://ddlc.moe o en Steam."
            $ style.say_dialogue = style.normal
            show noise zorder 3 at noisefade:
                linear 2 alpha 1
            "{cps=*2}Los archivos de DDLC son necesarios para jugar{/cps}{nw}"
            "{cps=*2}Los archivos de DDLC son necesarios para{/cps}{nw}"
            $ style.say_dialogue = style.edited
            "{cps=*5}Los archivos de DDLC son necesarios para j{/cps}{nw}"
            "{cps=*5}Los archivos de DDLC son necesarios y también SOLO MONIKA{/cps}{nw}"
            play sound "<to 1.5>sfx/interference.ogg"
            show tos4 as effect:
                yoffset 720
                linear 0.2 yoffset 0
                repeat
            show tos4 as effect0:
                yoffset 0
                linear 0.2 yoffset -720
                repeat
            pause 1.5
            scene black
            pause 3
            scene tos
            menu:
                "Acepto.":
                    scene tos2
                    with Dissolve (1.5)
                    pause 1.0
                    $ persistent.monika = False
                    $ persistent.secret_unlocked = False
                    $ persistent.first_run = True
                    pass




        if extra_settings:
            if process_check(["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]):
                $ persistent.lets_play = True
                call screen dialog("Let's Play Mode has been enabled automatically.\nThis mode allows you to skip content that\ncontains sensitive information or apply alternative\nstory options.\n\nThis setting will be dependent on the modder\nif they programmed these checks in their story.\n\n To turn off Let's Play Mode, visit Settings and\nuncheck Let's Play Mode.", 
                    [Hide("dialog"), Return()])
        scene white























    if not persistent.special_poems:
        python hide:

            persistent.special_poems = [0,0,0]


            a = range(1,12)



            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                
                
                a.remove(b)



    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload


    $ config.allow_skipping = False



    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black

        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return
























































    show green
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    if persistent.monika == True:
        $ config.version = "Solo Monika"
        $ config.name = "S O L O M O N I K A"
        $ persistent.ghost_menu = False
        $ splash_message = splash_message_default
        play music t1
        show intro with Dissolve(0.5, alpha=True)
        $ pause (2.5)
        hide intro
        python:
            currentpos = get_pos()
            startpos = currentpos - 0.1
            if startpos < 0: startpos = 0
            track = "<from " + str(startpos) + " to " + str(currentpos) + ">mod_assets/bgm/menu.mp3"
            renpy.music.play(track, loop=True)
        show intro_glitch
        $ config.window_title = _("Solo Monika")
        $ pause (3)
        show screen tear(8, offtimeMult=2, ontimeMult=10)
        $ pause (1)
        hide screen tear
        hide intro_glitch
        stop music
        scene black
        show splash_warning "{color=#08580e}S 0 L O M 0 N 1 K A.{/color}" with Dissolve(0.5, alpha=True)
        $ pause (1.5)
        hide splash_warning with Dissolve(0.5, alpha=True)
        $ splash_message = "{color=#08580e}E̸s̴t̸e̷ ̵j̷u̵e̸g̸o̴ ̸e̶s̷ ̸u̴n̷ ̴f̷a̸n̵g̸a̷m̶e̸ ̴n̶o̸ ̷o̴f̸i̸c̷i̷a̴l̶ ̴q̵u̶e̸ ̵n̶o̴ ̵e̷s̶t̴á̸ ̸a̷f̶i̶l̴i̵a̴d̴o̵ ̶c̸o̵n̸ ̸T̶e̴a̵m̶ ̷S̸a̸l̴v̶a̸t̶o.̵.̵.̶\n{/color}"
        show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
        $ pause(1.5)
        $ splash_message = "{color=#08580e}Por favor, no ÁÂÃÄÅÆÇÈÉÊ«¬®¯°±²³´µ¶·¸¹º{/color}"
        show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
        $ pause (2.5)
        hide splash_warning with Dissolve(0.5, alpha=True)
        $ config.allow_skipping = True
    else:
        $ config.main_menu_music = audio.t1
        $ renpy.music.play(config.main_menu_music)
        show intro with Dissolve(0.5, alpha=True)
        $ pause(2.5)
        hide intro with Dissolve(0.5, alpha=True)
        $ splash_message2 = renpy.random.choice(splash_message_default)
        show splash_warning "[splash_message2]" with Dissolve(0.5, alpha=True)
        $ pause (1.5)
        hide splash_warning
        $ splash_message = "Este juego es un producto no oficial que no está afiliado a Team Salvato...\n"
        show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
        $ pause(1.5)
        $ splash_message = "Este juego es un producto no oficial que no está afiliado a Team Salvato...\nPor favor, dadles cariño."
        show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
        $ pause (1.10)
        hide splash_warning with Dissolve(0.5, alpha=True)
        $ pause(0.01)
        $ config.allow_skipping = True
    return



label warningscreen:
    hide intro
    show warning
    pause 3.0






























label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal





























    if anticheat != persistent.anticheat:
        stop music
        scene black
        "No se puede cargar el archivo de guardado."
        "Oye, ¿tratas de hacer trampas?"
        $ m_name = "Monika"
        show monika 1 at t11
        if persistent.playername == "":
            m "Qué gracioso eres."
        else:
            m "Eres muy divertido, [persistent.playername]."
        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Un consejo: Puedes usar el botón de \"Saltar\" para \nadelantar los diálogos que ya has leído.", ok_action=Return())
    return


label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None




    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload




























label before_main_menu:
    if persistent.monika == True:
        stop music
    else:
        $ config.main_menu_music = audio.t1
    return



label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
