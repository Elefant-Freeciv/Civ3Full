
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-3.3-Devel-2023.Apr.05"

[info]

artists = "
    Tatu Rissanen <tatu.rissanen@hut.fi>
	 Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "Civ 3 Full/freeland/big/unitextras"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 128
dy = 96

tiles = { "row", "column", "tag"

; Veteran Levels: up to 9 military honors for experienced units

  0, 0, "unit.vet_1"
  0, 1, "unit.vet_2"
  0, 2, "unit.vet_3"
  0, 3, "unit.vet_4"
  0, 4, "unit.vet_5"
  0, 5, "unit.vet_6"
  0, 6, "unit.vet_7"
  0, 7, "unit.vet_8"
  0, 8, "unit.vet_9"

  0, 11, "unit.lowfuel"
  0, 11, "unit.tired"
}
