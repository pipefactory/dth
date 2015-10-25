init 1 python:

    import pygame
    import random

    class SkillWorkbench(renpy.Displayable):

        def __init__(self, **kwargs):

            super(SkillWorkbench, self).__init__(self, **kwargs)

            self.skill_workbanch_matrix = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # 5  =================================
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # 10 =================================
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # 15 =================================
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # 20 =================================
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # 25 =================================
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # 30 =================================
            ]

            self.skill_workbench = Image(_("images/skill_workbench.png"))
            self.skill_cmm_pow1 = Image(_("images/skill_cmm_pow1.png"))
            self.solid_orange = Solid("#f4b00d")

        def visit(self):

            return [
                self.skill_workbench,
                self.skill_cmm_pow1
            ]

        # This shows the table on the given layer.
        def show(self, layer='master'):

            ui.layer(layer)
            ui.add(self)
            ui.close()

        # This hides the table.
        def hide(self, layer='master'):

            ui.layer(layer)
            ui.remove(self)
            ui.close()

        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            # draw solid_orange
            r.blit(renpy.render(self.solid_orange, width, height, st, at), (0, 0))
            # draw skill_workbench
            r.blit(renpy.render(self.skill_workbench, 241, 601, st, at), (random.randint(50, 150), random.randint(50, 150)))

            debuglogger.debug("%s, %s, %s, %s, %s" % (repr(self), width, height, st, at))

            return r

        def per_interact(self):

            # renpy.redraw(self, 0)
            pass

        def event(self, evt, x, y, st):

            if evt.type == pygame.MOUSEBUTTONUP and evt.button == 1:
                return renpy.end_interaction("end")
            else:
                # debuglogger.debug("%s, %s, %s, %s, %s" % (repr(self), repr(evt), x, y, st))
                raise renpy.IgnoreEvent()

screen workstation(char_id):

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


screen character_workspace:

    pass



label lbl_character_workspace:

    "let's go into Character Workspace"

    call screen workstation("hakurei")

    # $ evt = renpy.call_screen("workstation", char_id="hakurei")

    # python:

    #     sw = SkillWorkbench()
    #     sw.show()

    #     while True:

    #         evt = ui.interact()

    #         debuglogger.debug("%s" % evt)

    #         if evt == "end":
    #             # sw.hide()
    #             break

    "It's [_return]"

    $ debuglogger.debug("%s" % _return)