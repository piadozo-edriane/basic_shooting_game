from python_calendar import Calendar
from dateutil.parser import parse

def calendar():
    date_from = parse('2023-08-23')
    date_to = parse('2024-08-23')
    calendar = Calendar.get(date_from, date_to)

    print('Nb days : %s' % len(calendar.days))  # Total days
    print('Nb weeks : %s' % len(calendar.weeks))  # Total weeks
    print('Nb months : %s' % len(calendar.months))  # Total months
    print('Nb years : %s' % len(calendar.years))  # Total years

    print('Nb days for Feb 2024 : %s' % len(calendar.nodes['2024-02'].days))  # Days in Feb 2024
    print('Nb days for the 18th week in 2024 : %s' % len(calendar.nodes['2024-W18'].days))  # Days in week 18
    print('Nb days in 2024 : %s' % len(calendar.nodes['2024'].days))  # Total days in 2024

    print('First day in range: %s' % calendar.days[0])
    print('Last day in range: %s' % calendar.days[-1])


calendar()
