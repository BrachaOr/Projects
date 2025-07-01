# coding=utf-8
import os
import shutil
import mimetypes

# יצירת תיקייה חדשה במיקום שנבחר
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# # העתקת קובץ מניתוב לניתוב
# def copy_file(sourcePath, targetPath):
#     shutil.copy(sourcePath, targetPath)
# העתקת קובץ מניתוב לניתוב
# def copy_file(file_name, path):
#     new_path = full_path(file_name)
#     shutil.copy(new_path, path)

# נתיב מלא של תיקייה
def full_path(folder_name):
    return os.path.abspath(folder_name)

# סוג הקובץ
# def type_file(file_name):
#     type, _ = mimetypes.guess_type(file_name)     # hgfffffffffffffffffffffff   ,______
#     if type:
#         print(fr"{file_name}סוג הקובץ הוא: ")
#     else:
#         type = print("לא ניתן לקבוע את סוג הקובץ הכנס סיומת של הקובץ.")
#     return type

# קבלת הניתוב המלא של הקובץ
def full_path_file(file_name):
    full_path = os.path.abspath(file_name)
    return full_path

# בדיקה האם תיקייה ריקה
def is_empty_folder(path):
    dir = os.listdir(path)
    if len(dir) == 0:
        return True
    return False

# מחיקת קובץ במיקום שנבחר
def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)

# מחיקת תיקייה חדשה במיקום שנבחר
# def delete_folder(path):
#     if os.path.exists(path):
#         if os.path.isdir(path) and not os.listdir(path):
#             os.rmdir(path)
#     else:
#         print("error")

# # כתיבת תוכן בקובץ או הוספת תוכן לקובץ קיים
# def write_in_file(f, str):
#     f.write(str)
#     f.close()

# רשימת כל הקבצים בתיקייה נתונה
# def list_files_in_folder(path):
#     return os.listdir(path)

# def copy_file(source, destination):
#     try:
#         print(f"Source: {source}, Destination: {destination}")
#         shutil.copy(source, destination)
#     except Exception as e:
#         raise ValueError('An error occurred: {}'.format(e))