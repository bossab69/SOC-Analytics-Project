import re

with open('auth.log', 'r') as log:
    for line in log:
        if 'Failed password' in line:
            print(line)
