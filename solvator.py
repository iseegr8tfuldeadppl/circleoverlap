import numpy

counter = 0
laps = 0

history = []

still = True
while still:
    counter += 1/numpy.pi
    if counter >= 4*3.14:
        laps += 1
        print(laps)
        counter -= 4*numpy.pi
    #print(str(history) + '\n')
    for i in range(len(history)):
        if counter==history[i]:
            print('laps: ' + str(laps) + ' ---- ' + 'counter: ' + str(counter) + '\n' + 'history: ' + str(history))
            still = False
            break
    history.append(counter)
