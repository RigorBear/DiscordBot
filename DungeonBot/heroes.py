import time
import random
from datetime import datetime
import constants

class Hero(object):

    def __init__(self, user, rating, level, type, gold, channel, max_hp, hp, min_dmg, max_dmg, abilities):
        self.user = user
        self.rating = rating
        self.level = level
        self.type = type
        self.gold = gold
        self.channel = channel
        self.max_hp = 50 + type.hpl
        self.min_dmg = type.min_dmg + (level*type.min_dmg)/10
        self.max_dmg = type.max_dmg + (level*type.max_dmg)/10
        self.abilities = []
        self.exp = 0

    def getExp(self, exp):
        self.exp = self.exp + exp
        if self.exp >= constants.EXP_LIST[self.level + 1]:
            self.level = levelUp()

        return self.level, self.exp

    def levelUp(self):
        self.level = self.level + 1
        if self.exp < constants.EXP_LIST[self.level]:
            self.exp = constants.EXP_LIST[self.level]

        return self.level