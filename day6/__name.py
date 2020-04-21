
#import argv

#   if __name__ == '__main__':


import os, sys

path = '/root/PycharmProjects/darnell/venv/python3test'

def work(filepath):
    newPath = r'/root/PycharmProjects/darnell/venv/python3test/day6'
    with open(filepath) as f:
        lineAllInfo = f.readlines()
        for lineInfo in lineAllInfo:

            mailStr = lineInfo.split('.')[0]
            dirstr = lineInfo.split('@')[1].split('.')[0]

            dirstrAbsPath = os.path.join(newPath, dirstr)
            if not os.path.exists(dirstrAbsPath):
                os.mkdir(dirstrAbsPath)
                newFilePath = os.path.join(dirstrAbsPath, dirstr + '.txt')
                with open(newFilePath, 'a') as f1:
                    f1.write(mailStr + '\n')

        else:
            pass


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
                work(fileAbsPath)



if __name__ == '__main__':
    getAllPath(path)
else:
    pass







