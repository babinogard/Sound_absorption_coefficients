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
