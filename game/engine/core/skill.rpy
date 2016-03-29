init -10 python:

    ###
    # Skill
    # The Skill class encapsulates a thing that a Chara can do - e.g. 'Attack' or 'Defend' or 'Move' or 'Summon' or whatever.
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
    # InherentSkill
    ###

    class PortableSkill(Skill):

        def __init__(self, identity, effects = []):
            Skill.__init__(self, identity, effects)

        def __str__(self):
            return 'PortableSkill(identity=[%s],effects=[%s])' % (self._identity, ','.join(str(tag) for tag in self._tags))

    ### 
    # BlessingSkill
    ###

    class BlessingSkill(PortableSkill):

        def __init__(self, identity, effects = []):
            PortableSkill.__init__(self, identity, effects)

        def __str__(self):
            return 'BlessingSkill(identity=[%s],effects=[%s])' % (self._identity, ','.join(str(tag) for tag in self._tags))

    ### 
    # TargetableSkill
    ###

    class TargetableSkill(PortableSkill):

        def __init__(self, identity, effects = [], target = None):
            self._target = target
            PortableSkill.__init__(self, identity, effects)

        def target():
            doc = "The target property."
            def fget(self):
                return self._target
            def fset(self, value):
                self._target = value
            def fdel(self):
                del self._target
            return locals()
        target = property(**target())

        def __str__(self):
            return 'TargetableSkill(identity=[%s],effects=[%s])' % (self._identity, ','.join(str(tag) for tag in self._tags))

    ###
    # SkillTarget
    ###

    class SkillTarget(object):

        def __init__(self):
            pass