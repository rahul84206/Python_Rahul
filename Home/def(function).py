def is_there(names,query):
    for name in names:
        if query==names:
            return True

print(is_there(['Jake','Jane','Alice'],'Tom'))
