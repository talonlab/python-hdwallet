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

    PUBLIC_KEY_ADDRESS_PREFIX = 0x37
    SCRIPT_ADDRESS_PREFIX = 0x8
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x221312b,
        "P2SH": 0x221312b
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x22d2533,
        "P2SH": 0x22d2533
    })
    MESSAGE_PREFIX = "\x18ProjectCoin Signed Message:\n"
    WIF_PREFIX = 0x75


class ProjectCoin(ICryptocurrency):

    NAME = "Project Coin"
    SYMBOL = "PRJ"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/projectcoincore/ProjectCoin",
        "WEBSITES": [
            "https://projectcoin.net"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 533
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