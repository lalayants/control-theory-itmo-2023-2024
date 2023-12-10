#!/usr/bin/env python3
from ev3dev.ev3 import LargeMotor
from ev3dev2.power import PowerSupply
import time
import os
import shutil

DATA_PATH = '/home/robot/data/task2_1'
if os.path.exists(DATA_PATH):
    shutil.rmtree(DATA_PATH)
os.makedirs(DATA_PATH)

volts = PowerSupply()
motorA = LargeMotor('outA')
    
KPs = [0.0025, 0.005, 0.01]
targets = [('const', lambda t: 0 * t + 1), ('linear', lambda t: 1 * t)]


def follow(target, kp, t=8):
    target_name, target_l = target
    start_time = time.time()
    start_pos = motorA.position
    file = open(f'DATA_PATH/{target_name}_{kp}.txt', "a")

    while (time.time() - start_time) < t:
        time_from_start = time.time() - start_time
        pos = motorA.position - start_pos
        target = target_l(time_from_start)
        error = target - pos
        u = kp * error
        file.write(f'{time.time() - start_time} {kp} {error}\n')
        motorA.run_direct(duty_cycle_sp=u)
    motorA.run_direct(duty_cycle_sp=0)
    

if __name__ == '__main__':
    try:
        for target in targets:
            for kp in KPs:
                print(target[0], kp)
                follow(target, kp)
                time.sleep(1)
    except Exception as e:
        raise e
    finally:
        motorA.stop(stop_action='brake')
