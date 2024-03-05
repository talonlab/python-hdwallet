#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Any, Union
)

from ..libs.base32 import (
    encode_no_padding, decode
)
from ..ecc import (
    IPublicKey, SLIP10Ed25519PublicKey, validate_and_get_public_key
)
from ..cryptocurrencies import Stellar
from ..crypto import xmodem_crc
from ..utils import (
    get_bytes, bytes_reverse, integer_to_bytes, bytes_to_string
)
from .iaddress import IAddress


class StellarAddress(IAddress):

    checksum_length: int = Stellar.PARAMS.CHECKSUM_LENGTH
    address_types: dict = {
        "private_key": Stellar.PARAMS.ADDRESS_TYPES.PRIVATE_KEY,
        "public_key": Stellar.PARAMS.ADDRESS_TYPES.PUBLIC_KEY
    }

    @staticmethod
    def name() -> str:
        return "Stellar"

    @staticmethod
    def compute_checksum(public_key: bytes) -> bytes:
        return bytes_reverse(xmodem_crc(public_key))

    @classmethod
    def encode(cls, public_key: Union[bytes, str, IPublicKey], **kwargs: Any) -> str:

        if not kwargs.get("address_type") or \
                kwargs.get("address_type") == "public_key":
            address_type: int = cls.address_types["public_key"]
        elif kwargs.get("address_type") == "private_key":
            address_type: int = cls.address_types["private_key"]
        else:
            raise ValueError("Invalid stellar address type")

        public_key: IPublicKey = validate_and_get_public_key(
            public_key=public_key, public_key_cls=SLIP10Ed25519PublicKey
        )
        payload: bytes = integer_to_bytes(address_type) + public_key.raw_compressed()[1:]
        checksum: bytes = cls.compute_checksum(payload)

        return encode_no_padding((payload + checksum).hex())

    @classmethod
    def decode(cls, address: str, **kwargs: Any) -> str:

        if not kwargs.get("address_type") or \
                kwargs.get("address_type") == "public_key":
            address_type: int = cls.address_types["public_key"]
        elif kwargs.get("address_type") == "private_key":
            address_type: int = cls.address_types["private_key"]
        else:
            raise ValueError("Invalid stellar address type")

        address_decode: bytes = get_bytes(decode(address))

        expected_length: int = (
            SLIP10Ed25519PublicKey.compressed_length() + cls.checksum_length
        )
        if len(address_decode) != expected_length:
            raise ValueError(f"Invalid length (expected: {expected_length}, got: {len(address_decode)})")

        checksum: bytes = address_decode[-1 * cls.checksum_length:]
        payload: bytes = address_decode[:-1 * cls.checksum_length]

        address_type_got: int = payload[0]
        if address_type != address_type_got:
            raise ValueError(f"Invalid address type (expected: {address_type}, got: {address_type_got})")

        checksum_got: bytes = cls.compute_checksum(payload)
        if checksum != checksum_got:
            raise ValueError(f"Invalid checksum (expected: {bytes_to_string(checksum)}, got: {bytes_to_string(checksum_got)})")

        public_key: bytes = payload[1:]
        if not SLIP10Ed25519PublicKey.is_valid_bytes(public_key):
            raise ValueError(f"Invalid {SLIP10Ed25519PublicKey.name()} public key {bytes_to_string(public_key)}")

        return bytes_to_string(public_key)