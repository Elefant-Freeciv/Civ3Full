
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-3.3-Devel-2023.Apr.05"

[info]

; Apolyton Tileset created by CapTVK with thanks to the Apolyton Civ2
; Scenario Community.

; Special thanks go to:
; Alex Mor and Captain Nemo for their excellent graphics work
; in the scenarios 2194 days war, Red Front, 2nd front and other misc graphics.
; Fairline for his huge collection of original Civ2 unit spanning centuries
; Bebro for his collection of mediveal units and ships

artists = "
    Alex Mor (Alex)
    Allard H.S. Höfelt (AHS)
    Bebro (BB)
    Captain Nemo (Nemo)(MHN)
    CapTVK (CT) <thomas@worldonline.nl>
    Curt Sibling (CS)
    Erwan (Erwan)
    Fairline (GB)
    GoPostal (GP)
    Oprisan Sorin (Sor)
    Tanelorn (T)
    Vodvakov
	 Adptation by Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "Civ 3 Full/freeland/big/units"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 64
dy = 48

tiles = { "row", "column", "tag"

  0,  0, "u.armor"
  0,  1, "u.howitzer"
  0,  2, "u.battleship"
  0,  3, "u.bomber"
  0,  4, "u.cannon"
  0,  5, "u.caravan"
  0,  6, "u.carrier"
  0,  7, "u.catapult"
  0,  8, "u.horsemen"
  0,  9, "u.chariot"
  0, 10, "u.cruiser"
  0, 11, "u.diplomat", "u.barbarian_leader"
  0, 12, "u.fighter"
  0, 13, "u.frigate"
  0, 14, "u.ironclad"
  0, 15, "u.knights"
  0, 16, "u.legion"
  0, 17, "u.mech_inf"
  0, 18, "u.warriors"
  0, 19, "u.musketeers"
  1,  0, "u.nuclear"
  1,  1, "u.phalanx"
  1,  2, "u.riflemen"
  1,  3, "u.caravel"
  1,  4, "u.settlers"
  1,  5, "u.submarine"
  1,  6, "u.transport"
  1,  7, "u.trireme"
  1,  8, "u.archers"
  1,  9, "u.cavalry"
  1, 10, "u.cruise_missile"
  1, 11, "u.destroyer"
  1, 12, "u.dragoons"
  1, 13, "u.explorer"
  1, 14, "u.freight"
  1, 15, "u.galleon"
  1, 16, "u.partisan"
  1, 17, "u.pikemen"
  2,  0, "u.marines"
  2,  1, "u.spy"
  2,  2, "u.engineers"
  2,  3, "u.artillery"
  2,  4, "u.helicopter"
  2,  5, "u.alpine_troops"
  2,  6, "u.stealth_bomber"
  2,  7, "u.stealth_fighter"
  2,  8, "u.aegis_cruiser"
  2,  9, "u.paratroopers"
  2, 10, "u.elephants"
  2, 11, "u.crusaders"
  2, 12, "u.fanatics"
  2, 13, "u.awacs"
  2, 14, "u.worker"

; Veteran Levels: up to 9 military honors for experienced units

;  3, 0, "unit.vet_1"
;  3, 1, "unit.vet_2"
;  3, 2, "unit.vet_3"
;  3, 3, "unit.vet_4"
;  3, 4, "unit.vet_5"
;  3, 5, "unit.vet_6"
;  3, 6, "unit.vet_7"
;  3, 7, "unit.vet_8"
;  3, 8, "unit.vet_9"
;
;  3, 11, "unit.lowfuel"
;  3, 11, "unit.tired"
}

