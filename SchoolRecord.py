import csv
import rds

def load_csv_to_rds(csv_reader_object, rds):
    row_count = 1
    for eachrow in csv_reader_object:
        if row_count == 1:
            return False
        else:
            insert_rds_row(row)
            row_count += 1
            return True





