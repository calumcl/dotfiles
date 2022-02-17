from __future__ import annotations
from typing import Callable, Any

import os
import pwd
import time

from newm.layout import Layout
from newm.helper import WobRunner, PaCtl

from pywm import (
    PYWM_MOD_LOGO,
    # PYWM_MOD_ALT
)


mod = PYWM_MOD_LOGO

def on_startup():
    os.system("waybar &")
    init_service = (
        "systemctl --user import-environment \
        DISPLAY WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
        "hash dbus-update-activation-environment 2>/dev/null && \
        dbus-update-activation-environment --systemd \
        DISPLAY WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
        "wl-paste -t text --watch clipman store",
        "nm-applet --indicator",
    )

    for service in init_service:
        service = f"{service} &"
        os.system(service)

term = 'kitty'

wob_runner = WobRunner("wob -a top -M 100")
pactl = PaCtl(0, wob_runner)

def on_reconfigure():
    gnome_schema = 'org.gnome.desktop.interface'
    wm_service_extra_config = (
        f"gsettings set {gnome_schema} gtk-theme 'Materia-compact'",  # change to the theme of your choice
        f"gsettings set {gnome_schema} icon-theme 'Papirus'",  # change to the icon of your choice
        f"gsettings set {gnome_schema} cursor-theme 'Adwaita'",  # change to the cursor of your choice
        f"gsettings set {gnome_schema} font-name 'Cantarell 10'",  # change to the font of your choice
    )

    for config in wm_service_extra_config:
        config = f"{config} &"
        os.system(config)
    
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
        ("M-r", lambda: os.system("wofi &")),
        ("M-c", lambda: os.system("google-chrome")),
        ("XF86MonBrightnessUp", lambda: os.system("light -A 5")),
        ("XF86MonBrightnessUp", lambda: os.system("light -U 5")),
        ("XF86AudioRaiseVolume", lambda: pactl.volume_adj(5)),
        ("XF86AudioLowerVolume", lambda: pactl.volume_adj(-5)),
        ("XF86AudioPlay", lambda: os.system("playerctl play-pause &")),
        ("XF86AudioMute", lambda: pactl.mute()),
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

panels = {
    'lock': {
        'cmd': f'{term} newm-panel-basic lock',
        'w': 0.7,
        'h': 0.7,
        'corner_radius': 50,
    },
}

bar = {'enabled': False}

def rules(view):
    common_rules = {
        'float': True,
        'float_size': (750, 750),
        'float_pos': (0.5, 0.35)
    }
    float_apps = (
        "pavucontrol", "blueman-manager"
    )
    blur_apps = (
        "kitty", "wofi", "waybar"
    )
    if view.app_id in float_apps:
        return common_rules
    if view.app_id in blur_apps:
        return {'blur': {'radius': 5, 'passes': 3}}
    return None


view = {
    'padding': 6,
    'fullscreen_padding': 0,
    'send_fullscreen': False,
    'rules': rules,
    'floating_min_size': False
}

background = {
    'path': '/home/calum/Pictures/wallpapers/gjmbZXv.jpg',
    'anim': True
}

outputs = [
    { 'name': 'eDP-1', 'scale': 1 }
]

pywm = {
    'xkb_layout': "gb",
    'focus_follows_mouse': True,
    'enable_xwayland': True,
}
