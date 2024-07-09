#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import Union

import secrets
import math

from ...utils import (
    bytes_to_integer, bytes_to_string, integer_to_bytes
)
from ..ientropy import IEntropy


class ELECTRUM_V2_ENTROPY_STRENGTHS:
    """
    Constants representing the entropy strengths for Electrum-V2.
    """

    ONE_HUNDRED_THIRTY_TWO: int = 132
    TWO_HUNDRED_SIXTY_FOUR: int = 264


class ElectrumV2Entropy(IEntropy):
    """
    Improved security with a BIP32-compatible seed and unique wordlist for mnemonic
    generation, providing better entropy and hierarchical deterministic key derivation.

    .. note::
        This class inherits from the ``IEntropy`` class, thereby ensuring that all functions are accessible.

    Here are available Electrum-V2 entropy strengths:

    +--------------------------+-------+
    | Name                     | Value |
    +==========================+=======+
    | ONE_HUNDRED_THIRTY_TWO   |  132  |
    +--------------------------+-------+
    | TWO_HUNDRED_SIXTY_FOUR   |  264  |
    +--------------------------+-------+
    """

    strengths = [
        ELECTRUM_V2_ENTROPY_STRENGTHS.ONE_HUNDRED_THIRTY_TWO,
        ELECTRUM_V2_ENTROPY_STRENGTHS.TWO_HUNDRED_SIXTY_FOUR
    ]

    @classmethod
    def name(cls) -> str:
        """
        Get the name of the entropy class.

        :return: The name of the entropy class.
        :rtype: str

        >>> from hdwallet.entropies.electrum.v2 import ElectrumV2Entropy
        >>> entropy: ElectrumV2Entropy = ElectrumV2Entropy(entropy="...")
        >>> entropy.name()
        "Electrum-V2"
        """

        return "Electrum-V2"

    @classmethod
    def generate(cls, strength: int) -> str:
        """
        Generates a new entropy value with the given strength.

        :param strength: The entropy value.
        :type strength: int

        :return: The generated entropy value for Electrum-V2.
        :rtype: str

        >>> from hdwallet.entropies.electrum.v2 import ElectrumV2Entropy
        >>> ElectrumV2Entropy.generate(strength=...)
        "..."
        """

        return bytes_to_string(
            integer_to_bytes(
                1 << (strength - 1) | secrets.randbits(strength)  # Ensure bit length equals with given strength
            )
        )

    @classmethod
    def is_valid_strength(cls, strength: int) -> bool:
        """
        Check if the provided strength is valid.

        :param strength: The entropy strength to validate.
        :type strength: int

        :return: True if the strength is valid, False otherwise.
        :rtype: bool

        >>> from hdwallet.entropies.electrum.v2 import ElectrumV2Entropy
        >>> ElectrumV2Entropy.is_valid_strength(strength=...)
        ...
        """

        for _strength in cls.strengths:
            if _strength - 11 <= strength <= _strength:
                return True
        return False

    @classmethod
    def are_entropy_bits_enough(cls, entropy: Union[bytes, int]) -> bool:
        """
        Check if the provided entropy has enough bits.

        :param entropy: The entropy value to check.
        :type entropy: Union[bytes, int]

        :return: True if the strength is valid, False otherwise.
        :rtype: bool

        >>> from hdwallet.entropies.electrum.v2 import ElectrumV2Entropy
        >>> ElectrumV2Entropy.are_entropy_bits_enough(entropy=...)
        ...
        """

        if isinstance(entropy, bytes):
            entropy: int = bytes_to_integer(entropy)

        entropy_strength: int = 0 if entropy <= 0 else math.floor(math.log(entropy, 2))
        return cls.is_valid_strength(entropy_strength)