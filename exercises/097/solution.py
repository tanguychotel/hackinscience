def love_meet(alice, bob):
    alice2 = set(alice)
    bob2 = set(bob)
    return(bob2).intersection(alice)


def affair_meet(alice, bob, silvester):
    alice2 = set(alice)
    bob2 = set(bob)
    silvester2 = set(silvester)
    c = (silvester2).intersection(alice2)
    d = [val for val in c if val not in bob2]
    D = set(d)
    return(D)
