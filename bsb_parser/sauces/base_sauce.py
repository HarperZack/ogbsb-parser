class BaseSauce:
    sauce_consistencies = [
        'wet',
        'buttered',
        'dry'
    ]

    def __init__(self, name, consistency='wet'):
        consistencies = list()
        consistencies.append(consistency)
        self.name = name
        for state in consistencies:
            if state.lower() == 'all':
                self.consistency = ['Wet', 'Buttered', 'Dry']
                break
            if state.lower() in self.sauce_consistencies:
                self.consistency = state.capitalize()

def search_sauce_list(name, sauce_list):
    for sauce in sauce_list:
        if '\'' in sauce.name:
            parsed_name = sauce.name.replace('\'', '')
            if parsed_name == name:
                return sauce
    for sauce in sauce_list:
        if sauce.name == name:
            return sauce
