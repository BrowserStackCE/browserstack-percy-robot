"""Robot Framework keyword library for Percy snapshots.

This library provides a simple keyword to invoke Percy snapshots using the
currently active SeleniumLibrary driver instance.

Usage in Robot Framework:
    Library    PercyLibrary.py

    Percy Snapshot    My Snapshot Name

Make sure PERCY_TOKEN is set in your environment when running tests.
"""

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from percy import percy_screenshot


class PercyLibrary:
    @keyword("Percy Snapshot")
    def percy_snapshot(self, name: str):
        """Take a Percy snapshot using the current SeleniumLibrary driver.

        The SeleniumLibrary browser instance is retrieved via BuiltIn.get_library_instance.
        """
        selib = BuiltIn().get_library_instance("SeleniumLibrary")
        driver = selib.driver
        percy_screenshot(driver, name)
