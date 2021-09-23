#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.helpers.parameters.dialog_params import DialogParams
from src.helpers.parameters.driving_params import DrivingParams
from src.helpers.parameters.interaction_params import InteractionParams


class RobotParams:
    def __init__(self, DialogParams, DrivingParams, InteractionParams):
        self.dialog = DialogParams
        self.driving = DrivingParams
        self.interaction = InteractionParams


robot_params = RobotParams(DialogParams, DrivingParams, InteractionParams)
