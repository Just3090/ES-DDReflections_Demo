








define config.name = "Doki Doki: The Reflection!"



define gui.show_name = True


define config.version = "1.0"



define gui.about = _("")






define build.name = "DDTheReflection!-DemoVer"


define config.has_sound = True


define config.has_music = True


define config.has_voice = False



define config.main_menu_music = audio.t1






define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)


define config.after_load_transition = None


define config.end_game_transition = Dissolve(.5)





define config.window = "auto"





define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


default preferences.text_cps = 50


default preferences.afm_time = 15


default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75






define config.save_directory = "DDLCMod-TheReflection"


define config.window_icon = "mod_assets/gui/window_icon.png"


define config.allow_skipping = True


define config.has_autosave = False


define config.autosave_on_quit = False


define config.autosave_slots = 0


define config.rollback_enabled = config.developer



define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)





init python:

















    if renpy.version_tuple == (6, 99, 12, 4, 2187):
        build.package(build.directory_name + "Mod", 'zip', 'mod', description="Ren'Py 6 DDLC Compliant Mod")
    else:
        build.package(build.directory_name + "Renpy7Mod", 'zip', 'windows linux mac renpy mod',
        description="Ren'Py 7 DDLC Compliant Mod")



    build.archive("scripts", 'mod')
    build.archive("mod_assets", 'mod')



    try: 
        build.renpy_patterns.remove(('renpy.py', ['all']))
        build.classify_renpy("renpy.py", "renpy all")
    except: pass

    try:
        build.early_base_patterns.remove(('*.sh', None))
        build.classify("LinuxLauncher.sh", "linux") 
        build.classify("*.sh", None)
    except: pass






    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/presplash.png", "scripts all")
    build.classify("game/**.rpyc", "scripts all")
    build.classify("game/README.md", None)
    build.classify("game/**/README.md", None)
    build.classify("game/**.txt", "scripts all")
    build.classify("game/**.chr", "scripts all")
    build.classify("game/advanced_scripts/**","scripts all") 
    build.classify("game/tl/**", "scripts all") 
    build.classify("game/mod_extras/**.rpyc", "scripts") 

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)
    build.classify('README.html','mod all')
    build.classify('README.linux', 'linux')


    build.documentation('README.html')

    build.include_old_themes = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
