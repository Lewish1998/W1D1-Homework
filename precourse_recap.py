name, building = 'lewis', 'clockwise'
week_num = 1
day_num = 1
hours_sitting = 6

string_length = len(building)
current_location = f"{name} is at {building}"
total_hours_sitting = day_num * hours_sitting

if week_num < 16:
    print('Course not completed')
else:
    print('Course (hopefully) completed')

name, building = name.title(), building.title()
