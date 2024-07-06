import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\Dell\Pictures\Screenshots"
destination_dir = r"C:\Users\Dell\Desktop\AUTOMATION PROJECTS"

def copy_folder_to_dir(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")


schedule.every().day.at("19:30").do(lambda: copy_folder_to_dir(source_dir, destination_dir))

while True:
   schedule.run_pending()
   time.sleep(60)