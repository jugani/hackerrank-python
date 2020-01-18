import re
def fun(s):
    # return True if s is a valid email, else return False
    if (s.find('@') == -1 or s.find('.') == -1):
        return False
    if (s.count('@') > 1 or s.count('.') > 1):
        return False    
    [username, website] = s.split('@')    
    if len(username) == 0 or len(website) == 0:
        return False
    [websitename, extn] = website.split('.')
    if not re.match("^[A-Za-z0-9_-]*$", username):
        return False
    if not websitename.isalnum():
        return False
    if len(extn) > 3:
        return False

    return True        




def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)