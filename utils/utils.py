import ctypes
import ctypes.wintypes
import subprocess
from datetime import datetime
import os
import csv

def get_hwnd():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    return hwnd

def get_date():
    date = datetime.now().strftime("%Y-%m-%d")
    return date

def get_time():
    time_hms = datetime.now().strftime("%H:%M:%S")
    return time_hms

def get_active_window_title():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
    
    return buff.value

def get_pid_from_hwnd(hwnd):
    pid = ctypes.wintypes.DWORD()
    ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    
    return pid.value

def get_process_name_by_pid(pid):
    try:
        output = subprocess.check_output(f'tasklist /FI "pid eq {pid}"', shell=True)
        lines = output.decode(errors="ignore").splitlines()
        # print("ouput", output)
        # print("lines", lines)
        
        if len(lines) >= 4:
            # print("return", lines[3].split()[0])
            return lines[3].split()[0]
        return "Unknown"
    except Exception as e:
        return f"Error: {e}"
    
def is_browser(process_name):
    browser = ["chrome.exe", "msedge.exe", "firefox.exe"]
    return process_name.lower() in browser

def extract_website_from_title(title):
    title = title.split(" - ")
    
    # if " - " in title:
    #     site = title.split(" - ")[0]
    #     return site.strip()
    # return title.strip()
    
def log_activity_csv(date, time_hms, application, process, title, hwnd):
    file_exists = os.path.isfile(f"./records/record_{date}.csv")
    
    with open(f"./records/record_{date}.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(["date", "time", "application", "process_name", "title", "hwnd"])
            
        writer.writerow([date, time_hms, application, process, title, hwnd])

if __name__ == "__main__":
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    title = get_active_window_title()
    pid = get_pid_from_hwnd(hwnd)

    # print("hwnd", hwnd)
    # print("pid", pid)    
    get_process_name_by_pid(pid)