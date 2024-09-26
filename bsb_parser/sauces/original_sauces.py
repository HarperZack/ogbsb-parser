from bsb_parser.sauces import base_sauce, sauce_names

class OriginalSauce(base_sauce.BaseSauce):
    def __init__(self, name, consistency='wet'):
        super().__init__(name, consistency)

    def show_sauce_stats(self):
        print(f'Name: {self.name}\n'
              f'Consistency: {self.consistency}\n'
              f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


def create_original_sauces_list():
    all_in = OriginalSauce(sauce_names.ALL_IN, 'all')
    bbq = OriginalSauce(sauce_names.BBQ, 'all')
    bbq_ranch = OriginalSauce(sauce_names.BBQ_RANCH, 'all')
    bobs_honey_mustard = OriginalSauce(sauce_names.BOBS_HONEY_MUSTARD)
    bobs_signature_hot = OriginalSauce(sauce_names.BOBS_SIGNATURE_HOT)
    cajun = OriginalSauce(sauce_names.CAJUN, 'all')
    cajun_garlic = OriginalSauce(sauce_names.CAJUN_GARLIC, 'all')
    cajun_ranch = OriginalSauce(sauce_names.CAJUN_RANCH, 'all')
    dark_bbq = OriginalSauce(sauce_names.DARK_BBQ)
    franks_red_hot = OriginalSauce(sauce_names.FRANKS_RED_HOT)
    garlic_butter = OriginalSauce(sauce_names.GARLIC_BUTTER)
    garlic_butter_dry = OriginalSauce(sauce_names.GARLIC_BUTTER_DRY, 'dry')
    garlic_butter_parm = OriginalSauce(sauce_names.GARLIC_BUTTER_PARM)
    garlic_ranch = OriginalSauce(sauce_names.GARLIC_RANCH, 'all')
    gold = OriginalSauce(sauce_names.GOLD)
    honey_bbq = OriginalSauce(sauce_names.HONEY_BBQ)
    honey_cajun = OriginalSauce(sauce_names.HONEY_CAJUN)
    honey_dijon = OriginalSauce(sauce_names.HONEY_DIJON)
    honey_garlic = OriginalSauce(sauce_names.HONEY_GARLIC)
    honey_old_bay = OriginalSauce(sauce_names.HONEY_OLD_BAY)
    honey_ranch = OriginalSauce(sauce_names.HONEY_RANCH)
    hot_buffalo_cajun = OriginalSauce(sauce_names.HOT_BUFFALO_CAJUN)
    hot_buffalo_garlic = OriginalSauce(sauce_names.HOT_BUFFALO_GARLIC)
    hot_buffalo_garlic_parm = OriginalSauce(sauce_names.HOT_BUFFALO_GARLIC_PARM)
    hot_cajun = OriginalSauce(sauce_names.HOT_CAJUN, 'all')
    hot_garlic = OriginalSauce(sauce_names.HOT_GARLIC, 'all')
    hot_garlic_parm = OriginalSauce(sauce_names.HOT_GARLIC_PARM, 'all')
    hot_honey = OriginalSauce(sauce_names.HOT_HONEY)
    hot_honey_garlic = OriginalSauce(sauce_names.HOT_HONEY_GARLIC)
    hot_old_bay = OriginalSauce(sauce_names.HOT_OLD_BAY, 'all')
    hot_ranch_dry = OriginalSauce(sauce_names.HOT_RANCH_DRY, 'dry')
    hottest_of_the_hot = OriginalSauce(sauce_names.HOTTEST_OF_THE_HOT)
    lemon_pepper = OriginalSauce(sauce_names.LEMON_PEPPER, 'all')
    lemon_pepper_parm = OriginalSauce(sauce_names.LEMON_PEPPER_PARM, 'all')
    lemon_pepper_ranch = OriginalSauce(sauce_names.LEMON_PEPPER_RANCH, 'all')
    medium = OriginalSauce(sauce_names.MEDIUM)
    medium_garlic_parm = OriginalSauce(sauce_names.MEDIUM_GARLIC_PARM)
    mild = OriginalSauce(sauce_names.MILD)
    mild_garlic_parm = OriginalSauce(sauce_names.MILD_GARLIC_PARM)
    mild_old_bay = OriginalSauce(sauce_names.MILD_OLD_BAY)
    mild_ranch = OriginalSauce(sauce_names.MILD_RANCH)
    old_bay = OriginalSauce(sauce_names.OLD_BAY, 'all')
    old_bay_ranch = OriginalSauce(sauce_names.OLD_BAY_RANCH, 'all')
    peppercorn_ranch = OriginalSauce(sauce_names.PEPPERCORN_RANCH)
    peppercorn_ranch_parm = OriginalSauce(sauce_names.PEPPERCORN_RANCH_PARM)
    plain = OriginalSauce(sauce_names.PLAIN)
    ranch = OriginalSauce(sauce_names.RANCH, 'all')
    salt_and_pepper = OriginalSauce(sauce_names.SALT_AND_PEPPER, 'all')
    salt_and_vinegar = OriginalSauce(sauce_names.SALT_AND_VINEGAR)
    seasoned = OriginalSauce(sauce_names.SEASONED)
    teriyaki = OriginalSauce(sauce_names.TERIYAKI)

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

ORIGINAL_SAUCE_LIST = create_original_sauces_list()

if __name__ == '__main__':
    test = base_sauce.search_sauce_list(sauce_names.BOBS_HONEY_MUSTARD, ORIGINAL_SAUCE_LIST)
    print(sauce_names.BOBS_HONEY_MUSTARD)
    test.show_sauce_stats()

