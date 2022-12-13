import json, csv
import pandas as pd


def export_to_csv(path='db.json', csv_file_name='csv_base.csv'):
    pd.set_option('display.max_columns', 50)
    df = pd.read_json(path)
    df.to_csv(csv_file_name)

#     with open(path, encoding='utf-8') as json_file:
#         data = json.load(json_file)
#
#     with open(csv_file_name, 'w') as csv_file:
#         csv.writer(csv_file)
