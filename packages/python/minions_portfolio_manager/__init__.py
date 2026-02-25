"""
Minions Portfolio-manager Python SDK

Agent to manage global hierarchies, ecosystems, and projects
"""

__version__ = "0.1.0"


def create_client(**kwargs):
    """Create a client for Minions Portfolio-manager.

    Args:
        **kwargs: Configuration options.

    Returns:
        dict: Client configuration.
    """
    return {
        "version": __version__,
        **kwargs,
    }

from .schemas import *
