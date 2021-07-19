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
import kenbot_backtesting.api as backtesting_api

import kenbot_commons.enums as common_enums

import kenbot_services.api as service_api
import kenbot_services.kenbot_channel_consumer as service_channel_consumer

import kenbot_tentacles_manager.api as tentacles_manager_api

import kenbot.channels as kenbot_channels
import kenbot.constants as constants


class ServiceFeedProducer(kenbot_channels.kenbotChannelProducer):
    """EvaluatorFactory class:
    - Create service feeds
    """

    def __init__(self, channel, kenbot):
        super().__init__(channel)
        self.kenbot = kenbot
        self.started = False

        self.service_feeds = []

    async def start(self):
        in_backtesting = backtesting_api.is_backtesting_enabled(self.kenbot.config)
        service_feed_factory = service_api.create_service_feed_factory(self.kenbot.config,
                                                                       self.kenbot.async_loop,
                                                                       self.kenbot.bot_id)
        for feed in service_feed_factory.get_available_service_feeds(in_backtesting):
            if tentacles_manager_api.is_tentacle_activated_in_tentacles_setup_config(
                    self.kenbot.tentacles_setup_config, feed.get_name()):
                await self.create_feed(service_feed_factory, feed, in_backtesting)

    async def start_feeds(self):
        self.started = True
        for feed in self.service_feeds:
            await self.send(bot_id=self.kenbot.bot_id,
                            subject=common_enums.kenbotChannelSubjects.UPDATE.value,
                            action=service_channel_consumer.kenbotChannelServiceActions.START_SERVICE_FEED.value,
                            data={
                                service_channel_consumer.kenbotChannelServiceDataKeys.INSTANCE.value: feed,
                                service_channel_consumer.kenbotChannelServiceDataKeys.EDITED_CONFIG.value:
                                    self.kenbot.get_edited_config(constants.CONFIG_KEY, dict_only=False)
                            })

    async def create_feed(self, service_feed_factory, feed, in_backtesting):
        await self.send(bot_id=self.kenbot.bot_id,
                        subject=common_enums.kenbotChannelSubjects.CREATION.value,
                        action=service_channel_consumer.kenbotChannelServiceActions.SERVICE_FEED.value,
                        data={
                            service_channel_consumer.kenbotChannelServiceDataKeys.EDITED_CONFIG.value:
                                self.kenbot.get_edited_config(constants.CONFIG_KEY, dict_only=False),
                            service_channel_consumer.kenbotChannelServiceDataKeys.BACKTESTING_ENABLED.value:
                                in_backtesting,
                            service_channel_consumer.kenbotChannelServiceDataKeys.CLASS.value: feed,
                            service_channel_consumer.kenbotChannelServiceDataKeys.FACTORY.value: service_feed_factory
                        })

    async def register_service_feed(self, instance):
        self.service_feeds.append(instance)

    async def stop(self):
        for service_feed in self.service_feeds:
            await service_api.stop_service_feed(service_feed)
