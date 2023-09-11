import unittest

from FIT2004A1 import restaurantFinder

class TestRestaurantFinder(unittest.TestCase):

    def test_3(self):

        d = 0

        site_list = [50, 10, 12, 65, 40, 95, 100, 12, 20, 30]

        total_revenue, selected_sites = restaurantFinder(d, site_list)

        self.assertEqual(total_revenue, 434) # Expected total annual revenue

        self.assertEqual(selected_sites, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Expected selected site numbers

    def test_1(self):

        d = 1

        site_list = [50, 10, 12, 65, 40, 95, 100, 12, 20, 30]

        total_revenue, selected_sites = restaurantFinder(d, site_list)

        self.assertEqual(total_revenue, 252) # Expected total annual revenue

        self.assertEqual(selected_sites, [1,4,6,8,10]) # Expected selected site numbers

    def test_2(self):

        d = 2

        site_list = [50, 10, 12, 65, 40, 95, 100, 12, 20, 30]

        total_revenue, selected_sites = restaurantFinder(d, site_list)

        self.assertEqual(total_revenue, 245) # Expected total annual revenue

        self.assertEqual(selected_sites, [1,4,7,10]) # Expected selected site numbers

    def test_3(self):

        d = 3

        site_list = [50, 10, 12, 65, 40, 95, 100, 12, 20, 30]

        total_revenue, selected_sites = restaurantFinder(d, site_list)

        self.assertEqual(total_revenue, 175) # Expected total annual revenue

        self.assertEqual(selected_sites, [1,6,10]) # Expected selected site number:

    def test_7(self):

        d = 7

        site_list = [50, 10, 12, 65, 40, 95, 100, 12, 20, 30]

        total_revenue, selected_sites = restaurantFinder(d, site_list)

        self.assertEqual(total_revenue, 100) # Expected total annual revenue

        self.assertEqual(selected_sites, [7]) # Expected selected site numbersdef test_single_site(self):

    def test_all_negative(self):

        d = 2

        site_list = [-50, -10, -12, -65, -40, -95, -100, -12, -20, -30]

        total_revenue, selected_sites = restaurantFinder(d, site_list)

        self.assertEqual(total_revenue, 0) # Expected total annual revenue

        self.assertEqual(selected_sites, []) # Expected selected site numbers

    def test_some_negative(self):

        d = 1

        site_list = [50, -10, 12, -65, -40, 95, -100, 12, -20, -30]

        total_revenue, selected_sites = restaurantFinder(d, site_list)

        self.assertEqual(total_revenue, 169) # Expected total annual revenue

        self.assertEqual(selected_sites, [1,3,6,8]) # Expected selected site numbers 



    def test_single(self): 

        d = 2

        site_list = [5]

        total_revenue, selected_sites = restaurantFinder(d, site_list)

        self.assertEqual(total_revenue, 5) # Expected total annual revenue

        self.assertEqual(selected_sites, [1]) # Expected selected site numbers

if __name__ == '__main__':
    unittest.main()