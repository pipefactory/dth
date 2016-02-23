screen workspace(identity):

    default evt = 0

    frame:
        background "#f4b00d"
        xfill True
        yfill True
        xpadding 0
        ypadding 0

        hbox:

            frame:
                background "#444"
                xfill False
                xsize 350
                yfill True

                vbox:
                    textbutton "frame1" xalign 0.5 action Return(0)

            frame:
                background "#888"
                xfill True
                yfill True

                hbox:
                    textbutton "frame3" xalign 0.5 action Return(2)