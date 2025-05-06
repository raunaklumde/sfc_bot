def save_kos_user(displayname):
    '''A function save the username of a user to be killed on sight.'''
    with open("kosusers.txt", "a", encoding="utf-8") as f:
        f.write(f"{displayname}\n")