#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.helpers.params.dialog_params import DialogParams
from src.helpers.params.driving_params import DrivingParams
from src.helpers.params.interaction_params import InteractionParams
from src.helpers.params.navigation_params import NavigationParams


class RobotParams:
    def __init__(self, DialogParams, DrivingParams, InteractionParams, NavigationParams):
        self.dialog = DialogParams
        self.driving = DrivingParams
        self.interaction = InteractionParams
        self.navigation = NavigationParams


robot_params = RobotParams(
    DialogParams, DrivingParams, InteractionParams, NavigationParams
)
