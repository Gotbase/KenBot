
Using a webhook with kenbot
============================

There are many ways to wake your kenbot up and make it do something, one of them is using a webhook. With a webhook, you can automatically send messages to your kenbot from any website supporting this system. https://www.tradingview.com is one of them.

In order to be able to receive the webhook's message, kenbot has to expose an API to the web, for this it uses https://ngrok.com/ that acts as a secure intermediary between the internet and your kenbot.

Setting up your kenbot's webhook
---------------------------------


#. In kenbot configuration, add the webhook service.
#. To set up your webhook configuration

   * Option 1: If your kenbot is not exposed to the Internet you have to : 
    - enable ngrok
    - create an account on https://ngrok.com/
    - enter your ngrok token into your kenbot's webhook service configuration.
   * Option 2: If your kenbot is exposed to the Internet you can disable ngrok and set the listening port and ip for the webhook

#. Activate a tentacle using a webhook service (like the trading view signals trading mode).
#. Restart your kenbot.
#. The webhook address will be displayed on your kenbot configuration and printed in your logs.

   .. image:: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/webhook_config.jpg
      :target: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/webhook_config.jpg
      :alt: webhook and tradingview config


   .. image:: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/webhook_log.jpg
      :target: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/webhook_log.jpg
      :alt: webhook log

About ngrok.com
---------------
You can use ngrok with a free account, the only drawback of having a free version is that your webhook address will change at every kenbot restart, you will have to update it on your message sender (like https://www.tradingview.com)
