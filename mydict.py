class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

s = Dict()
s.city = 'beijing'        # 点语法设置属性
s.name = 'aaaa'           # 点语法设置属性
s['sex'] = 'man'          # 传统字典语法设置属性
print(s)
#print(s.a)

s1 = Dict(a='A',b='B',c='C')
print(s1)
print(s1['a'])         # 传统字典访问
print(s1.a)            # 点语法访问