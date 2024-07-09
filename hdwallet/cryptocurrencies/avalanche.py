#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Secp256k1ECC
from ..const import (
    Info, Entropies, Mnemonics, Seeds, HDs, Addresses, AddressTypes, Networks, Params, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    HRP = "avax"
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x488ade4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x488b21e
    })
    WIF_PREFIX = 0x80


class Avalanche(ICryptocurrency):

    NAME = "Avalanche"
    SYMBOL = "AVAX"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/ava-labs/avalanchego",
        "WHITEPAPER": "https://www.avalabs.org/whitepapers",
        "WEBSITES": [
            "https://avax.network",
            "https://www.avalabs.org"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 9000
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
        "AVALANCHE": "Avalanche", "ETHEREUM": "Ethereum"
    })
    DEFAULT_ADDRESS = ADDRESSES.AVALANCHE
    ADDRESS_TYPES = AddressTypes({
        "C_CHAIN": "c-chain",
        "P_CHAIN": "p-chain",
        "X_CHAIN": "x-chain"
    })
    DEFAULT_ADDRESS_TYPE = ADDRESS_TYPES.P_CHAIN
    PARAMS = Params({
        "ADDRESS_TYPES": {
            "P_CHAIN": "P-",  # The Platform Chain (P-Chain) prefix
            "X_CHAIN": "X-"  # The Exchange Chain (X-Chain) prefix
        }
    })