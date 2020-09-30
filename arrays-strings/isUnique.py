def isUniqueChars(s :str)->bool:
    #my solution
    charDict = {}
    for char in s:
        if char in charDict:
            return False
        else:
            charDict[char]=True
    return True

# def isUniqueChars_ctci(s: str)->bool:



print(isUniqueChars("hb 627jh=j ()"))


