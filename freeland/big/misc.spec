
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-3.3-Devel-2023.Apr.05"

[info]

artists = "
	Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "Civ 3 Full/freeland/big/misc"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 128
dy = 64
pixel_border = 0

tiles = { "row", "column","tag"
  0, 0, "tx.darkness"
  0, 0, "t.dither_tile"
  0, 2, "mask.tile"
  0, 3, "tx.fog"
  1, 0, "t.l0.ocean1"
}

