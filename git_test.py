# Absorption calculator. Status of 2025-10-15

 
if __name__ == "__main__":
    
    # Calculate surface.
    def calc_surface(): 

        print("hello user!\nPlease type in your parameters.\nThis will allow us to complete your calculations:)")
        length, width, height = float(input("Length of room (m) : ")),float(input("Width of room (m) : ")),float(input("Height of room (m) : "))
        print(f"These are dimmensions of your room: {length}x{width}x{height}m")

        walls = length * height * 2 + width * height * 2
        ceilling = length * width
        floor = length * width
        v = length * width * height

        return walls, ceilling, floor, v


    # PAAC - power acoustic absorption coefficeint in air
    # SAC - sound absorption coefficient

    # Calculate specific surface absorption coefficeints in Sabins (square meters).
    def calc_absorption():

        walls, ceilling, floor, v = calc_surface()

        wallsSAC = float(input("Type in walls sound absorption coefficient: "))
        ceillingSAC = float(input("Type in ceilling sound absorption coefficient: "))
        floorSAC = float(input("Type in floor sound absorption coefficient: "))

        airPAAC = 0.001

        airSabin = v * airPAAC
        wallsSabin = walls * wallsSAC
        ceillingSabin = ceilling * ceillingSAC
        floorSabin = floor * floorSAC

        roomAA = airSabin + wallsSabin + ceillingSabin + floorSabin

        return roomAA

    # Calculates demand for acoustic materials, and gives various options for the same room.

    def adaptation_designer(difference):

        ecophonWallpanelSAC = 1.0
        ecophonWallm2 = 1.62

        megaWallpanelSAC = 0.85
        megaWallm2 = 0.9

        ceillingPanelSAC = 1.0
        ceillingPanelm2 = 1.44

        hangingPanelSAC = 2.6 #for each panel
        hangingPanelm2 = 1.44

        floorCarpetSAC = 0.15

        #YOU NEED DIMENSIONS OF SURFACES HERE!!!!!!!
        
        

        return 0


    # Compares the result with ISO standards.

    def ISO_standard_comparator():

        roomAA = calc_absorption()

        roomMinSAC = float(input("Type in the standardized sound absorption coefficient for your room: "))

        if roomAA < roomMinSAC:
                
                difference = roomMinSAC - roomAA
                print(f"Your room has to low sound absorption coefficient! {difference} more Sabins are needed. Choose which acoustic adaptation system is suitable for you")
                
                adaptation_designer(difference)
        else:
                print(f"Well done! You are master in acoustics:)")

        #print(f"Whole room acoustic absorption equals to {calc_absorption(0.001, 0.04, 0.03, 0.02)}")

    ISO_standard_comparator()


