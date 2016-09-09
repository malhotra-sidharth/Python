# Windows Webpage Blocker v1.0
# @author Sidharth Malhotra
# @date September 9, 2016
# @modified September 9, 2016
# @usage ################
# This script can be used to block a certain
# list of websites for a certain time span after which
# the blocked sites will be available for use.
# ***The current scipt modifies the 'hosts' file of Windows TCP/IP
# therefore it requires 'ADMINISTRATOR ACCESS' to perform
# the desired functions
# ***This script requires Python 3+ installed


#imports
import time
from datetime import datetime as dt

#hosts path in windows
path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'

#Redirect path
redirect = '127.0.0.1'

#Websites List
# Add the list of websites to be blocked below
websitesList = ['facebook.com',
                'www.facebook.com',
                'google.com',
                'www.google.com']

# Start hours in 24 hours clock
start_hours = 8              # change the time as per the requirements

#End hours in 24 hours clock
end_hours = 16               # change the time as per the requirements

#Process Starts
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_hours) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hours):
        # Opening the hosts file
        with open(path, 'r+') as file:
            content = file.read()
            for webpage in websitesList: # Iterate over the website list
                if webpage in content: # Check if website already blocked
                    pass
                else:
                    file.write('\n' + redirect + ' ' + webpage + '\n')
    else:
        # Open file and Check if sites exist
        with open(path, 'r+') as file:
            contentList = file.readlines() # Each line stored in contentList variable <list>
            file.seek(0)
            for line in contentList:
                if not any(webpage in line for webpage in websitesList): # Check if any website from the websites list is in the current line of content
                    file.write(line)
            file.truncate()

    #Check time every 5 seconds
    time.sleep(5)
