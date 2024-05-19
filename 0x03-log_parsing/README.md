# Log Metrics Script

>> This script reads log entries from stdin, processes them, and computes metrics such as the total file size and the number of occurrences of each status code.
>> The script prints these statistics after every 10 lines of input or upon receiving a keyboard interruption (CTRL + C).

## Log Entry Format
>> The script expects log entries to follow this format:
	<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

* Example log entries:
192.168.0.1 - [2023-05-19] "GET /projects/260 HTTP/1.1" 200 1234
192.168.0.2 - [2023-05-19] "GET /projects/260 HTTP/1.1" 404 5678


## Requirements

- Python 3.4.3 or higher

## Usage

1. Save the script as `0-stats.py`.
2. Create a log file with entries in the correct format and save it as `logfile.txt`.

### Running the Script with a Log File

Use the `cat` command to read the contents of the log file and pipe (`|`) it into the Python script:
```sh
cat logfile.txt | python3 0-stats.py

### Manually Inputting Log Entries

>> Alternatively, you can run the script and manually input log entries line by line:
	python3 log_metrics.py

>> Type or paste log entries one by one and press Enter after each.
>> When you want to stop and see the statistics, press CTRL + C on your keyboard.

### Output
>> After every 10 lines or upon keyboard interruption (CTRL + C), the script prints the following statistics:
	Total file size: the sum of all previous file sizes.
Number of lines by status code: the count of each status code that appeared in the input.

* Example output:
Total file size: 12345
200: 3
301: 1
404: 2
500: 1

* Example Log File
>> Here is an example of the logfile.txt file
192.168.0.1 - [2023-05-19] "GET /projects/260 HTTP/1.1" 200 1234
192.168.0.2 - [2023-05-19] "GET /projects/260 HTTP/1.1" 404 5678
192.168.0.3 - [2023-05-19] "GET /projects/260 HTTP/1.1" 301 910
192.168.0.4 - [2023-05-19] "GET /projects/260 HTTP/1.1" 500 1112
192.168.0.5 - [2023-05-19] "GET /projects/260 HTTP/1.1" 403 1324
192.168.0.6 - [2023-05-19] "GET /projects/260 HTTP/1.1" 401 645
192.168.0.7 - [2023-05-19] "GET /projects/260 HTTP/1.1" 200 2345
192.168.0.8 - [2023-05-19] "GET /projects/260 HTTP/1.1" 404 123
192.168.0.9 - [2023-05-19] "GET /projects/260 HTTP/1.1" 405 789
192.168.0.10 - [2023-05-19] "GET /projects/260 HTTP/1.1" 400 2567

## Handling Errors
>> If the format of a log entry does not match the expected format, that line will be skipped.

## Author:
>> Nontuthuzelo Ngwenya - Github(DeeGemini)

## License
>> None
