# SPDX-FileCopyrightText: 2024-present Adam Fourney <adamfo@microsoft.com>
#
# SPDX-License-Identifier: MIT

import asyncio
import base64
from pathlib import Path

import pytest

from markitdown_mcp.__main__ import convert_to_markdown


TEST_FILES_DIR = Path(__file__).resolve().parents[2] / "markitdown" / "tests" / "test_files"


def _call_convert_to_markdown(**kwargs: str | None) -> str:
    return asyncio.run(convert_to_markdown(**kwargs))


def test_convert_to_markdown_accepts_base64_html_payload() -> None:
    payload = base64.b64encode(b"<html><body><h1>Test</h1></body></html>").decode("ascii")

    result = _call_convert_to_markdown(
        content_base64=payload,
        filename="sample.html",
        mimetype="text/html",
        charset="utf-8",
        url="https://example.com/sample.html",
    )

    assert "# Test" in result


def test_convert_to_markdown_uses_filename_to_hint_notebook_payload() -> None:
    payload = base64.b64encode((TEST_FILES_DIR / "test_notebook.ipynb").read_bytes()).decode(
        "ascii"
    )

    result = _call_convert_to_markdown(
        content_base64=payload,
        filename="test_notebook.ipynb",
        mimetype="application/json",
        charset="ascii",
    )

    assert "# Test Notebook" in result
    assert 'print("markitdown")' in result


@pytest.mark.parametrize(
    "content_base64, expected_message",
    [
        ("", "content_base64 must not be empty"),
        ("not-base64", "content_base64 must be valid base64-encoded data"),
    ],
)
def test_convert_to_markdown_rejects_invalid_payloads(
    content_base64: str, expected_message: str
) -> None:
    with pytest.raises(ValueError, match=expected_message):
        _call_convert_to_markdown(content_base64=content_base64)
