#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Ed25519MoneroECC
from ..const import (
    CoinType, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    STANDARD = 0x12
    INTEGRATED = 0x13
    SUB_ADDRESS = 0x2a


class Stagenet(INetwork):

    STANDARD = 0x18
    INTEGRATED = 0x19
    SUB_ADDRESS = 0x24


class Testnet(INetwork):

    STANDARD = 0x35
    INTEGRATED = 0x36
    SUB_ADDRESS = 0x3f


class Monero(ICryptocurrency):

    NAME = "Monero"
    SYMBOL = "XMR"
    SOURCE_CODE = "https://github.com/monero-project/monero"
    ECC = SLIP10Ed25519MoneroECC
    COIN_TYPE = CoinType({
        "INDEX": 128,
        "HARDENED": True
    })
    NETWORKS = Networks({
        "MAINNET": Mainnet, "STAGENET": Stagenet, "TESTNET": Testnet
    })
    DEFAULT_NETWORK = NETWORKS.MAINNET
    ENTROPIES = Entropies((
        {"MONERO": "Monero"}, "BIP39"
    ))
    MNEMONICS = Mnemonics((
        {"MONERO": "Monero"}, "BIP39"
    ))
    SEEDS = Seeds((
        {"MONERO": "Monero"}, "BIP39"
    ))
    HDS = HDs({
        "MONERO": "Monero"
    })
    DEFAULT_HD = HDS.MONERO
    ADDRESSES = Addresses({
        "MONERO": "Monero"
    })
    DEFAULT_ADDRESS = ADDRESSES.MONERO