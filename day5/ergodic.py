import os

# print(os.getcwd())   ergodic
#遍历目录           普通遍历   深度遍历   广度遍历
path = '/root/PycharmProjects/darnell/venv/'
dir_sum = []
file_sum = []

def getAllDir(path, sp = '  '):
    fileList = os.listdir(path)
    #print(fileList)

    sp += '  '
    for fileName in fileList:
         fileAbsPath = os.path.join(path, fileName)


         if os.path.isdir(fileAbsPath):
             print(sp + 'dir :', fileName)

             dir_sum.append(fileName)

             getAllDir(fileAbsPath, sp)


         else :
             file_sum.append(fileName)

             print(sp + 'file:', fileName)
    # print(dir_sum, file_sum)
    sp += ' '

getAllDir(path)






#deep  ergodic   stack



# print(os.getcwd())
path = '/root/PycharmProjects/darnell/venv/python3test'

def getAllPath(path):
    stack = []
    stack.append(path)


    while len(stack) != 0:

        dirPath = stack.pop()

        fileList = os.listdir(dirPath)

        for file in fileList:
            fileAbsPath = os.path.join(dirPath, file)
            if os.path.isdir(fileAbsPath):
                print('is dir :', fileAbsPath)
                stack.append(fileAbsPath)
            else:
                print('is file: ', fileAbsPath)


getAllPath(path)



import collections
#quene定义了一个栈
#  quene    width
#print(os.getcwd())
path = r'/root/PycharmProjects/darnell/venv'

def fileAllPath2(path):
    quene = collections.deque()

    quene.append(path)

    while len(quene) != 0:
        dirPath = quene.popleft()
        fileAlldir = os.listdir(dirPath)

        for listFile in fileAlldir:
            fileAbsFile = os.path.join(path, listFile)
            if os.path.isdir(fileAbsFile):
                print('is dir :', fileAbsFile)
                quene.append(fileAbsFile)

            else:
                print('is file :', fileAbsFile)


fileAllPath2(path)
























