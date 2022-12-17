import holiday
import cert


def main():
    holiday.write_next_quarter_holidays_to_file()
    cert.cert_gen()


if __name__ == '__main__':
    main()
