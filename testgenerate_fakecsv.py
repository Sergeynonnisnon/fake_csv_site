from generate_fakecsv import *
a = gen_csv(5, [{'column_name': 'Date'},
                {'column_name': 'Address'},
                {'column_name': 'name'},
                {'column_name': 'Text',
                 'max_nb_chars': 20}]).to_csv()
print(a)