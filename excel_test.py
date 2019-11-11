import xlrd
import xlwt
from xlutils.copy import copy

#for test
con = [['192.178.29.1','second1','third1','fourth1'],['192.178.29.1','second1','third1','fourth1'],['192.178.29.2','second2','third2','fourth2'],['192.178.29.3','second3','third3','fourth3']]

def get_group(ip):
    print(ip)
    return str(ip)
#直接写
def write_excel2(filename,contend):
    book = xlwt.Workbook()
    sheet = book.add_sheet('test') #床架名为’test‘的sheet
    row = 0
    for j in contend:     #第一次写入数据到excel表，创建表
        sheet.write(0,row,j)
        row += 1
    book.save(filename)
#追加写
def write_excel3(filename,contend):
    workbook = xlrd.open_workbook(filename)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

    for j in range(0, len(contend)):
        new_worksheet.write(rows_old, j, contend[j])  # 追加写入数据，注意是从rows_old行开始写入

    new_workbook.save(filename)  # 保存工作簿


#根据ip分组，根据组名分别写入组excel文件中
def write_ipexcel(con):
    for item in con:
        print(item[0])
        import os
        group = get_group(item[0])
        path = os.path.join(r"F:\python_pro",group + '.xls')
        if os.path.exists(path) :
            write_excel3(path, item)
        else:
            write_excel2(path, item)

#mian
if len(con):
    print('有数据')
    write_ipexcel(con) #con为从数据库中查询到的列表

else:
    print('无数据')

