#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression pattern to match the log line format
log_pattern = re.compile(
    r'(?P<ip>\S+) - \[(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)'
)

# Define a function to print statistics
def print_statistics():
    print("Total file size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

# Handle keyboard interrupt (CTRL + C)
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Set the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read input from stdin
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group('status'))
            file_size = int(match.group('size'))

            # Add file size to total_size
            total_size += file_size

            # Increment the count for the status code if it is in status_counts
            if status_code in status_counts:
                status_counts[status_code] += 1

            # Increment line count
            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except Exception as e:
    print("An error occurred:", e)

# Print final statistics at the end of the input
print_statistics()

