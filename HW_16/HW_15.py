import logging
import sqlite3
logging.basicConfig(level=logging.DEBUG)


class PersonCRUD:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = self.__get_connection()
        self.cursor = self.__get_cursor()
        self.__create_table()

    def __get_connection(self):
        try:
            connection = sqlite3.connect(self.db_name)
            logging.debug(f'successful connection to {self.db_name}')
            return connection
        except sqlite3.Error as err:
            raise err

    def __get_cursor(self):
        return self.connection.cursor()

    def __create_table(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS person(
                person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR ,
                last_name VARCHAR,
                age INTEGER );'''
        self.cursor.execute(create_table_query)

    def create_person(self, first_name: str, last_name: str, age: int):
        create_person_query = 'INSERT INTO person (first_name, last_name, age) VALUES (?, ?, ?);'
        self.cursor.execute(create_person_query, (first_name, last_name, age))
        self.connection.commit()
        logging.info(f'person {first_name} {last_name} {age}successful connection')

    def update_person(self):
        update_table_query_first_name = 'UPDATE person SET first_name = "Dima" WHERE first_name = "dima";'
        self.cursor.execute(update_table_query_first_name)
        logging.info(f'person update successful')
        self.cursor.close()

    def delete_person(self, person_id):
        delete_person = 'DELETE FROM person WHERE person_id =?'
        self.cursor.execute(delete_person, (person_id,))
        self.connection.commit()
        logging.info(f'person with {person_id} successful deleted')

    def selected_person_name(self):
        selected_name = 'SELECT * FROM person WHERE first_name="Dima" OR age< 25'
        self.cursor.execute(selected_name)
        data = self.cursor.fetchall()
        for row in data:
            logging.info(row)
        self.connection.commit()
        logging.info(f'received the following data')

    def selected_person_age(self):
        selected_age = 'SELECT * FROM person WHERE age > ? AND age < ?'
        self.cursor.execute(selected_age, (15, 18))
        data = self.cursor.fetchall()
        for row in data:
            logging.info(row)
        self.connection.commit()
        logging.info(f'received the following data')


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
