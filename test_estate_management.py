import unittest
import unittest.mock
import io
from estate_management import *

class Test(unittest.TestCase):
    def test_house(self):
        house = House('attached', 'yes', '2', '122', '1', '1')
        self.assertEqual(house.beds, '1')
        self.assertEqual(house.garage, 'attached')
        self.assertTrue(isinstance(house, House))
        self.assertTrue(isinstance(house, Property))
        self.assertFalse(isinstance(house, Apartment))

    def test_purchase(self):
        purchase = Purchase('122', '1222')
        self.assertEqual(purchase.taxes, '1222')
        self.assertEqual(purchase.price, '122')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_purchase_display(self, stdout):
        purchase = Purchase('122', '1222')
        purchase.display()
        req = 'Purchase details\n Selling price: 122 \n Estimated taxes: 1222\n'
        self.assertEqual(stdout.getvalue(), req)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_house_display(self, stdout):
        house = House('attached', 'yes', '2', '122', '1', '1')
        house.display()
        req = ' Property details \n ================\n\nBedrooms: 1 \n Bathr' \
              'ooms: 1 \n Square footage: 122\nHouse details\n Stories: 2 \n' \
              ' Garage: attached \n Fenced: yes\n'
        self.assertEqual(stdout.getvalue(), req)

    def test_combined(self):
        args1, args2 = ('attached', 'yes', '2', '122', '1', '1'), ('2', '12')
        house, purchase = House(*args1), Purchase(*args2)
        house_purchase = HousePurchase(*args2, *args1)

        self.assertEqual(house_purchase.garage, 'attached')
        self.assertEqual(house_purchase.price, '2')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_agent(self, stdout):
        args1, args2 = ('attached', 'yes', '2', '122', '1', '1'), ('2', '12')

        agent = Agent()
        self.assertEqual(len(agent.property_list), 0)
        agent.property_list.append(HousePurchase(*args2, *args1))
        self.assertEqual(len(agent.property_list), 1)



if __name__ == '__main__':
    unittest.main()
