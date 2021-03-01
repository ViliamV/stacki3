import argparse
import asyncio

from functools import partial

from i3ipc import Event
from i3ipc.aio import Connection


def is_floating(container) -> bool:
    if container.floating:
        # We're on i3: on sway it would be None
        # May be 'auto_on' or 'user_on'
        return "_on" in container.floating
    else:
        # We are on sway
        return container.type == "floating_con"


async def set_splitting(i3, _, width: int) -> None:
    focused = (await i3.get_tree()).find_focused()
    if focused is None:
        return
    workspace = focused.workspace()
    number_of_tiled_windows = len([leaf for leaf in workspace.leaves() if not is_floating(leaf)])
    if number_of_tiled_windows == 1:
        await focused.command("splith")
    elif number_of_tiled_windows == 2:
        await focused.command("splitv")
        await focused.command(f"resize set width {width} ppt")


async def amain():
    parser = argparse.ArgumentParser(description="Stack layout for i3/sway wm.")
    parser.add_argument(
        "width",
        type=int,
        nargs="?",
        default=50,
        help="Optional width of second window in %%. Default: %(default)s",
    )
    args = parser.parse_args()
    width = min(max(args.width, 0), 100)
    i3 = await Connection(auto_reconnect=True).connect()
    i3.on(Event.WINDOW_NEW, partial(set_splitting, width=width)) # type: ignore
    i3.on(Event.WINDOW_CLOSE, partial(set_splitting, width=width)) # type: ignore
    await i3.main()


def main():
    asyncio.run(amain())
