import mysql.connector


def rds_operations(stmt):

    try:
        cnx = mysql.connector.connect(user='$$$$$', password='$$$$$$$$$$',
                              host='aws rds endpoint',
                                database='school_teacher')

        if cnx.is_connected():
            cursor = cnx.cursor()
        #stmt = "CREATE DATABASE school_teacher"
        #stmt = """CREATE TABLE school_teacher_count (id INT AUTO_INCREMENT PRIMARY KEY,
        #year VARCHAR(7),
        #primary_male INT,
        #primary_female INT,
        #primary_total INT)"""

        #    stmt="DESCRIBE school_teacher_count"
            #stmt = "DROP TABLE school_teacher_count;"

            cursor.execute(stmt)

            print("RDS operation success")

        cnx.close()
    except Exception as e:
        print(e)


def rds_drop_table():

    stmt = "DROP TABLE school_teacher_count;"

    rds_operations(stmt)
    return stmt


def rds_create_table():

    stmt = """CREATE TABLE school_teacher_count (id INT AUTO_INCREMENT PRIMARY KEY,
    start_year CHAR(4),
    end_year CHAR(4),
    primary_male INT,
    primary_female INT,
    primary_total INT)"""

    rds_operations(stmt)
    return stmt


def rds_insert_row(start_date,end_date,male_cnt,female_cnt, total_cnt):

    stmt = """INSERT INTO school_teacher_count (year,primary_male,primary_female,primary_total)
            VALUES({0}, {1}, {2}, {3}, {4})""". format(start_date,end_date,male_cnt,female_cnt, total_cnt)

    print(stmt)
    #rds_operations(stmt)
    return stmt

