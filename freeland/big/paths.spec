
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-3.3-Devel-2023.Apr.05"

[info]

artists = "
         Jacob Nevins
"

[file]
gfx = "Civ 3 Full/freeland/big/paths"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 128
dy = 64
pixel_border = 1

; Terrain special resources:
tiles = { "row", "column","tag"
  0, 0, "path.step"            ; turn boundary within path
  0, 1, "path.exhausted_mp"    ; tip of path, no MP left
  0, 2, "path.normal"          ; tip of path with MP remaining
  0, 3, "path.waypoint"
}
