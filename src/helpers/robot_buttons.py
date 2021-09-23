#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.helpers.buttons.applications import Applications
from src.helpers.buttons.connection import Connection
from src.helpers.buttons.control import Control
from src.helpers.buttons.face_recognition import FaceRecognition
from src.helpers.buttons.gui import Gui
from src.helpers.buttons.handlers import Handlers
from src.helpers.buttons.keyboard import Keyboard
from src.helpers.buttons.language_settings import LanguageSettings
from src.helpers.buttons.linguistic_base import LinguisticBase
from src.helpers.buttons.navigation import Navigation
from src.helpers.buttons.online_services import Internet
from src.helpers.buttons.promo import Promo
from src.helpers.buttons.settings import Settings
from src.helpers.buttons.start import Start
from src.helpers.buttons.system import System
from src.helpers.buttons.testing import Testing
from src.helpers.buttons.ubuntu import Ubuntu


class RobotButtons:
    def __init__(
        self, Applications, Connection,
        Control, FaceRecognition, Gui,
        Handlers, Keyboard, LanguageSettings,
        LinguisticBase, Navigation, Internet,
        Promo, Settings, Start,
        System, Testing, Ubuntu
    ):
        self.apps = Applications
        self.connection = Connection
        self.control = Control
        self.fr = FaceRecognition
        self.gui = Gui
        self.handler = Handlers
        self.kb = Keyboard
        self.lang = LanguageSettings
        self.lingvo = LinguisticBase
        self.nav = Navigation
        self.internet = Internet
        self.promo = Promo
        self.settings = Settings
        self.start = Start
        self.system = System
        self.testing = Testing
        self.ubuntu = Ubuntu


robot_buttons = RobotButtons(
    Applications, Connection, Control,
    FaceRecognition, Gui, Handlers,
    Keyboard, LanguageSettings, LinguisticBase,
    Navigation, Internet, Promo,
    Settings, Start, System,
    Testing, Ubuntu
)
