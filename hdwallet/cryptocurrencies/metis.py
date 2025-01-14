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

    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x0488ade4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x0488b21e
    })
    WIF_PREFIX = 0x80


class Metis(ICryptocurrency):

    NAME = "Metis"
    SYMBOL = "METIS"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/MetisProtocol/metis",
        "WHITEPAPER": "https://drive.google.com/file/d/1LS7CmKFt-FkfVXxSNu06hNgoZXxMzTC-/view",
        "WEBSITES": [
            "https://www.metis.io"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 60  # Ethereum coin type
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
        "ETHEREUM": "Ethereum"
    })
    DEFAULT_ADDRESS = ADDRESSES.ETHEREUM