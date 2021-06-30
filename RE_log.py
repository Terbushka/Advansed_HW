import re
import os

if os.path.exists('Incognito.log'):
    os.remove('Incognito.log')
with open('django-success.log', 'r') as logfile:
    while True:
        line = logfile.readline()
        if not line:
            break
        line = re.sub(r'\[\d*\/\w*\/\d*\s(\d{2}:?){3}\]', '[XX/XXX/XXXX XX:XX:XX]', line)

        line = re.sub(r'\/admin\/', '/****/', line)

        with open('Incognito.log', 'a') as file:
            file.write(line)