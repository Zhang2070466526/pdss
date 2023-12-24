import psycopg2
class connect_to_postgresql:
    def __init__(self):
        self.host = '172.16.6.131'
        self.username = 'root'
        self.passward = 'sa123'
        self.database = 'biosecurity-boot'
        self.charset = 'utf8'
    def select(self, sql):
        try:
            conn= psycopg2.connect(host=self.host, user=self.username, password=self.passward, database=self.database,port=5442)
            conn.set_client_encoding('utf-8')
            cur = conn.cursor()
            cur.execute(sql)
            select_list = cur.fetchall()
            # for row in select_list:
            #     print(row)
            cur.close()
            conn.close()
            return select_list

        except psycopg2.Error as e:
            print(e)
