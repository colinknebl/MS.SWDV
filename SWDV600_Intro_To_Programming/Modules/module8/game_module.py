from random import random, randrange

class Character:
    def __init__(self, strength, health):
        self._strength = strength
        self._health = health
        
    def getHealth(self):
        return self._health
    
    def takeHealth(self, amount):
        self._health = self._health - amount
        
    def getStrength(self):
        return self._strength

class Frodo(Character):
    
    def __init__(self):
        Character.__init__(self, 5, 100)
        self._companions = []
        self._ringResistance = 100
        
    def decreaseRingResistance(self, amount):
        self._ringResistance -= amount

    def setRingResistance(self, amount):
        self._ringResistance = amount

    def decreaseRingResistanceByPercent(self, percent):
        self._ringResistance = self._ringResistance * percent
        
    def addCompanions(self, companions):
        for companion in companions:
            self._companions.append(companion)
            
    def removeCompanions(self, companions):
        for companion in companions:
            if self._companions.count(companion) > 0:
                self._companions.remove(companion)
            
    def getCompanions(self):
        return self._companions[:]

    def getTimeToWearRingRemaining(self):
        return self._ringResistance
    
    def getStrength(self):
        return self._strength + (len(self._companions) * 5)
    
    def increaseHealth(self, amount):
        self._health = self._health + amount
        if self._health > 100:
            self._health = 100


class Enemy(Character):
    def __repr__(self):
        return '{} Enemy instance'.format(self._name)
    
    def __init__(self, name, strength):
        Character.__init__(self, strength, 100)
        self._name = name
    
    def getName(self):
        return self._name

class Game:
    
    def __init__(self, gui, steps):
        self._gui = gui
        self._steps = steps
        self._currentStep = 0
        self._frodo = Frodo()
        
    def _gameLoop(self):
        continueGame = True
        while not self._gameOver(continueGame):
            # initiate the step
            continueGame, decision = self._step()

            # run post decision logic
            self._postDecision(decision)

            # parse the user's decision
            self._parseDecision(decision)

            # closes the current step
            self._closeStep(self._steps[self._currentStep])

            if not self._frodoIsAlive():
                # wrap up the game because Frodo's health is depleted
                self._frodoDied()
                continueGame = False
            elif not self._frodoStillResistsRing():
                self._frodoOvertakenByRing()
                continueGame = False
            
            # updates the current game statistics
            self._gui.updateCurrentStats(self._frodo, self._currentStep + 1, len(self._steps))

            if continueGame:
                # with each step Frodo loses resistance to the ring
                self._frodo.decreaseRingResistance(10)
                self._currentStep += 1

    def _step(self):
        continueGame, decision = self._gui.step(self._steps[self._currentStep])
        return continueGame, decision

    def _frodoStillResistsRing(self):
        return self._frodo.getTimeToWearRingRemaining() > 0

    def _frodoIsAlive(self):
        return self._frodo.getHealth() > 0

    def _closeStep(self, step):
        self._gui.closeStep(step)
                
    def _postDecision(self, decision):
        self._gui.postDecision(decision)
        
    def _frodoDied(self):
        self._gui.frodoDied()

    def _frodoOvertakenByRing(self):
        self._gui.frodoOvertakenByRing()
        
    def _updateCompanions(self, companions):
        "Adds or removes companions from Frodo's companion list"
        if 'add' in companions and len(companions['add']) > 0:
            self._frodo.addCompanions(companions['add'])
        
        if 'remove' in companions and len(companions['remove']) > 0:
            self._frodo.removeCompanions(companions['remove'])
    
    def _parseDecision(self, decision):
        "Parses the data of the user's decision."
        if 'companions' in decision:
            self._updateCompanions(decision['companions'])
            
        if 'attack' in decision and decision['attack']['probability'] > 0.0:
            if random() < decision['attack']['probability']:
                enemy = Enemy(decision['attack']['enemy']['name'], decision['attack']['enemy']['strength'])
                self._handleAttack(enemy, decision['attack'])
                
        if 'increaseHealth' in decision:
            self._frodo.increaseHealth(decision['increaseHealth'])

        if 'setRingResistance' in decision:
            self._frodo.setRingResistance(decision['setRingResistance'])

        if 'decreaseRingResistance' in decision:
            self._frodo.decreaseRingResistanceByPercent(decision['decreaseRingResistance'])
            
    
    def _handleAttack(self, enemy, attackData):
        response = None
        if 'responseOptions' in attackData:
            response = self._gui.introAttack(enemy, attackData)
        self._runAttackSequence(enemy, response, attackData)

    def _fight(self, enemy): 
        attackRoundWins = {
            'frodo': 0,
            'enemy': 0
        }
        frodoStrength = self._frodo.getStrength()
        enemyStrength = enemy.getStrength()
        frodoHealth = self._frodo.getHealth()
        enemyHealth = enemy.getHealth()
        
        for i in range(3):
            frodoAttackPower = frodoStrength * random()
            enemyAttackPower = enemyStrength * random()
            
            if frodoAttackPower > enemyAttackPower:
                attackRoundWins['frodo'] += 1
                enemyHealth = enemyHealth - frodoStrength
            else:
                attackRoundWins['enemy'] += 1
                frodoHealth = frodoHealth - enemyStrength
                
        self._gui.attackSummary(attackRoundWins, enemy, self._frodo.getHealth(), frodoHealth)
        self._frodo.takeHealth(self._frodo.getHealth() - frodoHealth)
            
    def _runAttackSequence(self, enemy, response, attackData):
        if bool(response): 
            if response['choice'] == 'sword' or response['choice'] == 'fight':
                self._fight(enemy)
            else:
                self._frodo.decreaseRingResistance(randrange(1, 40))

            if 'companions' in response:
                    self._updateCompanions(response['companions'])
        else:
            self._fight(enemy)

    def _gameEnd(self):
        self._gui.gameOver()
    
    def _gameOver(self, continueGame):
        return not (continueGame and (self._currentStep < len(self._steps)) and self._frodo.getHealth() > 0 )# and self._frodoStillResistsRing() > 0) 
        
    def play(self):
        self._gui.introduction()
        self._gameLoop()