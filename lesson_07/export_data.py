import pandas as pd

from model import read_db


def export_to_csv(path='db.json', csv_file_name='csv_base.csv'):
    pd.set_option('display.max_columns', 50)
    df = pd.read_json(path)
    df.to_csv(csv_file_name)


def export_to_txt(path='db.json', txt_file_name='txt_base.txt'):
    data = read_db()
    with open(txt_file_name, 'w') as txt_file:
        for i in data:
            for k in i:
                txt_file.write(i[k])
                txt_file.write('\n')
            txt_file.write('\n')
