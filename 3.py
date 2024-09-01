# Callable objects
'''
class Callable:
    def __call__(self, *args, **kwargs):
        print("__call__ method is called")

obj = Callable()
obj()
'''
#----------------------------------------------
# Iterable
'''
numbers = [2, 5, 8]   # iterable
iterator1 = iter(numbers)   # iterator
print(next(iterator1))   # 2
print(next(iterator1))   # 5
#next(iterator1)   # 8
#next(iterator1)   # error:
'''
'''
class Repeat:
    def __init__(self, msg):
        self.msg = msg
        
    def __iter__(self):
        return self
        
    def __next__(self):
        return self.msg
    
obj = Repeat("car")
for message in obj:
    print(message)
'''
'''
#the last piece of code means the same as
obj_iterator = obj.__iter__() #create iterable from obj
while True:
    message = obj_iterator.__next__()
    print(message)
  '''    
#--------------------------------------------------
'''
class FiniteRepeat:
    def __init__(self, msg, max_count):
        self.msg = msg
        self.max_count = max_count
        self.count = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        return self.msg
    
obj = FiniteRepeat("car", 5)
for message in obj:
    print(message)
    '''
# the same
'''
obj = FiniteRepeat("car", 5)
obj_iterator = iter(obj)
while True:
  try:
    message = next(obj_iterator)
  except StopIteration:
    break
  print(message)'''
#------------------------------------------------
#Context manager
class ContextManager:
    def __init__(self):
        print('__init__ method called')
        
    def __enter__(self):
        print('__enter__ method called')
        return self
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
            print('__exit___ method called')

#with ContextManager() as manager:
#    print('inside with statement block')

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        
with FileManager('data.txt', 'w') as f:
    f.write("First Line\n")
    f.write("Second Line")