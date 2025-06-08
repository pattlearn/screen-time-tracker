import os
import time
from utils.utils import *
from utils.emailing import *

def test():
    hwnd = get_hwnd()
    title = get_active_window_title()
    print(f"title : {title}")
    pid = get_pid_from_hwnd(hwnd)
    print(f"pid : {pid}")
    process_name = get_process_name_by_pid(pid)
    print(f"process name : {process_name}")
    

if __name__ == "__main__":
    directory = "./records"
    os.makedirs(directory, exist_ok=True)
    
    # send the file via email
    date = get_date()
    if check_sending() > 0:
        folder_path = directory
        files = [file for file in os.listdir(folder_path)]
        
        for filename in files:
            date = filename.replace("record_", "").replace(".csv", "")
            send_email(filename=filename, date=date, folder_path=folder_path)
            remove_file(filename=filename)
    
    while True:
        try:
            time.sleep(1)
            
            # test()
            
            hwnd = get_hwnd()
            title = get_active_window_title()
            pid = get_pid_from_hwnd(hwnd)
            process_name = get_process_name_by_pid(pid)
            date = get_date()
            time_hms = get_time()
            
            if is_browser(process_name):
                application = "is a website"
            else:
                application = process_name
                
            log_activity_csv(date, time_hms, application, process_name, title, hwnd)
                
            print(f"date : {date}")
            print(f"time : {time_hms}")
            print(f"application : {application}")
            print(f"process_name : {process_name}")
            print(f"title : {title}")
            print(f"hwnd : {hwnd}")
            
            print("")
        
        except KeyboardInterrupt:
            print("[!]STOP MONITORING[!]")
            break