# coding=utf-8

from OS_static import *
from Commit_version import *
from datetime import datetime
import os
import shutil
import json


class Repository:
    def __init__(self):
        self.current_path = os.getcwd()
        self.dictionary = {}


    def wit_init(self):
        if os.path.exists(self.current_path+"\.wit"):
            print("Repository already exist.")
        else:
            create_folder(self.current_path+"\.wit)")
            create_folder(self.current_path+"\.wit\stage")
            create_folder(self.current_path+"\.wit\commit")
            print("Repository created successfully.")


    def wit_add(self, file_name):
        destination_directory = self.current_path+"\.wit\stage"  # ניתוב קבוע לתיקייה היעד
        try:
            # בודק אם הקובץ קיים
            if os.path.isfile(file_name):
                destination_path = os.path.join(destination_directory, file_name)
                shutil.copy(file_name, destination_path)
                print("File copied to"+ destination_path)
            else:
                return "File does not exist."
        except Exception as e:
            return str(e)



    def wit_commit(self, message):
        source_directory = self.current_path+"\.wit\stage"
        target_directory =self.current_path+"\.wit\commit"

        if os.path.exists(self.current_path+"\.wit\commit_data.json"):
            with open(self.current_path+"\.wit\commit_data.json", 'r') as json_file:
                self.dictionary = json.load(json_file)
        else:
            self.dictionary = {}

        if not is_empty_folder(source_directory):
            new_directory = os.path.join(target_directory, message)
            os.makedirs(new_directory, exist_ok=True)

            for file_name in os.listdir(source_directory):
                source_file = os.path.join(source_directory, file_name)
                if os.path.isfile(source_file):
                    target_file = os.path.join(new_directory, file_name)
                    shutil.move(source_file, target_file)  

            version_object = Commit_version(str(hash(message)), datetime.now(), message)

            self.dictionary[version_object.hash_code] = {
                'hash_code': version_object.hash_code,
                'date': str(version_object.date),  
                'message': version_object.message
            }

            with open(self.current_path+"\.wit\commit_data.json", 'w') as json_file:
                json.dump(self.dictionary, json_file, ensure_ascii=False, indent=4)

            print("Committed successfully")


    def wit_log(self):
        if not self.dictionary:
            print("no commits found.")
            return
        for hash_code, version_info in self.dictionary.items():
            print("Hash:" +hash_code+", Date:"+ version_info['date']+", Message:" + version_info['message'])


    def wit_status(self):
        if is_empty_folder(self.current_path+"\.wit\stage"):
            print("There are no uncommitted changes.")
        else:
            print("There are changes that have not been committed.")

    def wit_checkout(self, commit_id):
        if os.path.exists(self.current_path + "\.wit\commit_data.json"):
            with open(self.current_path+"\.wit\commit_data.json", 'r') as json_file:
                self.dictionary = json.load(json_file)
        else:
            print("No commit data found.")
            return
        if commit_id not in self.dictionary:
            print("Commit ID not found.")
            return
        commit_info = self.dictionary[commit_id]
        commit_directory = os.path.join(self.current_path, '.wit', 'commit', commit_info['message'])
        if not os.path.exists(commit_directory):
            print("No files found for this commit.")
            return
        shutil.rmtree(self.current_path+"\.wit\stage", ignore_errors=True)
        os.makedirs(self.current_path+"\.wit\stage", exist_ok=True)
        for file_name in os.listdir(commit_directory):
            source_file = os.path.join(commit_directory, file_name)
            destination_file = os.path.join(self.current_path+"\.wit\stage", file_name)
            shutil.copy(source_file, destination_file)  
        print("Checked out to commit" +commit_id+ "successfully.")

