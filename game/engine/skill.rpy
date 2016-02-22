init -10 python:

    ###
    # Skill
    # The Skill class encapsulates a thing that a Fighter can do - e.g. 'Attack' or 'Defend' or 'Move' or 'Summon' or whatever.
    # Ideally, a Skill instance should be a singleton/flyweight class, only one instance and no references back to the parent object. Or at least potentially be used like that.
    ###
    
    # TODO: Skill needs methods to listen to beginning and end of faction turn and Tick

    class Skill(Aware):

        def __init__(self, identity, effects = []):
            self._effects = effects
            Aware.__init__(self, identity)

        def effects():
            doc = "The effects property."
            def fget(self):
                return self._effects
            def fset(self, value):
                self._effects = value
            def fdel(self):
                del self._effects
            return locals()
        effects = property(**effects())

        def __str__(self):
            return 'Skill(identity=[%s],effects=[%s])' % (self._identity, ','.join(str(tag) for tag in self._tags))

    ### 
    # AwardSkill
    ###

    class AwardSkill(Skill):

        def __init__(self, identity, effects = []):
            Skill.__init__(self, identity, effects)

        def __str__(self):
            return 'AwardSkill(identity=[%s],effects=[%s])' % (self._identity, ','.join(str(tag) for tag in self._tags))

    ### 
    # InherentSkill
    ###

    class InherentSkill(Skill):

        def __init__(self, identity, effects = []):
            Skill.__init__(self, identity, effects)

        def __str__(self):
            return 'InherentSkill(identity=[%s],effects=[%s])' % (self._identity, ','.join(str(tag) for tag in self._tags))
    
    ### 
    # ActionableSkill
    ###

    class ActionableSkill(Skill):

        def __init__(self, identity, effects = []):
            Skill.__init__(self, identity, effects)

        def __str__(self):
            return 'ActionableSkill(identity=[%s],effects=[%s])' % (self._identity, ','.join(str(tag) for tag in self._tags))



    ###
    # SkillBlock
    ###

    class SkillBlock(object):

        def __init__(self, x = 0, y = 0, width = 1, height = 1, skill = None):
            self._x = x
            self._y = y
            self._width = width
            self._height = height
            self._skill = skill

        def x():
            doc = "The x property."
            def fget(self):
                return self._x
            def fset(self, value):
                self._x = value
            return locals()
        x = property(**x())

        def y():
            doc = "The y property."
            def fget(self):
                return self._y
            def fset(self, value):
                self._y = value
            return locals()
        y = property(**y())

        def width():
            doc = "The width property."
            def fget(self):
                return self._width
            def fset(self, value):
                self._width = value
            return locals()
        width = property(**width())

        def height():
            doc = "The height property."
            def fget(self):
                return self._height
            def fset(self, value):
                self._height = value
            return locals()
        height = property(**height())

        def skill():
            doc = "The skill property."
            def fget(self):
                return self._skill
            def fset(self, value):
                self._skill = value
            def fdel(self):
                del self._skill
            return locals()
        skill = property(**skill())

        def __str__(self):
            return 'Block[x=%s,y=%s,width=%s,height=%s]' % (self._x, self._y, self._width, self._height)