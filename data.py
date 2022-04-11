import gspread

gs = gspread.service_account(filename='credentials.json')

sh = gs.open_by_key('1O6AviSLAZx7KHmQ922DB-eUEZF-JlfwpLa5m9x3GLyE')

worksheet = sh.sheet1

res = worksheet.get_all_records()
print(res[0]['CRIM'])