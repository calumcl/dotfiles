local wezterm = require 'wezterm';
return {
  font = wezterm.font({
      family="Iosevka",
      harfbuzz_features= {"calt"}
    }),
  color_scheme= "Hopscotch.256",
  use_fancy_tab_bar= true,
  window_decorations= "RESIZE",
  keys = {
    {key="Enter", mods="SUPER",
      action=wezterm.action{SplitVertical={domain="CurrentPaneDomain"}}},
    {key="Enter", mods="SUPER|SHIFT",
      action=wezterm.action{SplitHorizontal={domain="CurrentPaneDomain"}}},
    {key="q", mods="SUPER|SHIFT", action=wezterm.action{CloseCurrentPane={confirm=true}}},
  },
}

