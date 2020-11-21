
# with open('notes.txt', 'w') as file:
#     file.write('sometodo...')
#
# file = open('notes.txt','w')
# try:
#     file.write('some to do.....')
# finally:
#     file.close()


# from threading import Lock
# lock = Lock()
#
# lock.acquire()
# #....
# lock.release()
#
# with lock:
#     #......



#
# class ManagedFile:
#     def __init__(self,filename):
#         print('init')
#         self.filename = filename
#
#     def __enter__(self):
#         print('enter')
#         self.file = open(self.filename, 'w')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#         if exc_type is not None:
#             print('exception has been handled')
#         #print('exec:', exc_type, exc_val)
#         print('exit')
#         return True
#
#
# with ManagedFile('notes.txt') as file:
#     print('do some stuff...')
#     file.write('some todooo....')
#     file.somemethod()
# print('continuing')



from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('Some todooooooo..........')
    



# Have to spend more time here and multiprocessing, logging as not clear whats happening