
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        while self.health > 0:
            return self.name + f" has received {damage} points of damage"
        return self.name + f" has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        while self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        return "A Saxon has died in combat"

    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy += [Viking()]
    
    def addSaxon(self, Saxon):
        self.saxonArmy += [Saxon()]

    def vikingAttack(self):
        

    
    
    
