from bsb_parser.sauces import base_sauce


class ComboSauce(base_sauce.BaseSauce):
    def __init__(self, name, consistency, category, description, riffed_sauces):
        super().__init__(name, consistency='all')
        if category == 'hot':
            self.category = 'Hot 🔥'
        if category == 'award':
            self.category = 'Award Winning 👑'
        if category == 'new':
            self.category = 'New 🐣'
        if category == 'classic':
            self.category = 'Classic Flavor *️'
        if category == 'pop':
            self.category = 'Popular 😍'
        if category == 'spicy':
            self.category = 'Spicy 🌶️'
        if category == 'sweet':
            self.category = 'Sweet 🍭'
        if category == 'sure':
            self.category = 'Sure Shot 𐀏'
        if category is None:
            self.category = None

        self.description = description

        self.riffed_sauces = riffed_sauces
        if self.riffed_sauces is not None:
            self.gather_riffed_sauces()

    def gather_riffed_sauces(self):
        pass

    def show_sauce_stats(self):
        print(f'Name: {self.name}\n'
              f'Consistency: {self.consistency}\n'
              f'Category: {self.category}\n'
              f'Description: {self.description}\n'
              f'Riffed Sauces: {self.riffed_sauces}\n'
              f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


def create_combo_sauces_list():
    ace_boogie = ComboSauce('Ace Boogie', 'buttered', 'award',
                            'Black Magic, Butter, Dry Ranch', ['black_magic', 'ranch'])
    aint_my_faulks = ComboSauce('Ain\'t My Faulks', ['buttered', 'dry'], 'new',
                                'Butter, Dry BBQ, Dry Carlic, Dry Ranch', ['bbq', 'garlic', 'ranch'])
    ashy_larry = ComboSauce('Ashy Larry', 'dry', None,
                            'Local Legend, Our Driest Seasoning', ['local legend'])
    results = [
        ace_boogie,
        aint_my_faulks,
        ashy_larry,
    ]

    return results


if __name__ == '__main__':
    combo_sauces_list = create_combo_sauces_list()
    test = base_sauce.search_sauce_list('ashy larry', combo_sauces_list)
    test.show_sauce_stats()
