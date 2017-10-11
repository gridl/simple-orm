import sqlite3

class Base:
    __tablename__ = 'test'

    def create(self):
        conn = sqlite3.connect('orm.db')
        cur = conn.cursor()
        field_names = [k for k in self.__class__.__dict__.keys() if not k.startswith('__')]
        query_string = []
        for field_name in field_names:
            string = field_name
            value = self.__class__.__dict__.get(field_name)
            string += ' '+value[0]+' '+value[1]
            query_string.append(string)
        query = 'CREATE TABLE IF NOT EXISTS '+ self.__class__.__tablename__ +' (' + ', '.join(query_string) + ')'
        print(query)
        cur.execute(query)
        conn.commit()

    def delete(self):
        conn = sqlite3.connect('orm.db')
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS ' + self.__class__.__tablename__)
        conn.commit()

    def insert(self, insert_fields):
        conn = sqlite3.connect('orm.db')
        cur = conn.cursor()
        fields = []
        values = []
        for k,v in insert_fields.items():
            fields.append(k)
            values.append("'"+str(v)+"'")
        query_string = 'INSERT INTO '+self.__class__.__tablename__+\
                       ' ('+", ".join(fields)+') VALUES ('\
                       +", ".join(values)+');'
        try:
            cur.execute(query_string)
        except sqlite3.IntegrityError:
            print('Вы забыли передать данные обязательного столбца')
        except sqlite3.OperationalError:
            print('Указана несуществующая таблица или столбец')
        else:
            print('Новая запись успешно добавлена')
            conn.commit()

    def update(self, update_fields, where = ''):
        conn = sqlite3.connect('orm.db')
        cur = conn.cursor()
        query_string = 'UPDATE '+\
                       self.__class__.__tablename__+\
                       ' SET '+update_fields
        if where:
            query_string+= ' WHERE '+where
        try:
            cur.execute(query_string)
        except sqlite3.OperationalError:
            print('Указана несуществующая таблица или столбец')
        else:
            conn.commit()

    def select(self, fields, where = ''):
        conn = sqlite3.connect('orm.db')
        cur = conn.cursor()
        field_names = [k for k in self.__class__.__dict__.keys() if not k.startswith('__')]
        query_string = 'SELECT ' + fields + ' FROM ' + self.__class__.__tablename__
        for field_name in field_names:
            value = self.__class__.__dict__.get(field_name)
            if len(value) > 2:
                for key in value[2].keys():
                    query_string += ' JOIN '+key+' ON '+value[2][key]
        if where:
            query_string += ' WHERE '+where
        try:
            cur.execute(query_string)
        except sqlite3.OperationalError:
            print('Указана несуществующая таблица или столбец')
        else:
            results = cur.fetchall()
            print(results)
            conn.commit()

    def select_all(self):
        conn = sqlite3.connect('orm.db')
        cur = conn.cursor()
        field_names = [k for k in self.__class__.__dict__.keys() if not k.startswith('__')]
        query_string = 'SELECT %s FROM %s;' % (', '.join(field_names), self.__class__.__tablename__)
        try:
            cur.execute(query_string)
        except sqlite3.OperationalError:
            print('Указана несуществующая таблица или столбец')
        else:
            results = cur.fetchall()
            print(results)
            conn.commit()



