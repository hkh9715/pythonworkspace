# print subdir ".py" files
# os.listdir/os.path.join/os.path.splitext/os.path.isdir/try...except PermissionError
# UTF-8

# import os

# def search(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]
#                 if ext == '.py':
#                     print(full_filename)
#     except PermissionError:
#         pass
# search("Around-View-Monitoring-AVM/")


#use os.walk for more easier and simpler code

import os

for (path, dir, files) in os.walk("Around-View-Monitoring-AVM/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))