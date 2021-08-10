#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from std_msgs.msg import Bool
from std_msgs.msg import UInt8
from std_msgs.msg import UInt16
from std_msgs.msg import Int32
from std_msgs.msg import Empty


class DrivingService:
    def __init__(self):
        '''
        publishers
        '''
        self._pub_drive_mode = rospy.Publisher(
            'drive/mode', UInt16, latch=True, queue_size=10
        )

        self._pub_to_point = rospy.Publisher(
            'drive/point', UInt16, latch=True, queue_size=10
        )

        self._pub_drive_pause = rospy.Publisher(
            'drive/pause', Bool, latch=True, queue_size=10
        )

        self._pub_charge_app = rospy.Publisher(
            'charge/runApplication', Empty, latch=True, queue_size=10
        )

        self._pub_drive_station = rospy.Publisher(
            'drive/station', Bool, latch=True, queue_size=10
        )
        '''
        переменные для включения subscribers 
        '''
        self._drive_mode_subscriber_state = False
        self._rwheel_subscriber_state = False
        self._lwheel_subscriber_state = False
        self._point_subscriber_state = False
        self._drive_pause_subscriber_state = False
        self._drive_station_subscriber_state = False
        self._drive_status_subscriber_state = False
        self._charge_state_subscriber_state = False

        '''
        переменные для геттеров
        '''
        self._current_drive_mode = 0
        self._wheels_data = []
        self._current_point = ''
        self._drive_pause_state = True
        self._drive_station_state = False
        self._drive_status = 0
        self._charge_state = False
        self._use_radius = rospy.get_param('driving/useRadius')

        self._timeout = 0.9

    # /drive/mode

    def autoModePub(self):
        autoMsg = UInt16()
        autoMsg.data = 1
        self._pub_drive_mode.publish(autoMsg)
        rospy.sleep(self._timeout)

    def joyModePub(self):
        joyMsg = UInt16()
        joyMsg.data = 0
        self._pub_drive_mode.publish(joyMsg)
        rospy.sleep(self._timeout)

    def driveModeListener(self):
        self._drive_mode_subscriber_state = True
        rospy.Subscriber(
            'drive/mode', UInt16, self._driveModeListener
        )
        rospy.sleep(self._timeout)

    def _driveModeListener(self, drive_mode):
        if self._drive_mode_subscriber_state:
            self._current_drive_mode = drive_mode.data
            self._drive_mode_subscriber_state = False
        rospy.sleep(self._timeout)

    def getDriveMode(self):
        rospy.sleep(self._timeout)
        return self._current_drive_mode

    # /drive/point

    def toPointPub(self, point):
        pointMsg = UInt16()
        pointMsg.data = point
        self._pub_to_point.publish(pointMsg)
        rospy.sleep(self._timeout)

    def pointListener(self):
        self._point_subscriber_state = True
        rospy.Subscriber(
            'drive/point', UInt16, self._pointListener
        )
        rospy.sleep(self._timeout)

    def _pointListener(self, point):
        if self._point_subscriber_state:
            self._current_point = point.data
            self._point_subscriber_state = False
        rospy.sleep(self._timeout)

    def getCurrentPoint(self):
        rospy.sleep(self._timeout)
        return self._current_point

    # /rwheel /lwheel

    def wheelsListener(self):
        self._wheels_data = []
        self._lwheel_subscriber_state = True
        self._rwheel_subscriber_state = True
        rospy.Subscriber(
            'rwheel', Int32, self._rwheelListener
        )
        rospy.Subscriber(
            'lwheel', Int32, self._lwheelListener
        )
        rospy.sleep(self._timeout)

    def _rwheelListener(self, rwheel_value):
        if self._rwheel_subscriber_state:
            self._wheels_data.append(rwheel_value.data)
            self._rwheel_subscriber_state = False
        rospy.sleep(self._timeout)

    def _lwheelListener(self, lwheel_value):
        if self._lwheel_subscriber_state:
            self._wheels_data.append(lwheel_value.data)
            self._lwheel_subscriber_state = False
        rospy.sleep(self._timeout)

    def getWheelsData(self):
        rospy.sleep(self._timeout)
        return self._wheels_data

    # /drive/pause

    def enableDrivePausePub(self):
        boolMsg = Bool()
        boolMsg.data = True
        self._pub_drive_pause.publish(boolMsg)
        rospy.sleep(self._timeout)

    def disableDrivePausePub(self):
        boolMsg = Bool()
        boolMsg.data = False
        self._pub_drive_pause.publish(boolMsg)
        rospy.sleep(self._timeout)

    def drivePauseListener(self):
        self._drive_pause_subscriber_state = True
        rospy.Subscriber(
            'drive/pause', Bool, self._drivePauseListener
        )
        rospy.sleep(self._timeout)

    def _drivePauseListener(self, pause):
        if self._drive_pause_subscriber_state:
            self._drive_pause_state = pause.data
            self._drive_pause_subscriber_state = False
        rospy.sleep(self._timeout)

    def getDrivePause(self):
        rospy.sleep(self._timeout)
        return self._drive_pause_state

    # /charge/runApplication /drive/station

    def chargeAppPub(self):
        empty = Empty()
        self._pub_charge_app.publish(empty)
        rospy.sleep(self._timeout)

    def driveStationPub(self):
        boolMsg = Bool()
        boolMsg.data = True
        self._pub_drive_station.publish(boolMsg)
        rospy.sleep(self._timeout)

    def driveStationListener(self):
        self._drive_station_subscriber_state = True
        rospy.Subscriber(
            'drive/station', Bool, self._driveStationListener
        )
        rospy.sleep(self._timeout)

    def _driveStationListener(self, drive_station):
        if self._drive_station_subscriber_state:
            self._drive_station_state = drive_station.data
            self._drive_pause_subscriber_state = False
        rospy.sleep(self._timeout)

    def getDriveStationStatus(self):
        rospy.sleep(self._timeout)
        return self._drive_station_state

    # /drive/status

    def driveStatusListener(self):
        self._drive_status_subscriber_state = True
        rospy.Subscriber(
            'drive/status', UInt8, self._driveStatusListener
        )
        rospy.sleep(self._timeout)

    def _driveStatusListener(self, drive_status):
        if self._drive_status_subscriber_state:
            self._drive_status = drive_status.data
            self._drive_status_subscriber_state = False
        rospy.sleep(self._timeout)

    def getDriveStatus(self):
        rospy.sleep(self._timeout)
        return self._drive_status

    # /charge/state

    def chargeStateListener(self):
        self._charge_state_subscriber_state = True
        rospy.Subscriber(
            'charge/state', Bool, self._chargeStateListenerCallback
        )
        rospy.sleep(self._timeout)

    def _chargeStateListenerCallback(self, charge_state):
        if self._charge_state_subscriber_state:
            self._charge_state = charge_state.data
            self._charge_state_subscriber_state = False
        rospy.sleep(self._timeout)

    def getChargeState(self):
        rospy.sleep(self._timeout)
        return self._charge_state

    def getUseRadius(self):
        rospy.sleep(self._timeout)
        return self._use_radius
