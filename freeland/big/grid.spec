
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-3.3-Devel-2023.Apr.05"

[info]

artists = "
	 Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "Civ 3 Full/freeland/big/grid"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 128
dy = 64
pixel_border = 0

tiles = { "row", "column", "tag"
  0, 0, "grid.main.we"
  0, 1, "grid.main.ns"
  0, 2, "grid.city.we"
  0, 3, "grid.city.ns"

  1, 0, "grid.worked.we"
  1, 1, "grid.worked.ns"
  1, 2, "grid.selected.we"
  1, 3, "grid.selected.ns"

  2, 0, "grid.coastline.we"
  2, 1, "grid.coastline.ns"
;  2, 2, "grid.unavailable"
  2, 3, "grid.unavailable"

  3, 0, "grid.borders.e"
  3, 1, "grid.borders.s"
  3, 2, "grid.borders.w"
  3, 3, "grid.borders.n"
}
