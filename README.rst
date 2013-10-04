=======
cardsim
=======


Simulations of card games, written in Python.
Probably useful to no one, but fun & a good brain-break/kata for me.

:author: Daniel Lindsley
:license: New BSD
:version: 0.1.0


Requirements
============

* Python 3.3.2+


War
===

Usage::

    # Without jitter, cards are picked up in a consistent order post-win.
    python war.py

    # With jitter, cards are picked up in a random order post-win.
    # Yes, it turns out that matters!
    python war.py yes

