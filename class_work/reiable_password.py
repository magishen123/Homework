password = input('>>>')
def check(password):
    counte = len(password)
    opushenie = password.lower()
    if counte > 8 and password != opushenie:
        return True
    else:
        return False

print(check(password))