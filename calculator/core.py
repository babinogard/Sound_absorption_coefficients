#from materials_rooms import Panel, Covering, Room


def calc_surface(length, width, height): 

    walls = length * height * 2 + width * height * 2
    ceilling = length * width
    floor = length * width
    v = length * width * height

    return walls, ceilling, floor, v

# PAAC - power acoustic absorption coefficeint in air
# SAC - sound absorption coefficient

# Calculate specific surface absorption coefficeints in Sabins (square meters).
def calc_absorption(length, width, height, wallsSAC, ceillingSAC, floorSAC):

    walls, ceilling, floor, v = calc_surface(length, width, height)

    airPAAC = 0.001

    airSabin = v * airPAAC
    wallsSabin = walls * wallsSAC
    ceillingSabin = ceilling * ceillingSAC
    floorSabin = floor * floorSAC

    roomAA = airSabin + wallsSabin + ceillingSabin + floorSabin

    return roomAA

# Calculates demand for acoustic materials, and gives various options for the same room.

def adaptation_designer(wallsSAC, ceillingSAC, ldim, wdim, hdim):

    ecophonWallpanelSAC = 1.0
    ecophonWallm2 = 1.62

    megaWallpanelSAC = 0.85
    megaWallm2 = 0.9

    ceillingPanelSAC = 1.0
    ceillingPanelm2 = 1.44

    hangingPanelSAC = 2.6 #for each panel
    hangingPanelm2 = 1.44

    floorCarpetSAC = 0.15

    # RECALLING DIMMENSIONS OF SURFACES HERE
    
    walls, ceilling, floor, v = calc_surface(ldim, wdim, hdim)
    
    numberWallPanels = walls//megaWallm2
    numberCeillingPanels = ceilling//ceillingPanelm2

    # RECALCULATION OF SOUND ABSORPTION COEFFICIENTS
    a = walls - numberWallPanels * megaWallm2
    b = ceilling - numberCeillingPanels * ceillingPanelm2

    fullWallABS = numberWallPanels * megaWallm2 * megaWallpanelSAC + a * wallsSAC
    fullCeillingABS = numberCeillingPanels * ceillingPanelm2 * ceillingPanelSAC + b * ceillingSAC
    fullFloorABS = floor * floorCarpetSAC

    designed_roomAA = fullWallABS +fullCeillingABS + fullFloorABS

    return designed_roomAA

# Compares the result with ISO standards.

def ISO_standard_comparator(length, width, height, wallsSAC, ceillingSAC, floorSAC, roomMinSAC):

    roomAA = calc_absorption(length, width, height, wallsSAC, ceillingSAC, floorSAC)

    # You should create base of various rooms
    difference = roomMinSAC - roomAA

    if roomAA < roomMinSAC:

            #HERE SHOULD BE SOME BOOLEAN STATEMENT THAT RETURN VALUE TO CLI
            result = False
            #print(f"Your room has to low sound absorption coefficient! {difference} more Sabins are needed. Choose which acoustic adaptation system is suitable for you")
            
            #adaptation_designer(difference, wallsSAC, ceillingSAC)
    else:
            #HERE SHOULD BE ANOTHER BOOLEAN STATEMENT THAT RETURN VALUE TO CLI
            result = True
            #print(f"Well done! You are master in acoustics:)")

    #print(f"Whole room acoustic absorption equals to {calc_absorption(0.001, 0.04, 0.03, 0.02)}")
    return result, difference