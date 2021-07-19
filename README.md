# kenbot [0.4.0-beta12](https://github.com/gotbase/kenbot/tree/dev/CHANGELOG.md)
[![PyPI](https://img.shields.io/pypi/v/kenbot.svg)](https://pypi.python.org/pypi/kenbot/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e07fb190156d4efb8e7d07aaa5eff2e1)](https://app.codacy.com/gh/gotbase/kenbot?utm_source=github.com&utm_medium=referral&utm_content=gotbase/kenbot&utm_campaign=Badge_Grade_Dashboard)[![Downloads](https://pepy.tech/badge/kenbot/month)](https://pepy.tech/project/kenbot)
[![Dockerhub](https://img.shields.io/docker/pulls/gotbase/kenbot.svg)](https://hub.docker.com/r/gotbase/kenbot)
[![Coverage Status](https://coveralls.io/repos/github/gotbase/kenbot/badge.svg?branch=dev)](https://coveralls.io/github/gotbase/kenbot?branch=dev)
[![kenbot-CI](https://github.com/gotbase/kenbot/workflows/kenbot-CI/badge.svg)](https://github.com/gotbase/kenbot/actions)
[![Build Status](https://cloud.drone.io/api/badges/gotbase/kenbot/status.svg)](https://cloud.drone.io/gotbase/kenbot)
[![UptimeRobot](https://img.shields.io/uptimerobot/ratio/30/m786447893-903b482e5158c8b6483760e8)](https://status.kenbot.online/)

#### kenbot Community
[![Active kenbot](https://img.shields.io/badge/dynamic/json.svg?&url=https://kenbotmetrics.herokuapp.com/metrics/community/count/0/-1/0&query=$.total&color=green&label=kenbots%20online%20this%20month)]()
[![Telegram Chat](https://img.shields.io/badge/telegram-chat-green.svg)](https://t.me/joinchat/F9cyfxV97ZOaXQ47H5dRWw)
[![Discord](https://img.shields.io/discord/530629985661222912.svg?logo=discord)](https://discord.gg/vHkcb8W)
[![Telegram News](https://img.shields.io/badge/telegram-news-blue.svg)](https://t.me/kenbot_Project)
[![Twitter](https://img.shields.io/twitter/follow/Drakkarskenbot.svg?label=Follow&style=social)](https://twitter.com/Drakkarskenbot)
<p align="center">
<img src="../assets/octopus.svg" alt="kenbot Logo" height="400" width="400">
</p>

![Web Interface](../assets/web-interface.gif)
## Description
[kenbot](https://www.kenbot.online/) is a powerful fully modular open-source cryptocurrency trading robot.

See the [kenbot official website](https://www.kenbot.online/).

This repository contains all the features of the bot (trading tools, evaluation engines, the backtesting toolkit, ...).
[kenbot's tentacles](https://github.com/gotbase/kenbot-tentacles) contains the bot's strategies and user interfaces.

To install kenbot with its tentacles, just use the [latest release for your system](https://github.com/gotbase/kenbot/releases/latest) and your kenbot is ready ! 

## Your kenbot
<a href="https://www.kenbot.online/guides/#telegram"><img src="../assets/telegram-interface.png" height="414" alt="Telegram interface"></a>
[![Twitter Interface](../assets/twitter-interface.png)](https://docs.kenbot.online/pages/Twitter-interface.html)

kenbot is highly customizable using its configuration and tentacles system. 
You can build your own bot using the infinite [configuration](https://www.kenbot.online/guides/#trading_modes) possibilities such as 
**technical analysis**, **social media processing** or even **external statistics management** like google trends.

kenbot is **AI ready**: Python being the main language for kenbot, it's easy to integrate machine-learning libraries such as [Tensorflow](https://github.com/tensorflow/tensorflow) or
any other lib and take advantage of all the available data and create a very powerful trading strategy. 

kenbot's main feature is **evolution** : you can [install](https://docs.kenbot.online/pages/Tentacle-Manager.html), 
[modify](https://docs.kenbot.online/pages/Customize-your-kenbot.html) and even [create](https://docs.kenbot.online/pages/Customize-your-kenbot.html#tentacle-customization-kenbot-v0-3) any tentacle you want to build your ideal cryptocurrency trading robot. You can even share your kenbot evolutions !

## Installation
kenbot's installation is **very simple**... because **very documented** ! See the [installation guides](https://www.kenbot.online/guides/#installation) for more info.

#### With executable
Follow the [2 steps installation guide](https://www.kenbot.online/executable_installation/) 

In short:
- Use the latest release on the [release page](https://github.com/gotbase/kenbot/releases/latest)

#### [With Docker](https://docs.kenbot.online/pages/With-Docker.html)
Follow the [docker installation guide](https://www.kenbot.online/docker_installation/) 

In short :
```
docker run -itd --name kenbot -p 80:5001 -v $(pwd)/user:/kenbot/user -v $(pwd)/tentacles:/kenbot/tentacles -v $(pwd)/logs:/kenbot/logs gotbase/kenbot:stable
```
And then open [http://localhost](http://localhost).

#### [With python sources](https://docs.kenbot.online/pages/With-Python-only.html)
Follow the [python installation guide](https://www.kenbot.online/python_installation/) 

In short :
```
git clone https://github.com/gotbase/kenbot.git
cd kenbot
python3 -m pip install -Ur requirements.txt
python3 start.py
```

#### One click deployment
Follow the [Digital Ocean installation guide](https://www.kenbot.online/digital_ocean_installation/) 

In short :

[![Deploy to DO](https://mp-assets1.sfo2.digitaloceanspaces.com/deploy-to-do/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/gotbase/kenbot/tree/master&refcode=40c9737100b1)

- Get 60-day free Digital Ocean hosting by registering with [kenbot referral link](https://m.do.co/c/40c9737100b1).

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/gotbase/kenbot)

- Free 24-hour demo repeatable indefinitely on Okteto simply using your Github account

## Exchanges
[![Binance](../assets/binance-logo.png)](https://www.binance.com)
[![Bitmex](../assets/bitmex-logo.png)](https://bitmex.com)
[![Bitmax](../assets/bitmax-logo.png)](https://bitmax.io)
[![Coinbase](../assets/coinbasepro-logo.png)](https://pro.coinbase.com)
[![Kucoin](../assets/kucoin-logo.png)](https://www.kucoin.com)
[![Bitfinex](../assets/bitfinex-logo.png)](https://www.bitfinex.com)
[![Bittrex](../assets/bittrex-logo.png)](https://bittrex.com)

kenbot supports many [exchanges](https://docs.kenbot.online/pages/Exchanges.html#kenbot-officially-supported-exchanges) thanks to the [ccxt library](https://github.com/ccxt/ccxt). 
To activate trading on an exchange, just configure kenbot with your api keys as described [on the exchange documentation](https://www.kenbot.online/guides/#exchanges).

## Disclaimer
Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS 
AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS. 

Always start by running a trading bot in simulation mode and do not engage money
before you understand how it works and what profit/loss you should
expect.

Do not hesitate to read the source code and understand the mechanism of this bot.

## Sponsors
<table>
<tr>
<td><a href="https://www.jetbrains.com" target="_blank">JetBrains</a> with PyCharm Pro.</td>
<td><a href="https://www.jetbrains.com" target="_blank"><p align="center"><img src="https://resources.jetbrains.com/storage/products/pycharm/img/meta/pycharm_logo_300x300.png" width="100px"></p></a></td>
</tr>
<tr>
<td>Special thanks to <a href="https://m.do.co/c/40c9737100b1" target="_blank">DigitalOcean</a> for hosting kenbot's open source tentacles and community websites.</td>
<td><a href="https://m.do.co/c/40c9737100b1" target="_blank"><p align="center"><img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/PNG/DO_Logo_Horizontal_Blue.png?utm_medium=opensource&utm_source=kenbot"></p></a></td>
</tr>
<tr>
<td>Thanks to <a href="https://okteto.com/" target="_blank">Okteto</a> for allowing kenbot developers to test their changes online with a simple button.</td>
<td><a href="https://okteto.com/" target="_blank"><p align="center"><img src="https://github.com/gotbase/kenbot/blob/assets/okteto.png?raw=true"></p></a></td>
</tr>
</table>
