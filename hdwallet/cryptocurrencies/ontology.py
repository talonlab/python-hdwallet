#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Nist256p1ECC
from ..const import (
    Info, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, Params, XPrivateKeyVersions, XPublicKeyVersions
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


class Ontology(ICryptocurrency):

    NAME = "Ontology"
    SYMBOL = "ONT"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/ontio/ontology",
        "WHITEPAPER": "https://docs.ont.io",
        "WEBSITES": [
            "https://ont.io"
        ]
    })
    ECC = SLIP10Nist256p1ECC
    COIN_TYPE = 1024
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
        "NEO": "Neo"
    })
    DEFAULT_ADDRESS = ADDRESSES.NEO
    PARAMS = Params({
        "ADDRESS_VERSION": 0x17
    })