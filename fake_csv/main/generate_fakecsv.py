"""
https://www.figma.com/file/GLah5wCMHIyw7hJI4Gekns/CSV-fake-data-generator?node-id=24278%3A2


"""

import random

from faker import Faker
import pandas as pd


class gen_csv:

    def __init__(self, rows_num, rows,column_sep,string_character,name ):
        """
        this class creates fake data and puts it in a file
        Full name (a combination of first name and last name)
        Job
        Email
        Domain name
        Phone number
        Company name
        Text (with specified range for a number of sentences)
        Integer (with specified range)
        Address
        Date
        :param rows_num: Integer
        :param rows: list of dict
        """
        self.fake = Faker()
        self.rows_num = int(rows_num)
        self.rows = rows
        self.column_sep = column_sep
        self.string_character = string_character
        self.name = name


    def gen_res(self):
        result = {}
        for i in self.rows:
            print(i)
            if i['type_column'] == 'Full name':
                result[i['name_column']] = [self.fake.name() for _ in range(self.rows_num)]
            if i['type_column'] == 'Job':
                result['job'] = [self.fake.job() for _ in range(self.rows_num)]
            if i['type_column'] == 'Email':
                result[i['name_column']] = [self.fake.email() for _ in range(self.rows_num)]
            if i['type_column'] == 'Domain name':
                result[i['name_column']] = [self.fake.domain_name() for _ in range(self.rows_num)]
            if i['type_column'] == 'Phone number':
                result[i['name_column']] = [self.fake.phone_number() for _ in range(self.rows_num)]
            if i['type_column'] == 'Company name':
                result[i['name_column']] = [self.fake.company() for _ in range(self.rows_num)]
            if i['type_column'] == 'Text':
                # TODO logic of min chars
                result[i['name_column']] = [self.fake.text(max_nb_chars=i['max_choise']) for _ in range(self.rows_num)]
            if i['type_column'] == 'Integer':
                result[i['name_column']] = [random.randint(i['min_choise'], i['max_choise']) for _ in range(self.rows_num)]
            if i['type_column'] == 'Address':
                result['Address'] = [self.fake.address() for _ in range(self.rows_num)]
            if i['type_column'] == 'Date':
                result[i['name_column']] = [self.fake.date() for _ in range(self.rows_num)]

        return result

    def to_csv(self):
        pd.DataFrame.from_dict(self.gen_res()).to_csv(f'main/source/{self.name}.csv',
                                                      sep=self.column_sep,
                                                      quotechar=self.string_character,
                                                      index=False,
                                                      )
        return f'main/source/{self.name}.csv'
