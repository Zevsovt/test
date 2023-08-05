import sqlite3


class User:
    def __init__(self, name, surname, gender):
        self.name = surname
        self.surname = surname
        self.gender = gender


def get_user_list(cursor):
    command = '''
                SELECT * FROM users;
                '''
    result = cursor.execute(command)
    users = result.fetchall()
    print(users)

def get_user(cursor, user_id):
    command = '''
                    SELECT * FROM users WHERE id = ?;
                    '''
    result = cursor.execute(command, (user_id,))
    users = result.fetchall()


def create_table_user(cursor):
    command = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT, 
                surname TEXT,
                gender TEXT);
            '''
    cursor.execute(command)

def add_user(cursor, user):
    command = '''
                INSERT INTO users(name, surname, gender)
                VALUES (?, ?, ?);
                '''
    cursor.execute(command, (user.name, user.surname, user.gender))

def update_user_name(cursor, value, user_id):
    command = '''
                UPDATE users SET name = ? WHERE id = ?;
                '''
    cursor.execute(command, (value, user_id))

def delete_users(cursor):
    command = '''
                    DELETE FROM users;
                    '''
    cursor.execute(command)

def delete_user_by_id(cursor, user_id):
    command = '''
                        DELETE FROM users WHERE id = ?;
                        '''
    cursor.execute(command, (user_id,))

def get_users_by_gender(cursor, gender):
    command = '''
        SELECT * FROM users WHERE gender = ?;
                        '''
    result = cursor.execute(command, (gender,)).fetchall()
    print(result)


if __name__ == '__main__':
    with sqlite3.connect('data.db') as cursor:
        create_table_user(cursor)
        delete_users(cursor)
        add_user(cursor, User(name='Максим', surname='Иванов', gender='male'))
        add_user(cursor, User(name='Владимир', surname='Петров', gender='male'))
        add_user(cursor, User(name='Катя', surname='Кузнецова', gender='female'))
        get_user(cursor, 1)
        update_user_name(cursor, 'Павел', 1)
        get_user(cursor, 1)
        get_users_by_gender(cursor, 'male')



















# try:
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
#
# except sqlite3.DatabaseError:
#     print('Произошла ошибка при подключении')

# finally:
#     connection.close()

# with sqlite3.connect('data.db') as cursor:
#     print(cursor)



