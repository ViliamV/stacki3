import argparse

from functools import partial

from i3ipc import Connection, Event


def is_floating(container) -> bool:
    if container.floating:
        # We're on i3: on sway it would be None
        # May be 'auto_on' or 'user_on'
        return "_on" in container.floating
    else:
        # We are on sway
        return container.type == "floating_con"


def set_splitting(i3, _, width: int):
    focused = i3.get_tree().find_focused()
    workspace = focused.workspace()
    number_of_tiled_windows = len([leaf for leaf in workspace.leaves() if not is_floating(leaf)])
    if number_of_tiled_windows == 1:
        focused.command("splith")
    elif number_of_tiled_windows == 2:
        focused.command("splitv")
        focused.command(f"resize set width {width} ppt")


def main():
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
    i3 = Connection()
    i3.on(Event.WINDOW_NEW, partial(set_splitting, width=width))
    i3.on(Event.WINDOW_CLOSE, partial(set_splitting, width=width))
    i3.main()
