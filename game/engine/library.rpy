init -10 python:

    import json

    class Library(object):

        def __init__(self):
            with renpy.file('resource/chara-list.json') as data:
                self._charas = json.load(data)

        def chara(self, identity):
            if identity in self._charas:
                return Chara(identity, **self._charas[identity])
            else:
                return Chara(identity)

        def skill(self, identity):
            pass