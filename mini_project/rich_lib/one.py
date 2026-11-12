from rich import print
#print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())


from rich.console import Console
console = Console()
console.print("Hello", "World!")
console.print("Hello", "World!", style="bold red")

