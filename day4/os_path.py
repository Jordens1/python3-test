import os


print(__file__)
path = '/root/PycharmProjects/darnell/venv/python3test/day3/b.txt'


print(os.uname())
print(os.getcwd())
# print(os.getenv('PATH'))
print(os.environ)
# print(os.listdir(path))
print('#',os.linesep,'#')
print(os.name)

print("#####################")
print(os.path.split(path))

print(os.path.isdir(path))
# os.chdir(os.join(os.path.split(path)[0],r.txt))
print(os.getcwd())

print(os.path.abspath('fbdgvjyk j.txt'))
# print(os.path.abspath())

print(os.path.join('/opt', 'cacert.pem'))

print(os.path.basename(path))
print(os.path.dirname(path))

print(os.path.splitext(path))


print(os.stat(path))
