

#在想要持久化的一些数据，可以使用pkile模块，相当于把内容写入了磁盘中  dump   load
def storeTree(inputTree, fielname):
  import pickle
  # 写文件时，注明 'wb'
  fw = open(fielname, 'wb')
  pickle.dump(inputTree, fw)
  fw.close()

def grabTree(filename):
  import pickle
   # 读文件时，注明 'rb'

  fr = open(filename, 'rb')
  return pickle.load(fr)

myTree = 'fjsb'

storeTree(myTree, 'r.txt')
print(grabTree('r.txt'))

# import pickle
# a = pickle.format_version
# print(pickle.compatible_formats)
# print(a)



















