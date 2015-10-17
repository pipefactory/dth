init:

    python:

        class CharacterWorkspace(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                self.mytext = Text(_("This is my first text"), size=36)

            def visit(self):

                return [ self.mytext ]

            def render(self, width, height, st, at):

                r = renpy.Render(width, height)

                mytext_render = renpy.render(self.mytext, width, height, st, at)
                mw, mh = mytext_render.get_size()
                r.blit(mytext_render, ((width - mw) / 2, (height - mh) / 2))

                renpy.redraw(self, 0)

                return r

            def event(self, ev, x, y, st):

                import pygame

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    return "end"
                else:
                    raise renpy.IgnoreEvent()