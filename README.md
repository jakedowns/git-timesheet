# git-timesheet
A tool to generate an estimated timesheet based on git commit history

### Usage

1. copy this script to the git repo of your choosing
2. run `python3 git-timesheet.py {name or email (no spaces!)} {start_date} {end_date}`

### Notes
1. it rounds down to the nearest hour for the first commit of the day
2. it rounds up to the nearest hour for the last commit of the day
3. Pro-Tip: copy/paste the output into ChatGPT and ask it to replace the commit messages with a summary of all work performed for each day

**Example:** `python3 git-timesheet.py jake 2023-04-24 2023-05-05`

**Output:** 
```
2023-04-24 | Mon | 00p - 06p | 6hrs
		60aafbb 12:24:25 hard-coded links
		971fc18 17:33:59 working on a fix

2023-04-25 | Tue | 09a - 04p | 7hrs
		b30cfcc 09:37:59 mounted check
		b18b72a 15:01:17 update server ip

2023-04-26 | Wed | 08a - 07p | 11hrs
		d10e130 08:26:05 fix NaN result
		6272232 18:31:42 updates

2023-04-27 | Thu | 08a - 01p | 5hrs
		185486f 08:32:54 rm
		ce89f00 09:06:54 colspan
		055fd93 12:54:20 height and drag fixes

2023-04-28 | Fri | 01p - 06p | 5hrs
		73842ee 15:04:09 add note
		2820cc1 16:34:16 update the .props object
		7b47ea7 17:07:53 fix timings

2023-04-29 | Sat | --

2023-04-30 | Sun | --

2023-05-01 | Mon | --

2023-05-02 | Tue | --

2023-05-03 | Wed | --

2023-05-04 | Thu | --

2023-05-05 | Fri | --

Total Estimated Hours: 34
```
