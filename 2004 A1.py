def restaurantFinder(d, site_list): #[50, 10, 12, 65, 40, 95, 100, 12, 20, 30]
    chosen_sites = []
    return restaurantFinder_aux(d, site_list, chosen_sites)

def restaurantFinder_aux(d, site_list, chosen_sites):
    if site_list == []:
        return  0
    else:
        return restaurantFinder_aux(d, site_list, chosen_sites)