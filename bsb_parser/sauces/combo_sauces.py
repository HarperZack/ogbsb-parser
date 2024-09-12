from bsb_parser.sauces import base_sauce, sauce_names
from bsb_parser.sauces.sauce_names import LIL_DAYNE


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

    def gather_riffed_sauces(self, sauce):
        pass

    def show_sauce_stats(self):
        print(f'Name: {self.name}\n'
              f'Consistency: {self.consistency}\n'
              f'Category: {self.category}\n'
              f'Description: {self.description}\n'
              f'Riffed Sauces: {self.riffed_sauces}\n'
              f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


def create_combo_sauces_list():
    ace_boogie = ComboSauce(sauce_names.ACE_BOOGIE, 'buttered', 'classic',
                            'Black Magic, Butter, Dry Ranch', [sauce_names.BLACK_MAGIC, sauce_names.RANCH])
    aint_my_faulks = ComboSauce(sauce_names.AINT_MY_FAULKS, ['buttered', 'dry'], 'new',
                                'Butter, Dry BBQ, Dry Carlic, Dry Ranch', [sauce_names.BBQ, sauce_names.GARLIC_RANCH])
    ashy_larry = ComboSauce(sauce_names.ASHY_LARRY, 'dry', None,
                            'Local Legend, Our Driest Seasoning', None)
    bad = ComboSauce(sauce_names.BAD, 'dry', 'hot',
                     'Buttered Atomic Dust', None)
    baby_blues = ComboSauce(sauce_names.BABY_BLUES, 'all', 'spicy',
                            'Blue Cheese, Frank\'s, Cayenne', None)
    big_easy = ComboSauce(sauce_names.BIG_EASY, 'all', 'spicy',
                          'BSB\'s Louisana Licker', None)
    big_fine_woman = ComboSauce(sauce_names.BIGFINEWOMAN2000, 'all', 'classic',
                                'Dark BBQ and Black Magic', [sauce_names.DARK_BBQ, sauce_names.BLACK_MAGIC])
    big_picture = ComboSauce(sauce_names.THE_BIG_PICTURE, 'all', None,
                             'Salt, Butter, and Parm', None)
    big_sexy = ComboSauce(sauce_names.BIG_SEXY, 'all', 'pop',
                          'Mark\'s signature flavor', None)
    black_and_gold = ComboSauce(sauce_names.BLACK_AND_GOLD, 'wet', 'pop',
                                'Gold BBQ & Black Magic', [sauce_names.GOLD, sauce_names.BBQ, sauce_names.BLACK_MAGIC])
    black_and_mild = ComboSauce(sauce_names.BLACK_AND_MILD, 'wet', 'classic',
                                'Mild Sauce and Black Magic', [sauce_names.MILD, sauce_names.BLACK_MAGIC])
    black_and_yellow = ComboSauce(sauce_names.BLACK_AND_YELLOW, 'wet', 'classic',
                                  'Sweet, Honey Mustard, & Black Magic', [sauce_names.BOBS_HONEY_MUSTARD, sauce_names.BLACK_MAGIC])
    black_and_frank_white = ComboSauce(sauce_names.BLACK_FRANK_WHITE, 'wet', 'pop',
                                       'Frank\'s White with Black Magic', [sauce_names.FRANK_WHITE, sauce_names.BLACK_MAGIC])
    black_magic = ComboSauce(sauce_names.BLACK_MAGIC, 'buttered','award',
                             'Butter & Black Magic Cajun Seasoning', [sauce_names.BLACK_MAGIC, sauce_names.CAJUN])
    black_opts = ComboSauce(sauce_names.BLACK_OPTS, 'buttered', None,
                            'Buttered Precision Spice', None)
    blue_steel = ComboSauce(sauce_names.BLUE_STEEL, 'wet', None,
                            'Mild Buffalo, Blue Cheese, and Parm', None)
    buc_nasty = ComboSauce(sauce_names.BUC_NASTY, 'wet', 'award',
                           'Honey Buffalo BBQ with Cajun', [sauce_names.HONEY_BBQ, sauce_names.HOT_BUFFALO_CAJUN])
    bugg_wings = ComboSauce(sauce_names.BUGG_WINGS, ['buttered'], 'new',
                            'Buttered honey with a chili lime molasses rub', [sauce_names.ESCOBAR_SEASON])
    butter_ss = ComboSauce(sauce_names.BUTTER_SS, 'buttered', None,
                           'Buttered Signature Seasoned', None)
    cali_love = ComboSauce(sauce_names.CALI_LOVE, 'wet', 'new',
                           'Hot Mango Habanero', None)
    capt_jack = ComboSauce(sauce_names.CAPT_JACK, 'wet', 'new',
                           'Mild Ranch with Spicy Seasonings', [sauce_names.MILD_RANCH])
    capt_insano = ComboSauce(sauce_names.CAPT_INSANO, 'buttered', 'hot',
                             'Buttered Honey with Hot Dry Buffalo', None)
    cash_grab = ComboSauce(sauce_names.CASH_CLUB, 'wet', 'pop',
                           'Mild Ranch with Garlic Butter Parm', [sauce_names.MILD_RANCH, sauce_names.GARLIC_BUTTER_PARM])
    chains = ComboSauce(sauce_names.CHAINS, 'wet', 'sure',
                        'Talk of Beaver Falls adding Ranch and Parm', [sauce_names.TALK_OF_BEAVER_FALLS, sauce_names.PEPPERCORN_RANCH_PARM])
    chili_palmer = ComboSauce(sauce_names.CHILI_PALMER, 'wet', 'sure',
                              'Ranch Dressing with Chili Powder', [sauce_names.RANCH])
    coffee_black = ComboSauce(sauce_names.COFFEE_BLACK, 'buttered', 'sure',
                              'Buttered Blackened coffee rub', None)
    cool_runnings = ComboSauce(sauce_names.COOL_RUNNINGS, 'wet', 'classic',
                               'Jamacian Jerk, Ranch', [sauce_names.JAMACIAN_JERK, sauce_names.RANCH])
    cousin_larry = ComboSauce(sauce_names.COUSIN_LARRY, 'buttered', None,
                              'Buttered Ashy Larry', [sauce_names.ASHY_LARRY])
    crazy_joes = ComboSauce(sauce_names.CRAZY_JOES, 'wet', 'new',
                            'Flaming Flamingo, Uncle Nick\'s, and Napoleon', [sauce_names.FLAMING_FLAMINGO, sauce_names.UNCLE_NICKS, sauce_names.NAPOLEON])
    d_and_a = ComboSauce(sauce_names.D_AND_A, 'buttered', 'new',
                         'Foxy Brown adding Honey', [sauce_names.FOXY_BROWN])
    dusty_roads = ComboSauce(sauce_names.DUSTY_ROADS, 'dry', None,
                             'Pepper and Celery Salt', None)
    escobar_season = ComboSauce(sauce_names.ESCOBAR_SEASON, 'dry', 'new',
                                'Chili Lime seasoning', None)
    eye_of_the_tiger = ComboSauce(sauce_names.EYE_OF_THE_TIGER, 'wet', 'pop',
                                  'Talk of Beaver Falls add Ranch', [sauce_names.TALK_OF_BEAVER_FALLS, sauce_names.RANCH])
    flaming_flamingo = ComboSauce(sauce_names.FLAMING_FLAMINGO, 'wet', 'pop',
                                  'Hot Garlic Chili Ranch', [sauce_names.HOT_GARLIC, sauce_names.RANCH])
    flossin_season = ComboSauce(sauce_names.FLOSSIN_SEASON, 'dry', None,
                                'Dry Ranch and Lowry\'s', [sauce_names.RANCH])
    fly_gators = ComboSauce(sauce_names.FLY_GATORS, 'wet', None,
                            'Honey Jalapeno with Buffalo Seasoning', None)
    fools_gold = ComboSauce(sauce_names.FOOLS_GOLD, 'wet', 'sure',
                            'Mildly Seasoned Gold BBQ topped with Parm', [sauce_names.GOLD, sauce_names.BBQ])
    foxy_brown = ComboSauce(sauce_names.FOXY_BROWN, 'buttered', 'sure',
                            'Buttered cinnamon chipotle coffee rub', [sauce_names.COFFEE_BLACK])
    frank_sinatra = ComboSauce(sauce_names.FRANK_SINATRA, 'wet', 'popular',
                               'Frank\'s, Blue Cheese, Parm', [sauce_names.FRANKS_RED_HOT])
    frank_white = ComboSauce(sauce_names.FRANK_WHITE, 'wet', 'pop',
                             'Mixture of Frank\'s and Ranch', [sauce_names.FRANKS_RED_HOT, sauce_names.RANCH])
    frankie_valli = ComboSauce(sauce_names.FRANKIE_VALLI, 'wet', 'pop',
                               'Mixture of Frank\'s, Ranch, and Parm', [sauce_names.FRANKS_RED_HOT, sauce_names.PEPPERCORN_RANCH_PARM])
    furios = ComboSauce(sauce_names.FURIOS, 'wet', 'new',
                        'Stickiest of the Icky adding Ranch', [sauce_names.STICKIEST_OF_THE_ICKY, sauce_names.RANCH])
    g_black = ComboSauce(sauce_names.G_BLACK, 'buttered', 'new',
                         'Black Magic with Garlic', [sauce_names.BLACK_MAGIC])
    gamechanger = ComboSauce(sauce_names.GAMECHANGER, 'wet', 'pop',
                             'Butter, Seasonings and Parm with Ranch', [sauce_names.BUTTER_SS, sauce_names.PEPPERCORN_RANCH_PARM]),
    general_tsos = ComboSauce(sauce_names.GENERAL_TSOS, 'wet', None,
                              'Traditional Asian Sauce', None)
    gold_fire = ComboSauce(sauce_names.GOLD_FIRE, 'wet', 'hot',
                           'Hot Gold BBQ', [sauce_names.GOLD, sauce_names.BBQ])
    good_riddance = ComboSauce(sauce_names.GOOD_RIDDANCE, 'wet', 'new',
                               'Black and Gold with Garlic and Parm', [sauce_names.BLACK_AND_GOLD, sauce_names.GARLIC_BUTTER_PARM])
    gung_ho = ComboSauce(sauce_names.GUNG_HO, 'wet', 'new',
                         'Korean BBQ', None)
    harlem_heat = ComboSauce(sauce_names.HARLEM_HEAT, 'dry', 'new',
                             'Dry Hot Buffalo Ranch', [sauce_names.HOT_BUFFALO_GARLIC, sauce_names.RANCH])
    harlem_shake = ComboSauce(sauce_names.HARLEM_SHAKE, 'buttered', 'new',
                              'Buttered Harlem Heat', [sauce_names.HARLEM_HEAT])
    honey_bunny = ComboSauce(sauce_names.HONEY_BUNNY, 'wet', 'sweet',
                             'Sweet Hot Chili Ranch', [sauce_names.RANCH])
    jaguar_paw = ComboSauce(sauce_names.JAGUAR_PAW, 'wet', 'new',
                            'Mean Green with a Chili Lime Cayenne Rub', [sauce_names.ESCOBAR_SEASON, sauce_names.MEAN_JOE_GREEN])
    jamacian_frank = ComboSauce(sauce_names.JAMACIAN_FRANK, 'wet', 'hot',
                                'HOT Jamacian Jerk', [sauce_names.JAMACIAN_JERK])
    jamacian_jerk = ComboSauce(sauce_names.JAMACIAN_JERK, 'buttered', 'classic',
                               'Butter and Jerk', None)
    jimmy_jump = ComboSauce(sauce_names.JIMMY_JUMP, 'dry', None,
                            'Frank White Dry Jerk Seasoning', [sauce_names.FRANK_WHITE])
    jive_turkey = ComboSauce(sauce_names.JIVE_TURKEY, 'all', None,
                             'Be thankful (Seriously, what even is does this mean???)', None)
    king_joffy_joe = ComboSauce(sauce_names.KING_JOFFY_JOE, 'wet', 'new',
                                'Black and Gold adding Dark BBQ', [sauce_names.BLACK_AND_GOLD, sauce_names.DARK_BBQ])
    kurupt_cajun = ComboSauce(sauce_names.KURUPT_CAJUN, 'buttered', None,
                              'Buttered Blackened Cajun', [sauce_names.CAJUN])
    lady_luck = ComboSauce(sauce_names.LADY_LUCK, 'wet', 'sure',
                           'Hot Sauce and Ranch Seasoning', [sauce_names.FRANKS_RED_HOT, sauce_names.RANCH])
    lavish_habits = ComboSauce(sauce_names.LAVISH_HABITS, 'buttered', None,
                               'Garlic Butter with Honey', None)
    lbj2la = ComboSauce(sauce_names.LBJ2LA, 'wet', 'sweet',
                        'Raspberry, Honey Mustard, and Black Magic', [sauce_names.BOBS_HONEY_MUSTARD, sauce_names.BLACK_MAGIC])
    lil_broski = ComboSauce(sauce_names.LIL_BROSKI, 'buttered', 'sweet',
                            'Buttered Honey Sweet Seasoning', None)
    lil_dayne = ComboSauce(sauce_names.LIL_DAYNE, 'wet', 'new',
                           'Honey Gold BBQ with a tangy seasoning', [sauce_names.GOLD, sauce_names.BBQ])
    low_ball_larry = ComboSauce(sauce_names.LOW_BALL_LARRY, 'wet', 'new',
                                'Signature Hot Wings with Lemon Pepper', [sauce_names.BOBS_SIGNATURE_HOT, sauce_names.LEMON_PEPPER])
    macho_man = ComboSauce(sauce_names.MACHO_MAN, 'wet', 'hot',
                           'Extra Hot Magic Man', [sauce_names.MAGIC_MAN])
    magic_man = ComboSauce(sauce_names.MAGIC_MAN, 'wet', 'spicy',
                           'Hot Sauce and Black Magic', [sauce_names.FRANKS_RED_HOT, sauce_names.BLACK_MAGIC])
    mapletron = ComboSauce(sauce_names.MAPLETRON, 'wet', 'new',
                           'Black and Gold with Maple Rub', [sauce_names.BLACK_AND_GOLD])
    mean_joe_green = ComboSauce(sauce_names.MEAN_JOE_GREEN, 'wet', 'classicl',
                                'Black and Gold with a Green Jalapeno Sauce', [sauce_names.BLACK_AND_GOLD])
    mister_cs = ComboSauce(sauce_names.MISTER_CS, 'buttered', 'classic',
                           'Black Magic and Parm', [sauce_names.BLACK_MAGIC])
    most_interesting = ComboSauce(sauce_names.THE_MOST_INTERESTING_FLAVOR, 'wet', 'classic',
                                  'Not Hot, Very Interesting (Seriously, what does this mean???)', None)
    mouse_trap = ComboSauce(sauce_names.MOUSE_TRAP, 'buttered', 'pop',
                            'Ziggy with a Slight Tweak', [sauce_names.ZIGGY_STARDUST])
    mr_dynamite = ComboSauce(sauce_names.MR_DYNAMITE, 'wet', 'hot',
                             'Hot Mr. Northside', [sauce_names.MR_NORTHSIDE])
    mr_nice = ComboSauce(sauce_names.MR_NICE, 'buttered', None,
                         'Buttered Dry Jerk Ranch Rub', [sauce_names.RANCH])
    mr_northside = ComboSauce(sauce_names.MR_NORTHSIDE, 'wet', 'classic',
                              'Honey Mustard and BBQ', [sauce_names.BOBS_HONEY_MUSTARD, sauce_names.BBQ])
    mr_pipp = ComboSauce(sauce_names.MR_PIPP, 'buttered', 'new',
                         'Ace Boogie adding Parm', [sauce_names.ACE_BOOGIE])
    ms_parker = ComboSauce(sauce_names.MS_PARKER, 'wet', 'new',
                           'Most Interesting Flavor adding BLack Magic', [sauce_names.THE_MOST_INTERESTING_FLAVOR, sauce_names.BLACK_MAGIC])
    napoleon = ComboSauce(sauce_names.NAPOLEON, 'wet', None,
                          'Sweet Buffalo', None)
    napoleon_cajun = ComboSauce(sauce_names.NAPOLEON_CAJUN, 'wet', None,
                                'Napoleon add Cajun', [sauce_names.NAPOLEON, sauce_names.CAJUN])
    napoleon_complex = ComboSauce(sauce_names.NAPOLEON_COMPLEX, 'wet', None,
                                  'Napoleon and BSB\'s Seasoning', [sauce_names.NAPOLEON, sauce_names.SEASONED])
    napoleon_dynamite = ComboSauce(sauce_names.NAPOLEON_DYNAMITE, 'wet', 'hot',
                                   'Napoleon and Cayenne Pepper', [sauce_names.NAPOLEON])
    napoleon_garlic = ComboSauce(sauce_names.NAPOLEON_GARLIC, 'wet', None,
                                 'Napoleon add Garlic', sauce_names.NAPOLEON)
    ole_school = ComboSauce(sauce_names.OLE_SCHOOL, 'wet', None,
                            'BSB\'s Signature Seasoned Medium Sauce', None)
    oxs = ComboSauce(sauce_names.OXS, 'dry', 'spicy',
                     'BBQ Jerk', [sauce_names.JAMACIAN_JERK, sauce_names.BBQ])
    pigeon_wings = ComboSauce(sauce_names.PIGEON_WINGS, 'wet', 'classic',
                              'Napoleon with Garlic and Parmesan Cheese', [sauce_names.NAPOLEON])
    playmaker = ComboSauce(sauce_names.PLAYMAKER, 'buttered', 'sure',
                           'Gamechanger with Mild Buffalo', [sauce_names.GAMECHANGER])
    polish_hill_strangler = ComboSauce(sauce_names.POLISH_HILL_STRANGLER, 'wet', 'hot',
                                       'Honey Mustard and Cayenne Pepper', [sauce_names.BOBS_HONEY_MUSTARD])
    pookie = ComboSauce(sauce_names.POOKIE, 'wet', 'classic',
                        'Talk of Beaver Falls and Pigeon', [sauce_names.TALK_OF_BEAVER_FALLS, sauce_names.PIGEON_WINGS])
    primadonna = ComboSauce(sauce_names.PRIMADONNA, 'wet', 'sure',
                            'Ranch Buffalo Mildly Seasoned', [sauce_names.RANCH])
    primetime = ComboSauce(sauce_names.PRIMETIME, 'classic', 'wet',
                           'Sweet Hot Garlic Golden BBQ', [sauce_names.HOT_GARLIC, sauce_names.GOLD, sauce_names.BBQ])
    real_dill = ComboSauce(sauce_names.REAL_DILL, 'dry', 'new',
                           'Our first venture with Dill!', None)
    ringside_rosie = ComboSauce(sauce_names.RINGSIDE_ROSIE, 'wet', 'new',
                                'Flaming Flamingo with a Chili Lime Molasses Rub', [sauce_names.FLAMING_FLAMINGO, sauce_names.ESCOBAR_SEASON])
    seasoned_vet = ComboSauce(sauce_names.RINGSIDE_ROSIE, 'dry', None,
                              'Pepper and Seasoned Salt', None)
    shaolin_strut = ComboSauce(sauce_names.SHAOLIN_STRUT, 'wet', 'new',
                               'Gung Ho with Mr. C\'s and Honey', [sauce_names.GUNG_HO, sauce_names.MISTER_CS])
    sheltons_shooters = ComboSauce(sauce_names.SHELTONS_SHOOTERS, 'wet', 'new',
                                   'Medium Garlic Cajun Parm', [sauce_names.MEDIUM_GARLIC_PARM, sauce_names.CAJUN])
    showtime = ComboSauce(sauce_names.SHOWTIME, 'buttered', None,
                          'Salt and Butter', None)
    steel_city = ComboSauce(sauce_names.STEEL_CITY, 'wet', 'award',
                            'Mild Buffalo with Ranch Seasoning and Parm', [sauce_names.MILD, sauce_names.RANCH])
    steiner_recliner = ComboSauce(sauce_names.STEINER_RECLINER, 'wet', 'new',
                                  'Sweet Jones with Ranch', [sauce_names.SWEET_JONES, sauce_names.RANCH])
    stickiest = ComboSauce(sauce_names.STICKIEST_OF_THE_ICKY, 'wet', 'sweet',
                           'Honey and All In Dry', [sauce_names.ALL_IN])
    still_flossin = ComboSauce(sauce_names.STILL_FLOSSIN, 'buttered', 'sure',
                               'Buttered Flossin\' Season', [sauce_names.FLOSSIN_SEASON])
    stupid_rookie = ComboSauce(sauce_names.STUPID_ROOKIE, 'wet', 'new',
                               'Golden Honey BBQ with Escobar Season', [sauce_names.HONEY_BBQ, sauce_names.GOLD, sauce_names.ESCOBAR_SEASON])
    sunday_funday = ComboSauce(sauce_names.SUNDAY_FUNDAY, 'buttered', 'new',
                               'Buttered dry ranch', [sauce_names.RANCH])
    superfly_tnt = ComboSauce(sauce_names.SUPERFLY_TNT, 'wet', 'hot',
                              'Hot Jamaican Jerk and Ranch Dressing', [sauce_names.JAMACIAN_FRANK, sauce_names.RANCH])
    sweet_chin_music = ComboSauce(sauce_names.SWEET_CHIN_MUSIC, 'buttered', 'hot',
                                  'Buttered Honey with Hot Black Magic', [sauce_names.BLACK_MAGIC])
    sweet_jones = ComboSauce(sauce_names.SWEET_JONES, 'wet', 'new',
                             'Honey Escobar Seasoning', [sauce_names.ESCOBAR_SEASON])
    sweet_lou = ComboSauce(sauce_names.SWEET_LOU, 'wet', 'new',
                           'Honey Lemon Pepper', [sauce_names.LEMON_PEPPER])
    talk_of_bf = ComboSauce(sauce_names.TALK_OF_BEAVER_FALLS, 'wet', 'award',
                            'Hot and Tangy. One of Our Bestsellers', None)
    three_rivers = ComboSauce(sauce_names.THREE_RIVERS, 'wet', 'classic',
                              'Honey Mustard, BBQ, and Ranch', [sauce_names.BOBS_HONEY_MUSTARD, sauce_names.BBQ_RANCH])
    thunderlips = ComboSauce(sauce_names.THUNDERLIPS, 'wet', 'hot',
                             'Ranch dressing and BSB\'s atomic dust (That isn\'t a listed flavor so...)', [sauce_names.RANCH])
    too_easy = ComboSauce(sauce_names.TOO_EASY, 'wet', None,
                          'Salt, Pepper, and Hot Sauce', [sauce_names.FRANKS_RED_HOT])
    tommy_buns = ComboSauce(sauce_names.TOMMY_BUNS, 'buttered', 'new',
                            'Jamaican Jerk with Chili Lime', [sauce_names.JAMACIAN_JERK, sauce_names.ESCOBAR_SEASON])
    trash_talk = ComboSauce(sauce_names.TRASH_TALK, 'wet', 'new',
                            'Chains adding Black Magic', [sauce_names.CHAINS, sauce_names.BLACK_MAGIC])
    tremendous_slouch = ComboSauce(sauce_names.TREMENDOUS_SLOUCH, 'dry', 'hot',
                                   'Hot BBQ Rub', None)
    troy = ComboSauce(sauce_names.TROY, 'wet', 'new',
                      'Hot Black and Gold', [sauce_names.BLACK_AND_GOLD])
    uncle_nicks = ComboSauce(sauce_names.UNCLE_NICKS, 'wet', 'classic',
                             'Hot Spicy Garlic honey BBQ', [sauce_names.HOT_GARLIC, sauce_names.HONEY_BBQ])
    uncle_ricos = ComboSauce(sauce_names.UNCLE_RICOS, 'wet', 'sure',
                             'Sweet Spicy Garlic Honey Mustard', [sauce_names.NAPOLEON_GARLIC, sauce_names.BOBS_HONEY_MUSTARD])
    velvet_jones = ComboSauce(sauce_names.VELVET_JONES, 'buttered', 'new',
                              'Buttered Honey Escobar Season', [sauce_names.ESCOBAR_SEASON])
    walk_of_bf = ComboSauce(sauce_names.WALK_OF_BEAVER_FALLS, 'wet', 'hot',
                            'Think Talk of Beaver Falls but HOTTER', [sauce_names.TALK_OF_BEAVER_FALLS])
    walk_of_the_doggs = ComboSauce(sauce_names.WALK_OF_THE_DOGGS, 'wet', 'new',
                                   'Pookie subbing Walk of Beaver Falls', [sauce_names.POOKIE, sauce_names.PIGEON_WINGS])
    westview_connection = ComboSauce(sauce_names.WESTVIEW_CONNECTION, 'wet', 'classic',
                                     'BSB\'s Wet Cajun Garlic with a Green Jalapeno Base', [sauce_names.CAJUN_GARLIC])
    william_henry_harrison = ComboSauce(sauce_names.WILLIAM_HENRY_HARRISON, 'wet', None,
                                        'Jamaican Jerk and Parmesian Cheese', [sauce_names.JAMACIAN_JERK])
    wink_and_gun = ComboSauce(sauce_names.WINK_AND_GUN, 'wet', None,
                              'Hot, Sweet Ranch', [sauce_names.RANCH])
    zach_attack = ComboSauce(sauce_names.ZACH_ATTACK, 'wet', 'new',
                             'Buc Nasty adding Black and Gold', [sauce_names.BUC_NASTY, sauce_names.BLACK_AND_GOLD])
    ziggy_stardust = ComboSauce(sauce_names.ZIGGY_STARDUST, 'buttered', None,
                                'Buttered Dry Buffalo with Seasoned Ranch', [sauce_names.NAPOLEON, sauce_names.RANCH])

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
