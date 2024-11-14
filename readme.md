# DDB Usage Tracker

A python script to track the number of active users on D&D Beyond.

It loads up the [D&D Beyond forums page](https://www.dndbeyond.com/forums), extracts data on the current number of users, and saves it to a CSV

## Installation

This is a python project, so use pip to install the necessary libraries:

`pip install`

## Running the Script

`python tracker.py`

The script will run and launch a browser session, loading the forums page of D&D Beyond, then waiting a few seconds before saving data and quitting.

1. It saves a copy of that page, in html format, to `./pages/`
2. It saves a line of data to `./data/dnd_usage.csv`

### Format of the CSV file

There are 4 fields of data on each line:

1. Standard timestamp
2. Total number of current active users
3. Currently active logged in users
4. Currently active logged out users

Note that 2 should equal 3 + 4

*A sample line of data*

`2024-11-14 00:00:08,13689,3341,10348`

## Misc notes

- Use `python --version` to check your version. Written using:
  - python 3.13.0
  - pip 24.3.1
- 