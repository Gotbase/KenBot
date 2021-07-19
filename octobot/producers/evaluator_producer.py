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
import kenbot_commons.enums as common_enums

import kenbot_backtesting.api as backtesting_api

import kenbot_evaluators.api as evaluator_api
import kenbot_evaluators.kenbot_channel_consumer as evaluator_channel_consumer

import kenbot.channels as kenbot_channel
import kenbot.logger as logger


class EvaluatorProducer(kenbot_channel.kenbotChannelProducer):
    """EvaluatorFactory class:
    - Create evaluators
    """

    def __init__(self, channel, kenbot):
        super().__init__(channel)
        self.kenbot = kenbot
        self.tentacles_setup_config = self.kenbot.tentacles_setup_config

        self.matrix_id = None

    async def start(self):
        self.matrix_id = await evaluator_api.initialize_evaluators(self.kenbot.config, self.tentacles_setup_config)
        await evaluator_api.create_evaluator_channels(
            self.matrix_id, is_backtesting=backtesting_api.is_backtesting_enabled(self.kenbot.config))
        await logger.init_evaluator_chan_logger(self.matrix_id)

    async def create_evaluators(self, exchange_configuration):
        await self.send(bot_id=self.kenbot.bot_id,
                        subject=common_enums.kenbotChannelSubjects.CREATION.value,
                        action=evaluator_channel_consumer.kenbotChannelEvaluatorActions.EVALUATOR.value,
                        data={
                            evaluator_channel_consumer.kenbotChannelEvaluatorDataKeys.TENTACLES_SETUP_CONFIG.value:
                                self.kenbot.tentacles_setup_config,
                            evaluator_channel_consumer.kenbotChannelEvaluatorDataKeys.MATRIX_ID.value:
                                self.kenbot.evaluator_producer.matrix_id,
                            evaluator_channel_consumer.kenbotChannelEvaluatorDataKeys.EXCHANGE_CONFIGURATION.value:
                                exchange_configuration
                        })


