def save_ally_factions(fac_name, invitelink):
    '''Saves the faction name and invite link to a text file.'''
    with open("allied_factions.txt", "a", encoding="utf-8") as f:
        f.write(f"{fac_name} | {invitelink}\n")
