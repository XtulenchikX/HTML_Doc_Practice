def write_log(query, file='command_history.log.txt'):
    """
    Записывает запрос к базе данных в файл журнала с указанием времени.

    Parameters
    ----------
    query : str
        Текст запроса к базе данных.

    file : str, optional
        Имя файла, в который будет записан запрос (по умолчанию 'command_history.log.txt').
    """
    import datetime as DT
    offset = DT.timedelta(hours=3)
    time = DT.datetime.now(DT.timezone(offset))
    time_format = "%d-%m-%Y %H:%M:%S"
    t_send = f"{time:{time_format}}"
    t_send = str(t_send)
    f = open(file, mode='a', errors='ignore')
    f.write(f"{query}; [{t_send}] \n \n")
    f.close()