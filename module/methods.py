def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False