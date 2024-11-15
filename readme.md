# Site Usage Tracker

![GitHub last commit](https://img.shields.io/github/last-commit/FaithLilley/DDB-usage-monitor?style=plastic&logo=github) ![GitHub repo size](https://img.shields.io/github/repo-size/FaithLilley/DDB-usage-monitor?style=plastic) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/playwright?style=plastic)

A python script to monitor and profile the number of active users on a website on an hourly basis.

It loads up the URL, extracts the data required and saves it to a CSV

## Installation

This is a python project, so use pip to install the necessary libraries:

`pip install`

## Running the Script

`python tracker.py`

The script will run and launch a browser session, loading the forums page of D&D Beyond, then waiting a few seconds before saving data and quitting the session.

It then waits between 58 and 62 minutes before repeating.

1. It saves a copy of that page, in html format, to `./pages/`
2. It saves a line of data to `./data/dnd_usage.csv`

### Format of the CSV file

`2024-11-14 00:00:08,13689,3341,10348`

There are 4 fields of data on each line:

1. Standard timestamp
2. Total number of current active users
3. Currently active logged in users
4. Currently active logged out users

Note that 2 should equal 3 + 4

## TO DO

- Update the delay so that the read time stays within +/- 2 mins of the hour mark.

## Misc notes

- Use `python --version` to check your version. Written using:
  - python 3.13.0
  - pip 24.3.1