class Snow:
    def __init__(self, name, composition, description, kinds, state_of_aggregation, uniqueness_elements):
        self.name = name
        self.composition = composition
        self.description = description
        self.__kinds = kinds
        self.__state_of_aggregation = state_of_aggregation
        self.__uniqueness_elements = uniqueness_elements

    def name_description(self):
        print(f'Наименование описываемого объекта {self.name}\n')

    def composition_description(self):
        self.composition = 'show.txt'
        file_name_opened = open(self.composition, 'r')
        lines = file_name_opened.readlines()
        print(f'{lines[0:3]} \n')
        file_name_opened.close()

    def descriptive_part(self):
        self.description = 'show.txt'
        file_name_opened = open(self.description, 'r')
        lines = file_name_opened.readlines()[3:]
        print(lines)

# --------------------------------------getter and setter for arguments--------------------------------------------

    def get_kinds(self):
        return self.__kinds

    def get_state_of_aggregation(self):
        return self.__state_of_aggregation

    def get_uniqueness_elements(self):
        return self.__uniqueness_elements

    def set_name(self, name):
        self.name = name

    def set_composition(self, composition):
        self.composition = composition

    def set_description(self, description):
        self.description = description

    def set_kinds(self, kinds):
        self.__kinds = kinds

    def set_state_of_aggregation(self, state_of_aggregation):
        self.__state_of_aggregation = state_of_aggregation

    def set_uniqueness_elements(self, uniqueness_elements):
        self.__uniqueness_elements = uniqueness_elements


snow = Snow(name='Snow', composition='show.txt', description='show.txt', kinds=None, state_of_aggregation=None,
            uniqueness_elements=None)

snow.name_description()
snow.composition_description()
snow.descriptive_part()


class Rain:

    def __init__(self, name, composition, description, kinds, state_of_aggregation):
        self.name = name
        self.composition = composition
        self.__description = description
        self.__kinds = kinds
        self.__state_of_aggregation = state_of_aggregation

    def name_description(self):
        print(f'Наименование описываемого объекта {self.name}\n')

    def composition_description(self):
        file_name_opened = open(self.composition, 'r')
        lines = file_name_opened.read()
        print(lines)
        file_name_opened.close()

# --------------------------------------getter and setter for arguments--------------------------------------------

    def get_kinds(self):
        return self.__kinds

    def get_state_of_aggregation(self):
        return self.__state_of_aggregation

    def get_description(self):
        return self.__description

    def set_name(self, name):
        self.name = name

    def set_composition(self, composition):
        self.composition = composition

    def set_description(self, description):
        self.__description = description

    def set_kinds(self, kinds):
        self.__kinds = kinds

    def set_state_of_aggregation(self, state_of_aggregation):
        self.__state_of_aggregation = state_of_aggregation


rain = Rain(name='Rain', composition='Rain.txt', description=None, kinds=None, state_of_aggregation=None)

rain.name_description()
rain.composition_description()


class Large_Hadron_Collider:

    def __init__(self, name, composition, description, kinds, state_of_aggregation):
        self.name = name
        self.composition = composition
        self.__description = description
        self.__kinds = kinds
        self.__state_of_aggregation = state_of_aggregation

    def name_description(self):
        print(f'Наименование описываемого объекта {self.name}\n')

    def composition_description(self):
        file_name_opened = open(self.composition, 'r')
        lines = file_name_opened.read()
        print(lines)
        file_name_opened.close()

# --------------------------------------getter and setter for arguments--------------------------------------------

    def get_kinds(self):
        return self.__kinds

    def get_state_of_aggregation(self):
        return self.__state_of_aggregation

    def get_description(self):
        return self.__description

    def set_name(self, name):
        self.name = name

    def set_composition(self, composition):
        self.composition = composition

    def set_description(self, description):
        self.__description = description

    def set_kinds(self, kinds):
        self.__kinds = kinds

    def set_state_of_aggregation(self, state_of_aggregation):
        self.__state_of_aggregation = state_of_aggregation


rain = Rain(name='Large Hadron Collider', composition='Large Hadron Collider.txt', description=None, kinds=None,
            state_of_aggregation=None)

rain.name_description()
rain.composition_description()


class Void:

    def __init__(self, name, composition, description, kinds, state_of_aggregation):
        self.name = name
        self.composition = composition
        self.__description = description
        self.__kinds = kinds
        self.__state_of_aggregation = state_of_aggregation

    def name_description(self):
        print(f'Наименование описываемого объекта {self.name}\n')

    def composition_description(self):
        file_name_opened = open(self.composition, 'r')
        lines = file_name_opened.read()
        print(lines)
        file_name_opened.close()

# --------------------------------------getter and setter for arguments--------------------------------------------

    def get_kinds(self):
        return self.__kinds

    def get_state_of_aggregation(self):
        return self.__state_of_aggregation

    def get_description(self):
        return self.__description

    def set_name(self, name):
        self.name = name

    def set_composition(self, composition):
        self.composition = composition

    def set_description(self, description):
        self.__description = description

    def set_kinds(self, kinds):
        self.__kinds = kinds

    def set_state_of_aggregation(self, state_of_aggregation):
        self.__state_of_aggregation = state_of_aggregation


rain = Rain(name='Void', composition='Void.txt', description=None, kinds=None,
            state_of_aggregation=None)

rain.name_description()
rain.composition_description()


class Black_hole:

    def __init__(self, name, composition, description, kinds, state_of_aggregation):
        self.name = name
        self.composition = composition
        self.__description = description
        self.__kinds = kinds
        self.__state_of_aggregation = state_of_aggregation

    def name_description(self):
        print(f'Наименование описываемого объекта {self.name}\n')

    def composition_description(self):
        file_name_opened = open(self.composition, 'r')
        lines = file_name_opened.read()
        print(lines)
        file_name_opened.close()

    # --------------------------------------getter and setter for arguments--------------------------------------------

    def get_kinds(self):
        return self.__kinds

    def get_state_of_aggregation(self):
        return self.__state_of_aggregation

    def get_description(self):
        return self.__description

    def set_name(self, name):
        self.name = name

    def set_composition(self, composition):
        self.composition = composition

    def set_description(self, description):
        self.__description = description

    def set_kinds(self, kinds):
        self.__kinds = kinds

    def set_state_of_aggregation(self, state_of_aggregation):
        self.__state_of_aggregation = state_of_aggregation


rain = Rain(name='Black hole', composition='Black Hole.txt', description=None, kinds=None,
            state_of_aggregation=None)

rain.name_description()
rain.composition_description()
