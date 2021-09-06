"""
https://www.figma.com/file/GLah5wCMHIyw7hJI4Gekns/CSV-fake-data-generator?node-id=24278%3A2


"""
import random

from faker import Faker
import pandas as pd


class gen_csv:

    def __init__(self, rows_num, rows):
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
        self.rows_num = rows_num
        self.rows = rows

    def gen_res(self):
        result = {}
        for i in self.rows:
            if i['column_name'] == 'name':
                result['name'] = [self.fake.name() for _ in range(self.rows_num)]
            if i['column_name'] == 'job':
                result['job'] = [self.fake.job() for _ in range(self.rows_num)]
            if i['column_name'] == 'Email':
                result['Email'] = [self.fake.email() for _ in range(self.rows_num)]
            if i['column_name'] == 'Domain name':
                result['Domain name'] = [self.fake.domain_name() for _ in range(self.rows_num)]
            if i['column_name'] == 'Phone number':
                result['Phone number'] = [self.fake.phone_number() for _ in range(self.rows_num)]
            if i['column_name'] == 'Company name':
                result['Company name'] = [self.fake.company_name() for _ in range(self.rows_num)]
            if i['column_name'] == 'Text':
                # TODO logic of min chars
                result['Text'] = [self.fake.text(max_nb_chars=i['max_nb_chars']) for _ in range(self.rows_num)]
            if i['column_name'] == 'Integer':
                result['Integer'] = [random.randint(i['min'], i['max']) for _ in range(self.rows_num)]
            if i['column_name'] == 'Address':
                result['Address'] = [self.fake.address() for _ in range(self.rows_num)]
            if i['column_name'] == 'Date':
                result['Date'] = [self.fake.date() for _ in range(self.rows_num)]

        return result

    def to_csv(self):
        # TODO logic give a name
        return pd.DataFrame.from_dict(self.gen_res()).to_csv(f'source/name.csv')
