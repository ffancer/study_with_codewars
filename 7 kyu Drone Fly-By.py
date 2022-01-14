def fly_by(lamps, drone):
    a = lamps[:len(drone)]
    b = lamps[len(drone):]
    return lamps[:len(drone)], b


print(fly_by('xxxxxx', '====T'), 'ooooox')
print(fly_by('xxxxxxxxx', '==T'), 'oooxxxxxx')
print(fly_by('xxxxxxxxxxxxxxx', '=========T'), 'ooooooooooxxxxx')
