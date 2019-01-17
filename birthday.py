birthday = "1-May-12"

from datetime import datetime

raw_date = "1-May-12"
date_format = "%d-%b-%y"

parsed_date = datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%m/%d/%Y") # 01/11/17
print(date_str)