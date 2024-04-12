class Logger(object):
  
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Logger, cls).__new__(cls)
    return cls.instance

l1 = Logger()
l2 = Logger()
print(l1 is l2)
