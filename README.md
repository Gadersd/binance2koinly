Binance to Koinly CSV Converter
===============================

This is a Python script that converts Binance US or Binance CSV transaction history files to Koinly's native CSV format. This script was created because Koinly has a software bug that prevents it from importing Binance US CSV files correctly.

Prerequisites
-------------

To use this script, you'll need:

*   Python 3.x installed on your machine
*   A Binance US or Binance CSV transaction history file
*   A Koinly account

Usage
-----

To use the script, open a terminal window and navigate to the project directory. Then, run the following command:

    python b2k.py INPUT_FILE_PATH OUTPUT_FILE_PATH

where:

*   `INPUT_FILE_PATH` is the file path of your Binance US or Binance CSV transaction history file.
*   `OUTPUT_FILE_PATH` is the desired file path of your converted Koinly CSV file.

For example:

    python b2k.py ~/Downloads/Binance-US-Transactions-2022.csv ~/Documents/Koinly-Transactions-2022.csv

Once the script has finished running, you can import the output CSV file into Koinly.

Notes
-----

*   This script has only been tested with Binance US CSV files, but it should also work with Binance CSV files.
*   The script assumes that your Binance US or Binance CSV file follows the standard format that is generated by Binance. If your file has a different format, the script may not work correctly.
*   The script will overwrite the output file if it already exists, so be careful when specifying the output file path.

Contributing
------------

If you find any issues or have suggestions for improvements, feel free to open an issue or pull request on the [GitHub repository](https://github.com/Gadersd/binance2koinly).

License
-------

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
