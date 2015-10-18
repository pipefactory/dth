init -1 python:

    import pygame

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

            self._sensitive = True

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
            # draw skill_workbench
            r.blit(renpy.render(self.skill_workbench, 241, 601, st, at), (100, 100))

            return r

        def per_interact(self):

            renpy.redraw(self, 0)

        def set_sensitive(self, value):

            self._sensitive = value

        def event(self, evt, x, y, st):

            if not self._sensitive:
                return ""
            elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1:
                return renpy.end_interaction("end")
            else:
                raise renpy.IgnoreEvent()

        def interact(self):

            evt = ui.interact()
            if evt == "end":
                self._sensitive = False
            else:
                self._sensitive = True
            return evt

label character_workspace:

    "let's go into Character Workspace"

    scene black with dissolve


label skill_workbench:

    $ flag = True

    python:

        sw = SkillWorkbench()
        sw.show()

        while flag:

            evt = sw.interact()

            if evt == "end":
                sw.hide()
                flag = False

    scene white with dissolve

    "It's [evt]"