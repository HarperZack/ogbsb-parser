from bsb_parser.sauces import base_sauce


class OriginalSauce(base_sauce.BaseSauce):
    def __init__(self, name, consistency='wet'):
        super().__init__(name, consistency)

    def show_sauce_stats(self):
        print(f'Name: {self.name}\n'
              f'Consistency: {self.consistency}\n'
              f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


def create_original_sauces_list():
    all_in = OriginalSauce('All In', 'all')
    bbq = OriginalSauce('BBQ', 'all')
    bbq_ranch = OriginalSauce('BBQ Ranch', 'all')
    bobs_honey_mustard = OriginalSauce('Bob\'s Honey Mustard')
    bobs_signature_hot = OriginalSauce('Bob\'s Signature Hot')
    cajun = OriginalSauce('Cajun', 'all')
    cajun_garlic = OriginalSauce('Cajun Garlic', 'all')
    cajun_ranch = OriginalSauce('Cajun Ranch', 'all')
    dark_bbq = OriginalSauce('Dark BBQ')
    franks_red_hot = OriginalSauce('Frank\'s Red Hot')
    garlic_butter = OriginalSauce('Garlic Butter')
    garlic_butter_dry = OriginalSauce('Garlic Butter Dry', 'dry')
    garlic_butter_parm = OriginalSauce('Garlic Butter Parm')
    garlic_ranch = OriginalSauce('Garlic Ranch', 'all')
    gold = OriginalSauce('Gold')
    honey_bbq = OriginalSauce('Honey BBQ')
    honey_cajun = OriginalSauce('Honey Cajun')
    honey_dijon = OriginalSauce('Honey Dijon')
    honey_garlic = OriginalSauce('Honey Garlic')
    honey_old_bay = OriginalSauce('Honey Old Bay')
    honey_ranch = OriginalSauce('Honey Ranch')
    hot_buffalo_cajun = OriginalSauce('Hot Buffalo Cajun')
    hot_buffalo_garlic = OriginalSauce('Hot Buffalo Garlic')
    hot_buffalo_garlic_parm = OriginalSauce('Hot Buffalo Garlic Parm')
    hot_cajun = OriginalSauce('Hot Cajun', 'all')
    hot_garlic = OriginalSauce('Hot Garlic', 'all')
    hot_garlic_parm = OriginalSauce('Hot Garlic Parm', 'all')
    hot_honey = OriginalSauce('Hot Honey')
    hot_honey_garlic = OriginalSauce('Hot Honey Garlic')
    hot_old_bay = OriginalSauce('Hot Old Bay', 'all')
    hot_ranch_dry = OriginalSauce('Hot Ranch Dry', 'dry')
    hottest_of_the_hot = OriginalSauce('Hottest of the Hot')
    lemon_pepper = OriginalSauce('Lemon Pepper', 'all')
    lemon_pepper_parm = OriginalSauce('Lemon Pepper Parm', 'all')
    lemon_pepper_ranch = OriginalSauce('Lemon Pepper Ranch', 'all')
    medium = OriginalSauce('Medium')
    medium_garlic_parm = OriginalSauce('Medium Garlic Parm')
    mild = OriginalSauce('Mild')
    mild_garlic_parm = OriginalSauce('Mild Garlic Parm')
    mild_old_bay = OriginalSauce('Mild Old Bay')
    mild_ranch = OriginalSauce('Mild Ranch')
    old_bay = OriginalSauce('Old Bay', 'all')
    old_bay_ranch = OriginalSauce('Old Bay Ranch', 'all')
    peppercorn_ranch = OriginalSauce('Peppercorn Ranch')
    peppercorn_ranch_parm = OriginalSauce('Peppercorn Parm')
    plain = OriginalSauce('Plain')
    ranch = OriginalSauce('Ranch', 'all')
    salt_and_pepper = OriginalSauce('Salt and Pepper', 'all')
    salt_and_vinegar = OriginalSauce('Sale and Vinegar')
    seasoned = OriginalSauce('Seasoned')
    teriyaki = OriginalSauce('Teriyaki')

    results = [
        all_in,
        bbq,
        bbq_ranch,
        bobs_honey_mustard,
        bobs_signature_hot,
        cajun,
        cajun_garlic,
        cajun_ranch,
        dark_bbq,
        franks_red_hot,
        garlic_butter,
        garlic_butter_dry,
        garlic_butter_parm,
        garlic_ranch,
        gold,
        honey_bbq,
        honey_cajun,
        honey_dijon,
        honey_garlic,
        honey_old_bay,
        honey_ranch,
        hot_buffalo_cajun,
        hot_buffalo_garlic,
        hot_buffalo_garlic_parm,
        hot_cajun,
        hot_garlic,
        hot_garlic_parm,
        hot_honey,
        hot_honey_garlic,
        hot_old_bay,
        hot_ranch_dry,
        hottest_of_the_hot,
        lemon_pepper,
        lemon_pepper_parm,
        lemon_pepper_ranch,
        medium,
        medium_garlic_parm,
        mild,
        mild_garlic_parm,
        mild_old_bay,
        mild_ranch,
        old_bay,
        old_bay_ranch,
        peppercorn_ranch,
        peppercorn_ranch_parm,
        plain,
        ranch,
        salt_and_pepper,
        salt_and_vinegar,
        seasoned,
        teriyaki
    ]

    return results


if __name__ == '__main__':
    original_sauces_list = create_original_sauces_list()

    test = base_sauce.search_sauce_list('bobs honey mustard', original_sauces_list)
    test.show_sauce_stats()
