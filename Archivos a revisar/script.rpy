




label start:

    call _phone_register from _call__phone_register_1





    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer






    $ s_name = "??????"
    $ m_name = "??????"
    $ n_name = "???????"
    $ y_name = "????"


    $ quick_menu = True



    $ style.say_dialogue = style.normal



    $ in_sayori_kill = None


    $ allow_skipping = True
    $ config.allow_skipping = True




    if persistent.monika == True:
        stop music
        python:
            try: sys.modules['renpy.error'].report_exception("Why it is not working...?", False)
            except: pass
        call screen dialog(message="Game Error: several .chr files are missing or are corrupted.", ok_action=Return())
        call screen dialog(message="Error fatal spotted.\nThe game is going to reset to prevent any damage on your computer.\nCheck traceback.txt for more details.", ok_action=Call(label="monika_end"))
    else:
        call prologue from _call_prologue

        call ch1_main from _call_ch1_main

        call ch2_main from _call_ch2_main

        call ch3_main from _call_ch3_main































    label monika_end:
        python:
            del persistent.playername
    $ persistent.secret_unlocked = True
    $ persistent.seen_monika = True
    $ persistent.secret = True
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
