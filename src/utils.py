from datetime import datetime

def parse_dict_to_number(result: dict) -> int:
    return int(result["$numberInt"])

def parse_dict_to_date(result: dict) -> datetime:
    return datetime.fromtimestamp(int(result["$date"]["$numberLong"]) / 1000)
