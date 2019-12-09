from Person import Person

class Customer(Person):

    def __str__(self):
        return 'Customer<' + super().__str__() + '>'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.purchased_items = []
        self.loyalty_program = {
            'isMember': False,
            'points': 0
        }

    def enroll_in_loyalty_program(self):
        self.loyalty_program['isMember'] = True

    def is_loyalty_program_member(self):
        return self.loyalty_program['isMember']

    def get_loyalty_program_points(self):
        return self.loyalty_program['points']

    def make_purchase(self, purchased_item):
        if self.account_balance < purchased_item['price']:
            return self.__str__() + ' insufficient funds to purchase item!'
        else:
            self.purchased_items.append(purchased_item)
            self.charge_account(purchased_item['price'])
            return self.__str__() + ' purchased' + purchased_item['name']