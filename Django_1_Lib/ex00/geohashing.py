import sys
import antigravity

def is_valid_date(date_str):
    parts = date_str.split('-')
    if len(parts) != 3:
        return False
    year, month, day = parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    year, month, day = int(year), int(month), int(day)
    if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True

def is_valid_latitude(latitude):
    return -90 <= latitude <= 90

def is_valid_longitude(longitude):
    return -180 <= longitude <= 180

def geohashing():
    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage: geohashing.py <latitude> <longitude> <date in YYYY-MM-DD format>")
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        date_str = sys.argv[3]
        if not is_valid_latitude(latitude):
            raise ValueError("Latitude must be between -90 and 90")
        
        if not is_valid_longitude(longitude):
            raise ValueError("Longitude must be between -180 and 180")
        
        if not is_valid_date(date_str):
            raise ValueError("Date must be in YYYY-MM-DD format and must be a valid date")
        antigravity.geohash(latitude, longitude, date_str.encode('utf-8'))
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    geohashing()
