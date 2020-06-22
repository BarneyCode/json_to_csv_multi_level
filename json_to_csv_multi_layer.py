import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
import sys
import pandas as pd
import flat_table


def convert(filename):
    df = pd.read_json(filename, lines=True)
    rati = flat_table.normalize(df)
    rati.to_csv('output.csv')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('please type the json file name or path')
        exit(0)
    else:
        convert(sys.argv[1])
