def save_faction_name(name):
    '''A function to save the username of an enemy faction, which is then stored in a text file called 'factions.txt'.'''
    with open("factions.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}\n")