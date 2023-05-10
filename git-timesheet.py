#!/usr/bin/env python3

# Git-timesheet v0.0.1
# Generated with GPT-4
# https://github.com/jakedowns/git-timesheet

import subprocess
from datetime import datetime, timedelta

# Parse command line arguments
import sys

if len(sys.argv) < 4:
    print("Usage: python3 script.py email start_date end_date")
    sys.exit(1)

email = sys.argv[1]
start_date = sys.argv[2]
end_date = sys.argv[3]

# Validate command line arguments
if not email:
    print("Email is required")
    sys.exit(1)
if not start_date:
    print("Start date is required (format: YYYY-MM-DD)")
    sys.exit(1)
if not end_date:
    print("End date is required (format: YYYY-MM-DD)")
    sys.exit(1)

# Convert start and end dates to datetime objects
start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

total_estimated_hours = 0

# Loop through the dates in the range and calculate total hours worked on each day
while start_datetime <= end_datetime:
    date_str = start_datetime.strftime("%Y-%m-%d")
    git_cmd = (
        f'git log --author="{email}" --since="{date_str} 00:00:00" --until="{date_str} 23:59:59" '
        '--pretty=format:"%h|%ad|%s" --date=format:"%Y-%m-%d %H:%M:%S"'
    )
    try:
        output = subprocess.check_output(git_cmd, shell=True, text=True)
    except subprocess.CalledProcessError:
        output = ""

    commits = []
    earliest_hour = None
    latest_hour = None

    for line in output.strip().split('\n'):
        commit_parts = line.split('|')
        if len(commit_parts) < 3:
            continue

        commit_hash, commit_date, commit_msg = commit_parts
        commit_time = datetime.strptime(commit_date, "%Y-%m-%d %H:%M:%S")

        commit_hour = commit_time.hour
        commit_minute = commit_time.minute

        if earliest_hour is None or (commit_hour < earliest_hour or
                                     (commit_hour == earliest_hour and commit_minute < 30)):
            earliest_hour = commit_hour
        if latest_hour is None or (commit_hour > latest_hour or
                                   (commit_hour == latest_hour and commit_minute >= 30)):
            latest_hour = commit_hour

        commits.insert(0, f"\t\t{commit_hash[:7]} {commit_time.time()} {commit_msg}\n")

    if earliest_hour is not None and latest_hour is not None:
        earliest_hour_str = f"{earliest_hour:02d}a" if earliest_hour < 12 else f"{earliest_hour-12:02d}p"
        latest_hour_str = f"{latest_hour:02d}a" if latest_hour < 12 else f"{latest_hour-12:02d}p"
        total_hours = latest_hour - earliest_hour
        if commit_minute > 0 or latest_hour == 12:
            total_hours += 1
            latest_hour_str = f"{latest_hour+1:02d}a" if latest_hour < 11 else f"{latest_hour+1-12:02d}p"
        total_estimated_hours += total_hours
        summary_line = f"{date_str} | {start_datetime.strftime('%a')} | {earliest_hour_str} - {latest_hour_str} | {total_hours}hrs"
    else:
        summary_line = f"{date_str} | {start_datetime.strftime('%a')} | --"


    print(summary_line)
    print("".join(commits))

    start_datetime += timedelta(days=1)

print(f"Total Estimated Hours: {total_estimated_hours}")
