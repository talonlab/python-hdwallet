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
    SCRIPT_ADDRESS_PREFIX = 0x5
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x9e0488b2,
        "P2SH": 0x9e0488b2
    })
    MESSAGE_PREFIX = "\x18Digitalcoin Signed Message:\n"
    WIF_PREFIX = 0x9e


class Digitalcoin(ICryptocurrency):

    NAME = "Digitalcoin"
    SYMBOL = "DGC"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/lomtax/digitalcoin",
        "WHITEPAPER": "https://github.com/lomtax/digitalcoin/blob/master/README.md",
        "WEBSITES": [
            "http://digitalcoin.co",
            "https://digitalcoin.tech"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 18
    SUPPORT_BIP38 = True
    NETWORKS = Networks({
        "MAINNET": Mainnet
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