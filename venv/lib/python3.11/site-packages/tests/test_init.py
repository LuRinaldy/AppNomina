import unittest
from datetime import datetime

from dateutil.parser import parse
from python_calendar import Calendar


class TestCalendar(unittest.TestCase):
    def test_get_calendar_until(self):
        date_from = parse('2023-08-23')
        date_to = parse('2024-08-23')
        calendar = Calendar.get(date_from, date_to, incl_last_day=False)

        self.assertEqual(calendar.first_day, '2023-08-23')
        self.assertEqual(calendar.last_day, '2024-08-22')

        self.assertEqual(len(calendar.days), 366)
        self.assertEqual(len(calendar.weeks), 53)
        self.assertEqual(len(calendar.nodes['2024-W18'].days), 7)
        self.assertEqual(len(calendar.months), 13)
        self.assertEqual(len(calendar.nodes['2024-02'].days), 29)
        self.assertEqual(len(calendar.years), 2)
        self.assertEqual(len(calendar.nodes['2024'].days), 235)

        date_from = parse('2023-12-23')
        date_to = parse('2024-02-19')
        calendar = Calendar.get(date_from, date_to, incl_last_day=False)

        self.assertEqual(calendar.first_day, '2023-12-23')
        self.assertEqual(calendar.last_day, '2024-02-18')

        self.assertEqual(len(calendar.days), 58)
        self.assertEqual(len(calendar.weeks), 9)
        self.assertEqual(len(calendar.months), 3)
        self.assertEqual(len(calendar.years), 2)

        date_from = parse('2023-01-02')
        date_to = parse('2023-01-09')
        calendar = Calendar.get(date_from, date_to, incl_last_day=False)

        self.assertEqual(calendar.first_day, '2023-01-02')
        self.assertEqual(calendar.last_day, '2023-01-08')

        self.assertEqual(len(calendar.days), 7)
        self.assertEqual(len(calendar.weeks), 1)
        self.assertEqual(len(calendar.months), 1)
        self.assertEqual(len(calendar.years), 1)

        date_from = parse('2023-08-22')
        date_to = parse('2023-08-29')
        calendar = Calendar.get(date_from, date_to, incl_last_day=False)

        self.assertEqual(calendar.first_day, '2023-08-22')
        self.assertEqual(calendar.last_day, '2023-08-28')

        self.assertEqual(len(calendar.days), 7)
        self.assertEqual(len(calendar.weeks), 2)
        self.assertEqual(len(calendar.months), 1)
        self.assertEqual(len(calendar.years), 1)

        date_from = parse('2023-08-21')
        date_to = parse('2023-08-28')
        calendar = Calendar.get(date_from, date_to, incl_last_day=False)

        self.assertEqual(calendar.first_day, '2023-08-21')
        self.assertEqual(calendar.last_day, '2023-08-27')

        self.assertEqual(len(calendar.days), 7)
        self.assertEqual(len(calendar.weeks), 1)
        self.assertEqual(len(calendar.months), 1)
        self.assertEqual(len(calendar.years), 1)

        date_from = parse('2023-08-22')
        date_to = parse('2024-08-29')
        calendar = Calendar.get(date_from, date_to, incl_last_day=False)

        self.assertEqual(calendar.first_day, '2023-08-22')
        self.assertEqual(calendar.last_day, '2024-08-28')

        self.assertEqual(len(calendar.days), 373)
        self.assertEqual(len(calendar.weeks), 54)
        self.assertEqual(len(calendar.months), 13)
        self.assertEqual(len(calendar.years), 2)

    def test_get_calendar_until_values(self):
        date_from = parse('2023-08-23')
        date_to = parse('2024-08-23')
        calendar = Calendar.get(date_from, date_to, incl_last_day=False)

        self.assertEqual(calendar.first_day, '2023-08-23')
        self.assertEqual(calendar.last_day, '2024-08-22')

        self.assertEqual(list(calendar.years), ['2023', '2024'])
        self.assertEqual(list(calendar.months), [
            '2023-08',
            '2023-09',
            '2023-10',
            '2023-11',
            '2023-12',
            '2024-01',
            '2024-02',
            '2024-03',
            '2024-04',
            '2024-05',
            '2024-06',
            '2024-07',
            '2024-08'
        ])

        date_from = parse('2023-12-23')
        date_to = parse('2024-01-03')
        calendar = Calendar.get(date_from, date_to)

        self.assertEqual(calendar.first_day, '2023-12-23')
        self.assertEqual(calendar.last_day, '2024-01-03')

        self.assertEqual(list(calendar.years), ['2023', '2024'])
        self.assertEqual(list(calendar.months), [
            '2023-12',
            '2024-01',
        ])
        self.assertEqual(calendar.nodes['2023-12'].number, 12)
        self.assertEqual(calendar.nodes['2023-12'].year, 2023)
        self.assertEqual(len(calendar.nodes['2023-12'].days), 9)

        self.assertEqual(list(calendar.weeks), [
            '2023-W51',
            '2023-W52',
            '2024-W01'
        ])
        self.assertEqual(calendar.nodes['2023-W51'].number, 51)
        self.assertEqual(calendar.nodes['2023-W51'].year, 2023)
        self.assertEqual(len(calendar.nodes['2023-W51'].days), 2)

        self.assertEqual(list(calendar.days), [
            '2023-12-23',
            '2023-12-24',
            '2023-12-25',
            '2023-12-26',
            '2023-12-27',
            '2023-12-28',
            '2023-12-29',
            '2023-12-30',
            '2023-12-31',
            '2024-01-01',
            '2024-01-02',
            '2024-01-03'
        ])
        self.assertEqual(calendar.nodes['2023-12-23'].date, datetime(2023, 12, 23, 0, 0))

    def test_get_calendar_with_time(self):
        date_from = parse('2023-08-23')
        date_to = parse('2024-08-23T00:00:01')
        calendar = Calendar.get(date_from, date_to)
        self.assertEqual(len(calendar.days), 367)
        self.assertEqual(calendar.first_day, '2023-08-23')
        self.assertEqual(calendar.last_day, '2024-08-23')

        date_from = parse('2023-08-23T06:24:02')
        date_to = parse('2024-08-23T06:24:02')
        calendar = Calendar.get(date_from, date_to)
        self.assertEqual(len(calendar.days), 367)
        self.assertEqual(calendar.first_day, '2023-08-23')
        self.assertEqual(calendar.last_day, '2024-08-23')

        calendar = Calendar.get(date_from, date_to)
        self.assertEqual(len(calendar.days), 367)
        self.assertEqual(calendar.first_day, '2023-08-23')
        self.assertEqual(calendar.last_day, '2024-08-23')

        date_from = parse('2023-08-23')
        date_to = parse('2024-08-23T00:00:01')
        calendar = Calendar.get(date_from, date_to)
        self.assertEqual(len(calendar.days), 367)
        self.assertEqual(calendar.first_day, '2023-08-23')
        self.assertEqual(calendar.last_day, '2024-08-23')

    def test_get_calendar_weird(self):
        date_from = parse('2023-08-23')
        date_to = parse('2023-08-23')
        calendar = Calendar.get(date_from, date_to)

        self.assertEqual(calendar.first_day, '2023-08-23')
        self.assertEqual(calendar.last_day, '2023-08-23')

        date_from = parse('2023-08-23')
        date_to = parse('2023-08-23')
        calendar = Calendar.get(date_from, date_to, incl_last_day=False)

        self.assertEqual(calendar.first_day, None)
        self.assertEqual(calendar.last_day, None)
