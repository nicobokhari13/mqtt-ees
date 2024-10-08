# To Do

## 9-8-24 Finish everything

- try top-down approach with
- check tailwindow use in publisher.py

## 9-1-24 Finished Config Monitor and Template Config

`experiment-runner` branch
- start.py mimics `main_ees.py`, see [`main_walkthrough.md`](/vtc-f24-experiment-runners/main_walkthrough.md)
- concurrent execution via thread or process?
  - see [multiprocessing module](https://docs.python.org/3/library/multiprocessing.html)
- start.py uses flag parsing, then move execution to experiment runner
- use argparser [for flags](https://stackoverflow.com/questions/11604653/how-to-add-command-line-arguments-with-flags-in-python3)
  - not using cli-args-system : `pip3 install cli-args-system` because package manaagement not necessary with this codebase

```python
from cli_args_system import Args

#for dont try to convert the host
args = Args(convert_numbers=False)

hostname = args.flag_str('h','hostname','host')
username = args.flag_str('u','user','username','password')
password = args.flag_str('p','password')


print(f'host: {hostname}')
print(f'username: {username}')
print(f'password: {password}')
```
  
## 8-8-24 Switch to Inspiron Dev

New development laptop just droppped
- Camera ready paper is submitted -> Conference to-dos will be generated
- Clean up files in each directory
- Write Issues

## 7-25-24 Switch to Surface

Thinkpad is in the repair shop. 
**Only do vtc 2024 code, inform Song that the previous simulation and testbed code hasn't been documented or organized yet. **
Ask Song about making a GitHub organization (for the Pervasive Computing Lab )

- check paths used, update them
- survey all files, removed commented out sections
- write issues
- comment each file + purpose of structures
  - for each structure, determine functions that modify or read to it
- write README with running instructions
- write SPEC on project specification, control flow and diagrams

## 5-10-24 Friday Planning
- Read VTC draft entirely
- Consider necessary figures for intro, system workflow
- Make observation period a configurable value

## 5-9-24 Thursday Planning 
- Separate RR into 
  - max remaining battery
  - min number of tasks
- Consider system lasting time ("uptime")
  - make observation period a configurable constant
  - in code
    - change configured constant until the first instance of a device consumption > capacity
      - if this happens, change a boolean value to true
      - if this boolean is true, only save the system's consumption for the previous observation period
    - perform this for the max_batt, min_task, and random algorithms first as CC will take longer

## 5-6-24 Monday Planning
- Finished acquiring data
- Perform analysis
- Start writing paper with % of average battery consumption reduction for the system or device

## 5-4-24 Saturday Planning
- Outline areas of codebase for the following features
  - save results for a single round in the same file
  - random task allocation algorithm
- Determine number of rounds for each algorithm
- Remove all metrics csv

## Planning 
- Consider energy consumption helper to acquire the timeline of frequnecies over period T
- Publishing units should keep a frequency timeline with all frequency "timestamps" during the observation period
- Topic Container should already create a timeline from 0 - T observation period with each mulitple of frequencies in the dictionary 
- Since T = 1 hour (3,600,000 milliseconds)
  - number of sensing tasks = # frequencies
  - number of communication tasks = # effective executions = calculateExecutions()
    - consider the simple function in exact.py
- round robin tracks the order of devices for each topic, as in rotate topics in order of devices (alphabetically)
- Configurables:
  - threshold
  - smallest latency - maximum latency in milliseconds

