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
import os
import pathlib

PROJECT_NAME = "kenbot"
AUTHOR = "gotbase"
SHORT_VERSION = "0.4.0"  # major.minor.revision
PATCH_VERSION = ""  # patch : pX
VERSION_DEV_PHASE = "b"  # alpha : a / beta : b / release candidate : rc
VERSION_PHASE = "12"  # XX
VERSION = f"{SHORT_VERSION}{VERSION_DEV_PHASE}{VERSION_PHASE}"
LONG_VERSION = f"{SHORT_VERSION}{PATCH_VERSION}{VERSION_DEV_PHASE}{VERSION_PHASE}"

# kenbot urls
kenbot_WEBSITE_URL = os.getenv("kenbot_ONLINE_URL", "https://www.kenbot.online")
kenbot_DOCS_URL = os.getenv("DOCS_kenbot_ONLINE_URL", "https://docs.kenbot.online")
kenbot_ONLINE = os.getenv("TENTACLES_kenbot_ONLINE_URL", "https://tentacles.kenbot.online")
kenbot_FEEDBACK = os.getenv("FEEDBACK_kenbot_ONLINE_URL", "https://feedback.kenbot.online/")
REPOSITORY = "repository"
TENTACLES_REPOSITORY = "tentacles"
OFFICIALS = "officials"
TENTACLE_CATEGORY = "full"
TENTACLE_PACKAGE_NAME = "base"
TENTACLE_PACKAGES = "packages"
COMPILED_TENTACLE_CATEGORY = "extra"

DEFAULT_COMMUNITY_URL = "TODO"
kenbot_COMMUNITY_URL = os.getenv("COMMUNITY_SERVER_URL", DEFAULT_COMMUNITY_URL)
kenbot_COMMUNITY_AUTH_URL = f"{kenbot_COMMUNITY_URL}spree_oauth/token"
kenbot_COMMUNITY_ACCOUNT_URL = f"{kenbot_COMMUNITY_URL}api/v2/storefront/account"
kenbot_COMMUNITY_PACKAGES_URL = f"{kenbot_COMMUNITY_URL}api/v2/storefront/tentacle/packages"

kenbot_BINARY_PROJECT_NAME = "kenbot-Binary"

# tentacles
ENV_TENTACLES_URL = "TENTACLES_URL"
ENV_COMPILED_TENTACLES_URL = "COMPILED_TENTACLES_URL"
ENV_TENTACLES_REPOSITORY = "TENTACLES_REPOSITORY"
ENV_TENTACLES_URL_TAG = "TENTACLES_URL_TAG"
ENV_TENTACLE_PACKAGE_NAME = "TENTACLE_PACKAGE_NAME"
ENV_TENTACLES_PACKAGES_TYPE = "TENTACLES_PACKAGES_TYPE"
ENV_TENTACLES_PACKAGES_SOURCE = "TENTACLES_PACKAGES_SOURCE"
ENV_COMPILED_TENTACLES_CATEGORY = "COMPILED_TENTACLES_CATEGORY"
ENV_COMPILED_TENTACLES_PACKAGES_TYPE = "COMPILED_TENTACLES_PACKAGES_TYPE"
ENV_TENTACLE_CATEGORY = "TENTACLE_CATEGORY"
ENV_COMPILED_TENTACLES_SUBCATEGORY = "COMPILED_TENTACLES_SUBCATEGORY"
TENTACLES_REQUIRED_VERSION = f"{os.getenv(ENV_TENTACLES_URL_TAG, LONG_VERSION)}"
# url ending example: 	tentacles/officials/packages/full/base/latest/any_platform.zip

DEFAULT_TENTACLES_PACKAGE_NAME = "kenbot-Default-Tentacles"

# logs
LOGS_FOLDER = "logs"
ENV_ENABLE_DEBUG_LOGS = "ENABLE_DEBUG_LOGS"

# config types keys
CONFIG_KEY = "config"
TENTACLES_SETUP_CONFIG_KEY = "tentacles_setup"

# terms of service
CONFIG_ACCEPTED_TERMS = "accepted_terms"

# DEBUG
CONFIG_DEBUG_OPTION = "DEV-MODE"
FORCE_ASYNCIO_DEBUG_OPTION = False

# Files
# Store the path of the kenbot directory from this file since it can change depending on the installation path
# (local sources, python site-packages, ...)
kenbot_FOLDER = pathlib.Path(__file__).parent.absolute()
CONFIG_FOLDER = f"{kenbot_FOLDER}/config"
SCHEMA = "schema"
CONFIG_FILE_SCHEMA = f"{CONFIG_FOLDER}/config_{SCHEMA}.json"
PROFILE_FILE_SCHEMA = f"{CONFIG_FOLDER}/profile_{SCHEMA}.json"
DEFAULT_CONFIG_FILE = f"{CONFIG_FOLDER}/default_config.json"
DEFAULT_PROFILE_FILE = f"{CONFIG_FOLDER}/default_profile.json"
DEFAULT_PROFILE_AVATAR_FILE_NAME = "default_profile.png"
DEFAULT_PROFILE_AVATAR = f"{CONFIG_FOLDER}/{DEFAULT_PROFILE_AVATAR_FILE_NAME}"
LOGGING_CONFIG_FILE = f"{CONFIG_FOLDER}/logging_config.ini"
LOG_FILE = f"{LOGS_FOLDER}/{PROJECT_NAME}.log"

# Optimizer
OPTIMIZER_FORCE_ASYNCIO_DEBUG_OPTION = False
OPTIMIZER_DATA_FILES_FOLDER = f"{kenbot_FOLDER}/strategy_optimizer/optimizer_data_files"

# Channel
kenbot_CHANNEL = "kenbot"

kenbot_KEY = b'uVEw_JJe7uiXepaU_DR4T-ThkjZlDn8Pzl8hYPIv7w0='
