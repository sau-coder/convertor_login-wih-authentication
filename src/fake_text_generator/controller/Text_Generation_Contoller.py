from faker import Faker

from src.fake_text_generator.utils.Fake_Text_Generation_Types import (
    Fake_Text_Generation_Types,
)


class Text_Generation_Contoller:
    def __init__(self, conversion_type):
        self.conversion_type = conversion_type
        self.result = None
        self.fake_text_generator = Faker()

    def get_fake_address(self):
        building_number = self.fake_text_generator.building_number()
        street_name = self.fake_text_generator.street_name()
        city_suffix = self.fake_text_generator.city_suffix()
        city = self.fake_text_generator.city()
        postalcode = self.fake_text_generator.postcode()
        state = self.fake_text_generator.state()
        country = self.fake_text_generator.country()

        self.result = {
            "building_number": building_number,
            "street_name": street_name,
            "city_suffix": city_suffix,
            "city": city,
            "postalcode": postalcode,
            "state": state,
            "country": country,
        }

    def get_fake_name(self):
        self.result = {"name": self.fake_text_generator.name()}

    def get_fake_text(self):
        if Fake_Text_Generation_Types.address == self.conversion_type:
            self.get_fake_address()
        elif Fake_Text_Generation_Types.name == self.conversion_type:
            self.get_fake_name()

        return self.result
