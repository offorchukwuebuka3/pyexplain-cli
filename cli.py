import os
import click
import openai
from rich.console import Console

console = Console()

@click.command()
@click.option('--code', prompt='Paste your Python code', help='The Python code to explain.')
def explain_code(code):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        console.print("[bold red]Missing API Key[/bold red]")
        return

    prompt = f"Explain this Python code in plain English:\n\n{code}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        console.print(f"\n[bold cyan]Explanation:[/bold cyan]\n{response['choices'][0]['message']['content']}")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

if __name__ == '__main__':
    explain_code()
