class AdventureGameTextGui:
    
    def introduction(self):
        print('### Introduction ###')
        print('You are Frodo, the fearless Hobbit from J.R.R. Tolkien\'s Middle Earth.')
        print('The goal of the game is to destroy the one ring that rules them all!\n')
        print('### Gameplay instructions ###')
        print('At certain points you may be asked if you want to wear the ring to hide from an enemy.')
        print('Wearing the ring may save you some health, but if Frodo\'s ring resistance is depleted, the game is over.')
        print('Also, as you progress through the game the time remaining to wear the ring will be depleted by 10 points each step.\n')
        print('If you encounter attackers along your journey, you may have the option to fight or run from them.')
        print('Frodo\'s attack strength is based on how many companions you currently have.')
        print('The enemies can also deplete Frodo\'s health.')
        print('Both Frodo\'s health and his ring resistance start at 100.\n')
        print('Good luck!\n\n')
        
    def step(self, step):
        print(step['event'])
        self._printMessages(step['preDecisionMessages'])
        userDecision = self._getInput(step['decision'])
        
        decision = step['decisions'][userDecision]

        # Prints the postDecisionMessages of the step
        self.midStep(step)
        
        return decision['continueGame'], decision
        
    def midStep(self, step):
        'Prints the postDecisionMessages of the step'
        if 'postDecisionMessages' in step and len(step['postDecisionMessages']) > 0:
            self._printMessages(step['postDecisionMessages'])

    def closeStep(self, step):
        if 'closeStepMessages' in step:
            self._printMessages(step['closeStepMessages'])
            
    def _printMessages(self, messages):
        'Loops through the messages and prints them'
        for msg in messages:
            print(msg)
        print()
        
    def postDecision(self, decision):
        'Prints the decision messages after the decision has been made'
        self._printMessages(decision['messages'])

    def _getDecisionValidAnswers(self, prompt):
        """
            Gets the valid answers to the step - returns a tuple.
            If the prompted answers are (y/n), will return tuple (y, n)
            If the prompted answers are (fight/ring), will return tuple (fight, ring)
        """
        openParenIndex = prompt.find('(') + 1
        closeParenIndex = prompt.find(')')
        choices = prompt[openParenIndex:closeParenIndex]
        ans1, ans2 = choices.split('/')
        return ans1.strip(), ans2.strip()

    def _getInput(self, prompt):
        'Get the user input for the step decision'
        resp = input(prompt)

        ans1, ans2 = self._getDecisionValidAnswers(prompt)
        
        while resp != ans1 and resp != ans2:
            print('Invalid entry, please enter "{}" or "{}" to proceed.'.format(ans1, ans2))
            resp = input(prompt)
        
        print()

        if resp == ans1:
            return 1
        else:
            return 0
        
    def gameOver(self):
        print('\nThanks for playing!')
        
    def updateCurrentStats(self, frodo, currentStep, totalSteps):
        "Print the current game stats"
        if currentStep == totalSteps:
            print('*** Game Summary ***')
        else:
            print('*** Status Report ***')
        print('Companions: {}'.format(self._stringifySeq(frodo.getCompanions())))
        print('Health: {}'.format(frodo.getHealth()))
        print('Ring Resistance: {0:0.1f}%'.format(frodo.getTimeToWearRingRemaining()))
        if currentStep == totalSteps:
            print('You have completed all {} steps - game over'.format(currentStep))
        else:
            print('Completed step {} of {} on your journey.'.format(currentStep, totalSteps))
        print()
        
    def _stringifySeq(self, seq, n=0):
        "Takes a sequence of strings and concatenates them together into a single string"
        if n >= len(seq):
            return ''
        else:
            sep = ', '
            if n == (len(seq) - 1):
                sep = ''
            return '' + seq[n] + sep + self._stringifySeq(seq, n=n+1)

    def introAttack(self, enemy, attackData):
        print('{} is/are attacking!'.format(enemy.getName()))

        userDecision = input(attackData['responseOptions']['prompt'])
        print()
        
        opt1 = attackData['responseOptions']['outcomes'][0]['choice']
        opt2 = attackData['responseOptions']['outcomes'][1]['choice']
        
        validInput = [opt1, opt2]
    
        while validInput.count(userDecision) == 0:
            print('Invalid input, please enter "{}" or "{}" to proceed'.format(opt1, opt2))
            userDecision = input(attackData['responseOptions']['prompt'])
            print()
        
        response = attackData['responseOptions']['outcomes'][validInput.index(userDecision)]
        self._printMessages(response['messages'])
            
        return response
    
    def frodoDied(self):
        print('Your enemy proved to be too much!')
        print('Better luck next time.')
        print()

    def frodoOvertakenByRing(self):
        print('The ring proved to be too much, and Frodo was overtaken by it\'s power!')
        print('Better luck next time.')
        print()
    
    def attackSummary(self, attackRoundWins, enemy, prevHealth, currentHealth):
        "Prints the attack summary."
        print('=== Attack results ===')
        
        healthLost = prevHealth - currentHealth
        if attackRoundWins['frodo'] > attackRoundWins['enemy']:
            if healthLost > 0:
                print('You won! But the battle took a toll - you lost {} health.'.format(healthLost))
            else:
                print('You won! And you managed to defeat your enemy without getting hurt!')
        else:
            print('{} won! You lost {} health.'.format(enemy.getName(), healthLost))
        print()