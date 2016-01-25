import sys
import re

pattern = re.compile(r'^([\w+\-]+|\".*\")(\.[\w+\-]+)*@[\w]+(\.[\w]+)*$')

def formatBool(bool):
    if bool:
        return 'true'
    return 'false'

def isValidEmail(email):
    return not None == pattern.match(email)

emails = open(sys.argv[1],'r')
for email in emails:    
    if not email:
        continue
    print formatBool(isValidEmail(email))
emails.close()
