from __future__ import annotations
from typing import Callable, Any

import os
import pwd
import time

from newm.layout import Layout

from newm import (
    SysBackendEndpoint_alsa,
    SysBackendEndpoint_sysfs
)

from pywm import (
    PYWM_MOD_LOGO,
    # PYWM_MOD_ALT
)


mod = PYWM_MOD_LOGO

def on_startup():
    def on_startup():
        init_service = (
            "systemctl --user import-environment \
            DISPLAY WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
            "hash dbus-update-activation-environment 2>/dev/null && \
            dbus-update-activation-environment --systemd \
            DISPLAY WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
            "wl-paste -t text --watch clipman store",
            "waybar",
            "nm-applet --indicator",
        )

        for service in init_service:
            service = f"{service} &"
            os.system(service)

term = 'kitty'


def on_reconfigure():
    os.system("notify-send newm \"Reloaded configuration\" &")

def key_bindings(layout: Layout) -> list[tuple[str, Callable[[], Any]]]:
    return [
        ("M-h", lambda: layout.move(-1, 0)),
        ("M-j", lambda: layout.move(0, 1)),
        ("M-k", lambda: layout.move(0, -1)),
        ("M-l", lambda: layout.move(1, 0)),
        ("M-u", lambda: layout.basic_scale(1)),
        ("M-n", lambda: layout.basic_scale(-1)),
        ("M-t", lambda: layout.move_in_stack(1)),

        ("M-H", lambda: layout.move_focused_view(-1, 0)),
        ("M-J", lambda: layout.move_focused_view(0, 1)),
        ("M-K", lambda: layout.move_focused_view(0, -1)),
        ("M-L", lambda: layout.move_focused_view(1, 0)),

        ("M-C-h", lambda: layout.resize_focused_view(-1, 0)),
        ("M-C-j", lambda: layout.resize_focused_view(0, 1)),
        ("M-C-k", lambda: layout.resize_focused_view(0, -1)),
        ("M-C-l", lambda: layout.resize_focused_view(1, 0)),

        ("M-Return", lambda: os.system(f"{term} &")),
        ("M-r", lambda: os.system("rofi -show run &")),
        ("M-c", lambda: os.system("google-chrome")),
        ("XF86MonBrightnessUp", lambda: os.system("light -A 5")),
        ("XF86MonBrightnessUp", lambda: os.system("light -U 5")),
        ("XF86AudioRaiseVolume", lambda: os.system("amixer set Master 5%+")),
        ("XF86AudioLowerVolume", lambda: os.system("amixer set Master 5%-")),
        ("XF86AudioPlay", lambda: os.system("playerctl play-pause &")),
        ("XF86AudioMute", lambda: os.system("amixer set Master toggle")),
        ("M-q", lambda: layout.close_focused_view()),

        ("M-p", lambda: layout.ensure_locked(dim=True)),
        ("M-P", lambda: layout.terminate()),
        ("M-C", lambda: layout.update_config()),

        ("M-f", lambda: layout.toggle_fullscreen()),

        ("ModPress", lambda: layout.toggle_overview()),
        ("Print", lambda: os.system('grim ~/screen-"$(date +%s)".png &')),
        ("M-Print", lambda: os.system('grim -g "$(slurp)" ~/screen-"$(date\
            +%s)".png &'))

    ]

sys_backend_endpoints = [
    SysBackendEndpoint_sysfs(
        "backlight",
        "/sys/class/backlight/intel_backlight/brightness",
        "/sys/class/backlight/intel_backlight/max_brightness"),
    SysBackendEndpoint_sysfs(
        "kbdlight",
        "/sys/class/leds/smc::kbd_backlight/brightness",
        "/sys/class/leds/smc::kbd_backlight/max_brightness"),
    SysBackendEndpoint_alsa(
        "volume")
]
bar = {
    'enabled': False,
    'top_texts': lambda: [
        pwd.getpwuid(os.getuid())[0],
        time.strftime("%c"),
        "%d%% %s" % (psutil.sensors_battery().percent, "↑" if
                     psutil.sensors_battery().power_plugged else "↓")
    ],
    'bottom_texts': lambda: [
        "CPU: %d%%" % psutil.cpu_percent(interval=1),
        get_nw(),
        "RAM: %d%%" % psutil.virtual_memory().percent
    ]
}

background = {
    'path': '/home/calum/Pictures/wallpapers/gjmbZXv.jpg',
    'anim': True
}

outputs = [
    { 'name': 'eDP-1', 'scale': 2. }
]

pywm = {
    'xkb_layout': "gb",
    'focus_follows_mouse': True,
    'enable_xwayland': True,
}
