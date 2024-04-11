# coding:utf-8
import glob
import shutil

# 获取当前路径下的所有内容
# 判断 Item 类型(文件还是文件夹)
# 递归
def search(path):
  target = glob.os.path.join(path, '*')
  items = glob.glob(target)

  for item in items:
    if glob.os.path.isdir(item):
      search(item)
    else:
      print(item)
      pathList = glob.os.path.split(item)
      print(pathList)
      name = pathList[-1]
      newName = '%s_%s' % ('0', name)
      newPath = glob.os.path.join(pathList[0], newName)
      shutil.move(item, newPath)

if __name__ == '__main__':
  filePath = r'C:\learning\Python\file\example'
  search(filePath)
