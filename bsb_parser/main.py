from sauces import original_sauces, combo_sauces, base_sauce, sauce_names

if __name__ == '__main__':
    list_of_original_sauces = original_sauces.create_original_sauces_list()
    og_test_name = sauce_names.TERIYAKI

    list_of_combo_sauces = combo_sauces.create_combo_sauces_list()
    combo_test_name = sauce_names.ASHY_LARRY

    test_og = base_sauce.search_sauce_list(og_test_name, list_of_original_sauces)
    test_og.show_sauce_stats()
    test_combo = base_sauce.search_sauce_list(combo_test_name, list_of_combo_sauces)
    test_combo.show_sauce_stats()

