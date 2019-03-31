from dateutil.parser import parse

def is_valid_date(date_string):
  try:
    test_date = parse(date_string)
  except ValueError:
    return False
  else:
    return True
