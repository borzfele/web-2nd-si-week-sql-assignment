import psycopg2


def main_menu():
    print('Oi moite! How u goin\'?')
    print('This is my advice to use our databases and stuff.')
    print('1 - Returns the name of the mentors. (First, Last)')
    print('2 - Returns the nicknames of mentors working of beautiful city of Miskolc.')
    print('3 - Returns the full name of Carol.')
    print('4 - Find the other girl.')
    print('5 - Add the new applicant.')
    print('6 - Update Jemima\'s phone number.')
    menu_num = input('Type the number of the menu you would like to use: ')
    return menu_num


def name_of_mentors():
    connect_str = "dbname='borzfele' user='borzfele' host='localhost' password='91december30'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    names = cursor.fetchall()
    return names


def nicknames_of_miskolc_mentors():
    connect_str = "dbname='borzfele' user='borzfele' host='localhost' password='91december30'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""SELECT nick_name FROM mentors WHERE city = 'Miskolc';""")
    nicknames = cursor.fetchall()
    return nicknames


def full_name_of_carol():
    connect_str = "dbname='borzfele' user='borzfele' host='localhost' password='91december30'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name), phone_number FROM applicants WHERE first_name = 'Carol'""")
    full_name = cursor.fetchall()
    return full_name


def find_not_carol():
    connect_str = "dbname='borzfele' user='borzfele' host='localhost' password='91december30'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name), phone_number FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu'""")
    full_name = cursor.fetchall()
    return full_name


def add_new_applicant():
    connect_str = "dbname='borzfele' user='borzfele' host='localhost' password='91december30'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');""")
    cursor.execute("""SELECT * FROM applicants WHERE application_code = '54823'""")
    dataz = cursor.fetchall()
    return dataz


def main():
    menu_num = main_menu()
    if menu_num == '1':
        name_of_mentors()
    if menu_num == '2':
        nicknames_of_miskolc_mentors()
    if menu_num == '3':
        full_name_of_carol()
    if menu_num == '4':
        find_not_carol()
    if menu_num == '5':
        print(add_new_applicant())


if __name__ == '__main__':
    main()
