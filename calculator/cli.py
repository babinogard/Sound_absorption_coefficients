import typer
from core import ISO_standard_comparator, adaptation_designer
from materials_rooms import Panel, Covering

app = typer.Typer()

@app.command()
def calculate(length: float, width: float, height: float, wallssac: float, ceillingsac: float, floorsac: float, roomminsac: float):

    result, difference = ISO_standard_comparator(length, width, height, wallssac, ceillingsac, floorsac, roomminsac)

    if result == True:
        typer.echo(f"✨ Well done, the room is {difference} above minimal Sabin value ✨")
    elif result == False:
        typer.echo("You need acoustic adaptation. Choose the material for each surface")

        # HERE YOU HAVE TO PRINT OUT LIST OF MATERIALS AND HOW TO CONSTRUCT COMMENT THAT YOU HAVE TO USE
        #enumerate(Panel)
        #enumerate(Covering)
        
        
        a = typer.prompt("Input the coefficients of wall materials", type = float)
        b = typer.prompt("Input the coefficients of ceilling materials", type = float)
        designed_roomAA = adaptation_designer(a, b, length, width, height)

        typer.echo(f"✨ Well done, the room has {designed_roomAA} Sabins now, and it meets ISO standards ✨")

    else:
        typer.echo("Error. Wrong returned value")

if __name__=="__main__":
    app()