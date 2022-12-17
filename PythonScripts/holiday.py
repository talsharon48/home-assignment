import requests
import datetime
from consts import EventsConsts, GenericConsts
import json
from typing import Any, List, Dict, Text


def fetch_events(year: int) -> List[Dict[Text, Any]]:
    """
    :param year: The year to fetch the events
    :return: JSON of all jewish events in the yea
    :return:
    """
    res = requests.get(GenericConsts.API_FORMAT.format(YEAR=year))
    res.raise_for_status()
    return res.json()[EventsConsts.EVENTS_KEY]


def get_month_quarter(month: int) -> int:
    """
    :param month: month of the year
    :return: the month's quarter
    """
    return (month - 1) // GenericConsts.QUARTER_LENGTH + 1


def find_next_quarter(month: int) -> int:
    """
    :param month: current month of the year
    :return: the next quarter by number
    """
    current_quarter = get_month_quarter(month)
    return current_quarter % 4 + 1


def check_holiday_next_quarter(event: Dict[Text, Any], next_quarter: int) -> bool:
    """
    :param event: an event from the hebcal API
    :param next_quarter: next quarter
    :return: true whether the event is holiday and in the next quarter, false otherwise
    """
    event_month = int(event[EventsConsts.DATE_KEY].split("-")[1])
    return event[EventsConsts.CATEGORY_KEY] == EventsConsts.HOLIDAY_VAL and next_quarter == get_month_quarter(
        event_month)


def get_next_quarter_date() -> (int, int):
    """
    :return: the next quarter start month and year
    """
    month = datetime.date.today().month
    year = datetime.date.today().year
    next_quarter = find_next_quarter(month)
    if next_quarter == 1:
        year += 1
    return next_quarter, year


def get_next_quarter_holidays() -> List[Dict[Text, Text]]:
    """
    :return: all jewish holidays in the next quarter
    """
    next_quarter, year = get_next_quarter_date()
    events = fetch_events(year)
    return [{EventsConsts.HEBREW_KEY: event[EventsConsts.HEBREW_KEY],
             EventsConsts.DATE_KEY: event[EventsConsts.DATE_KEY]}
            for event in events if check_holiday_next_quarter(event, next_quarter)]


def dump_to_json_file(data: Any, filename: str = GenericConsts.JSON_FILE) -> None:
    """
    :param filename: name of json file
    :param data: the data to be dumped to file
    """
    with open(filename, 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


def write_next_quarter_holidays_to_file():
    """
    gets next quarter holidays and write it to json file
    """
    next_quarter_holidays = get_next_quarter_holidays()
    dump_to_json_file(next_quarter_holidays)
