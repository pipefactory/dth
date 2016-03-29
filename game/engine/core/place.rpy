init -10 python:

    ###
    # Chara
    ###
    
    class Place(Aware):

        def __init__(self, identity, **kwargs):
            self._name = kwargs['name'] if 'name' in kwargs else '_undefined_'
            Aware.__init__(self, identity)

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

        def __str__(self):
            return 'Place(' + ','.join("%s=[%s]" % item for item in vars(self).items()) + ')'