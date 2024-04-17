import gspread
import pandas as pd

gc = gspread.service_account(filename='murmurate/murmurate-email-34f60d2ba6cd.json')

wks = gc.open_by_key('1uBARUdToGUDsreuGWSO5s7Nq528Szo3o1ET589wS_Sg')
sheet = wks.get_worksheet(0)

word_dict = {}

for col in range(1, len(sheet.row_values(1)) + 1):
    word_dict[sheet.col_values(col)[0]] = sheet.col_values(col)[1:]

df = pd.DataFrame(word_dict)

# df.sort_values('Last User', ascending=False, inplace = True)

print(df)