#Finding Dates in Text
#a) Regex for:
#YYYY-MM-DD
#b) Implement:
#def find_dates(text: str) -> list[str]
#c) Tests:
#Multiple valid dates
#Ignore invalid (2026-13-40)
#d) Extend:
#Handle errors using pytest.raises
#e) Modify regex for:
#DD/MM/YYYY format
import re
from datetime import datetime

class InvalidDateFormat(Exception):
    pass

def find_dates(text: str) -> list:
    if not isinstance(text, str):
        raise InvalidDateFormat("Input must be a string")

    date_patt = r"(\d{4}-\d{2}-\d{2})|(\d{2}/\d{2}/\d{4})"
    matches = re.findall(date_patt, text)
    
    valid_dates = []
    for m in matches:
        date_str = m[0] if m[0] else m[1]
        date = "%Y-%m-%d" if m[0] else "%d/%m/%Y"
        
        try:
            d = datetime.strptime(date_str, date).date()
            valid_dates.append(d)
        except ValueError:
            pass
            
    return valid_dates
