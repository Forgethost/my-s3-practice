from tranform import *
#from s3access import *
from rds import *
#from SchoolRecord import *


def main():

    transform_object = Transform()
    start_year, end_year = transform_object.extract_date("2012-13")
    formatted_year = Year(start_year,end_year)
    print(formatted_year.start_year)
    #rds_drop_table()
    rds_create_table()
    rds_insert_row("2012", "2013",12,14,27)


if __name__ == "__main__":
    main()