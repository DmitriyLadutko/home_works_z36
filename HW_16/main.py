from HW_15 import *


if __name__ == '__main__':
    person_db_name = PersonCRUD(db_name='person')
    # person_db_name.create_person(first_name="Ilia", last_name="ILin", age=24)
    # person_db_name.create_person(first_name="Ivan", last_name="Ivanov", age=21)
    # person_db_name.create_person(first_name="Petr", last_name="Petrov", age=10)
    # person_db_name.create_person(first_name="Sidor", last_name="Sidorov", age=16)
    # person_db_name.create_person(first_name="Alexandr", last_name="Alexandrov", age=28)
    # person_db_name.create_person(first_name="Dima", last_name="Ladutko", age=29)

    # person_db_name.update_person()
    # person_db_name.delete_person(person_id=1)
    # person_db_name.selected_person_name()
    person_db_name.selected_person_age()