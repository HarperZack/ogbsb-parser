class BaseSauce:
    sauce_consistencies = [
        'wet',
        'buttered',
        'dry'
    ]

    def __init__(self, name, consistency='wet'):
        self.name = name

        if consistency.lower() == 'all':
            self.consistency = ['wet', 'buttered', 'dry']
        if consistency.lower() in self.sauce_consistencies:
            self.consistency = consistency


def search_sauce_list(name, list):
    for sauce in list:
        if '\'' in sauce.name.lower():
            parsed_name = sauce.name.lower().replace('\'', '')
            if parsed_name.lower() == name.lower():
                return sauce
    for sauce in list:
        if sauce.name.lower() == name.lower():
            return sauce
