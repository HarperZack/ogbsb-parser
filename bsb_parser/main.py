from sauces import original_sauces, combo_sauces, base_sauce, sauce_names

if __name__ == '__main__':
    # og_test_name = sauce_names.TERIYAKI
    combo_test_name = sauce_names.POOKIE

    # test_og = base_sauce.search_sauce_list(og_test_name, original_sauces.ORIGINAL_SAUCE_LIST)
    # test_og.show_sauce_stats()

    test_combo = base_sauce.search_sauce_list(combo_test_name, combo_sauces.COMBO_SAUCE_LIST)
    # test_combo.show_sauce_stats()

    combo_sauces.gather_riffed_sauces(test_combo)

