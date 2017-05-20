import psycopg2


def main_menu():
    print('Oi moite! How u goin\'?')
    print('This is my advice to use our databases and stuff.')
    print('1 - Returns the name of the mentors. (First, Last)')
    print('2 - Returns the nicknames of mentors working of beautiful city of Miskolc.')

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



def main():
    menu_num = main_menu()
    if menu_num == '1':
        name_of_mentors()


if __name__ == '__main__':
    main()
