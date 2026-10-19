import math

def clean_sensor_readings(values):
    """Clean a list of mixed sensor values and return a list of floats."""
    cleaned = []
    if values is None:
         return cleaned

    for item in values:
        try:
            number = float(item)

        except (TypeError,ValueError):
            continue

        if math.isnan(number) or number < 0:
            continue
        if number > 500.0:
            number = 500.0
        cleaned.append(number)    
    return cleaned


assert clean_sensor_readings([1,'2.5',None, -3,'abc',600,])== [1.0, 2.5, 500.0]  
assert clean_sensor_readings([]) ==  []
assert clean_sensor_readings([None, 'X' , -1]) == []
print("All test passed")