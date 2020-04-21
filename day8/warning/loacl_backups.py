import os, sys, time, ast


def backup(file_content):
    #path  = r'/root/PycharmProjects/darnell/venv/python3test/day8/'
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    file_name = now + r'.txt'
    f1 = open(file_name, 'w')
    f1.close()
    #file_absName = os.path.join(path, file_name)


    with open(file_name, mode='a+', encoding='utf-8') as f:

        #info_dict = ast.literal_eval(file_content)
        for d, v in file_content.items():
            #f.write("%s : %s " % (d , file_content[d]))

            f.write(str(d) + '\n')
            f.write(str(v) + '\n')

    f2 = open(file_name, 'r')
    fileAllContent = f2.read()
    f2.close()

    pathabs = os.path.join(os.getcwd(), file_name)
    #return fileAllContent
    return pathabs






