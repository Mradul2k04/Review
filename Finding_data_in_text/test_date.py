import pytest
from datetime import datetime
from date import find_dates, InvalidDateFormat

def check_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise InvalidDateFormat(f"Invalid date: {dategit_str}")

def test_multiple_dates():
    text = "Valid: 2024-05-20, 15/08/2023. Ignore: 2026-13-40."
    results = find_dates(text)
    assert len(results) == 2

def test_invalid_date_exception():
    with pytest.raises(InvalidDateFormat):
        check_date("2026-13-40")
