easter
======

Calculation of the date for the Orthodox easter

Usage
======

    python ./easter.py
    
Example of output:

    2010 - 04 Apr (04.04.2010)
    2011 - 24 Apr (24.04.2011)
    2012 - 15 Apr (15.04.2012)
    2013 - 05 May (05.05.2013)
    2014 - 20 Apr (20.04.2014)
    2015 - 12 Apr (12.04.2015)
    2016 - 01 May (01.05.2016)
    2017 - 16 Apr (16.04.2017)
    2018 - 08 Apr (08.04.2018)
    2019 - 28 Apr (28.04.2019)

Advanced Usage
======

By default, script prints the dates for the range of 2010-2019.
To see a dae for specific years, change the range on string 19:

    for y in range(2010, 2020):
    
For example:

    for y in range(2013, 2014):

Will output the date of easter only for year 2013
