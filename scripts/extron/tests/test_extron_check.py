"""Unit tests for the Extron ControlScript module checker
(scripts/extron/extron_check.py).

These drive the AST-based constraint checks that verify a generated device
module obeys reference/extron/EXTRON_CONSTRAINTS.md. The checks are pure
(stdlib `ast` only), so they run on any platform with no Extron toolchain and
no external type checker installed.

Each fixture below is a minimal device module: GOOD_* sources must produce no
diagnostics for the code under test; BAD_* sources must each raise exactly the
one diagnostic code they are named for.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import extron_check as ec  # noqa: E402


def codes(source):
    """Return the set of diagnostic codes raised for a module source string."""
    return {d.code for d in ec.check_source(source)}


# --- Fixtures -------------------------------------------------------------

# A correct async Ethernet module (trimmed from EXTRON_PATTERNS.md §1):
# ReceiveData is buffered, Connect() result is checked, no blocking sleep,
# no SendAndWait mixed with ReceiveData. It must be completely clean.
GOOD_ASYNC = r'''
from extronlib.interface import EthernetClientInterface
from extronlib.system import Wait

class Display:
    def __init__(self, host):
        self._link = EthernetClientInterface(host, 23)
        self._buffer = b''
        self._link.ReceiveData = self._onRx

    def Connect(self):
        if 'Connected' not in self._link.Connect(10):
            Wait(5, self.Connect)

    def _onRx(self, interface, data):
        self._buffer += data
        while True:
            frame, delim, rest = self._buffer.partition(b'\r')
            if not delim:
                break
            self._buffer = rest

    def SetPower(self, on):
        self._link.Send(b'PWR=ON\r' if on else b'PWR=OFF\r')
'''

# A correct synchronous poller (EXTRON_PATTERNS.md §3): uses SendAndWait and
# has NO ReceiveData handler, so it must NOT trip the mixing check.
GOOD_POLLER = r'''
import re
from extronlib.interface import EthernetClientInterface
from extronlib.system import Wait

class Poller:
    def __init__(self, host, port):
        self._link = EthernetClientInterface(host, port)
        self._rex = re.compile(b'PWR=(ON|OFF)\r')

    def Connect(self):
        if 'Connected' not in self._link.Connect(10):
            Wait(5, self.Connect)

    def QueryPower(self):
        resp = self._link.SendAndWait(b'PWR?\r', 0.3, deliRex=self._rex)
        return bool(resp)
'''

# ReceiveData bound via the @event decorator instead of attribute assignment,
# still buffered. Must be clean (exercises decorator-based handler discovery).
GOOD_EVENT_DECORATOR = r'''
from extronlib import event
from extronlib.interface import EthernetClientInterface

client = EthernetClientInterface('1.2.3.4', 23)
_buffer = b''

@event(client, 'ReceiveData')
def onRx(interface, data):
    global _buffer
    _buffer += data
'''

# Blocking sleep — violates constraint #9.
BAD_SLEEP = r'''
import time
from extronlib.interface import EthernetClientInterface

class Dev:
    def __init__(self, host):
        self._link = EthernetClientInterface(host, 23)

    def Reset(self):
        self._link.Send(b'RESET\r')
        time.sleep(2)
        self._link.Send(b'GO\r')
'''

# Connect() result discarded — violates constraint #7.
BAD_CONN = r'''
from extronlib.interface import EthernetClientInterface

class Dev:
    def __init__(self, host):
        self._link = EthernetClientInterface(host, 23)

    def Connect(self):
        self._link.Connect(10)
'''

# ReceiveData handler parses the raw event data as a whole message with no
# buffering — violates constraints #4/#5.
BAD_RXBUF = r'''
from extronlib.interface import EthernetClientInterface

class Dev:
    def __init__(self, host):
        self._link = EthernetClientInterface(host, 23)
        self._link.ReceiveData = self._onRx

    def _onRx(self, interface, data):
        text = data.decode()
        if text.startswith('PWR=ON'):
            self.power = True
'''

# Same interface bound to ReceiveData AND used with SendAndWait — constraint #6.
BAD_MIX = r'''
from extronlib.interface import EthernetClientInterface

class Dev:
    def __init__(self, host):
        self._link = EthernetClientInterface(host, 23)
        self._buffer = b''
        self._link.ReceiveData = self._onRx

    def _onRx(self, interface, data):
        self._buffer += data

    def Poll(self):
        return self._link.SendAndWait(b'PWR?\r', 0.3)
'''


# --- Good sources are clean ----------------------------------------------

@pytest.mark.parametrize("source", [GOOD_ASYNC, GOOD_POLLER, GOOD_EVENT_DECORATOR])
def test_good_sources_have_no_diagnostics(source):
    assert ec.check_source(source) == []


# --- Each bad source raises exactly its own code -------------------------

def test_bad_sleep_flags_only_sleep():
    assert codes(BAD_SLEEP) == {"EX-SLEEP"}


def test_bad_conn_flags_only_conn():
    assert codes(BAD_CONN) == {"EX-CONN"}


def test_bad_rxbuf_flags_only_rxbuf():
    assert codes(BAD_RXBUF) == {"EX-RXBUF"}


def test_bad_mix_flags_only_mix():
    assert codes(BAD_MIX) == {"EX-MIX"}


# --- Diagnostics carry a line number and a message -----------------------

def test_diagnostic_has_line_and_message():
    diags = ec.check_source(BAD_SLEEP)
    assert len(diags) == 1
    d = diags[0]
    assert d.line > 0
    assert d.message
    assert d.severity in ("error", "warning")


# --- Syntax errors are reported, not raised ------------------------------

def test_syntax_error_is_reported_as_diagnostic():
    diags = ec.check_source("def broken(:\n    pass\n")
    assert any(d.code == "EX-SYNTAX" for d in diags)
