#!/usr/bin/env python3
from ev3dev.ev3 import LargeMotor
from ev3dev2.power import PowerSupply
import time
import os
import shutil


DATA_PATH = '/home/robot/data/task1'
if os.path.exists(DATA_PATH):
    shutil.rmtree(DATA_PATH)
os.makedirs(DATA_PATH)


volts = PowerSupply()
motorA = LargeMotor('outA')

def step_response(U, t=4):
    start_time = time.time()
    start_pos = motorA.position
    motorA.run_direct(duty_cycle_sp=U)
    file = open(f'{DATA_PATH}/{U}.txt', "a")
    while (time.time() - start_time) < t:
        file.write(f'{time.time() - start_time} {motorA.position - start_pos} {motorA.speed} {U} {volts.measured_volts}\n')
    motorA.run_direct(duty_cycle_sp=0)
    file.close()
    
    
if __name__ == '__main__':
    try:
        for i in range(-5, 6, 1):
            if i == 0:
                continue
            
            U = i * 20
            step_response(U)
    except Exception as e:
        raise e
    finally:
        motorA.stop(stop_action='brake')
        