








label lockdown_check:

    $ version = renpy.version()

    scene black

    if renpy.version_tuple > (8, 0, 0, 22062402):
        "{b}Warning:{/b} The mod template you are using to mod DDLC in is not recommended for Ren'Py 8 use."
        "Mods designed for Ren'Py 8 should instead download the Python 3 version of the mod template in order to mod DDLC properly."
        "Running this mod template on this version of Ren'Py may be prone to bugs that may be fixed already in the Python 3 template."

        menu:
            "By continuing to run your mod on Ren'Py 8, you acknowledge this disclaimer and the possible problems that can happen on a older Python 2 template."
            "I agree.":
                $ persistent.lockdown_warning = True
                return

    elif renpy.version_tuple > (7, 5, 3, 22083102) and not persistent.lockdown_warning:
        "{b}Warning:{/b} The version of Ren'Py you are trying to mod DDLC on has not been tested for modding compatibility."
        "The last recent version of Ren'Py that works for DDLC mods is \"{i}Ren'Py 7.5.1{/i}\"."
        "Running DDLC or your DDLC mod on a higher version than the one tested may introduce bugs and other game breaking features."

        menu:
            "By continuing to run your mod on [version!q], you acknowledge this disclaimer and the possible problems that can happen on a untested Ren'Py version."
            "I agree.":
                $ persistent.lockdown_warning = True
                return
    else:

        $ persistent.lockdown_warning = True

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
