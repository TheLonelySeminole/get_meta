# get_meta.py

+ Python script using Playerctl to pull metadata from Spotify and output json data to a custom Waybar module
+ Added on-click to play or pause
+ Waybar config
Add "custom/media" to module section and then paste this in config
'''
  "custom/media": {
    "format": "  {}",
    "exec": "/home/william/code/Python/playerctl/get_meta.py",
    "interval": 2,
    "return-type": "json",
    "on-click": "playerctl play-pause"
  },
'''
