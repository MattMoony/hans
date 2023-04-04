"""
Responsible for storing some information
about the state of the CLI session
"""

from dataclasses import dataclass


@dataclass
class CLISessionState:
    """
    Stores some data about the current 
    state of the CLI. This class can be
    extended to store more information
    that might be relevant to CLI functions.
    """

    session: "CmdSession"
    """The prompt session taking commands from the user."""
