#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        self._width =  value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        self._height =  value
    
    @property
    def resolution(self):
        return self._height * self._width

s = Screen()
s._height = 1024
s._width = 768
print(s.resolution)
