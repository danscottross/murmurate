import gspread

gc = gspread.service_account(filename='murmurate-email-34f60d2ba6cd.json')

wks = gc.open_by_key('1uBARUdToGUDsreuGWSO5s7Nq528Szo3o1ET589wS_Sg')
sheet = wks.get_worksheet(0)

output = sheet.cell(2,2).value

print(output)