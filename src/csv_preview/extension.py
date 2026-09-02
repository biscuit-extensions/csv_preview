from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class CsvPreview(Extension):
    """Tabular viewer and editor for CSV and TSV files"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("CSV Preview extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("CSV Preview installed successfully.")
