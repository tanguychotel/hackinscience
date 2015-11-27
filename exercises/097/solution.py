def love_meet(alice, bob):
    alice2 = set(alice)
    bob2 = set(bob)
    b = [val for val in alice2 if val in bob2]
    return(b)
