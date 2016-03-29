# The game starts here.
label start:

    scene bg white

    $ chara = library.chara('usami_sumireko')

    if chara is not None:
        "[chara]"
    else:
        "chara undefined"

    show screen workspace("usami_sumireko")
    # show screen side_test

    pause