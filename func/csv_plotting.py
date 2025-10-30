from datetime import datetime
from pathlib import Path
import csv

def getFiletoLines(file_name: str):
    path = Path(file_name)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"file {file_name} cannot be found.")
    else:
        return contents.splitlines() #lines

def printHeaders(file_name: str): #Debugging purposes
    lines = getFiletoLines(file_name)
    reader = csv.reader(lines)
    header_row = next(reader)

    # Checks for first ele of reader
    for index, column_header in enumerate(header_row): 
        print(index, column_header)

def captureTempsDate(file_name: str, date_index: int, index: int, index2: int = None):
    lines = getFiletoLines(file_name)
    reader = csv.reader(lines)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
            high = int(row[index])
            low = int(row[index2]) if index2 is not None else None
        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dates.append(current_date)
            highs.append(high)
            if index2 is not None:
                lows.append(low)

    if index2 is not None:
        return dates, highs, lows
    return dates, highs
