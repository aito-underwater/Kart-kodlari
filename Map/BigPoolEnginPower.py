def geEnginePower(runningTime):
    enginePower = [0] * 6

    enginePower[0] = 50
    enginePower[1] = 50
    enginePower[2] = 0
    enginePower[3] = 0
    enginePower[4] = 0
    enginePower[5] = 0


    print(runningTime)
#
# if runningTime < 5:  # 1
#     enginePower[0] = 1700
#     enginePower[1] = 1300
#     enginePower[2] = 1300
#     enginePower[3] = 1700
#     enginePower[4] = 1500
#     enginePower[5] = 1500
#
# elif runningTime < 10:  # 2
#
#     enginePower[0] = 1300
#     enginePower[1] = 1700
#     enginePower[2] = 1700
#     enginePower[3] = 1300
#     enginePower[4] = 1500
#     enginePower[5] = 1500
#
# elif runningTime < 15:  # 3
#     enginePower[0] = 1700
#     enginePower[1] = 1700
#     enginePower[2] = 1700
#     enginePower[3] = 1700
#     enginePower[4] = 1500
#     enginePower[5] = 1500
#
# elif runningTime < 20:  # 4
#     enginePower[0] = 1300
#     enginePower[1] = 1300
#     enginePower[2] = 1300
#     enginePower[3] = 1300
#     enginePower[4] = 1500
#     enginePower[5] = 1500
#
# elif runningTime < 25:  # 5
#     enginePower[0] = 1700
#     enginePower[1] = 1500
#     enginePower[2] = 1500
#     enginePower[3] = 1700
#     enginePower[4] = 1500
#     enginePower[5] = 1500
#
# elif runningTime < 30:  # 6
#     enginePower[0] = 1500
#     enginePower[1] = 1700
#     enginePower[2] = 1700
#     enginePower[3] = 1500
#     enginePower[4] = 1500
#     enginePower[5] = 1500
#
# elif runningTime < 35:  # 7
#     enginePower[0] = 1300
#     enginePower[1] = 1500
#     enginePower[2] = 1500
#     enginePower[3] = 1300
#     enginePower[4] = 1500
#     enginePower[5] = 1500
#
# elif runningTime < 40:  # 8
#     enginePower[0] = 1500
#     enginePower[1] = 1300
#     enginePower[2] = 1300
#     enginePower[3] = 1500
#     enginePower[4] = 1500
#     enginePower[5] = 1500
#
# elif runningTime < 45:  # 9
#     enginePower[0] = 1500
#     enginePower[1] = 1500
#     enginePower[2] = 1500
#     enginePower[3] = 1500
#     enginePower[4] = 2000
#     enginePower[5] = 2000
#
# elif runningTime < 50:  # 10
#     enginePower[0] = 1500
#     enginePower[1] = 1500
#     enginePower[2] = 1500
#     enginePower[3] = 1500
#     enginePower[4] = 1000
#     enginePower[5] = 1000
# # else:
# #     timer = time.time()
#     runningTime = round(time.time() - timer, 2)
    return enginePower
