import threading
    
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    age = local_school.age
    print('Hello, %s %s (in %s)' % (std, age, threading.current_thread().name))
    print(local_school)
    print(std)

def process_thread(name, age):
    # 绑定ThreadLocal的student:
    local_school.student = name
    local_school.age = age
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice','20'), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob','30'), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
