class BaseSauce:
    sauce_consistencies = [
        'wet',
        'buttered',
        'dry'
    ]

    def __init__(self, name, consistency='wet'):
        self.name = name
        for state in consistency:
            if state.lower() == 'all':
                self.consistency = ['Wet', 'Buttered', 'Dry']
            if state.lower() in self.sauce_consistencies:
                self.consistency = consistency.capitalize()


def search_sauce_list(name, list):
    for sauce in list:
        if '\'' in sauce.name:
            parsed_name = sauce.name.replace('\'', '')
            if parsed_name == name:
                return sauce
    for sauce in list:
        if sauce.name == name:
            return sauce
