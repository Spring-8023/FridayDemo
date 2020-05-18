class People:
  country='China'
  def __init__(self,name):
    self.name=name
  def people_info(self):
    print('%s is xxx' %(self.name))
obj=People('aaa')
print(hasattr(People,'country'))
#返回值：True
print('country' in People.__dict__)
#返回值：True
print(hasattr(obj,'people_info'))
#返回值：True
print(People.__dict__)
##{'__module__': '__main__', 'country': 'China', '__init__': <function People.__init__ at 0x1006d5620>, 'people_info': <function People.people_info at 0x10205d1e0>, '__dict__': <attribute '__dict__' of 'People' objects>, '__weakref__': <attribute '__weakref__' of 'People' objects>, '__doc__': None}