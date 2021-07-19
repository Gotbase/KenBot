#  gotbase kenbot
#  Copyright (c) gotbase, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import kenbot.constants as constants
import kenbot.commands as commands
import kenbot.community


class kenbotAPI:

    def __init__(self, kenbot):
        self._kenbot = kenbot

    def is_initialized(self) -> bool:
        return self._kenbot.initialized

    def get_exchange_manager_ids(self) -> list:
        return self._kenbot.exchange_producer.exchange_manager_ids

    def get_global_config(self) -> dict:
        return self._kenbot.config

    def get_startup_config(self) -> object:
        return self._kenbot.get_startup_config(constants.CONFIG_KEY)

    def get_edited_config(self, dict_only=True) -> object:
        return self._kenbot.get_edited_config(constants.CONFIG_KEY, dict_only=dict_only)

    def get_startup_tentacles_config(self) -> object:
        return self._kenbot.get_startup_config(constants.TENTACLES_SETUP_CONFIG_KEY)

    def get_edited_tentacles_config(self) -> object:
        return self._kenbot.get_edited_config(constants.TENTACLES_SETUP_CONFIG_KEY)

    def set_edited_tentacles_config(self, config):
        self._kenbot.set_edited_config(constants.TENTACLES_SETUP_CONFIG_KEY, config)

    def get_trading_mode(self) -> object:
        return self._kenbot.get_trading_mode()

    def get_tentacles_setup_config(self) -> object:
        return self._kenbot.tentacles_setup_config

    def get_start_time(self) -> float:
        return self._kenbot.start_time

    def get_bot_id(self) -> str:
        return self._kenbot.bot_id

    def get_matrix_id(self) -> str:
        return self._kenbot.evaluator_producer.matrix_id

    def get_aiohttp_session(self) -> object:
        return self._kenbot.get_aiohttp_session()

    def get_community_auth(self) -> kenbot.community.CommunityAuthentication:
        return self._kenbot.community_auth

    def run_in_main_asyncio_loop(self, coroutine):
        return self._kenbot.run_in_main_asyncio_loop(coroutine)

    def run_in_async_executor(self, coroutine):
        return self._kenbot.task_manager.run_in_async_executor(coroutine)

    def stop_tasks(self) -> None:
        self._kenbot.task_manager.stop_tasks()

    def stop_bot(self) -> None:
        commands.stop_bot(self._kenbot)

    @staticmethod
    def restart_bot() -> None:
        commands.restart_bot()

    def update_bot(self) -> None:
        commands.update_bot(self)
