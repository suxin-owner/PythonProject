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
    
    def __str__(self):
        return "Student object (%s, %s, %s)" % (self.name, self.age, self.score)

# 序列化方法一
def student2dict(stu):
    return {
    'name': stu.name,
    'age': stu.age,
    'score': stu.score
    }

s1 = Student('Bob', 30, 88)
std1 = json.dumps(s1, default=student2dict)
print(std1)

# 序列化方法二:匿名函数写法
s2 = Student('Bob', 20, 100)
std2 = json.dumps(s2, default=lambda x : x.__dict__)
print(std2)

# 将json str 反序列化成一个对象
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
s3 = json.loads(json_str, object_hook=lambda d : Student(d['name'], d['age'], d['score']))
print(s3)