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

    PUBLIC_KEY_ADDRESS_PREFIX = 0x1e
    SCRIPT_ADDRESS_PREFIX = 0x0d
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x0221312b,
        "P2SH": 0x0221312b
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x022d2533,
        "P2SH": 0x022d2533
    })
    MESSAGE_PREFIX = "\x19Divi Signed Message:\n"
    WIF_PREFIX = 0xd4


class Testnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x1e
    SCRIPT_ADDRESS_PREFIX = 0x0d
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x3a805837,
        "P2SH": 0x3a805837
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x3a8061a0,
        "P2SH": 0x3a8061a0
    })
    MESSAGE_PREFIX = "\x19Divi Signed Message:\n"
    WIF_PREFIX = 0xd4


class Divi(ICryptocurrency):

    NAME = "Divi"
    SYMBOL = "DIVI"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/Divicoin/Divi",
        "WHITEPAPER": "https://wiki.diviproject.org/#whitepaper",
        "WEBSITES": [
            "https://www.diviproject.org",
            "https://diviwallet.com"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 301
    SUPPORT_BIP38 = True
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