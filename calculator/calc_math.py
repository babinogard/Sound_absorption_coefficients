from tabulate import tabulate
from materials_rooms import Panel, PANELS

from dataclasses import fields
'''
import typer

print(typer.__file__)

app = typer.Typer()

@app.command()
def func(value: int, number: int):

    if value > number:
        typer.echo("Value is bigger than number")
    
    elif value < number:
        typer.echo("Value is smaller than number")

    elif value == number:
        typer.echo("Value is equal to number")

    else:
        typer.echo("Error: wrong value")

if __name__=="__main__":
    app()
'''
def numerate():

#    for x in fields(Panel):
#        print(x.name, x.)

#    for x, p in enumerate(PANELS, 1):
#        print(tabulate(f"{x}.{p.name},  {p.function},  {p.absorption}"))
    

    headers = ["number", "name", "function", "absorption", "surface", "length", "width"]
    print("\n" + tabulate(PANELS, headers=headers)+ "\n")

numerate()