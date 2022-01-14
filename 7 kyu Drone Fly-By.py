def fly_by(lamps, drone):
    return lamps[:len(drone)].replace('x', 'o') + lamps[len(drone):]


print(fly_by('xxxxxx', '====T'), 'ooooox')
print(fly_by('xxxxxxxxx', '==T'), 'oooxxxxxx')
print(fly_by('xxxxxxxxxxxxxxx', '=========T'), 'ooooooooooxxxxx')
