from pymysql import Connection
import math
import datetime
import csv
import pandas as pd
from time import sleep
from sqlalchemy import create_engine
import codecs
def changecsv():#将将可恶的收件明细CSV文件gb18030编码的csv文件编码转换为UTF8
    with codecs.open('原始数据/1月收件.csv', 'r', encoding='gb18030') as fin:
        csv_reader = csv.reader(fin)
        rows = [row for row in csv_reader]
    with open('原始数据/1月收件.csv', 'w', newline='', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerows(rows)
        print('csv编码已转换完成UTF8')
def upload_csv_to_mysql():#·将收件的csv文件导入mysql数据库
    df = pd.read_csv('原始数据/1月收件.csv')
    engine = create_engine(f'mysql+pymysql://{'root'}:{'root'}@{'localhost'}/{'cj'}')
    df.to_sql('second', con=engine, index=False, if_exists='append')
    print("原始数据B已成功导入SQL")
    print("####################################################")
def upload_xlsx_to_mysql():#将驿站+门面+散户数据xlsx文件导入mysql数据库
    df = pd.read_excel(f'原始数据/12月驿站发件 (副本).xlsx')
    engine = create_engine(f'mysql+pymysql://{'root'}:{'root'}@{'localhost'}/{'cj'}')
    df.to_sql(name="first", con=engine, index=False, if_exists="append")
    print("原始数据A已成功导入SQL")
    print("####################################################")
    sleep(1)
def Yizhan():#驿站数据明细

    conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'cj',         # 数据库名
    )
    sql="select 门店名称,运单号,目的地,收件重量 from first where 门店名称 in ('新乡牧野丰鑫商行店','新乡牧野褐石公园社区店','新乡牧野二十二店')"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    sql1="select 目的地,level1,level2,level3,level4 from price "
    cursor = conn.cursor()
    cursor.execute(sql1)
    result1 = cursor.fetchall()

    for a in range(len(result)):
        for b in ('新乡牧野丰鑫商行店','新乡牧野褐石公园社区店','新乡牧野二十二店'):
            if result[a][0]==b:
                calnull门店名称=result[a][0]
                calnull运单号=result[a][1]
                calnull目的地=result[a][2]
                calnull收件重量=float(result[a][3])
                for a1 in range(len(result1)):
                    calnull计费=float(0.00)
                    calresult=float(0.00)
                    calnulllevel1=float(result1[a1][1])
                    calnulllevel2=float(result1[a1][2])
                    calnulllevel3=float(result1[a1][3])
                    calnulllevel4=float(result1[a1][4])
                    
                    if  0<calnull收件重量<1:
                        calnull计费=calnulllevel1
                    elif calnull收件重量>1 and calnull收件重量<2:
                        calnull计费=calnulllevel2
                    elif calnull收件重量>2 and calnull收件重量<3:
                        calnull计费=calnulllevel3
                    elif calnull收件重量>=3:
                        calnull计费=calnulllevel1+calnulllevel4*math.ceil(calnull收件重量-1)
                    elif  calnull收件重量==2:
                        calnull计费=calnulllevel3
                        calnull收件重量+=0.02
                    elif calnull收件重量==1:
                        calnull计费=calnulllevel2
                        calnull收件重量+=0.02
    
                    if result1[a1][0]==calnull目的地:
                        sql3="INSERT INTO cj.calnull(门店名称, 目的地, 运单号, 收件重量, 计费)VALUES('{}', '{}', '{}', '{}', '{}')".format(calnull门店名称,calnull目的地,calnull运单号, calnull收件重量, calnull计费)
                        cursor = conn.cursor()
                        cursor.execute(sql3)
                        cursor.connection.commit()

                        cursor.close()
    print("驿站数据明细数据已成功导入SQL")
    print("####################################################")
    date = datetime.date.today()
    sql4="select 门店名称,sum(计费) from calnull group by 门店名称"
    cursor = conn.cursor()
    cursor.execute(sql4)
    result4 = cursor.fetchall()
    for a in range(len(result4)):
        sql5="INSERT INTO cj.cal VALUES('{}', '快递超市', '{}', '{}')".format(result4[a][0],result4[a][1],date)
        cursor = conn.cursor()
        cursor.execute(sql5)
        cursor.connection.commit()
        cursor.close()
    print("驿站结算总额数据已成功导入SQL")
    print("####################################################")
    sleep(1)
    special('cj.calnull')
def special(sqlname):#计算新疆西藏特殊项函数
    conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'cj',         # 数据库名
    )
    sqlspecial="select 目的地,收件重量,计费 from {} where 目的地 in ('新疆维吾尔自治区','西藏')".format(sqlname)
    cursor = conn.cursor()
    cursor.execute(sqlspecial)
    sqlspecialresult = cursor.fetchall()
    for speciala in range(len(sqlspecialresult)):
        special计件重量=float(sqlspecialresult[speciala][1])  
        special计费=math.ceil(special计件重量)*15
        specialsql="UPDATE {} SET  计费='{}' where 目的地 in ('新疆维吾尔自治区','西藏')".format(sqlname,special计费)
        cursor = conn.cursor()
        cursor.execute(specialsql)
        cursor.connection.commit()
        cursor.close()
    print("SQL{}表新疆西藏特殊件数据已更正".format(sqlname))
    print("####################################################")        
    sleep(1)
    return sqlname
def ShopPersion():#计算门店名称&寄件人数据明细
    conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'cj',         # 数据库名
    )
    sql="select 店铺名称,寄件人,运单号,目的地,收件重量 from first where 门店名称 =''"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    shopsql="select 目的地,level1,level2,level3,level4 from priceshop "
    cursor = conn.cursor()
    cursor.execute(shopsql)
    result1 = cursor.fetchall()
    for a in range(len(result)):
                shop店铺名称=result[a][0]
                shop寄件人=result[a][1]
                shop运单号=result[a][2]
                shop目的地=result[a][3]
                shop收件重量=float(result[a][4])
                for a1 in range(len(result1)):
                    shop计费=float(0.00)
                    shopresult=float(0.00)
                    shoplevel1=float(result1[a1][1])
                    shoplevel2=float(result1[a1][2])
                    shoplevel3=float(result1[a1][3])
                    shoplevel4=float(result1[a1][4])
                    
                    if  0<shop收件重量<1:
                        shop计费=shoplevel1
                    elif shop收件重量>1 and shop收件重量<2:
                        shop计费=shoplevel2
                    elif shop收件重量>2 and shop收件重量<3:
                        shop计费=shoplevel3
                    elif shop收件重量>=3:
                        shop计费=shoplevel1+shoplevel4*math.ceil(shop收件重量-1)
                    elif  shop收件重量==2:
                        shop计费=shoplevel3
                        shop收件重量+=0.02
                    elif shop收件重量==1:
                        shop计费=shoplevel2
                        shop收件重量+=0.02
                    if result1[a1][0]==shop目的地:
                        shopsql1="INSERT INTO calnullshop(店铺名称,寄件人,目的地,运单号,收件重量,计费) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(shop店铺名称,shop寄件人,shop目的地,shop运单号,shop收件重量,shop计费)
                        cursor = conn.cursor()
                        cursor.execute(shopsql1)
                        cursor.connection.commit()
                        cursor.close()
    print("门店名称&寄件人明细数据已成功导入SQL")
    print("####################################################")
    special('cj.calnullshop')
    date = datetime.date.today()

    sqla="select 店铺名称,sum(计费) from cj.calnullshop  where 店铺名称 !=''  group by 店铺名称"
    cursor = conn.cursor()
    cursor.execute(sqla)
    resulta = cursor.fetchall()
    for a in range(len(resulta)):
        sqlb="INSERT INTO cj.cal VALUES('{}', '店铺', '{}', '{}')".format(resulta[a][0],resulta[a][1],date)
        cursor = conn.cursor()
        cursor.execute(sqlb)
        cursor.connection.commit()
    print("店铺结算总额数据已成功导入SQL")
    print("####################################################")

    sqlc="select 寄件人,sum(计费) from cj.calnullshop  where 店铺名称='' group by  寄件人"
    cursor = conn.cursor()
    cursor.execute(sqlc)
    resultc = cursor.fetchall()
    for b in range(len(resultc)):
        sql7="INSERT INTO cj.cal VALUES('{}', '散户', '{}', '{}')".format(resultc[b][0],resultc[b][1],date)
        cursor = conn.cursor()
        cursor.execute(sql7)
        cursor.connection.commit()
        cursor.close()
    print("散户总额数据已成功导入SQL")
    print("####################################################")



    sleep(1)
def Output():
    print("####################################################")
    print("####################################################")
    print("####################################################")
    engine = create_engine(f'mysql+pymysql://{'root'}:{'root'}@{'localhost'}/{'cj'}')
    query = f"SELECT * FROM {'calnull'}"
    df = pd.read_sql_query(query, engine)
    output_file = '新数据/AAA驿站数据明细.xlsx'
    df.to_excel(output_file, index=False)
    print(f"AAA驿站数据明细.xlsx数据已成功导出到 {output_file}")
    query1 = f"SELECT * FROM {'cal'}"
    df = pd.read_sql_query(query1, engine)
    output_file = '新数据/AAA结算总额统计.xlsx'
    df.to_excel(output_file, index=False)
    print(f"AAA结算总额统计.xlsx数据已成功导出到 {output_file}")
    query2 = f"SELECT * FROM {'calnullshop'}"
    df = pd.read_sql_query(query2, engine)
    output_file = '新数据/AAA门店名称&寄件人明细.xlsx'
    df.to_excel(output_file, index=False)
    print(f"AAA门店名称&寄件人明细.xlsx数据已成功导出到 {output_file}")



    query3 = f"SELECT * FROM {'second'}"
    df = pd.read_sql_query(query3, engine)
    output_file = '新数据/BBB面单原始表数据.xlsx'
    df.to_excel(output_file, index=False)
    print(f"BBB面单原始表数据.xlsx数据已成功导出到 {output_file}")


    query4 = f"SELECT * FROM {'calnullsecond'}"
    df = pd.read_sql_query(query4, engine)
    output_file = '新数据/BBB面单修正数据.xlsx'
    df.to_excel(output_file, index=False)
    print(f"BBB面单修正数据---数据已成功导出到 {output_file}")
    query5 = f"SELECT * FROM {'calsecond'}"
    df = pd.read_sql_query(query5, engine)
    output_file = '新数据/BBB面单结算统计.xlsx'
    df.to_excel(output_file, index=False)
    print(f"BBB面单结算统计.xlsx数据已成功导出到 {output_file}")





    sleep(1) 
def DeleteA():
    conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'cj',         # 数据库名
    )
    sql6="DELETE FROM calnull;"
    sql7="DELETE FROM cal;"
    sql8="DELETE FROM calnullshop;"
    cursor = conn.cursor()
    cursor.execute(sql6)
    cursor.connection.commit()
    cursor.execute(sql7)
    cursor.connection.commit()
    cursor.execute(sql8)
    cursor.connection.commit()
    cursor.close()
    print("####################################################")
    print("SQL修正数据已成功清空")
    sleep(1)
def DeleteAfirst():
    conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'cj',         # 数据库名
    )
    sql6="DELETE FROM first;"
    cursor = conn.cursor()
    cursor.execute(sql6)
    cursor.connection.commit()
    cursor.close()
    print("####################################################")
    print("SQL原始数据A已成功清空")
    print("####################################################")
#################################################################################3
def DeleteBsecond():
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
    print("SQL原始数据B已成功清空")
    print("####################################################")
def DeleteB():
    conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'cj',         # 数据库名
    )
    sql6="DELETE FROM calnullsecond;"
    cursor = conn.cursor()
    cursor.execute(sql6)
    cursor.connection.commit()
    cursor.close()
    sql7="DELETE FROM calsecond;"
    cursor = conn.cursor()
    cursor.execute(sql7)
    cursor.connection.commit()
    cursor.close()
    print("####################################################")
    print("calsecond已成功清空")
    print("####################################################")
    print("calnullsecond已成功清空")

def Sendshop():#计算面单数据明细
    conn = Connection(
        host = 'localhost',        # 主机名（或IP地址）
        port = 3306,               # 端口号,默认的mysql都是3306
        user = 'root',             # 用户名
        password = 'root',       # 对应用户的密码
        database = 'cj',         # 数据库名
    )
    sql="SELECT 面单发放客户, 单号, 收件扫描日期, 揽收业务员, 客户名称, 结算客户, 目的地, 结算重量, 应收运费 FROM second;"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result[1])
    shopsql="select 目的地,level1,level2,level3,level4 from priceshop "
    cursor = conn.cursor()
    cursor.execute(shopsql)
    result1 = cursor.fetchall()
    for a in range(len(result)):
                a面单发放客户=result[a][0]
                a单号=result[a][1]
                a收件扫描日期=result[a][2]
                a揽收业务员=result[a][3]
                a客户名称=result[a][4]
                a结算客户=result[a][5]
                a目的地=result[a][6]
                a结算重量=float(result[a][7])
                for a1 in range(len(result1)):
                    a应收运费=float(0.00)
                    shoplevel1=float(result1[a1][1])
                    shoplevel2=float(result1[a1][2])
                    shoplevel3=float(result1[a1][3])
                    shoplevel4=float(result1[a1][4])
                    
                    if  0<a结算重量<1:
                        a应收运费=shoplevel1
                    elif a结算重量>1 and a结算重量<2:
                        a应收运费=shoplevel2
                    elif a结算重量>2 and a结算重量<3:
                        a应收运费=shoplevel3
                    elif a结算重量>=3:
                        a应收运费=shoplevel1+shoplevel4*math.ceil(a结算重量-1)
                    elif  a结算重量==2:
                        a应收运费=shoplevel3
                        a结算重量+=0.02
                    elif a结算重量==1:
                        a应收运费=shoplevel2
                        a结算重量+=0.02
                    print("面单客户修正数据比较多，请耐心等待")
                    if result1[a1][0]==a目的地:
                        asql="INSERT INTO calnullsecond (面单发放客户, 单号, 收件扫描日期, 揽收业务员, 客户名称, 结算客户, 目的地, 结算重量, 应收运费)VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format( a面单发放客户,a单号,a收件扫描日期,  a揽收业务员,  a客户名称,  a结算客户,  a目的地,  a结算重量, round(a应收运费,3))
                        cursor = conn.cursor()
                        cursor.execute(asql)
                        cursor.connection.commit()
                        cursor.close()
    print("面单客户修正数据明细数据已成功导入SQL")
    print("####################################################")
    special('cj.calnullshop')
    date = datetime.date.today()
    bsql="select 面单发放客户,count(*),sum(应收运费) from  calnullsecond  group by 面单发放客户"
    cursor = conn.cursor()
    cursor.execute(bsql)
    resulta = cursor.fetchall()
    for a in range(len(resulta)):
        #INSERT INTO calsecond (面单发放客户, 面单总数, 总计费, 登记时间) VALUES('', '', '', '');
        sqlb="INSERT INTO calsecond (面单发放客户, 面单总数, 总计费, 登记时间) VALUES('{}', '{}', '{}', '{}')".format(resulta[a][0],resulta[a][1],resulta[a][2],date)
        cursor = conn.cursor()
        cursor.execute(sqlb)
        cursor.connection.commit()
    print("面单客户结算总额数据已成功导入SQL")
    print("####################################################")

if __name__ == '__main__':
    #########################
    #changecsv()将csv文件编码转换为UTF8
    DeleteA()#清空CALNULL,CAL,CALNULLSHOP数据表
    DeleteAfirst()#清空first数据表
    DeleteBsecond()#清空second数据表
    DeleteB()#清空second数据表
    upload_xlsx_to_mysql()#导入原始驿站+门面+散户的数据first到数据库
    upload_csv_to_mysql()#导入发件面单的second到数据库
    Yizhan()#计算驿站数据明细
    ShopPersion()#计算门店名称&寄件人数据明细
    Sendshop()#计算面单数据明细
    Output()#·输出驿站+门店+散户数据明细数据到Excel文件



