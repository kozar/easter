import datetime

def get_easter_for_year(year):

    a = (19*(year%19) + 15)%30;
    b = (2*(year%4) + 4*(year%7) + 6*a + 6) % 7;

    if (a + b) > 9:
        day = a + b - 9;
        month = 4;
    else:
        day = 22 + a + b;
        month = 3;

    e = datetime.date(year, month, day) + datetime.timedelta(days=13);

    return e.strftime('%Y - %d %b (%d.%m.%Y)');

for y in range(2010, 2020):
    print(get_easter_for_year(y));
