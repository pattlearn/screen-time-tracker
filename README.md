# ScreenTime Tracker

A simple Python-based screen time monitoring tool that logs the active window's title, process name, and timestamp to a CSV file. Useful for tracking productivity or usage patterns over time.

## Features

- Logs the title of the currently focused window.
- Identifies the associated process name and PID.
- Differentiates web browsers from other applications.
- Records data to a CSV file (`record.csv`) with the following fields:
  - `date`
  - `time`
  - `application`
  - `process_name`
  - `title`
  - `hwnd` (window handle)

## Usage

### Prerequisites

- Python

### Installation

Clone this repository:

```bash
git clone https://github.com/Rattanapatt/screentime-tracker-public.git
cd screentime-tracker-public
```

### To Run

Run the script

```bash
py main.py
```

Or

```bash
python main.py
```
