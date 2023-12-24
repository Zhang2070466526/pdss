import pymssql


class EhrConnect:
    def __init__(self):
        self.host = '172.16.6.197'
        self.username = 'sa'
        self.passward = 'eHr123'
        self.database = 'T9IMS'
        self.charset = 'utf8'

    def select(self, sql):
        try:
            db = pymssql.connect(host=self.host, user=self.username, password=self.passward, database=self.database,
                                 port=1433, charset='utf8')
            cursor = db.cursor(as_dict=True)
            # print(sql)
            cursor.execute(sql)
            select_list = cursor.fetchall()
            cursor.close()
            db.close()
            return select_list
        except Exception as e:
            print(e)
            return []

    def update(self, sql):
        """
        创建或更新
        :param sql:
        :return:
        """
        try:
            db = pymssql.connect(host=self.host, user=self.username, password=self.passward, database=self.database,
                                 port=1433)
            cursor = db.cursor(as_dict=True)
            update_result = cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return True
        except Exception as e:
            print(e)
            return False

    def create(self, sql):
        """
        创建或更新
        :param sql:
        :return:
        """
        try:
            db = pymssql.connect(host=self.host, user=self.username, password=self.passward, database=self.database,
                                 port=1433)
            cursor = db.cursor(as_dict=True)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return True
        except Exception as e:
            print(e)
            return False





class OAConnect:
    def __init__(self):
        self.host = '172.16.6.194'
        self.username = 'sa'
        self.passward = 'Runergy@0919'
        self.database = 'ekp1002'
        self.charset = 'utf8'

    def select(self, sql):
        try:
            db = pymssql.connect(host=self.host, user=self.username, password=self.passward, database=self.database,
                                 port=1433)
            cursor = db.cursor(as_dict=True)
            cursor.execute(sql)
            select_list = cursor.fetchall()
            cursor.close()
            db.close()
            return select_list
        except Exception as e:
            print(e)
            return []

    def update(self, sql):
        """
        创建或更新
        :param sql:
        :return:
        """
        try:
            db = pymssql.connect(host=self.host, user=self.username, password=self.passward, database=self.database,
                                 port=1433)
            cursor = db.cursor(as_dict=True)
            update_result = cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return True
        except Exception as e:
            print(e)
            return False

    def create(self, sql):
        """
        创建或更新
        :param sql:
        :return:
        """
        try:
            db = pymssql.connect(host=self.host, user=self.username, password=self.passward, database=self.database,
                                 port=1433)
            cursor = db.cursor(as_dict=True)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return True
        except Exception as e:
            print(e)
            return False

