import json
from pathlib import Path
import pandas as pd








if __name__ == "__main__":
    files = Path('data').glob('*.xlsx')
    data_list = []
    for file in files:
        data_list.append(pd.read_excel(file))
    final = pd.concat(data_list)
    final.to_excel('sum.xlsx')
