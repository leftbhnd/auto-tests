#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import time

from promobot_msgs.msg import ASRResult
from promobot_msgs.msg import Answer
from promobot_msgs.msg import FaceArray
from promobot_msgs.msg import Face
from promobot_msgs.msg import FaceScore
from promobot_msgs.msg import TTSCommand
from promobot_msgs.msg import Interaction
from promobot_msgs.msg import ScriptProcess
from promobot_msgs.msg import ServoStates
from sensor_msgs.msg import Joy
from std_msgs.msg import Empty
from std_msgs.msg import UInt16
from std_msgs.msg import UInt8
from std_msgs.msg import Bool
from std_msgs.msg import String
from std_msgs.msg import Empty
from std_msgs.msg import Int32


class AutoTest:
    def __init__(self):
        '''
        publishers&subscribers для asr / tts
        '''
        rospy.Subscriber(
            'answers/answer', Answer, self._answersListenerCallback
        )
        self._pub_text_to_asr = rospy.Publisher(
            'asr/result', ASRResult, queue_size=10
        )
        self._pub_text_to_tts = rospy.Publisher(
            'tts/start', TTSCommand, queue_size=10
        )
        self._pub_cancel_speech = rospy.Publisher(
            'tts/cancel', Empty, queue_size=10
        )
        '''
        publishers&subscribers для faceRecognize
        '''
        self._pub_face_to_faceArray = rospy.Publisher(
            'face/info/array', FaceArray, queue_size=10
        )
        '''
        publishers&subscribers для drive
        '''
        self._pub_drive_mode = rospy.Publisher(
            'drive/mode', UInt16, queue_size=10
        )

        rospy.Subscriber(
            'drive/point', UInt16, self._pointListenerCallback
        )
        self._pub_drive_to_point = rospy.Publisher(
            'drive/point', UInt16, queue_size=10
        )

        rospy.Subscriber(
            'drive/pause', Bool, self._drivePauseListenerCallback
        )
        self._pub_drive_pause = rospy.Publisher(
            'drive/pause', Bool, queue_size=10
        )

        rospy.Subscriber(
            'drive/station', Bool, self._driveStationListenerCallback
        )
        self._pub_drive_station = rospy.Publisher(
            'drive/station', Bool, queue_size=10
        )

        rospy.Subscriber(
            'drive/status', UInt8, self._driveStatusListenerCallback
        )
        rospy.Subscriber(
            'rwheel', Int32, self._rwheelListenerCallback
        )
        rospy.Subscriber(
            'lwheel', Int32, self._lwheelListenerCallback
        )
        rospy.Subscriber(
            'charge/state', Bool, self._chargeStateListenerCallback
        )
        '''
        publishers&subscribers для joy
        '''
        self._pub_joy_phrase_mode = rospy.Publisher(
            'joy/speech/switch', Empty, queue_size=10
        )

        self._pub_joy_cmd = rospy.Publisher('joy', Joy, queue_size=10)

        '''
        publishers&subscribers для interaction
        '''
        rospy.Subscriber(
            'interaction', Interaction, self._interactionListenerCallback
        )
        self._pub_interaction = rospy.Publisher(
            'interaction', Interaction, queue_size=10
        )

        '''
        publishers&subscribers для script/servos
        '''
        rospy.Subscriber(
            'script/process', ScriptProcess, self._scriptProcessListenerCallback
        )
        rospy.Subscriber(
            'promobot_servos/core', ServoStates, self._servoStateListenerCallback
        )

        '''
        Переменные subscribers
        '''
        self._answer_subscriber_state = False
        self._interaction_subscriber_state = False
        self._rwheel_subscriber_state = False
        self._lwheel_subscriber_state = False
        self._point_subscriber_state = False
        self._drive_pause_subscriber_state = False
        self._drive_station_subscriber_state = False
        self._drive_status_subscriber_state = False
        self._charge_state_subscriber_state = False
        self._script_process_subscriber_state = False
        self._servos_state_subscriber_state = False
        '''
        Переменные для getters
        '''
        self._robot_answer = ''
        self._interaction_state = ''
        self._interaction_reason = ''
        self._rwheel_data = ''
        self._lwheel_data = ''
        self._current_point = ''
        self._drive_pause_state = True
        self._drive_station_state = False
        self._drive_status = 0
        self._charge_state = False
        self._script_name = ''
        self._script_state = False
        self._servos_state = []
        '''
        param's getter
        '''
        self._levels_order = rospy.get_param('answers/levels_order')
        '''
        sleep for publishers
        '''
        self._timeout = 0.5
    '''
    методы для asr / tts
    '''

    def asrPub(self, values):
        asr_result = ASRResult()
        asr_result.header.frame_id = "asr"
        asr_result.header.stamp = rospy.get_rostime()
        asr_result.source = 0
        asr_result.uuid = values.uuid
        asr_result.text = values.text
        asr_result.final = 1
        asr_result.conf = 1.0
        self._pub_text_to_asr.publish(asr_result)
        rospy.sleep(self._timeout)

    def ttsPub(self, values):
        tts_command = TTSCommand()
        tts_command.text = values.text
        tts_command.terminate = False
        tts_command.uuid = values.uuid
        tts_command.ignore_saving = False
        tts_command.rate = 0
        self._pub_text_to_tts.publish(tts_command)
        rospy.sleep(self._timeout)

    def cancelSpeech(self):
        self._pub_cancel_speech.publish()
        rospy.sleep(self._timeout)

    def answersListener(self):
        self._robot_answer = ''
        self._answer_subscriber_state = True
        rospy.sleep(self._timeout)

    def _answersListenerCallback(self, data):
        if self._answer_subscriber_state:
            self._robot_answer = data.replica.text
            self._answer_subscriber_state = False

    def getAnswer(self):
        rospy.sleep(self._timeout)
        return self._robot_answer.decode('utf-8')

    def getLevelsOrder(self):
        return self._levels_order
    '''
    методы для faceRecognize
    '''

    def facePub(self, values):
        face_array = FaceArray()
        face = Face()
        face_score = FaceScore()
        face.type = values.type
        face.source = 1
        face.is_tracking = True
        face.track_id = 10
        face.id = values.id
        face.gender = 0
        face.age = 0.0
        face.emotion = ''
        face.facemask = values.facemask
        face.is_fake = False
        face_score.source = 3
        face_score.personSource = 1
        face_score.id = values.id
        face_score.score = values.score
        face.persons = [face_score]
        face_array.faces.append(face)
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)

    '''
    методы для driving
    '''

    def autoModePub(self):
        self._pub_drive_mode.publish(1)
        rospy.sleep(self._timeout)

    def joyModePub(self):
        self._pub_drive_mode.publish(0)
        rospy.sleep(self._timeout)

    def driveToPointPub(self, values):
        self._pub_drive_to_point.publish(values.point)
        rospy.sleep(self._timeout)

    def wheelsListener(self):
        self._lwheel_subscriber_state = True
        self._rwheel_subscriber_state = True
        rospy.sleep(self._timeout)

    def _rwheelListenerCallback(self, data):
        if self._rwheel_subscriber_state:
            self._rwheel_data = data
            self._rwheel_subscriber_state = False

    def _lwheelListenerCallback(self, data):
        if self._lwheel_subscriber_state:
            self._lwheel_data = data
            self._lwheel_subscriber_state = False

    def pointListener(self):
        self._point_subscriber_state = True
        rospy.sleep(self._timeout)

    def _pointListenerCallback(self, data):
        if self._point_subscriber_state:
            self._current_point = data
            self._point_subscriber_state = False

    def drivePausePub(self):
        self._pub_drive_pause.publish(not self._drive_pause_state)
        rospy.sleep(self._timeout)

    def drivePauseListener(self):
        self._drive_pause_subscriber_state = True
        rospy.sleep(self._timeout)

    def _drivePauseListenerCallback(self, data):
        if self._drive_pause_subscriber_state:
            self._drive_pause_state = data
            self._drive_pause_subscriber_state = False

    def driveStationPub(self):
        self._pub_drive_station.publish(True)
        rospy.sleep(self._timeout)

    def driveStationListener(self):
        self._drive_station_subscriber_state = True
        rospy.sleep(self._timeout)

    def _driveStationListenerCallback(self, data):
        if self._drive_station_subscriber_state:
            self._drive_station_state = data
            self._drive_pause_subscriber_state = False

    def driveStatusListener(self):
        self._drive_status_subscriber_state = True
        rospy.sleep(self._timeout)

    def _driveStatusListenerCallback(self, data):
        if self._drive_status_subscriber_state:
            self._drive_status = data
            self._drive_status_subscriber_state = False

    def chargeStateListener(self):
        self._charge_state_subscriber_state = True
        rospy.sleep(self._timeout)

    def _chargeStateListenerCallback(self, data):
        if self._charge_state_subscriber_state:
            self._charge_state = data
            self._charge_state_subscriber_state = False

    def getWheelsData(self):
        rospy.sleep(self._timeout)
        return [self._rwheel_data, self._rwheel_data]

    def getCurrentPoint(self):
        rospy.sleep(self._timeout)
        return self._current_point

    def getDrivePause(self):
        rospy.sleep(self._timeout)
        return self._drive_pause_state

    def getDriveStationStatus(self):
        rospy.sleep(self._timeout)
        return self._drive_station_state

    def getDriveStatus(self):
        rospy.sleep(self._timeout)
        return self._drive_status

    def getChargeState(self):
        rospy.sleep(self._timeout)
        return self._charge_state
    '''
    методы для joy
    '''

    def switchJoyPhraseMode(self):
        self._pub_joy_phrase_mode.publish()
        rospy.sleep(self._timeout)

    def sendJoyCommand(self, values):
        joy = Joy()
        joy.header.frame_id = ''
        joy.header.stamp = rospy.get_rostime()
        joy.axes = values['axes']
        joy.buttons = values['buttons']
        self._pub_joy_cmd.publish(joy)
        rospy.sleep(self._timeout)

    '''
    методы для interaction
    '''

    def startInteraction(self, values):
        interaction = Interaction()
        interaction.state = values.state
        interaction.reason = values.reason
        self._pub_interaction.publish(interaction)
        rospy.sleep(self._timeout)

    def interactionListener(self):
        self._interaction_subscriber_state = True
        rospy.sleep(self._timeout)

    def _interactionListenerCallback(self, data):
        if self._interaction_subscriber_state:
            self._interaction_state = data.state
            self._interaction_reason = data.reason
            self._interaction_subscriber_state = False

    def getInteraction(self):
        rospy.sleep(self._timeout)
        return [self._interaction_state, self._interaction_reason]

    '''
    методы для script/servos
    '''

    def scriptProcessListener(self):
        self._script_process_subscriber_state = True
        rospy.sleep(self._timeout)

    def _scriptProcessListenerCallback(self, data):
        if self._script_process_subscriber_state:
            self._script_state = data.state
            self._script_name = data.name
            self._script_process_subscriber_state = False

    def servoStateListener(self):
        self._servos_state = []
        self._servos_state_subscriber_state = True
        rospy.sleep(self._timeout)

    def _servoStateListenerCallback(self, data):
        if self._servos_state_subscriber_state:
            self._servos_state.append(date)
            rospy.sleep(self._timeout)
            self._servos_state_subscriber_state = False

    def getScriptProcess(self):
        rospy.sleep(self._timeout)
        return [self._script_name, self._script_state]

    def getServosState(self):
        rospy.sleep(self._timeout)
        return self._servos_state