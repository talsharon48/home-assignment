class EventsConsts:
    CATEGORY_KEY = "category"
    HOLIDAY_VAL = "holiday"
    DATE_KEY = "date"
    EVENTS_KEY = "items"
    HEBREW_KEY = "hebrew"


class GenericConsts:
    API_FORMAT = "https://hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year={YEAR}&month=x&ss=on&mf=on&c=on&geo=geoname&geonameid=3448439&M=on&s=on"
    QUARTER_LENGTH = 3
    JSON_FILE = 'holidays.json'


class CertConsts:
    KEY_FILE = "private.key"
    CERT_FILE = "self_signed.crt"
    VALID_FROM_SECONDS = 0
    EXPIRE_IN_SECONDS = 60 * 60 * 24 * 365 * 10
    SERIAL_NUMBER = 0
    DNS = "nice-assignment.local"
    KEY_SIZE = 4096
    HASH_METHOD = 'sha512'
