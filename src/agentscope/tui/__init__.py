# -*- coding: utf-8 -*-
"""Interactive terminal UI components for AgentScope."""

try:
    from ._ui._chat import ChatUI
    from ._launcher import launch_tui
    from ._ui._messages import MessagesUI
except ImportError as error:
    if error.name == "textual":
        raise ImportError(
            'Install TUI support with: pip install "agentscope[tui]"',
        ) from error
    raise

__all__ = [
    "ChatUI",
    "MessagesUI",
    "launch_tui",
]
