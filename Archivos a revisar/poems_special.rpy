




image poem_special1 = "poem_special/poem_special1.png"
image poem_special2 = "poem_special/poem_special2.png"
image poem_special3 = "poem_special/poem_special3.png"
image poem_special4 = "poem_special/poem_special4.png"
image poem_special5:
    "poem_special/poem_special5a.png"
    10.0
    "poem_special/poem_special5b.png"
image poem_special6 = "poem_special/poem_special6.png"
image poem_special7a = "poem_special/poem_special7a.png"
image poem_special7b = "poem_special/poem_special7b.png"
image poem_special8 = "poem_special/poem_special8.png"
image poem_special9 = "poem_special/poem_special9.png"
image poem_special10 = "poem_special/poem_special10.png"
image poem_special11 = "poem_special/poem_special11.png"



image poem_end = ConditionSwitch(
    "persistent.clearall == True", "poem_special/poem_end_clearall.png",
    "True", "poem_special/poem_end.png")





label poem_special(poem=1):
    $ quick_menu = False
    play sound page_turn

    if poem == 7:
        show poem_special7a as ps with Dissolve(1.0)
    else:
        show expression "poem_special" + str(poem) as ps with Dissolve(1.0)

    $ pause()

    if poem == 2:
        play sound "sfx/giggle.ogg"
    elif poem == 7:
        show poem_special7b as ps
        $ pause(0.01)

    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
