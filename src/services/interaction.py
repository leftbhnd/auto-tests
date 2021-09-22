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
        subscribers
        '''
        rospy.Subscriber(
            'interaction', Interaction, self._interactionListener
        )

        '''
        переменные для геттеров
        '''
        self._interaction_state = False
        # reason's type: Speech = 0, Face = 1, Click = 2, Hark = 3
        self._interaction_reason = 0

        self._timeout = 0.5

    def interactionPub(self, state, reason):
        interaction = Interaction()
        interaction.state = state
        interaction.reason = reason
        self._pub_interaction.publish(interaction)
        rospy.sleep(self._timeout)

    def _interactionListener(self, interaction):
        self._interaction_state = interaction.state
        self._interaction_reason = interaction.reason

    def getInteraction(self):
        return [self._interaction_state, self._interaction_reason]
