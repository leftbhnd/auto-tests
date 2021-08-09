#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from std_msgs.msg import Bool
from std_msgs.msg import UInt16
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
            'drive/station', Empty, latch=True, queue_size=10
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
        self._current_drive_mode = ''
        self._wheels_data = []
        # self._rwheel_data = ''
        # self._lwheel_data = ''
        self._current_point = ''
        self._drive_pause_state = True
        self._drive_station_state = False
        self._drive_status = 0
        self._charge_state = False
        '''
        переменные для Publishers
        '''
        self._joy_mode = 0
        self._auto_mode = 1

        self._timeout = 0.5

    # /drive/mode

    def autoModePub(self):
        self._pub_drive_mode.publish(self._auto_mode)
        rospy.sleep(self._timeout)

    def joyModePub(self):
        self._pub_drive_mode.publish(self._joy_mode)
        rospy.sleep(self._timeout)

    def driveModeListener(self):
        rospy.sleep(self._timeout)
        self._drive_mode_subscriber_state = True
        rospy.Subscriber(
            'drive/mode', UInt16, self._driveModeListener
        )

    def _driveModeListener(self, data):
        if self._drive_mode_subscriber_state:
            self._current_drive_mode = data.data
            self._drive_mode_subscriber_state = False

    def getDriveMode(self):
        rospy.sleep(self._timeout)
        return self._current_drive_mode

    # /drive/point

    def toPointPub(self, point):
        self._pub_to_point.publish(point)
        rospy.sleep(self._timeout)

    def pointListener(self):
        rospy.sleep(self._timeout)
        self._point_subscriber_state = True
        rospy.Subscriber(
            'drive/point', UInt16, self._pointListener
        )

    def _pointListener(self, data):
        if self._point_subscriber_state:
            self._current_point = data.data
            self._point_subscriber_state = False

    def getCurrentPoint(self):
        rospy.sleep(self._timeout)
        return self._current_point

    # /rwheel /lwheel

    def wheelsListener(self):
        rospy.sleep(self._timeout)
        self._wheels_data = []
        self._lwheel_subscriber_state = True
        self._rwheel_subscriber_state = True
        rospy.Subscriber(
            'rwheel', Int32, self._rwheelListener
        )
        rospy.Subscriber(
            'lwheel', Int32, self._lwheelListener
        )

    def _rwheelListener(self, data):
        if self._rwheel_subscriber_state:
            self._wheels_data.append(data.data)
            #self._rwheel_data = data.data
            self._rwheel_subscriber_state = False

    def _lwheelListener(self, data):
        if self._lwheel_subscriber_state:
            self._wheels_data.append(data.data)
            #self._lwheel_data = data.data
            self._lwheel_subscriber_state = False

    def getWheelsData(self):
        rospy.sleep(self._timeout)
        return self._wheels_data
        # return [self._rwheel_data, self._rwheel_data]

    # /drive/pause

    def enableDrivePausePub(self):
        self._drive_pause_state = True
        self._pub_drive_pause.publish(self._drive_pause_state)
        rospy.sleep(self._timeout)

    def disableDrivePausePub(self):
        self._drive_pause_state = False
        self._pub_drive_pause.publish(self._drive_pause_state)
        rospy.sleep(self._timeout)

    def drivePauseListener(self):
        rospy.sleep(self._timeout)
        self._drive_pause_subscriber_state = True
        rospy.Subscriber(
            'drive/pause', Bool, self._drivePauseListener
        )

    def _drivePauseListener(self, data):
        if self._drive_pause_subscriber_state:
            self._drive_pause_state = data.data
            self._drive_pause_subscriber_state = False

    def getDrivePause(self):
        rospy.sleep(self._timeout)
        return self._drive_pause_state

    # /charge/runApplication /drive/station

    def chargeAppPub(self):
        self._pub_charge_app.publish()
        rospy.sleep(self._timeout)

    def driveStationPub(self):
        self._pub_drive_station.publish(True)
        rospy.sleep(self._timeout)

    def driveStationListener(self):
        rospy.sleep(self._timeout)
        self._drive_station_subscriber_state = True
        rospy.Subscriber(
            'drive/station', Bool, self._driveStationListener
        )

    def _driveStationListener(self, data):
        if self._drive_station_subscriber_state:
            self._drive_station_state = data.data
            self._drive_pause_subscriber_state = False

    def getDriveStationStatus(self):
        rospy.sleep(self._timeout)
        return self._drive_station_state

    # /drive/status

    def driveStatusListener(self):
        rospy.sleep(self._timeout)
        self._drive_status_subscriber_state = True
        rospy.Subscriber(
            'drive/status', UInt8, self._driveStatusListener
        )

    def _driveStatusListener(self, data):
        if self._drive_status_subscriber_state:
            self._drive_status = data.data
            self._drive_status_subscriber_state = False

    def getDriveStatus(self):
        rospy.sleep(self._timeout)
        return self._drive_status

    # /charge/state

    def chargeStateListener(self):
        rospy.sleep(self._timeout)
        self._charge_state_subscriber_state = True
        rospy.Subscriber(
            'charge/state', Bool, self._chargeStateListenerCallback
        )

    def _chargeStateListenerCallback(self, data):
        if self._charge_state_subscriber_state:
            self._charge_state = data
            self._charge_state_subscriber_state = False

    def getChargeState(self):
        rospy.sleep(self._timeout)
        return self._charge_state
