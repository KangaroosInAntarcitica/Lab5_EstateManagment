def get_valid_input(input_string, valid_options):
    """
    Function responsible for getting input from user, that is limited to
    certain criteria - a list of possible options (valid options)
    """
    input_string += ' (%s)' % ', '.join(valid_options)
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)

    return response.lower()


class Property:
    """
    Class representing a real estate or immovable part of such property
    Contains information about the size of the property, number of bedrooms,
    bathrooms and possibly other characteristics if object is modified
    to have them
    """
    def __init__(self, square_feet='', beds='', baths='', *args, **kwargs):
        """ Initializes a class object """
        super().__init__(*args, **kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths

    def display(self):
        """ Shows all the default property information to user """
        print(' Property details \n ================')
        print()
        print('Bedrooms: %s \n Bathrooms: %s \n Square footage: %s' % \
              (self.beds, self.baths, self.square_feet))

    @staticmethod
    def prompt_init():
        """
        Responsible for getting valid input of the property information
        from user and returning it as a dict of arguments
        """
        return dict(square_feet = input('Enter the square feet: '),
                    beds = input('Enter the number of bedrooms: '),
                    baths = input('Enter the number of baths: '))


class Apartment(Property):
    """
    Represents an apartment property with similar characteristics to
    property object, but some additional information, like laundry and balcony
    """
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony='', laundry='', *args, **kwargs):
        """ Initialise the class object with default parameters """
        super().__init__(*args, **kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Show information about the apartment after displaying all the default
        information for any property
        """
        super().dixplay()
        print('Apartament details')
        print(' Laundry: %s \n Has balcony: %s' % (self.laundry, self.balcony))

    @staticmethod
    def prompt_init():
        """
        Responsible for getting valid input of the property information
        from user and returning it as a dict of arguments
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input('What laundry facilities does the property '
                                  'have?', Apartment.valid_laundries)
        balcony = get_valid_input('What balcony  does the property have?',
                                  Apartment.valid_balconies)
        parent_init.update({'laundry': laundry, 'balcony': balcony})

        return parent_init


class House(Property):
    """
    A class representing a property in form of some land and a house
    Contains all the default property info, together with attributes,
    representing a garage and whether the land is fenced or not
    """
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, garage='', fenced='', num_stories='', *args, **kwargs):
        """ Initialize the property as a House and Property object """
        super().__init__(*args, **kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Display the house characteristics, together with default property info
        """
        super().display()
        print('House details')
        print(' Stories: %s \n Garage: %s \n Fenced: %s' % \
              (self.num_stories, self.garage, self.fenced))

    @staticmethod
    def prompt_init():
        """
        Responsible for getting valid input of the property information
        from user and returning it as a dict of arguments
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input('Is the yard fenced? ', House.valid_fenced)
        garage = get_valid_input('Is there a garage? ', House.valid_garage)
        num_stories = input('How many stories? ')

        parent_init.update({'num_stories': num_stories,
                            'fenced': fenced, 'garage': garage})

        return parent_init


class Purchase:
    """
    A class representing a single property that is available for sale
    right now, with information about its price and estimated other
    required payments for purchase
    """
    def __init__(self, price='', taxes='', *args, **kwargs):
        """ Initialise as an object containing price information """
        super().__init__(*args, **kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """ Show information about the item for sale """
        print('Purchase details')
        print(' Selling price: %s \n Estimated taxes: %s' %
              (self.price, self.taxes))

    @staticmethod
    def prompt_init():
        """ Gets input from user, used to initialize a Purchase object"""
        return dict(
            price = input('What is the selling price? '),
            taxes = input('What are the estimated taxes? '))


class Rental:
    """
    Class used to show that something is available for rental and representing
    the price and possible taxes and other expences of this operation
    """
    def __init__(self, furnished='', utilities='', rent='', *args, **kwargs):
        """ Initialize the object """
        super().__init__(*args, **kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """ Show rental details to user """
        print('Rental details')
        print(' Rent: %s \n Estimated utilities: %s \n Furnished: %s' %
              (self.rent, self.utilities, self.furnished))

    @staticmethod
    def prompt_init():
        """ Get input from user, used to initialize a Purchase object"""
        return dict(
            rent = input('What is the monthly rent? '),
            utilities = input('What are the estimated utilities? '),
            furnished = get_valid_input('Is the property furnished? ',
                                        ['yes', 'no'])
        )


# It is possible to replace the connections in the following 4 classes from
# inheritance to composition, if each class had an __init__ function,
# where it created a separeate Property and Purchase or Rental objects.
# Then if one needed to get information about house they would write:
# hose_rental_object.house.square_feet , for example.
# This however makes code less readable, larger and complicates stuff in the
# Agent object

# So all this was found not appropriate for this exact case, although could
# have been possibly implemented

class HouseRental(Rental, House):
    """
    A class representing a house that is put for rental, having the details
    of both House and transaction to be made to rent the house
    """
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init


class HousePurchase(Purchase, House):
    """
    A class representin a house that is put for sale, having the details
    of both House and transaction to be made to purchase the house and the
    piece of land, that goes with the specified house
    """
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class ApartmentRental(Rental, Apartment):
    """
    A class representin an appartment that is put for rental, having the
    details of both flat and transaction to be made to rent it
    """
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentPurchase(Purchase, Apartment):
    """
    A class representin an appartment and everything you need to buy it
    """
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class Agent:
    """
    A class, used for creating information about a single real estate agent,
    containing details on all the available property that they are
    responsible for selling or renting and having the ability to perform
    the purchase or rental of the property with an agreement
    """
    type_map = {
        ('house', 'rental'): HouseRental,
        ('house', 'purchase'): HousePurchase,
        ('apartment', 'rental'): ApartmentRental,
        ('apartment', 'purchase'): ApartmentPurchase
    }

    def __init__(self):
        """ Initialize the agent """
        self.property_list = []

    def display_properties(self):
        """ Displays all properties, that agent can sell or rent """
        for property in self.property_list:
            property.display()

    def create_property(self):
        """
        Creates an object representing a  property that can be used in
        other methods for different actions with it
        """
        property_type = get_valid_input(
            'What type of property? ', ('house', 'apartment'))
        payment_type = get_valid_input(
            'What payment type? ', ('purchase', 'rental'))

        # find out what kind of property object we need
        PropertyClass = self.type_map[(property_type, payment_type)]
        # initialize the object
        return PropertyClass(**PropertyClass.prompt_init())

    def add_property(self):
        """
        Adds a property to the list of all properties as desired by user
        """
        self.property_list.append(self.create_property())

    def remove_property(self):
        """
        Removes a property which has the same attributes as specified by user
        """
        desired_property, count = self.create_property(), 0

        for item in self.property_list:
            if item.__dict__ == desired_property.__dict__:
                count += 1
                self.property_list.remove(item)

        print('After search %d items were removed from list.' % count)

    def buy_property(self):
        """
        Represents the action of buying a property
        """
        desired_property, found_property = self.create_property(), None

        # find the property
        for item in self.property_list:
            if item.__dict__ == desired_property.__dict__:
                found_property = item

        # return it to user
        print('Property was %sfound', '' if found_property else 'not ')
        return found_property
