#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Secp256k1ECC
from ..const import (
    WitnessVersions, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x47
    SCRIPT_ADDRESS_PREFIX = 0x21
    HRP = "viacoin"
    WITNESS_VERSIONS = WitnessVersions({
        "P2WPKH": 0x00,
        "P2WSH": 0x00
    })
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x0488ade4,
        "P2WPKH_IN_P2SH": 0x0488ade4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x0488b21e,
        "P2WPKH_IN_P2SH": 0x0488b21e
    })
    MESSAGE_PREFIX = "\x18Viacoin Signed Message:\n"
    WIF_PREFIX = 0xc7


class Testnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x7f
    SCRIPT_ADDRESS_PREFIX = 0xc4
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x4358394,
        "P2SH": 0x4358394
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x43587cf,
        "P2SH": 0x43587cf
    })
    MESSAGE_PREFIX = "\x18Viacoin Signed Message:\n"
    WIF_PREFIX = 0xff


class Viacoin(ICryptocurrency):

    NAME = "Viacoin"
    SYMBOL = "VIA"
    SOURCE_CODE = "https://github.com/viacoin/viacore-viacoin"
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 14
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