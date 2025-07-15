import os
import pickle

d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

print(os.path.abspath('.'))

print(pickle.dumps(d))

f = open('/Users/suxin/Desktop/Self/Python/PythonProject/dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('/Users/suxin/Desktop/Self/Python/PythonProject/dump.txt', 'rb')
s = pickle.load(f)
f.close()

print(f'反序列化的内容是：{s}') 


# json
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(stu):
    return {
    'name': stu.name,
    'age': stu.age,
    'score': stu.score
    }

s = Student('Bob', 30, 88)
print(json.dumps(s, default=student2dict))
