#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))

    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    line_count = 0
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    status_codes = {}

    try:
        for line in sys.stdin:
            parts = line.split()

            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            total_size += file_size

            if status_code in valid_codes:
                status_codes[status_code] = (
                        status_codes.get(status_code, 0) + 1
                        )

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        except KeyboardInterrupt:
            pass
        finally:
            print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
