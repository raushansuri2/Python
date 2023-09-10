from datetime import date

def get_age(year_of_birth, current_year):
    return (int(current_year) - int(year_of_birth))

print(get_age('2018',date.today().year))