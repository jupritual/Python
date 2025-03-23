def trial(t):
    return lambda z : z * t
twointo = trial(2)
threeinto = trial(3)
print(twointo(22))
print(threeinto(22))
