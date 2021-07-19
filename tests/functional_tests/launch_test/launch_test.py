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
import asyncio
import pytest

from kenbot_commons.logging.logging_util import get_logger
from kenbot_trading.api.exchange import cancel_ccxt_throttle_task
from tentacles.Services.Interfaces.web_interface import WebInterface
from kenbot_commons.tests.test_config import load_test_config
from kenbot.commands import start_bot
from kenbot.logger import init_logger
from kenbot.kenbot import kenbot

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


@pytest.mark.timeout(12)
async def test_run_bot():
    # avoid web interface in this test
    WebInterface.enabled = False
    bot = kenbot(load_test_config(dict_only=False), ignore_config=True)
    bot.task_manager.init_async_loop()
    await start_bot(bot, init_logger())
    await asyncio.sleep(10)
    await stop_bot(bot)


async def stop_bot(bot):
    # force all logger enable to display any error
    stop_logger = get_logger("StopBotLogger")
    import logging
    for logger in logging.Logger.manager.loggerDict.values():
        logger.disabled = False

    stop_logger.info("Stopping tasks...")
    await bot.stop()

    if bot.task_manager.tools_task_group:
        bot.task_manager.tools_task_group.cancel()

    # close community session
    if bot.community_handler:
        await bot.community_handler.stop_task()

    cancel_ccxt_throttle_task()

    stop_logger.info("Tasks stopped.")
