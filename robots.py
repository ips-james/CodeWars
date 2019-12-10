robot_1 = {
    "name": "Rocky",
    "health": 100,
    "speed": 20,
    "tactics": ["punch", "punch", "laser", "missile"]
}
robot_2 = {
    "name": "Missile Bob",
    "health": 100,
    "speed": 21,
    "tactics": ["missile", "missile", "missile", "missile"]
}
tactics = {
    "punch": 20,
    "laser": 30,
    "missile": 35
}
# todo: need to cope with blank tactics / robots who have run out of tactics


def fight(robot_1, robot_2, t):
    first_robot = robot_1
    second_robot = robot_2
    if robot_1['speed'] < robot_2['speed']:
        first_robot = robot_2
        second_robot = robot_1
    round_number = 0
    while first_robot['health'] > 0 and second_robot['health'] > 0:
        action = first_robot['tactics']
        second_robot['health'] -= tactics[action[round_number//2]]
        round_number += 1
        action = second_robot['tactics']
        first_robot['health'] -= tactics[action[round_number // 2]]
        round_number += 1
    if first_robot['health'] < 0:
        return second_robot['name'] + ' has won the fight.'
    if second_robot['health'] < 0:
        return first_robot['name'] + ' has won the fight.'



print(fight(robot_1, robot_2, tactics))
