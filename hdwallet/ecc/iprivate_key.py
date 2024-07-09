#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from __future__ import annotations

from typing import Any
from abc import (
    ABC, abstractmethod
)

from .ipublic_key import IPublicKey


class IPrivateKey(ABC):

    @staticmethod
    @abstractmethod
    def name() -> str:
        pass

    @classmethod
    @abstractmethod
    def from_bytes(cls, private_key: bytes) -> "IPrivateKey":
        pass

    @abstractmethod
    def raw(self) -> bytes:
        pass

    @abstractmethod
    def public_key(self) -> IPublicKey:
        pass

    @abstractmethod
    def underlying_object(self) -> Any:
        pass

    @staticmethod
    @abstractmethod
    def length() -> int:
        pass

    @classmethod
    def is_valid_bytes(cls, private_key: bytes) -> bool:
        """
        Checks if the given point is a valid bytes.

        :param private_key: The bytes to be validated.
        :type private_key: bytes

        :return: True if the point is valid, False otherwise.
        :rtype: bool

        >>> from {module_path} import {class_name}
        >>> {class_name}.is_valid_bytes(private_key=...)
        ...
        """

        try:
            cls.from_bytes(private_key)
            return True
        except ValueError:
            return False