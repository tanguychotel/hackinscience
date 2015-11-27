def love_meet(alice, bob):
    alice2 = set(alice)
    bob2 = set(bob)
    b = [val for val in alice2 if val in bob2]
    return(b)


def affair_meet(alice, bob, silvester):
    alice2 = set(alice)
    bob2 = set(bob)
    silvester2 = set(silvester)
    c = [val for val in alice2 if val in silvester2]
    d = [val for val in c if val not in bob2]
    return(d)
