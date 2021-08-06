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
        publishers для asr / tts
        '''
        self._pub_text_to_asr = rospy.Publisher(
            'asr/result', ASRResult, latch=True, queue_size=10
        )
        self._pub_text_to_tts = rospy.Publisher(
            'tts/start', TTSCommand, latch=True, queue_size=10
        )
        self._pub_cancel_speech = rospy.Publisher(
            'tts/cancel', Empty, latch=True, queue_size=10
        )
        '''
        publishers для faceRecognize
        '''
        self._pub_face_to_faceArray = rospy.Publisher(
            'face/info/array', FaceArray, latch=True, queue_size=10
        )
        '''
        publishers для drive
        '''
        self._pub_drive_mode = rospy.Publisher(
            'drive/mode', UInt16, latch=True, queue_size=10
        )

        self._pub_drive_to_point = rospy.Publisher(
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
        publishers для joy
        '''
        self._pub_joy_phrase_mode = rospy.Publisher(
            'joy/speech/switch', Empty, latch=True, queue_size=10
        )

        self._pub_joy_cmd = rospy.Publisher(
            'joy', Joy, latch=True, queue_size=10)

        '''
        publishers для interaction
        '''

        self._pub_interaction = rospy.Publisher(
            'interaction', Interaction, latch=True, queue_size=10
        )

        '''
        Переменные subscribers
        '''
        self._answer_subscriber_state = False
        self._interaction_subscriber_state = False
        self._drive_mode_subscriber_state = False
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
        self._interaction_state = False
        self._interaction_reason = 0
        self._current_mode = ''
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

    def asrPub(self, data):
        asr_result = ASRResult()
        asr_result.header.frame_id = "asr"
        asr_result.header.stamp = rospy.get_rostime()
        asr_result.source = 0
        asr_result.uuid = data.uuid
        asr_result.text = data.text
        asr_result.final = 1
        asr_result.conf = 1.0
        self._pub_text_to_asr.publish(asr_result)
        rospy.sleep(self._timeout)

    def ttsPub(self, data):
        tts_command = TTSCommand()
        tts_command.text = data.text
        tts_command.terminate = False
        tts_command.uuid = data.uuid
        tts_command.ignore_saving = False
        self._pub_text_to_tts.publish(tts_command)
        rospy.sleep(self._timeout)

    def cancelSpeech(self):
        self._pub_cancel_speech.publish()
        rospy.sleep(self._timeout)

    def answersListener(self):
        rospy.sleep(self._timeout)
        self._robot_answer = ''
        self._answer_subscriber_state = True
        rospy.Subscriber(
            'answers/answer', Answer, self._answersListenerCallback
        )

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

    def facePub(self, data):
        face_array = FaceArray()
        face = Face()
        face_score = FaceScore()
        face.type = data.type
        face.source = 1
        face.is_tracking = data.is_tracking
        face.track_id = data.track_id
        face.id = data.id
        face.gender = 0
        face.age = 0.0
        face.emotion = ''
        face.liveness_type = 0
        face_score.source = 3
        face_score.personSource = 1
        face_score.id = data.id
        face_score.score = data.score
        face.persons = [face_score]
        # чистим массив лиц перед отправкой
        face_array.faces = []
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)
        # публикуем нужное лицо
        face_array.faces.append(face)
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)

    '''
    методы для driving
    '''
    # объединить в одну, назвать changeDrivingMode

    def autoModePub(self):
        self._pub_drive_mode.publish(1)
        rospy.sleep(self._timeout)

    def joyModePub(self):
        self._pub_drive_mode.publish(0)
        rospy.sleep(self._timeout)

    def driveModeListener(self):
        rospy.sleep(self._timeout)
        self._drive_mode_subscriber_state = True
        rospy.Subscriber(
            'drive/mode', UInt16, self._driveModeListenerCallback
        )

    def _driveModeListenerCallback(self, data):
        if self._drive_mode_subscriber_state:
            self._current_mode = data.data
            self._drive_mode_subscriber_state = False

    def driveToPointPub(self, point):
        self._pub_drive_to_point.publish(point)
        rospy.sleep(self._timeout)

    def pointListener(self):
        rospy.sleep(self._timeout)
        self._point_subscriber_state = True
        rospy.Subscriber(
            'drive/point', UInt16, self._pointListenerCallback
        )

    def _pointListenerCallback(self, data):
        if self._point_subscriber_state:
            self._current_point = data.data
            self._point_subscriber_state = False

    def wheelsListener(self):
        rospy.sleep(self._timeout)
        self._lwheel_subscriber_state = True
        self._rwheel_subscriber_state = True
        rospy.Subscriber(
            'rwheel', Int32, self._rwheelListenerCallback
        )
        rospy.Subscriber(
            'lwheel', Int32, self._lwheelListenerCallback
        )

    def _rwheelListenerCallback(self, data):
        if self._rwheel_subscriber_state:
            self._rwheel_data = data.data
            self._rwheel_subscriber_state = False

    def _lwheelListenerCallback(self, data):
        if self._lwheel_subscriber_state:
            self._lwheel_data = data.data
            self._lwheel_subscriber_state = False

    def drivePausePub(self):
        self._drive_pause_state = not self._drive_pause_state
        self._pub_drive_pause.publish(self._drive_pause_state)
        rospy.sleep(self._timeout)

    def drivePauseListener(self):
        rospy.sleep(self._timeout)
        self._drive_pause_subscriber_state = True
        rospy.Subscriber(
            'drive/pause', Bool, self._drivePauseListenerCallback
        )

    def _drivePauseListenerCallback(self, data):
        if self._drive_pause_subscriber_state:
            self._drive_pause_state = data.data
            self._drive_pause_subscriber_state = False

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
            'drive/station', Bool, self._driveStationListenerCallback
        )

    def _driveStationListenerCallback(self, data):
        if self._drive_station_subscriber_state:
            self._drive_station_state = data.data
            self._drive_pause_subscriber_state = False

    def driveStatusListener(self):
        rospy.sleep(self._timeout)
        self._drive_status_subscriber_state = True
        rospy.Subscriber(
            'drive/status', UInt8, self._driveStatusListenerCallback
        )

    def _driveStatusListenerCallback(self, data):
        if self._drive_status_subscriber_state:
            self._drive_status = data.data
            self._drive_status_subscriber_state = False

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

    def getDriveMode(self):
        rospy.sleep(self._timeout)
        return self._current_mode

    def getCurrentPoint(self):
        rospy.sleep(self._timeout)
        return self._current_point

    def getWheelsData(self):
        rospy.sleep(self._timeout)
        return [self._rwheel_data, self._rwheel_data]

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

    def sendJoyCommand(self, commands):
        for command in commands:
            joy = Joy()
            joy.header.frame_id = ''
            joy.header.stamp = rospy.get_rostime()
            joy.axes = command['axes']
            joy.buttons = command['buttons']
            self._pub_joy_cmd.publish(joy)
            rospy.sleep(self._timeout)

    '''
    методы для interaction
    '''

    def startInteraction(self, data):
        interaction = Interaction()
        interaction.state = data.state
        interaction.reason = data.reason
        self._pub_interaction.publish(interaction)
        rospy.sleep(self._timeout)

    def interactionListener(self):
        rospy.sleep(self._timeout)
        self._interaction_subscriber_state = True
        rospy.Subscriber(
            'interaction', Interaction, self._interactionListenerCallback
        )

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
        rospy.sleep(self._timeout)
        self._script_process_subscriber_state = True
        rospy.Subscriber(
            'script/process', ScriptProcess, self._scriptProcessListenerCallback
        )

    def _scriptProcessListenerCallback(self, data):
        if self._script_process_subscriber_state:
            self._script_state = data.process
            self._script_name = data.name
            self._script_process_subscriber_state = False

    def servoStateListener(self):
        rospy.sleep(self._timeout)
        self._servos_state = []
        self._servos_state_subscriber_state = True
        rospy.Subscriber(
            'promobot_servos/core', ServoStates, self._servoStateListenerCallback
        )

    def _servoStateListenerCallback(self, data):
        if self._servos_state_subscriber_state:
            self._servos_state.append(data)
            rospy.sleep(self._timeout)
            self._servos_state_subscriber_state = False

    def getScriptProcess(self):
        rospy.sleep(self._timeout)
        return [self._script_name, self._script_state]

    def getServosState(self):
        rospy.sleep(self._timeout)
        return self._servos_state
