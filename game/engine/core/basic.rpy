init -99 python:

    ###
    # Aware
    ###

    class Aware(object):

        def __init__(self, identity):
            self._identity = identity

        def identity():
            doc = "The identity property."
            def fget(self):
                return self._identity
            def fset(self, value):
                self._identity = value
            return locals()
        identity = property(**identity())

    ###
    # Effect
    ###

    class Effect(object):

        def __init__(self):
            pass

        def __str__(self):
            return 'Effect'