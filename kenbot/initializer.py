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
import kenbot_tentacles_manager.api as tentacles_manager_api
import kenbot.constants as constants


class Initializer:
    """Initializer class:
    - Initialize services, constants and tools
    """

    def __init__(self, kenbot):
        self.kenbot = kenbot

    async def create(self):
        # initialize tentacle configuration
        tentacles_config_path = self.kenbot.get_startup_config(constants.CONFIG_KEY, dict_only=False).\
            get_tentacles_config_path()
        self.kenbot.tentacles_setup_config = tentacles_manager_api.get_tentacles_setup_config(tentacles_config_path)

        # create kenbot channel
        await self.kenbot.global_consumer.initialize()
