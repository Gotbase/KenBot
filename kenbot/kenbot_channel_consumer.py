#  gotbase kenbot-Trading
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
#  Lesser General License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import async_channel.channels as channel_instances
import async_channel.util as channel_creator

import kenbot_commons.enums as enums
import kenbot_commons.logging as logging

import kenbot_evaluators.kenbot_channel_consumer as evaluator_channel_consumer

import kenbot_services.kenbot_channel_consumer as service_channel_consumer

import kenbot_trading.api as trading_api
import kenbot_trading.kenbot_channel_consumer as trading_channel_consumer

import kenbot.channels as kenbot_channel
import kenbot.logger as logger


class kenbotChannelGlobalConsumer:

    def __init__(self, kenbot):
        self.kenbot = kenbot
        self.logger = logging.get_logger(self.__class__.__name__)

        # the list of kenbot channel consumers
        self.kenbot_channel_consumers = []

        # the kenbot Channel instance
        self.kenbot_channel = None

    async def initialize(self):
        # Creates kenbot Channel
        self.kenbot_channel: kenbot_channel.kenbotChannel = await channel_creator.create_channel_instance(
            kenbot_channel.kenbotChannel, channel_instances.set_chan_at_id,
            is_synchronized=True, bot_id=self.kenbot.bot_id)

        # Initialize global consumer
        self.kenbot_channel_consumers.append(
            await self.kenbot_channel.new_consumer(self.kenbot_channel_callback, bot_id=self.kenbot.bot_id))

        # Initialize trading consumer
        self.kenbot_channel_consumers.append(
            await self.kenbot_channel.new_consumer(
                trading_channel_consumer.kenbot_channel_callback,
                bot_id=self.kenbot.bot_id,
                action=[action.value for action in trading_channel_consumer.kenbotChannelTradingActions]
            ))

        # Initialize evaluator consumer
        self.kenbot_channel_consumers.append(
            await self.kenbot_channel.new_consumer(
                evaluator_channel_consumer.kenbot_channel_callback,
                bot_id=self.kenbot.bot_id,
                action=[action.value for action in evaluator_channel_consumer.kenbotChannelEvaluatorActions]
            ))

        # Initialize service consumer
        self.kenbot_channel_consumers.append(
            await self.kenbot_channel.new_consumer(
                service_channel_consumer.kenbot_channel_callback,
                bot_id=self.kenbot.bot_id,
                action=[action.value for action in service_channel_consumer.kenbotChannelServiceActions]
            ))

    async def kenbot_channel_callback(self, bot_id, subject, action, data) -> None:
        """
        kenbot channel consumer callback
        :param bot_id: the callback bot id
        :param subject: the callback subject
        :param action: the callback action
        :param data: the callback data
        """
        if subject == enums.kenbotChannelSubjects.NOTIFICATION.value:
            if action == trading_channel_consumer.kenbotChannelTradingActions.EXCHANGE.value:
                if trading_channel_consumer.kenbotChannelTradingDataKeys.EXCHANGE_ID.value in data:
                    exchange_id = data[trading_channel_consumer.kenbotChannelTradingDataKeys.EXCHANGE_ID.value]
                    self.kenbot.exchange_producer.exchange_manager_ids.append(exchange_id)
                    await logger.init_exchange_chan_logger(exchange_id)
                    exchange_configuration = trading_api.get_exchange_configuration_from_exchange_id(exchange_id)
                    await self.kenbot.evaluator_producer.create_evaluators(exchange_configuration)
                    # If an exchange is created before interface producer is done, it will be registered via
                    # self.kenbot.interface_producer directly on creation
                    await self.kenbot.interface_producer.register_exchange(exchange_id)
            elif action == evaluator_channel_consumer.kenbotChannelEvaluatorActions.EVALUATOR.value:
                if not self.kenbot.service_feed_producer.started:
                    # Start service feeds now that evaluators registered their feed requirements
                    await self.kenbot.service_feed_producer.start_feeds()
            elif action == service_channel_consumer.kenbotChannelServiceActions.INTERFACE.value:
                await self.kenbot.interface_producer.register_interface(
                    data[service_channel_consumer.kenbotChannelServiceDataKeys.INSTANCE.value])
            elif action == service_channel_consumer.kenbotChannelServiceActions.NOTIFICATION.value:
                await self.kenbot.interface_producer.register_notifier(
                    data[service_channel_consumer.kenbotChannelServiceDataKeys.INSTANCE.value])
            elif action == service_channel_consumer.kenbotChannelServiceActions.SERVICE_FEED.value:
                await self.kenbot.service_feed_producer.register_service_feed(
                    data[service_channel_consumer.kenbotChannelServiceDataKeys.INSTANCE.value])

    async def stop(self) -> None:
        """
        Remove all kenbot Channel consumers
        """
        for consumer in self.kenbot_channel_consumers:
            await self.kenbot_channel.remove_consumer(consumer)
