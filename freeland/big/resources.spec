
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-3.3-Devel-2023.Apr.05"

[info]

artists = "
	 Tim F. Smith <yoohootim@hotmail.com> (isotrident graphics)
	 Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "Civ 3 Full/freeland/big/resources"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 128
dy = 64
pixel_border = 0

; Terrain special resources:
tiles = { "row", "column","tag"

 0, 0, "ts.oasis:0"
 0, 1, "ts.oil:0"

 1, 0, "ts.buffalo:0"
 1, 1, "ts.wheat:0"

 2, 0, "ts.pheasant:0"
 2, 1, "ts.silk:0"

 3, 0, "ts.coal:0"
 3, 1, "ts.wine:0"

 4, 0, "ts.gold:0"
 4, 1, "ts.iron:0"

 5, 0, "ts.tundra_game:0"
 5, 1, "ts.furs:0"

 6, 0, "ts.arctic_ivory:0"
 6, 1, "ts.arctic_oil:0"

 7, 0, "ts.peat:0"
 7, 1, "ts.spice:0"

 8, 0, "ts.gems:0"
 8, 1, "ts.fruit:0"

 9, 0, "ts.fish:0"
 9, 1, "ts.whales:0"

 0, 2, "ts.seals:0"
 0, 3, "ts.forest_game:0"

 1, 2, "ts.horses:0"
 1, 3, "ts.grassland_resources:0", "ts.river_resources:0"

 3, 2, "tx.village:0"
 3, 3, "user.attention", "user.infratile"

 4, 2, "tx.mine:0"
 4, 3, "tx.oil_mine:0", "tx.oil_rig:0"

 9, 2, "tx.fallout:0"
 9, 3, "tx.pollution:0"

}
