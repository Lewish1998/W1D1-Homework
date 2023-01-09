name, building_name = 'lewis', 'clockwise'
week_num = 1
day_num = 1
hours_sitting = 6

string_length = len(building_name)
where_am_i = f"{name} is at {building_name}"
total_hours_sitting = day_num * hours_sitting

if week_num < 16:
    print('Course not completed')
else:
    print('Course (hopefully) completed')

name, building_name = name.title(), building_name.title()