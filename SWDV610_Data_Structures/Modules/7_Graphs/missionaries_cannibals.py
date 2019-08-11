from copy import deepcopy

class MissionaryAndCannibals:

    def __init__(self, num_of_each=3):
        self.bank1 = {'cannibals': num_of_each, 'missionaries': num_of_each}
        self.bank2 = {'cannibals': 0, 'missionaries': 0}
        self.boat = {'cannibals': 0, 'missionaries': 0}
        self.moves = []
        self.num_of_each = num_of_each
        self.moves.append({
            'summary': 'Start',
            'state': self.get_state()
        })


    def run(self):
        # while there are people on bank 1
        while not self.complete():
            if self.boat_has_space():
                self._transfer()

    def _transfer(self):
        self.load_boat()
        self.unload_boat()

    def boat_has_space(self):
        return self.boat.get('cannibals') + self.boat.get('missionaries') < 2

    def load_boat(self):
        summary = None
        if self.bank1.get('cannibals') > 0 or self.bank1.get('missionaries') > 0:
            # if there are an equal number of missionaries as cannibals on bank 1
            if self.bank1.get('missionaries') == self.bank1.get('cannibals'):
                # load boat with cannibal
                self._load('cannibals')
                summary = 'cannibal loaded on boat'
            else: # load boat with missionary
                self._load('missionaries')
                summary = 'missionary loaded on boat'
            self.moves.append({
                'summary': summary,
                'state': self.get_state()
            })

    def _load(self, person):
        self.bank1[person] -= 1
        self.boat[person] += 1

    def unload_boat(self):
        summary = None
        if self.boat.get('missionaries') + self.boat.get('cannibals') == 2 or self.bank1_is_empty():
            # if there are an equal number of missionaries as cannibals on bank 2
            if self.bank2.get('missionaries') == self.bank2.get('cannibals'):
                # unload missionary
                self._unload('missionaries')
                summary = 'missionary unloaded from boat'
            else: # unload cannibal
                self._unload('cannibals')
                summary = 'cannibal unloaded from boat'

            self.moves.append({
                'summary': summary,
                'state': self.get_state()
            })

    def _unload(self, person):
        self.boat[person] -= 1
        self.bank2[person] += 1

    def bank1_is_empty(self):
        return self.bank1.get('cannibals') <= 0 and self.bank1.get('missionaries') <= 0

    def bank2_is_full(self):
        return self.bank2.get('cannibals') >= self.num_of_each and self.bank2.get('missionaries') >= self.num_of_each

    def boat_is_empty(self):
        return self.boat.get('cannibals') == 0 and self.boat.get('missionaries') == 0

    def complete(self):
        return self.bank1_is_empty() and self.bank2_is_full()

    def get_state(self):
        return {
            'bank1': deepcopy(self.bank1),
            'bank2': deepcopy(self.bank2),
            'boat': deepcopy(self.boat)
        }

    def print_state(self):
        print() # print space
        print('Bank 1 : {} cannibal(s), {} missionary/ies'.format(self.bank1.get('cannibals'), self.bank1.get('missionaries')))
        print('Boat   : {} cannibal(s), {} missionary/ies'.format(self.boat.get('cannibals'), self.boat.get('missionaries')))
        print('Bank 2 : {} cannibal(s), {} missionary/ies'.format(self.bank2.get('cannibals'), self.bank2.get('missionaries')))


def pretty_print(moves):
    print('Number of moves:', len(moves) - 2)
    for move in moves:
        print('Move Summary:', move.get('summary'))
        print('Bank 1 :', move.get('state').get('bank1'))
        print('Boat   :', move.get('state').get('boat'))
        print('Bank 2 :', move.get('state').get('bank2'))
        print()


def main():
    mc = MissionaryAndCannibals()
    mc.run()

    pretty_print(mc.moves)


if __name__ == '__main__':
    main()