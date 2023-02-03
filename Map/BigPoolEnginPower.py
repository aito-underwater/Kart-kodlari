import time
def geEnginePower(runningTime, ):
    enginePower = [0] * 6

    enginePower[0] = 10
    enginePower[1] = 10
    enginePower[2] = 10
    enginePower[3] = 10
    enginePower[4] = 10
    enginePower[5] = 10


    print(runningTime)


    if runningTime < 5:  # 1
        enginePower[0] = 75
        enginePower[1] = -25
        enginePower[2] = -25
        enginePower[3] = 75
        enginePower[4] = 0
        enginePower[5] = 0

    elif runningTime < 10:  # 2

        enginePower[0] = -25
        enginePower[1] = 75
        enginePower[2] = 75
        enginePower[3] = -25
        enginePower[4] = 0
        enginePower[5] = 0

    elif runningTime < 15:  # 3
        enginePower[0] = 75
        enginePower[1] = 75
        enginePower[2] = 75
        enginePower[3] = 75
        enginePower[4] = 0
        enginePower[5] = 0

    elif runningTime < 20:  # 4
        enginePower[0] = -25
        enginePower[1] = -25
        enginePower[2] = -25
        enginePower[3] = -25
        enginePower[4] = 0
        enginePower[5] = 0

    elif runningTime < 25:  # 5
        enginePower[0] = 75
        enginePower[1] = 0
        enginePower[2] = 0
        enginePower[3] = 75
        enginePower[4] = 0
        enginePower[5] = 0

    elif runningTime < 30:  # 6
        enginePower[0] = 0
        enginePower[1] = 75
        enginePower[2] = 75
        enginePower[3] = 0
        enginePower[4] = 0
        enginePower[5] = 0

    elif runningTime < 35:  # 7
        enginePower[0] = -25
        enginePower[1] = 0
        enginePower[2] = 0
        enginePower[3] = -25
        enginePower[4] = 0
        enginePower[5] = 0

    elif runningTime < 40:  # 8
        enginePower[0] = 0
        enginePower[1] = -25
        enginePower[2] = -25
        enginePower[3] = 0
        enginePower[4] = 0
        enginePower[5] = 0

    elif runningTime < 45:  # 9
        enginePower[0] = 0
        enginePower[1] = 0
        enginePower[2] = 0
        enginePower[3] = 0
        enginePower[4] = 100
        enginePower[5] = 100

    elif runningTime < 50:  # 10
        enginePower[0] = 0
        enginePower[1] = 0
        enginePower[2] = 0
        enginePower[3] = 0
        enginePower[4] = -100
        enginePower[5] = -100
    else:
        timer = time.time()
        runningTime = round(time.time() - timer, 2)
        return enginePower
