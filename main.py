
from pymysql import Connection
import math
import datetime
import fuzzywuzzy.fuzz as fuzz
import time
import csv
import pandas as pd
from time import sleep
from sqlalchemy import create_engine
import codecs
import os
class sqlConnect:
    def __init__(self):
        self.user="root"
        self.password="root"
        self.host="localhost"
        self.database="fan"
        self.port=3306
    def connect_mysql(self):
            self.conn = Connection(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
            self.cursor = self.conn.cursor()
            print("#######################################################################################################################")

    def execute_sql(self,sql):
        self.conn = Connection(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        self.conn.commit()
        print("执行成功!")

   

        
class loadData(sqlConnect):
    def __init__(self,table_name,file_path,csv_table):
        super().__init__()
        sqlConnect().connect_mysql
        self.file_path = file_path
        self.table_name = table_name
        self.csv_table = csv_table
    def change_csv(self):
        try:
            with codecs.open(self.csv_table, 'r', encoding='gb18030') as self.fin:
                self.csv_reader = csv.reader(self.fin)
                self.rows = [row for row in self.csv_reader]
            with open(self.csv_table, 'w', newline='', encoding='utf-8') as self.fout:
                csv_writer = csv.writer(self.fout)
                csv_writer.writerows(self.rows)
                print(f'{self.csv_table}  gb18030 编码已转换完成  UTF8格式')
        except:
                print(f'{self.csv_table}   编码已经是UTF8格式,无需转换')
    def load_csv_to_mysql(self):
        self.df = pd.read_csv(f'{ self.file_path }/{self.csv_table}')
        engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}')
        self.df.to_sql(name=self.table_name, con=engine, index=False, if_exists='append')
        print(f"原始数据 {self.csv_table} 已导入到数据库{self.database}的 {self.table_name}")
     
class outputData(sqlConnect):
    def __init__(self,user_name,out_table_name):
        super().__init__()
        sqlConnect().connect_mysql()
        self.out_table_name =  out_table_name

 
        self.user_name = user_name 
        self.out_putfile_name = f'{self.user_name}.xlsx'
    def output_mysql_to_xlsx(self,condition1,condition2): 
        engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}')
        self.condition1=condition1
        self.condition2=condition2
        query = f"SELECT * FROM {self.out_table_name} WHERE {self.condition1} = '{self.condition2}'"
        print(query)
        sleep(3)
        self.df = pd.read_sql_query(query, engine)
        self.df.to_excel(self.out_putfile_name, index=False)
        print(f"查询结果已导出到{self.out_putfile_name}")
        print(f"用户 {self.user_name} 的数据表 {self.out_table_name} 导出到 {self.out_putfile_name} 成功!")

class dataProcess(sqlConnect):
    def __init__(self):
        super().__init__()
        sqlConnect().connect_mysql()
    def insert_user_price(self,username):
        self.username=username
        print(f"开始导入用户{self.username}的价格数据")
        self.a=int(input("请选择价格表模板:输入1,使用便宜价格模板;输入2,使用昂贵价格模板)"))
        if self.a==1:
            self.sql_price1=[f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '青海', 2.8, 3.4, 5.0, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '宁夏回族自治区', 2.8, 4.5, 5.5, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '上海', 2.8, 4.5, 5.0, 3.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '北京', 4.5, 5.5, 6.5, 3.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '西藏自治区', 25.0, 25.0, 25.0, 25.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '重庆', 2.8, 3.4, 4.0, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '天津', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '山东省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '山西省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '江苏省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '河北省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '湖北省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '湖南省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '陕西省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '安徽省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '云南省', 2.8, 3.4, 4.0, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '海南省', 2.8, 3.4, 5.0, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '内蒙古自治区', 2.8, 4.5, 5.5, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '新疆维吾尔自治区', 15.0, 15.0, 15.0, 15.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '广东省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '青海省', 2.8, 3.4, 5.0, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '江西省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '福建省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '贵州省', 2.8, 3.4, 4.0, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '吉林省', 2.8, 3.4, 4.0, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '四川省', 2.8, 3.4, 4.0, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '辽宁省', 2.8, 3.4, 4.0, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '广西壮族自治区', 2.8, 3.4, 4.0, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '河南省', 2.8, 3.4, 4.0, 1.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '甘肃省', 2.8, 3.4, 5.0, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '浙江省', 2.8, 3.4, 4.0, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '黑龙江省', 2.8, 3.4, 4.0, 3.5);",
                            ]
            for self.i in range(len(self.sql_price1)):
                sqlConnect().execute_sql(sql=self.sql_price1[self.i])
                print(f"已导入第{self.i+1}条数据")
            print(f"用户{self.username}的价格数据导入成功!")
        elif self.a==2:
            self.sql_price2=[f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}','青海', 3.5, 4.0, 6.0, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '宁夏回族自治区', 3.5, 4.0, 6.0, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '上海', 3.5, 4.5, 5.0, 3.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '北京', 5.0, 6.0, 7.0, 4.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '西藏自治区', 15.0, 15.0, 15.0, 15.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '重庆', 3.5, 4.0, 4.5, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '天津', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '山东省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '山西省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '江苏省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '河北省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '湖北省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '湖南省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '陕西省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '安徽省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '云南省', 3.5, 4.0, 4.5, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '海南省', 3.5, 4.0, 6.0, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '内蒙古自治区', 3.5, 4.0, 6.0, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '新疆维吾尔自治区', 15.0, 15.0, 15.0, 15.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '广东省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '青海省', 3.5, 4.0, 6.0, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '江西省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '福建省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '贵州省', 3.5, 4.0, 4.5, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '吉林省', 3.5, 4.0, 4.5, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '四川省', 3.5, 4.0, 4.5, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '辽宁省', 3.5, 4.0, 4.5, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '广西壮族自治区', 3.5, 4.0, 4.5, 3.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '河南省', 3.5, 4.0, 4.5, 1.5);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '甘肃省', 3.5, 4.0, 4.5, 6.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '浙江省', 3.5, 4.0, 4.5, 2.0);",
                            f"INSERT INTO user_price (`user`, 目的地, level1, level2, level3, level4) VALUES('{self.username}', '黑龙江省', 3.5, 4.0, 4.5, 3.5);",
                            ]
            for self.j in range(len(self.sql_price2)):
                sqlConnect().execute_sql(sql=self.sql_price2[self.j])
                print(f"已导入第{self.j+1}条数据")
            print(f"用户{self.username}的价格数据导入成功!")

        else:
                print("输入错误")

    def delete_user_price(self,username):
         self.conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'fan',         # 数据库名
    )
         self.cursor = self.conn.cursor()
         self.sql_delete_user_price=f"DELETE FROM user_price WHERE user='{username}'"
         self.cursor.execute(self.sql_delete_user_price)
         self.conn.commit()
         print(f"用户{username}的价格数据已删除成功!")
    def select_user_price(self):
         self.conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'fan',         # 数据库名
    )
         self.cursor = self.conn.cursor()
         self.sql_select_user_price="SELECT * FROM user_price"
         self.cursor.execute(self.sql_select_user_price)
         self.result=self.cursor.fetchall()
         print(f"共有{len(self.result)}条数据")
         for self.i in range(len(self.result)):
             print(self.result[self.i])
    def delete_csv_data_table(self):
        self.conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'fan',         # 数据库名
    )
        self.cursor = self.conn.cursor()
        self.sql_delete_csv_data="DELETE FROM csv_data_table"
        self.cursor.execute(self.sql_delete_csv_data)
        self.conn.commit()
    def delete_user_price_table(self):
        self.conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'fan',         # 数据库名
    )
        self.cursor = self.conn.cursor()
        self.sql_delete_user_price="DELETE FROM user_price"
        self.cursor.execute(self.sql_delete_user_price)
        self.conn.commit()
  
         
    def calculations_data(self,user):
        self.conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'fan',         # 数据库名
    )
        self.cursor = self.conn.cursor()
        self.面单发放客户=user
        self.sql_select_csv_data_table=f"SELECT * FROM csv_data_table WHERE 面单发放客户='{self.面单发放客户}'"
        self.cursor.execute(self.sql_select_csv_data_table)
        self.result=self.cursor.fetchall()


        self.sql_select_user_price=f"SELECT * FROM user_price WHERE user='{self.面单发放客户}'"
        self.cursor.execute(self.sql_select_user_price)
        self.result1=self.cursor.fetchall()

        for self.a in range(len(self.result)):
            self.结算重量=self.result[self.a][12]
            self.目的地=self.result[self.a][10]
            self.应收运费=self.result[self.a][14]
            for self.b in range(len(self.result1)):
                    self.level1=self.result1[self.b][3]
                    self.level2=self.result1[self.b][4]
                    self.level3=self.result1[self.b][5]
                    self.level4=self.result1[self.b][6]
                    self.score=fuzz.partial_ratio(self.目的地,self.result1[self.b][2])
           
                    if 100>=self.score>=90:
                        print(f"原始表格中的目的地{self.目的地}，数据库中的目的地{self.result1[self.b][2]}，匹配得分：",self.score) 
                     
                        if self.score>=90 and self.result1[self.b][2] in  ('新疆维吾尔自治区','西藏自治区'):
                            #sleep(1)
                            self.应收运费=self.level1*math.ceil(self.结算重量)
                        elif self.score>=90 :
                            if 0<self.结算重量<1:
                                self.应收运费=self.level1
                            elif self.结算重量>=1 and self.结算重量<2:
                                self.应收运费=self.level2
                            elif self.结算重量>=2 and self.结算重量<3:
                                self.应收运费=self.level3
                            elif self.结算重量>=3:
                                self.应收运费=self.level1+self.level4*math.ceil(self.结算重量-1)
                            elif self.结算重量==2:
                                self.应收运费=self.level3
                                #self.结算重量+=0.02
                            elif self.结算重量==1:
                                self.应收运费=self.level2
                                #self.结算重量+=0.02
                            elif self.结算重量==0:
                                self.应收运费=0
                    elif 0<self.score<90:
                         pass
                    #print(f"########原始表格中的目的地{self.目的地}，数据库中的目的地{self.result1[self.b][2]}，匹配得分：",self.score) 
                    #if self.目的地==self.result1[self.b][2]:
                    if self.score>=90:
                        self.sql_update_csv_data_table=f"UPDATE csv_data_table SET 应收运费='{self.应收运费}' WHERE 面单发放客户='{self.面单发放客户}'  AND 单号='{self.result[self.a][1]}'"
                        self.cursor.execute(self.sql_update_csv_data_table)
                        self.conn.commit()
                        print(f"用户{self.面单发放客户}的运单号{self.result[self.a][1]}的结算重量{self.结算重量}的应收运费已更新为{self.应收运费}")
        print(f"用户{self.面单发放客户}的运单数据已更新应收运费成功!")
class auto_run():
    def auto_run_select_user_price(self):
        self.conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'fan',         # 数据库名
    )

        self.cursor = self.conn.cursor()
        self.sql_select_user_price="SELECT  distinct `user` FROM user_price "
        self.cursor.execute(self.sql_select_user_price)
        self.user_list_result=self.cursor.fetchall()
        self.user_list=[]
        for self.a in range(len(self.user_list_result)):
            self.user_list.append(self.user_list_result[self.a][0])
        print(f"共有{len(self.user_list)}个用户，等待计算运费的所有用户为：{self.user_list}")


        self.cursor = self.conn.cursor()
        self.sql_select_CSVDATA="SELECT  distinct 面单发放客户 FROM csv_data_table "
        self.cursor.execute( self.sql_select_CSVDATA)
        self.CSV_user_list_result=self.cursor.fetchall()
        self.CSV_user_list=[]
        for self.a in range(len(self.CSV_user_list_result)):
            self.CSV_user_list.append(self.CSV_user_list_result[self.a][0])

        print(f"共有{len(self.CSV_user_list)}个用户，CSV数据中的所有用户为：{self.CSV_user_list}")
        self.cunzai_list=[]
        for self.item in self.user_list:
             if self.item in self.CSV_user_list:
                self.user_one=self.user_list.index(self.item)
                print(f"正在处理{self.user_one+1}个用户{self.item}的数据")
                self.cunzai_list.append(self.item)
        print(f"共有{len(self.cunzai_list)}个用户，需要计算运费的用户为：{self.cunzai_list}")
        self.cursor = self.conn.cursor()
        for self.a in range(len(self.cunzai_list)):
            self.面单发放客户=str(self.cunzai_list[self.a])
            print(f"正在处理{self.a+1}个用户{self.面单发放客户}的数据")
            self.dataProcess=dataProcess()
            self.dataProcess.calculations_data(user=self.面单发放客户)          
            current_time = time.strftime("%Y-%m", time.localtime())
            self.user=self.cunzai_list[self.a]#=input("请输入导出面单发放客户的用户名：")
            self.month=input("请输入统计数据的月份：")
            print(f"正在导出{self.user}的{self.month}月份账单数据")
            self.out=outputData(user_name=self.month+"月份账单"+self.user+ current_time,out_table_name='csv_data_table')
            self.out.output_mysql_to_xlsx(condition1='面单发放客户',condition2=self.user)
            print(f"一共{len(self.cunzai_list)}个用户代导出数据，用户{self.user}的运单数据已导出成功！")

            
class run_main():
    def __init__(self):
        self.a=0
    def run(self):
            print("######################################欢迎使用SSR运单数据处理系统################################")
            print("功能列表：")
            print("1.导入CSV数据至数据库")
            print("2.新建用户价格表")
            print("3.删除用户价格表")
            print("4.查看所有用户价格表")
            print("5.计算用户运费")
            print("6.导出用户运费数据")
            print("7.格式化CSV数据库总表")
            print("8.格式化用户价格表")
            print("9.auto run one key!")
            print("######################################欢迎使用SSR运单数据处理结果################################")
  
            self.a=int(input("请输入功能编号："))
            if self.a==1:
                    self.csv_name=str(input("请输入CSV文件名包含后缀csv,例如:data.csv::::"))
                    self.load= loadData(table_name='csv_data_table',file_path='CSV_DATA',csv_table=self.csv_name)

                    self.load.change_csv()
                    self.load.load_csv_to_mysql()
               
                 
                    print(f"CSV文件{self.csv_name}已导入数据库成功！")
                    run_main().run()
            elif self.a==2:
                    self.dataProcess=dataProcess()
                    self.username=str(input("请输入新建价格表的客户名："))
                    self.dataProcess.insert_user_price(username=self.username)
                    run_main().run()
            elif self.a==5:
                            self.面单发放客户=str(input("请输入计算运费的面单发放客户："))
                            self.dataProcess=dataProcess()
                            self.dataProcess.calculations_data(user=self.面单发放客户)
                            run_main().run()
            elif self.a==6:
                            import time
                            current_time = time.strftime("%Y-%m", time.localtime())

                            self.user=input("请输入导出面单发放客户的用户名：")
                            self.month=input("请输入统计数据的月份：")
                            self.out=outputData(user_name=self.month+"月份账单"+self.user+ current_time,out_table_name='csv_data_table')
                            self.out.output_mysql_to_xlsx(condition1='面单发放客户',condition2=self.user)
                            print(f"用户{self.user}的运单数据已导出成功！")
                            run_main().run()
            elif self.a==3:
                        self.username=str(input("请输入删除价格表的客户名："))
                        self.dataProcess=dataProcess()
                        self.dataProcess.delete_user_price(username=self.username)
                        run_main().run()
            elif self.a==4:
                    self.dataProcess=dataProcess()
                    print("所有用户价格表：")
                    print(self.dataProcess.select_user_price())
                    run_main().run()     
            elif self.a==7:
                    self.dataProcess=dataProcess()
                    self.dataProcess.delete_csv_data_table()
                    print("CSV数据库总表已格式化成功~")
                    run_main().run()
            elif self.a==8:
                    self.dataProcess=dataProcess()
                    self.dataProcess.delete_user_price_table() 
                    print("用户价格表已格式化成功！")
                    run_main().run()
            elif self.a==9:
                    self.auto=auto_run()
                    self.auto.auto_run_select_user_price()
                    print("Success!!!!!!!!!!")
                    run_main().run()             
            else:
                    print("输入错误") 
                    run_main().run()      
            
if __name__ == '__main__':
    run_main().run()

