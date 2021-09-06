from celery import shared_task
from .models import Schema, Column, Sets
from .generate_fakecsv import gen_csv


@shared_task
def create_csv(id_set):
    set = Sets.objects.get(id=id_set)

    rows_num = set.rows
    schema = Schema.objects.get(name_schema=set.name_schema)
    column_sep = schema.column_cep
    string_character = schema.string_character

    colums = Column.objects.filter(name_schema=set.name_schema)

    rows = []
    col = {}
    for column in colums:
        col['name_column'] = column.name_column
        col['type_column'] = column.type_column
        col['min_choise'] = column.min_choise
        col['max_choise'] = column.max_choise
        rows.append(col)
        col = {}

    print(rows_num, rows, column_sep, string_character, id_set)
    path_csv = gen_csv(rows_num, rows, column_sep, string_character, id_set).to_csv()
    set.download_link = path_csv
    set.status = 'Ready'
    set.save()

    return 'all good'
