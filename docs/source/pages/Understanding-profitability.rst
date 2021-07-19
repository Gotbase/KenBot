
Profitability in kenbot
========================

Every asset in kenbot is valued using the **reference market** setting (available in `Trading settings <Trader.html#reference-market>`_\ ). Profitabily follows this principle.

To compute its profitability, kenbot evaluates the value of all its traded assets (the ones available for trading in its configuration) by getting their value in reference market. Profitability is the difference between the total value of the traded assets when the kenbot session started and the total value of current holdings at the moment profitability is displayed.


.. image:: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/home.jpg
   :target: https://raw.githubusercontent.com/gotbase/kenbot/assets/wiki_resources/home.jpg
   :alt: home


Current Portfolio
-----------------

Current Portfolio is the profitability (as always evaluated versus reference market) of the current holdings. It is the difference in percents between the current portfolio value and its value at the beginning of the kenbot session. Since it's the current holdings, all trades have been take into account in this value.

Initial Portfolio
-----------------

Initial Portfolio is the profitability of the initial portfolio (as if kenbot did not trade at all and holdings would have remain the same). It is the difference in percents between this initial portfolio value at the moment profitability is displayed and its value at the beginning of the kenbot session.

Traded symbols average profitability
------------------------------------

Traded symbols average profitability is the average value difference in percents of all traded assets. It does not take holdings into account. It can be used to have a quick view of the global state of the traded assets relatively to the reference market.
