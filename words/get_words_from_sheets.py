import gspread
import pandas as pd
import datetime as dt
import random
import datetime as dt

import sys
sys.path.append('/Users/danross/GitHub/murmurate')

def retrieve(number):
    gc = gspread.service_account(filename='murmurate-email-34f60d2ba6cd.json')
    words_key = '1uBARUdToGUDsreuGWSO5s7Nq528Szo3o1ET589wS_Sg'
    sh = gc.open_by_key(words_key)
    wks = sh.get_worksheet(0)

    df = pd.DataFrame(wks.get_all_records())

    df.sort_values('Last Used', ascending=True, inplace=True)

    top_20_percent = int(len(wks.col_values(1)) * 0.1)
    df_new = df.iloc[:top_20_percent]

    indexes = random.sample(range(0, top_20_percent), 3)
    target_words = df_new.iloc[indexes,0].tolist()

    date = dt.datetime.today().strftime('%Y-%m-%d')

    for target_word in target_words:
        cell = wks.find(target_word)
        wks.update_cell(cell.row, 3, date)

    return df_new.iloc[indexes,:]
