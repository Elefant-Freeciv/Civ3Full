;
; The names for city tiles are not free and must follow the following rules.
; The names consists of style name, _ , size. The style name is as specified
; in cities.ruleset file. The size indicates which size city must
; have to be drawn with a tile. E.g. european_4 means that the tile is to be
; used for cities of size 4+ in european style. Obviously the first tile
; must be style_name_0. The sizes must be in ascending order.
; There must also be a style_name_wall tile used to draw the wall and
; an occupied tile to indicate a miltary units in a city.
; The maximum size supported now is 31, but there can only be MAX_CITY_TILES
; normal tiles. The constant is defined in common/city.h and set to 8 now.
;

[spec]

; Format and options of this spec file:
options = "+Freeciv-3.0-spec"

[info]

artists = "
	 Adaptation Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "Civ 3 Full/freeland/big/cities/misc-cities"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 128
dy = 96

tiles = { "row", "column", "tag"

; default tiles

 0,  3, "cd.city"
 0,  3, "cd.city_wall"
 0,  7, "cd.occupied"

 0,  7, "city.asian_occupied_0"
 0,  7, "city.tropical_occupied_0"
 0,  7, "city.celtic_occupied_0"
 0,  7, "city.classical_occupied_0"
 0,  7, "city.babylonian_occupied_0"
 0,  7, "city.european_occupied_0"
 0,  7, "city.industrial_occupied_0"
 0,  7, "city.electricage_occupied_0"
 0,  7, "city.modern_occupied_0"
 0,  7, "city.postmodern_occupied_0"

; used by all city styles

 0,  0, "city.disorder"
 0,  1, "base.airbase_mg"
 0,  2, "tx.airbase_full"
 0,  4, "base.fortress_fg"
 0,  5, "base.fortress_bg"
 0,  6, "extra.ruins_mg"
}
