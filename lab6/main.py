# ex1
# import os
# import sys
# import re
#
#
# def ex1(directory, extension):
#     if re.match(r'^\.[a-zA-Z0-9]+$', extension) is None:
#         raise Exception("Extension is not valid")
#
#     try:
#         if not os.path.isdir(directory):
#             raise NotADirectoryError("Invalid directory path")
#
#         if not os.access(directory, os.R_OK):
#             raise PermissionError("No read permissions for directory")
#
#         files = [file for file in os.listdir(directory) if file.endswith(extension)]
#
#         if not files:
#             raise FileNotFoundError(f"No files with '{extension}' extension found in '{directory}'")
#
#         for file_name in files:
#             file_path = os.path.join(directory, file_name)
#             try:
#                 with open(file_path, 'r') as file:
#                     print(f"File: {file_name}:")
#                     print(file.read())
#             except FileNotFoundError:
#                 print(f"File '{file_name}' not found.")
#             except IOError as e:
#                 print(f"Error reading '{file_name}': {e}")
#
#     except FileNotFoundError as e:
#         print(e)
#     except ValueError as e:
#         print(e)
#     except Exception as e:
#         print(e)
#
#
# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         raise Exception("Wrong number of parameters")
#     else:
#         _dir = sys.argv[1]
#         _ext = sys.argv[2]
#         ex1(_dir, _ext)


# ex2
# import os
#
#
# def ex2(directory):
#     try:
#         if not os.path.isdir(directory):
#             raise NotADirectoryError("Invalid directory path")
#
#         if not os.access(directory, os.R_OK):
#             raise PermissionError("No read permissions for directory")
#
#         files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
#
#         if not files:
#             raise FileNotFoundError(f"No files found in '{directory}'")
#
#         for index, file_name in enumerate(files, start=1):
#             file_path = os.path.join(directory, file_name)
#             new_file_name = f"file{index}.{file_name.split('.')[-1]}"
#             new_file_path = os.path.join(directory, new_file_name)
#
#             try:
#                 os.rename(file_path, new_file_path)
#             except OSError as e:
#                 print(f"Error renaming '{file_name}': {e}")
#
#     except FileNotFoundError as e:
#         print(e)
#     except Exception as e:
#         print(e)
#
#
# if __name__ == "__main__":
#     _dir = input("Directory: ")
#     ex2(_dir)


# ex3
# import os
# import sys
#
#
# def ex3(directory):
#     total_size = 0
#     try:
#         if not os.path.exists(directory):
#             raise NotADirectoryError("Invalid directory path")
#
#         if not os.access(directory, os.R_OK):
#             raise PermissionError("No read permissions for directory")
#
#         for root, dirs, files in os.walk(directory):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 try:
#                     size = os.path.getsize(file_path)
#                     total_size += size
#                 except OSError as e:
#                     print(f"Error accessing file '{file_path}': {e}")
#
#         print(f"Total size: {total_size} bytes")
#     except Exception as e:
#         print(e)
#
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Wrong number of parameters")
#     else:
#         _dir = sys.argv[1]
#         ex3(_dir)


# ex4
# import os
# import sys
#
#
# def ex4(directory):
#     try:
#         if not os.path.exists(directory):
#             raise NotADirectoryError("Directory not found")
#
#         if not os.access(directory, os.R_OK):
#             raise PermissionError("No read permissions for directory")
#
#         files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
#
#         if not files:
#             print(f"No files found in '{directory}'")
#         else:
#             ext = {}
#             for file_name in files:
#                 file_ext = os.path.splitext(file_name)[1]
#                 if file_ext not in ext:
#                     ext[file_ext] = 1
#                 else:
#                     ext[file_ext] += 1
#
#             print("Number of files by extension:")
#             for extension, count in ext.items():
#                 print(f"{extension}: {count}")
#
#     except FileNotFoundError as e:
#         print(e)
#     except PermissionError as e:
#         print(e)
#     except Exception as e:
#         print(e)
#
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Wrong number of parameters")
#     else:
#         _dir = sys.argv[1]
#         ex4(_dir)
