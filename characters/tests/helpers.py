from faker.providers import BaseProvider


# Custom provider for Futurama characters
class FuturamaProvider(BaseProvider):
    def full_name(self):
        return self.random_element([
            "Philip Jay Fry", "Turanga Leela", "Bender Bending Rodríguez",
            "Amy Wong"
        ])

    def gender(self):
        return self.random_element([
            "Male", "Female",
        ])

    def species(self):
        return self.random_element(["Human", "Mutant", "Robot", "Martian"])

    def occupation(self):
        return self.random_element([
            "Intergalactic Delivery Boy", "Captain and Pilot", "Planet Express Worker", "Intern"])

    def sayings(self):
        return self.random_element([
            "Shut up and take my money!", "With my Oxo Goodgrips cheese knife, I stab at thee!",
            "I'm a fraud. A poor, lazy, sexy fraud.", "Ew, pukeatronic!",
        ])
