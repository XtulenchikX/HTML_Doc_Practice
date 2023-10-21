import sqlite3
from another_func import write_log

def connect(database_name):
    """
    Устанавливает соединение с указанной базой данных SQLite.

    Parameters
    ----------
    database_name : str
        Название базы данных, с которой нужно установить соединение.

    Returns
    -------
    sqlite3.Connection или None
        Объект соединения с базой данных. В случае неудачного соединения возвращает None.
    """
    con = None
    try:
        con = sqlite3.connect(database_name)
    except sqlite3.DatabaseError:
        print(f'Не удалось установить соединение с базой данных "{database_name}"')
    else:
        return con

def close(con):
    """
    Закрывает соединение с базой данных.

    Parameters
    ----------
    con : sqlite3.Connection
        Объект соединения с базой данных.
    """
    con.close()

def read_all(con, table):
    """
    Отображает все строки из указанной таблицы в базе данных.

    Parameters
    ----------
    con : sqlite3.Connection
        Объект соединения с базой данных.

    table : str
        Название таблицы, из которой нужно извлечь данные.
    """
    if con is not None:
        cur = con.cursor()
        query = f"SELECT * FROM {table}"
        write_log(query)
        try:
            res = cur.execute(query)
        except sqlite3.OperationalError:
            print(f'Таблица с названием "{table}" не существует')
        else:
            for row in res:
                print(row)

def insert(con, table, *values):
    """
    Добавляет данные в указанную таблицу в базе данных.

    Parameters
    ----------
    con : sqlite3.Connection
        Объект соединения с базой данных.

    table : str
        Название таблицы, в которую будут вставлены данные.

    values : dict
        Значения данных, которые будут вставлены в виде последовательности словарей.
    """
    if con is not None:
        cur = con.cursor()
        inp = ' '
        for elem in values:
            inp = inp + f"('{elem['name']}', {elem['height']}, '{elem['created']}'), "
        inp = inp[:-2]
        try:
            query = f"INSERT INTO {table} (name, height, created) VALUES {inp}"
            cur.execute(query)
            con.commit()
            write_log(query)
        except sqlite3.OperationalError:
            print(f"Ошибка при добавлении данных {values} в таблицу {table}")

def delete(con, table, *conditions):
    """
    Удаляет данные из указанной таблицы в базе данных на основе условий.

    Parameters
    ----------
    con : sqlite3.Connection
        Объект соединения с базой данных.

    table : str
        Название таблицы, из которой будут удалены данные.

    conditions : str
        Условия, определяющие, какие данные будут удалены.
    """
    if con is not None:
        cur = con.cursor()
        for cond in conditions:
            try:
                query = f"DELETE FROM {table} WHERE {cond}"
                cur.execute(query)
                con.commit()
                write_log(query)
            except sqlite3.OperationalError:
                print(f"Ошибка при удалении данных по условию {cond} из таблицы {table}")

def update(con, table, *params):
    """
    Обновляет данные в указанной таблице в базе данных на основе указанных параметров.

    Parameters
    ----------
    con : sqlite3.Connection
        Объект соединения с базой данных.

    table : str
        Название таблицы, в которой будут обновлены данные.

    params : str
        Параметры, определяющие, какие данные будут обновлены.
    """
    if con is not None:
        cur = con.cursor()
        for param in params:
            try:
                query = f"UPDATE {table} SET {param[0]} WHERE {param[1]}"
                cur.execute(query)
                con.commit()
                write_log(query)
            except sqlite3.OperationalError:
                print(f"Ошибка обновления: {param[0]} с условием {param[1]} в таблице {table}")