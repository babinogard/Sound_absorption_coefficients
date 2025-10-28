import typer
from core import ISO_standard_comparator, adaptation_designer
from materials_rooms import Panel
from materials_rooms import Covering

app = typer.Typer()

@app.command
def calculate(length: float, width: float, height: float, wallsSAC: float, ceillingSAC: float, floorSAC: float, roomMinSAC: float):

    result, difference = ISO_standard_comparator(length, width, height, wallsSAC, ceillingSAC, floorSAC, roomMinSAC)

    if result == True:
        print(f"Well done, the room is {difference} above minimal Sabin value")
    elif result == False:
        print("You need acoustic adaptation. Choose the material for each surface")
        # HERE YOU HAVE TO PRINT OUT LIST OF MATERIALS AND HOW TO CONSTRUCT COMMENT THAT YOU HAVE TO USE
        enumerate(Panel)
        enumerate(Covering)

        designed_roomAA = adaptation_designer(wallsSAC, ceillingSAC)



    else:
        print("Error. Wrong returned value")

if __name__=="__main__":
    app()