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

from __future__ import print_function
import os
import sys


# binary tentacle importation
sys.path.append(os.path.dirname(sys.executable))

bot_instance = None
global_config = None


def __init__(bot, config):
    global bot_instance
    bot_instance = bot

    global global_config
    global_config = config


# TODO: find a better way to keep track of the bot instance in kenbot module
def set_bot(bot):
    global bot_instance
    bot_instance = bot


def get_bot():
    return bot_instance


def get_config():
    return global_config