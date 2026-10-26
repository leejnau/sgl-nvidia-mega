# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the SGLang project
"""Deployment query widths and prepared token rows; no runtime dependencies."""

DECODE_WIDTHS = (1, 2, 3, 4, 5, 6, 7, 8, 16, 32, 64)
VERIFY_QUERIES = (4, 5, 6, 7, 8)
MAX_ROWS = 64


def token_widths(tokens_per_request: int) -> tuple[int, ...]:
    """q1 retains its decode bins; verification prepares whole requests only."""
    if type(tokens_per_request) is not int or tokens_per_request not in (
        1,
        *VERIFY_QUERIES,
    ):
        raise ValueError("Kimi K3 requires q1 decode or fixed q4-8 verification")
    if tokens_per_request == 1:
        return DECODE_WIDTHS
    return tuple(range(tokens_per_request, MAX_ROWS + 1, tokens_per_request))
