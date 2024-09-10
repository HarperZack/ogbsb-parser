from bsb_parser.sauces import base_sauce, sauce_names

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
    ace_boogie = ComboSauce(sauce_names.ACE_BOOGIE, 'buttered', 'award',
                            'Black Magic, Butter, Dry Ranch', ['black_magic', 'ranch'])
    aint_my_faulks = ComboSauce(sauce_names.AINT_MY_FAULKS, ['buttered', 'dry'], 'new',
                                'Butter, Dry BBQ, Dry Carlic, Dry Ranch', ['bbq', 'garlic', 'ranch'])
    ashy_larry = ComboSauce(sauce_names.ASHY_LARRY, 'dry', None,
                            'Local Legend, Our Driest Seasoning', ['local legend'])
    bad = ComboSauce(sauce_names.BAD)
    baby_blues = ComboSauce(sauce_names.BABY_BLUES)
    big_easy = ComboSauce(sauce_names.BIG_EASY)
    big_fine_woman = ComboSauce(sauce_names.BIGFINEWOMAN2000)
    big_picture = ComboSauce(sauce_names.THE_BIG_PICTURE)
    big_sexy = ComboSauce(sauce_names.BIG_SEXY)
    black_and_gold = ComboSauce(sauce_names.BLACK_AND_GOLD)
    black_and_mild = ComboSauce(sauce_names.BLACK_AND_MILD)
    black_and_yellow = ComboSauce(sauce_names.BLACK_AND_YELLOW)
    black_and_frank_white = ComboSauce(sauce_names.BLACK_FRANK_WHITE)
    black_magic = ComboSauce(sauce_names.BLACK_MAGIC)
    black_opts = ComboSauce(sauce_names.BLACK_OPTS)
    blue_steel = ComboSauce(sauce_names.BLUE_STEEL)
    buc_nasty = ComboSauce(sauce_names.BUC_NASTY)
    bugg_wings = ComboSauce(sauce_names.BUGG_WINGS)
    butter_ss = ComboSauce(sauce_names.BUTTER_SS)
    cali_love = ComboSauce(sauce_names.CALI_LOVE)
    capt_jack = ComboSauce(sauce_names.CAPT_JACK)
    capt_insano = ComboSauce(sauce_names.CAPT_INSANO)
    cash_grab = ComboSauce(sauce_names.CASH_CLUB)
    chains = ComboSauce(sauce_names.CHAINS)
    chili_palmer = ComboSauce(sauce_names.CHILI_PALMER)
    coffee_black = ComboSauce(sauce_names.COFFEE_BLACK)
    cool_runnings = ComboSauce(sauce_names.COOL_RUNNINGS)
    cousin_larry = ComboSauce(sauce_names.COUSIN_LARRY)
    crazy_joes = ComboSauce(sauce_names.CRAZY_JOES)
    d_and_a = ComboSauce(sauce_names.D_AND_A)
    dusty_roads = ComboSauce(sauce_names.DUSTY_ROADS)
    escobar_season = ComboSauce(sauce_names.ESCOBAR_SEASON)
    eye_of_the_tiger = ComboSauce(sauce_names.EYE_OF_THE_TIGER)
    flaming_flamingo = ComboSauce(sauce_names.FLAMING_FLAMINGO)
    flossin_season = ComboSauce(sauce_names.FLOSSIN_SEASON)
    fly_gators = ComboSauce(sauce_names.FLY_GATORS)
    fools_gold = ComboSauce(sauce_names.FOOLS_GOLD)
    foxy_brown = ComboSauce(sauce_names.FOXY_BROWN)
    frank_sinatra = ComboSauce(sauce_names.FRANK_SINATRA)
    frank_white = ComboSauce(sauce_names.FRANK_WHITE)
    frankie_valli = ComboSauce(sauce_names.FRANKIE_VALLI)
    furios = ComboSauce(sauce_names.FURIOS)
    g_black = ComboSauce(sauce_names.G_BLACK)
    gamechanger = ComboSauce(sauce_names.GAMECHANGER)




    results = [
        ace_boogie,
        aint_my_faulks,
        ashy_larry,
        bad,
        baby_blues,
        big_easy,
        big_fine_woman,
        big_picture,
        big_sexy,
        black_and_gold,
        black_and_mild,
        black_and_yellow,
        black_and_frank_white,
        black_magic,
        black_opts,
        blue_steel,
        buc_nasty,
        bugg_wings,
        butter_ss,
        cali_love,
        capt_jack,
        capt_insano,
        cash_grab,
        chains,
        chili_palmer,
        coffee_black,
        cool_runnings,
        cousin_larry,
        crazy_joes,
        d_and_a



    ]

    return results


if __name__ == '__main__':
    combo_sauces_list = create_combo_sauces_list()
    test = base_sauce.search_sauce_list(sauce_names.ASHY_LARRY, combo_sauces_list)
    test.show_sauce_stats()
