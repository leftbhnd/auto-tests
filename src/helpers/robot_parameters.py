#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.helpers.parameters.dialog_parameters import DialogParameters
from src.helpers.parameters.driving_parameters import DrivingParameters
from src.helpers.parameters.interaction_parameters import InteractionParameters


class RobotParameters:
    def __init__(self, DialogParameters, DrivingParameters, InteractionParameters):
        self.dialog = DialogParameters
        self.driving = DrivingParameters
        self.interaction = InteractionParameters


robot_parameters = RobotParameters(
    DialogParameters, DrivingParameters, InteractionParameters
)
