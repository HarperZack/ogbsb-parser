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
    ace_boogie = ComboSauce(sauce_names.ACE_BOOGIE, 'buttered', 'award',
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
    big_fine_woman = ComboSauce(sauce_names.BIGFINEWOMAN2000, 'all', 'sure',
                                'Dark BBQ and Black Magic', [sauce_names.DARK_BBQ, sauce_names.BLACK_MAGIC])
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
    """
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
    general_tsos = ComboSauce(sauce_names.GENERAL_TSOS)
    gold_fire = ComboSauce(sauce_names.GOLD_FIRE)
    good_riddance = ComboSauce(sauce_names.GOOD_RIDDANCE)
    gung_ho = ComboSauce(sauce_names.GUNG_HO)
    harlem_heat = ComboSauce(sauce_names.HARLEM_HEAT)
    harlem_shake = ComboSauce(sauce_names.HARLEM_SHAKE)
    honey_bunny = ComboSauce(sauce_names.HONEY_BUNNY)
    jaguar_paw = ComboSauce(sauce_names.JAGUAR_PAW)
    jamacian_frank = ComboSauce(sauce_names.JAMACIAN_FRANK)
    jamacian_jerk = ComboSauce(sauce_names.JAMACIAN_JERK)
    jimmy_jump = ComboSauce(sauce_names.JIMMY_JUMP)
    jive_turkey = ComboSauce(sauce_names.JIVE_TURKEY)
    king_joffy_joe = ComboSauce(sauce_names.KING_JOFFY_JOE)
    kurupt_cajun = ComboSauce(sauce_names.KURUPT_CAJUN)
    lady_luck = ComboSauce(sauce_names.LADY_LUCK)
    lavish_habits = ComboSauce(sauce_names.LAVISH_HABITS)
    lbj2la = ComboSauce(sauce_names.LBJ2LA)
    lil_broski = ComboSauce(sauce_names.LIL_BROSKI)
    lil_dayne = ComboSauce(sauce_names.LIL_DAYNE)
    low_ball_larry = ComboSauce(sauce_names.LOW_BALL_LARRY)
    macho_man = ComboSauce(sauce_names.MACHO_MAN)
    magic_man = ComboSauce(sauce_names.MAGIC_MAN)
    mapletron = ComboSauce(sauce_names.MAPLETRON)
    mean_joe_green = ComboSauce(sauce_names.MEAN_JOE_GREEN)
    mister_cs = ComboSauce(sauce_names.MISTER_CS)
    most_interesting = ComboSauce(sauce_names.THE_MOST_INTERESTING_FLAVOR)
    mouse_trap = ComboSauce(sauce_names.MOUSE_TRAP)
    mr_dynamite = ComboSauce(sauce_names.MR_DYNAMITE)
    mr_northside = ComboSauce(sauce_names.MR_NORTHSIDE)
    mr_pipp = ComboSauce(sauce_names.MR_PIPP)
    ms_parker = ComboSauce(sauce_names.MS_PARKER)
    napoleon = ComboSauce(sauce_names.NAPOLEON)
    napoleon_cajun = ComboSauce(sauce_names.NAPOLEON_CAJUN)
    napoleon_complex = ComboSauce(sauce_names.NAPOLEON_COMPLEX)
    napoleon_dynamite = ComboSauce(sauce_names.NAPOLEON_DYNAMITE)
    napoleon_garlic = ComboSauce(sauce_names.NAPOLEON_GARLIC)
    ole_school = ComboSauce(sauce_names.OLE_SCHOOL)
    oxs = ComboSauce(sauce_names.OXS)
    pigeon_wings = ComboSauce(sauce_names.PIGEON_WINGS)
    playmaker = ComboSauce(sauce_names.PLAYMAKER)
    polish_hill_strangler = ComboSauce(sauce_names.POLISH_HILL_STRANGLER)
    pookie = ComboSauce(sauce_names.POOKIE)
    primadonna = ComboSauce(sauce_names.PRIMADONNA)
    primetime = ComboSauce(sauce_names.PRIMETIME)
    real_dill = ComboSauce(sauce_names.REAL_DILL)
    ringside_rosie = ComboSauce(sauce_names.RINGSIDE_ROSIE)
    seasoned_vet = ComboSauce(sauce_names.RINGSIDE_ROSIE)
    shaolin_strut = ComboSauce(sauce_names.SHAOLIN_STRUT)
    sheltons_shooters = ComboSauce(sauce_names.SHELTONS_SHOOTERS)
    showtime = ComboSauce(sauce_names.SHOWTIME)
    steel_city = ComboSauce(sauce_names.STEEL_CITY)
    steiner_recliner = ComboSauce(sauce_names.STEINER_RECLINER)
    stickiest = ComboSauce(sauce_names.STICKIEST_OF_THE_ICKY)
    still_flossin = ComboSauce(sauce_names.STILL_FLOSSIN)
    stupid_rookie = ComboSauce(sauce_names.STUPID_ROOKIE)
    sunday_funday = ComboSauce(sauce_names.SUNDAY_FUNDAY)
    superfly_tnt = ComboSauce(sauce_names.SUPERFLY_TNT)
    sweet_chin_music = ComboSauce(sauce_names.SWEET_CHIN_MUSIC)
    sweet_jones = ComboSauce(sauce_names.SWEET_JONES)
    sweet_lou = ComboSauce(sauce_names.SWEET_LOU)
    talk_of_bf = ComboSauce(sauce_names.TALK_OF_BEAVER_FALLS)
    three_rivers = ComboSauce(sauce_names.THREE_RIVERS)
    thunderlips = ComboSauce(sauce_names.THUNDERLIPS)
    too_easy = ComboSauce(sauce_names.TOO_EASY)
    tommy_buns = ComboSauce(sauce_names.TOMMY_BUNS)
    trash_talk = ComboSauce(sauce_names.TRASH_TALK)
    tremendous_slouch = ComboSauce(sauce_names.TREMENDOUS_SLOUCH)
    troy = ComboSauce(sauce_names.TROY)
    uncle_nicks = ComboSauce(sauce_names.UNCLE_NICKS)
    uncle_ricos = ComboSauce(sauce_names.UNCLE_RICOS)
    velvet_jones = ComboSauce(sauce_names.VELVET_JONES)
    walk_of_bf = ComboSauce(sauce_names.WALK_OF_BEAVER_FALLS)
    walk_of_the_doggs = ComboSauce(sauce_names.WALK_OF_THE_DOGGS)
    westview_connection = ComboSauce(sauce_names.WESTVIEW_CONNECTION)
    william_henry_harrison = ComboSauce(sauce_names.WILLIAM_HENRY_HARRISON)
    wink_and_gun = ComboSauce(sauce_names.WINK_AND_GUN)
    zach_attack = ComboSauce(sauce_names.ZACH_ATTACK)
    ziggy_stardust = ComboSauce(sauce_names.ZIGGY_STARDUST)
"""
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
