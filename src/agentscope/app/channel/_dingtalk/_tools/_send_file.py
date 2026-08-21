# -*- coding: utf-8 -*-
"""Send a workspace file to a specified DingTalk user or group."""

from pathlib import Path

from pydantic import Field

from .....message import TextBlock, ToolResultState
from .....tool import ParamsBase, ToolChunk
from ._base import _ack, _DingTalkToolBase


class _SendFileParams(ParamsBase):
    """Arguments for sending a workspace file to a target."""

    path: str = Field(
        description="Absolute path to a file in the calling workspace.",
    )
    target: str = Field(
        pattern=r"^(user|group):.+$",
        description="Encoded target returned by ListConversations or "
        "ListUsers.",
    )


class SendFile(_DingTalkToolBase):
    """Send a supported workspace file to a DingTalk target."""

    name: str = "SendFile"
    description: str = """Send a workspace file to a specified DingTalk user \
or group.

Supported DingTalk file extensions are doc, docx, pdf, rar, xlsx, and zip. \
Obtain ``target`` from a discovery tool. The operation requires \
confirmation. Use ``SendImage`` for inline images."""
    is_read_only: bool = False
    input_schema: dict = _SendFileParams.model_json_schema()

    async def __call__(self, path: str, target: str) -> ToolChunk:
        """Read a workspace file and send it to a target.

        Args:
            path (`str`): Workspace file path.
            target (`str`): Encoded DingTalk target.

        Returns:
            `ToolChunk`: DingTalk acceptance or workspace error.
        """
        # Refuse an oversized file before reading it: the channel
        # checks again after, but a limit that only applies once the
        # bytes are in memory does not limit anything.
        entry = await self._backend.stat(path)
        limit = self._channel.max_media_bytes
        if entry is not None and (entry.size_bytes or 0) > limit:
            return ToolChunk(
                content=[
                    TextBlock(
                        text=(
                            f"SendFile: {path!r} is larger than the "
                            f"{limit}-byte limit."
                        ),
                    ),
                ],
                state=ToolResultState.ERROR,
            )
        try:
            raw = await self._backend.read_file(path)
        except Exception as error:  # pylint: disable=broad-except
            return ToolChunk(
                content=[
                    TextBlock(
                        text=f"SendFile: cannot read {path!r}: {error}",
                    ),
                ],
                state=ToolResultState.ERROR,
            )
        file_name = Path(path).name
        accepted = await self._channel.send_file_to(
            target,
            raw,
            file_name,
        )
        return _ack(accepted, f"file {file_name} to {target}")
