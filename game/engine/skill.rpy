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

        def getEffects(self):
            return self._effects
        Effects = property(getEffects)

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