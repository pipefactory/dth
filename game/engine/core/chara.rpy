init -10 python:

    ###
    # Chara
    ###

    class Chara(Aware):

        def __init__(self, identity, **kwargs):
            self._name = kwargs['name'] if 'name' in kwargs else '_undefined_'
            self._graze = kwargs['graze'] if 'graze' in kwargs else 0
            self._typelist = kwargs['typelist'] if 'typelist' in kwargs else []
            self._grouplist = kwargs['grouplist'] if 'grouplist' in kwargs else []
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

        def typelist():
            doc = "The typelist property."
            def fget(self):
                return self._typelist
            def fset(self, value):
                self._typelist = value
            def fdel(self):
                del self._typelist
            return locals()
        typelist = property(**typelist())

        def grouplist():
            doc = "The grouplist property."
            def fget(self):
                return self._grouplist
            def fset(self, value):
                self._grouplist = value
            def fdel(self):
                del self._grouplist
            return locals()
        grouplist = property(**grouplist())

        ###
        # internal
        # ===============================================================
        ###

        def __str__(self):
            return 'Chara(' + ','.join("%s=[%s]" % item for item in vars(self).items()) + ')'
