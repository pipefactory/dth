screen workspace:

    python:
        rangelist = range(0, 100)

    tag characterWorkspace
    modal True

    default characterIdentity = ''

    frame:
        background "#f4b00d"
        xfill True
        yfill True
        xpadding 0
        ypadding 0

        hbox:
            frame:
                background "#222"
                xfill False
                xsize 150
                yfill True

            frame:
                background "#444"
                xfill False
                xsize 350
                yfill True

                vbox:
                    side "c r":
                        text "Avaliable Character"
                        button:
                            text "S/L"

                    side "c r":
                        viewport id "ws_charlist":
                            draggable True
                            mousewheel True

                            grid 1 len(rangelist):

                                for i in rangelist:

                                    side "c r":
                                        frame:
                                            background "#8aa41b"
                                            text 'box' + str(i)
                                            xfill True
                                            yfill False
                                            ysize 80

                                        button:
                                            text "kk"

                        vbar value YScrollValue("ws_charlist")

            frame:
                background "#888"
                xfill True
                yfill True

                hbox:
                    textbutton "frame3":
                        xalign 0.5
                        action [Return(2)]