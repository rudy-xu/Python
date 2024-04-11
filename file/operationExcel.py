# coding:utf-8

"""
xlrd
- sheet.nrows 返回总行数
- sheet.ncols 返回总列数
- sheet.get_rows() 返回每行内容列表

xlsxwriter
- xlsxwriter.Workbook()  生成 excel 对象
- add_worksheet() 添加工作簿  --------------- 值得注意得是其会删除其他已有的 sheet
- sheet.write() 书写内容
- book.close()  关闭 excel对象
"""

import xlrd
import xlsxwriter

def readExcel(path):
  execl = xlrd.open_workbook(path)

  # get sheet name
  for i in execl.sheets():
    print(i.name)

  excelContent = []
  sheet =  execl.sheet_by_index(0)
  for items in sheet.get_rows():
    content = []
    for item in items:
      content.append(item.value)
    excelContent.append(content)

  return excelContent


def writeExcel(path, content=None):
  excel = xlsxwriter.Workbook(path)
  book = excel.add_worksheet('Copy_学生手册')
  excel.add_worksheet('test')

  if content:
    for index, item in enumerate(content):
      for sub_index, sub_item in enumerate(item):
        book.write(index, sub_index, sub_item)
  else:
    print('content is null')

  excel.close()


if __name__ == "__main__":
  resFilePath = './example/study.xlsx'
  targetFilePath = './example/copy.xlsx'
  res = readExcel(resFilePath)
  print(res)
  writeExcel(targetFilePath, res)
