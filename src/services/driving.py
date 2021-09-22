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
        subscribers
        '''
        rospy.Subscriber(
            'drive/mode', UInt16, self._driveModeListener
        )
        rospy.Subscriber(
            'drive/point', UInt16, self._pointListener
        )
        rospy.Subscriber(
            'rwheel', Int32, self._rwheelListener
        )
        rospy.Subscriber(
            'lwheel', Int32, self._lwheelListener
        )
        rospy.Subscriber(
            'drive/pause', Bool, self._drivePauseListener
        )
        rospy.Subscriber(
            'drive/station', Bool, self._driveStationListener
        )
        rospy.Subscriber(
            'drive/status', UInt8, self._driveStatusListener
        )
        rospy.Subscriber(
            'charge/state', Bool, self._chargeStateListenerCallback
        )
        '''
        переменные для геттеров
        '''
        self._current_drive_mode = 0
        self._rwheel_data = 0
        self._lwheel_data = 0
        self._current_point = 0
        self._drive_pause_state = True
        self._drive_station_state = False
        self._drive_status = 0
        self._charge_state = False

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

    def _driveModeListener(self, drive_mode):
        self._current_drive_mode = drive_mode.data

    def getDriveMode(self):
        return self._current_drive_mode

    # /drive/point
    def toPointPub(self, point):
        pointMsg = UInt16()
        pointMsg.data = point
        self._pub_to_point.publish(pointMsg)
        rospy.sleep(self._timeout)

    def _pointListener(self, point):
        self._current_point = point.data

    def getCurrentPoint(self):
        return self._current_point

    # /rwheel /lwheel
    def _rwheelListener(self, rwheel_value):
        self._rwheel_data = rwheel_value.data

    def _lwheelListener(self, lwheel_value):
        self._lwheel_data = lwheel_value.data

    def getWheelsData(self):
        return [self._rwheel_data, self._lwheel_data]

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

    def _drivePauseListener(self, pause):
        self._drive_pause_state = pause.data

    def getDrivePause(self):
        return self._drive_pause_state

    # /charge/runApplication /drive/station
    def chargeAppPub(self):
        empty_msg = Empty()
        self._pub_charge_app.publish(empty_msg)
        rospy.sleep(self._timeout)

    def driveStationPub(self):
        boolMsg = Bool()
        boolMsg.data = True
        self._pub_drive_station.publish(boolMsg)
        rospy.sleep(self._timeout)

    def _driveStationListener(self, drive_station):
        self._drive_station_state = drive_station.data

    def getDriveStationStatus(self):
        return self._drive_station_state

    # /drive/status
    def _driveStatusListener(self, drive_status):
        self._drive_status = drive_status.data

    def getDriveStatus(self):
        return self._drive_status

    # /charge/state
    def _chargeStateListenerCallback(self, charge_state):
        self._charge_state = charge_state.data

    def getChargeState(self):
        return self._charge_state

    def getUseRadius(self):
        useRadius = rospy.get_param('driving/useRadius')
        return useRadius
