local wezterm = require 'wezterm';
return {
  font = wezterm.font({
      family="Iosevka",
      harfbuzz_features= {"calt"}
    }),
  color_scheme= "lovelace",
  use_fancy_tab_bar= true,
  window_decorations= "RESIZE"
}
