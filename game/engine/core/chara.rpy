init -10 python:

    class Talent(Aware):

        def __init__(self):
            pass

    class Group(Aware):

        def __init__(self):
            pass

    ###
    # Chara
    ###

    class Chara(Aware):

        def __init__(self, identity, **kwargs):
            self._name = kwargs['name'] if 'name' in kwargs else '_undefined_'
            self._desc = kwargs['desc'] if 'desc' in kwargs else ''
            self._graze = kwargs['graze'] if 'graze' in kwargs else 0
            self._positions = kwargs['positions'] if 'positions' in kwargs else []
            self._groups = kwargs['groups'] if 'groups' in kwargs else []
            Aware.__init__(self, identity)

        ###
        # Property
        # ===============================================================
        ###

        def name():
            doc = "The name property."
            def fget(self):
                return self._name
            def fset(self, value):
                self._name = value
            def fdel(self):
                del self._name
            return locals()
        name = property(**name())

        def desc():
            doc = "The desc property."
            def fget(self):
                return self._desc
            def fset(self, value):
                self._desc = value
            def fdel(self):
                del self._desc
            return locals()
        desc = property(**desc())

        def graze():
            doc = "The graze property."
            def fget(self):
                return self._graze
            def fset(self, value):
                self._graze = value
            def fdel(self):
                del self._graze
            return locals()
        graze = property(**graze())

        def positions():
            doc = "The positions property."
            def fget(self):
                return self._positions
            def fset(self, value):
                self._positions = value
            def fdel(self):
                del self._positions
            return locals()
        positions = property(**positions())

        def groups():
            doc = "The groups property."
            def fget(self):
                return self._groups
            def fset(self, value):
                self._groups = value
            def fdel(self):
                del self._groups
            return locals()
        groups = property(**groups())
