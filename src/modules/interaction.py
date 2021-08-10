#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import Interaction


class InteractionService:
    def __init__(self):
        '''
        publishers
        '''
        self._pub_interaction = rospy.Publisher(
            'interaction', Interaction, latch=True, queue_size=10
        )
        '''
        переменные для включения subscribers 
        '''
        self._interaction_subscriber_state = False
        '''
        переменные для геттеров 
        '''
        self._interaction_state = False
        self._interaction_reason = 0

        self._timeout = 0.5

    def interactionPub(self, data):
        interaction = Interaction()
        interaction.state = data.state
        interaction.reason = data.reason
        self._pub_interaction.publish(interaction)
        rospy.sleep(self._timeout)

    def interactionListener(self):
        self._interaction_subscriber_state = True
        rospy.Subscriber(
            'interaction', Interaction, self._interactionListener
        )
        rospy.sleep(self._timeout)

    def _interactionListener(self, data):
        if self._interaction_subscriber_state:
            self._interaction_state = data.state
            self._interaction_reason = data.reason
            self._interaction_subscriber_state = False
        rospy.sleep(self._timeout)

    def getInteraction(self):
        rospy.sleep(self._timeout)
        return [self._interaction_state, self._interaction_reason]