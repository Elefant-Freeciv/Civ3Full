
[spec]

; Format and options of this spec file:
options = "+Freeciv-3.0-spec"

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

 0, 0, "ts.oasis"
 0, 1, "ts.oil"

 1, 0, "ts.buffalo"
 1, 1, "ts.wheat"

 2, 0, "ts.pheasant"
 2, 1, "ts.silk"

 3, 0, "ts.coal"
 3, 1, "ts.wine"

 4, 0, "ts.gold"
 4, 1, "ts.iron"

 5, 0, "ts.tundra_game"
 5, 1, "ts.furs"

 6, 0, "ts.arctic_ivory"
 6, 1, "ts.arctic_oil"

 7, 0, "ts.peat"
 7, 1, "ts.spice"

 8, 0, "ts.gems"
 8, 1, "ts.fruit"

 9, 0, "ts.fish"
 9, 1, "ts.whales"

 0, 2, "ts.seals"
 0, 3, "ts.forest_game"

 1, 2, "ts.horses"
 1, 3, "ts.grassland_resources", "ts.river_resources"

 3, 2, "tx.village"
 3, 3, "user.attention"

 4, 2, "tx.mine"
 4, 3, "tx.oil_mine", "tx.oil_rig"

 9, 2, "tx.fallout"
 9, 3, "tx.pollution"

}
