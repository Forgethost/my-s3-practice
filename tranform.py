import re

class Year:
    def __init__(self, start_yr, end_yr):
        self.start_year = start_yr
        self.end_year = end_yr

class Transform:

    def extract_date(self, inputyear):

        end_year = re.findall(".+[-](.+)", inputyear)[0]
        start_year = re.findall("(.+)[-].+", inputyear)[0]
        return start_year, end_year

