#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Secp256k1ECC
from ..const import (
    Info, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x3f
    SCRIPT_ADDRESS_PREFIX = 0x7d
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0xee8031e8,
        "P2SH": 0xee8031e8
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0xee80286a,
        "P2SH": 0xee80286a
    })
    MESSAGE_PREFIX = None
    WIF_PREFIX = 0xbf


class Testnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x7f
    SCRIPT_ADDRESS_PREFIX = 0xc4
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x76c1077a,
        "P2SH": 0x76c1077a
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x76c0fdfb,
        "P2SH": 0x76c0fdfb
    })
    MESSAGE_PREFIX = None
    WIF_PREFIX = 0xff


class ShadowCash(ICryptocurrency):

    NAME = "Shadow Cash"
    SYMBOL = "SDC"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/shadowproject/shadow",
        "WHITEPAPER": "https://github.com/shadowproject/whitepapers",
        "WEBSITES": [
            "http://shadowproject.io"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 35
    NETWORKS = Networks({
        "MAINNET": Mainnet, "TESTNET": Testnet
    })
    DEFAULT_NETWORK = NETWORKS.MAINNET
    ENTROPIES = Entropies({
        "BIP39"
    })
    MNEMONICS = Mnemonics({
        "BIP39"
    })
    SEEDS = Seeds({
        "BIP39"
    })
    HDS = HDs({
        "BIP32", "BIP44"
    })
    DEFAULT_HD = HDS.BIP44
    ADDRESSES = Addresses({
        "P2PKH", "P2SH"
    })
    DEFAULT_ADDRESS = ADDRESSES.P2PKH