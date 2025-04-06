import csv
import codecs
from pymysql import Connection
import csv
import codecs
import pandas as pd
from sqlalchemy import create_engine
def Changecsv():
    with codecs.open('原始数据/1月收件.csv', 'r', encoding='gb18030') as fin:
        csv_reader = csv.reader(fin)
        rows = [row for row in csv_reader]
    with open('原始数据/1月收件.csv', 'w', newline='', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerows(rows)
        print('csv编码已转换完成UTF8')
def upload_csv_to_mysql():

    df = pd.read_csv('原始数据/1月收件.csv')
    engine = create_engine(f'mysql+pymysql://{'root'}:{'root'}@{'localhost'}/{'cj'}')
    df.to_sql('second', con=engine, index=False, if_exists='append')
def Deletefirst():
    conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'cj',         # 数据库名
    )
    sql6="DELETE FROM second;"
    cursor = conn.cursor()
    cursor.execute(sql6)
    cursor.connection.commit()
    cursor.close()
    print("####################################################")
    print("SQL原始数据已成功清空")
    print("####################################################")
Deletefirst()
upload_csv_to_mysql()
