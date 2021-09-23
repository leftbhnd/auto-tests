#!/usr/bin/env python
# -*- coding: utf-8 -*-
from params.dialog_params import DialogParams
from params.driving_params import DrivingParams
from params.interaction_params import InteractionParams


class RobotParams:
    def __init__(self, DialogParams, DrivingParams, InteractionParams):
        self.dialog = DialogParams
        self.driving = DrivingParams
        self.interaction = InteractionParams


robot_params = RobotParams(DialogParams, DrivingParams, InteractionParams)
