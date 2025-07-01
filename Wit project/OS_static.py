# coding=utf-8
import os
import shutil
import mimetypes


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def full_path(folder_name):
    return os.path.abspath(folder_name)



def full_path_file(file_name):
    full_path = os.path.abspath(file_name)
    return full_path

def is_empty_folder(path):
    dir = os.listdir(path)
    if len(dir) == 0:
        return True
    return False

def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
