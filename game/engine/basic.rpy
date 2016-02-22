init -99 python:

    ###
    # Aware
    ###

    class Aware(object):

        def __init__(self, identity):
            self._identity = identity

        def getIdentity(self):
            return self._identity
        Identity = property(getIdentity)

    ###
    # Block
    ###

    class Block(object):

        def __init__(self, width = 1, height = 1):
            self._width = width
            self._height = height

        def getWidth(self):
            return self._width
        Width = property(self._width)

        def getHeight(self):
            return self._height
        Height = property(self._height)