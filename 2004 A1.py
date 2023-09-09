def restaurantFinder(d, site_list): #[50*, 10, 12, 65*, 40, 95*, 100, 12*, 20] + [30*] [1,4,6,8,10]
    chosen_sites = []
    total_earnings = 0
    restaurantFinder_aux(d, site_list, chosen_sites, total_earnings)
    return chosen_sites

def restaurantFinder_aux(d, site_list, chosen_sites, total_earnings):
    if site_list[-1] > site_list[-2]:
        if
    if site_list == []:
        return  0
    else:
        return restaurantFinder_aux(d, site_list.pop(), chosen_sites)

        #new add