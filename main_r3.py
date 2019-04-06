#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "Rishav Rajendra, Benji Lee"
__license__ = "MIT"
__status__ = "Development"

import cv2
import numpy as np
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
from constants import fwd, rev, BUTTONPIN, LEDPIN, CONTACT_PIN
from get_stats_from_image import get_data, get_midpoint, mothership_angle, corrected_angle
from targetApproach import approach, check_pick_up
from mothership_commands import map_mothership, approach_mothership_side, mothership_drop
from nav.gridMovement import GridMovement
from misc import wait_for_button, get_sensor_data, align_corner, map, follow_path, \
begin_round, go_home, back_dat_ass_up, map_JSON, closest_point, kill_block
from nav.grid import Grid
import queue, threading, serial, time, math
from datetime import datetime
from video_thread import VideoThread

import sys
sys.path.append("../tensorflow_duckling/models/research/object_detection/")
from image_processing import Model

import warnings
warnings.filterwarnings('ignore')

def main():
    # Initialize frame rate calculation
    frame_rate_calc = 1
    freq = cv2.getTickFrequency()
    font = cv2.FONT_HERSHEY_SIMPLEX

    objectifier = Model()

    # Start serial connection to arduino
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
    time.sleep(1)

    # Initialize queues
    pic_q = queue.LifoQueue(5)
    command_q = queue.Queue()
    # Inizialize grid anf gridmovement
    grid = Grid(8,8)
    movement = GridMovement(grid, ser)
    # Initialize VideoThread
    vt = VideoThread(pic_q, objectifier)
    vt.start()
    
    # Setup GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTONPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(CONTACT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LEDPIN, GPIO.OUT, initial=GPIO.LOW)
    
    # Keep track of movements after approach is called
    approach_movement_list = queue.LifoQueue()

    wait_for_button(GPIO)
    time.sleep(5)
    
    print("Starting round")
    
    # map the targets from json file
    map_JSON(mars1.json,movement)
    # now set the maximum amount of obstacles based on amount of targets 
    # grid.set_obstacles_max()
    
    # begin_round(movement, pic_q)

    print("I will try and map the mothership")
    # MOTHERSHIP
    grid.mothership.extend([(),(),(),()])
    movement.set_access_point(())
    # SIDE POINT
    movement.set_side_point(())
    #OBSTACLES
    grid.obstacles.extend([])
    # map_mothership(movement, pic_q)
    print("Mothership is located in the following tiles: ", grid.mothership)

    # We can save these values in movement.access_point so other functions with access to movement
    # can use these
    mothership_angle, dist, side_angle = approach_mothership_side(movement, pic_q, ser, GPIO)
    movement.set_mothership_angle(mothership_angle)
    movement.set_side_angle(side_angle)
    movement.set_access_dist(dist)

    print("Mothership angle: {}, Distance: {}, Side_angle: {}".format(mothership_angle, dist, side_angle))

    print("Going home")
    # go_home(movement, pic_q)
    """
    # pick up and drop blocks
    for target in len(grid.targets):
        movement.current_target = target
        # movement.current_target = closest_point(grid.targets, movement.current)
        movement.set_goal(movement.current_target)
        follow_path(movement, pic_q)
        approach(movement, pic_q)
        checks = check_pick_up(movement, pic_q)
        if checks[0]:
            targetId = checks[1]
            movement.move(fwd, 4)
            movement.drop()
            movement.move(rev, 4)
            # grid.targets.remove(movement.current_target)
            # kill_block(movement, pic_q)
        else:
            approach(movement, pic_q)
            checks = check_pick_up(movement, pic_q)
                if checks[0]:
                    targetId = checks[1]
                    movement.move(fwd, 4)
                    movement.drop()
                    movement.move(rev, 4)
                    # grid.targets.remove(movement.current)
                    # kill_block(movement, pic_q)
        if not checks[0]:
            movement.drop()

        back_dat_ass_up(movement, pic_q)
        go_home(movement,pic_q)
    """
    # now try to map mothership and drop blocks
    # map_mothership(movement, pic_q)
    # if not grid.mothership:
    #     map_mothership(movement, pic_q)
    # if not grid.mothership:
    #     go_home(movement, pic_q)
    #     wait_for_button(GPIO)
    # else:
    while grid.targets:
        movement.current_target = closest_point(grid.targets, movement.current)
        movement.set_goal(movement.current_target)
        follow_path(movement, pic_q,False,False)
        approach(movement, pic_q)
        checks = check_pick_up(movement, pic_q)
        if checks[0]:
            targetId = checks[1]
            grid.targets.remove(movement.current_target)
        else:
            approach(movement, pic_q)
            checks = check_pick_up(movement, pic_q)
                if checks[0]:
                    targetId = checks[1]
                    grid.targets.remove(movement.current_target)
        back_dat_ass_up(movement, pic_q)
        if not checks[0]:
            go_home(movement, pic_q)
        else:
            movement.set_goal(movement.get_access_point())
            follow_path(movement, pic_q, True, False)
            movement.face(movement.get_side_point())
            mothership_drop(dist, mothership_angle, side_angle, block_id, movement, serial, pic_q)
            go_home(movement, pic_q)


    
    print("Round over")
    wait_for_button(GPIO)
        
    """
    targs = [(4,7), (4, 0)]
    for item in targs:
        movement.set_goal(item)
        follow_path(movement, pic_q)
        approach(movement, pic_q)
        success, target_id = check_pick_up(movement, pic_q)
        print("Success: {}, Target Id: {}".format(success, target_id))
        back_dat_ass_up(movement, pic_q)
        go_home(movement, pic_q)
        
        print("Access point is: ",movement.get_access_point())
        movement.set_goal(movement.get_access_point())
        follow_path(movement, pic_q, True)
        movement.face(movement.get_side_point())
        
        block_id = 2
        
        print("Going to drop it")
        mothership_drop(dist, mothership_angle, side_angle, block_id, movement, ser, pic_q, GPIO)
        go_home(movement, pic_q)
    """
    vt.join()
    #camera.close()

if __name__ == '__main__':
    main()