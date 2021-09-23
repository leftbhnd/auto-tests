#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.helpers.modals.adding_faces_modal import AddingFacesModal
from src.helpers.modals.answers_log_modal import AnswersLogModal
from src.helpers.modals.connection_info_modal import ConnectionInfoModal
from src.helpers.modals.identification_modal import IdentificationModal
from src.helpers.modals.no_connection_modal import NoInternetConnection
from src.helpers.modals.password_modal import PasswordModal
from src.helpers.modals.promo_modal import PromoModal
from src.helpers.modals.radius_modal import RadiusModal
from src.helpers.modals.restart_modal import RestartModal
from src.helpers.modals.save_modals import SaveModal
from src.helpers.modals.speech_settings_modal import SpeechSettingsModal
from src.helpers.modals.testing_modal import TestingModal
from src.helpers.modals.wifi_password_modal import WifiPasswordModal


class RobotModals:
    def __init__(
        self, AddingFacesModal, AnswersLogModal,
        ConnectionInfoModal, IdentificationModal, NoInternetConnection,
        PasswordModal, PromoModal, RadiusModal,
        RestartModal, SaveModal, SpeechSettingsModal,
        TestingModal, WifiPasswordModal
    ):
        self.add_face = AddingFacesModal
        self.ans_log = AnswersLogModal
        self.connection_info = ConnectionInfoModal
        self.ident = IdentificationModal
        self.no_connection = NoInternetConnection
        self.pwd = PasswordModal
        self.promo = PromoModal
        self.radius = RadiusModal
        self.restart = RestartModal
        self.save = SaveModal
        self.speech_settings = SpeechSettingsModal
        self.testing = TestingModal
        self.wifi_pwd = WifiPasswordModal


robot_modals = RobotModals(
    AddingFacesModal, AnswersLogModal, ConnectionInfoModal,
    IdentificationModal, NoInternetConnection, PasswordModal,
    PromoModal, RadiusModal, RestartModal,
    SaveModal, SpeechSettingsModal, TestingModal,
    WifiPasswordModal
)
