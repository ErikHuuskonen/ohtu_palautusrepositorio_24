from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    # Kysytään käyttäjältä maa ja kausi
    country = input("Enter the country code (e.g., FIN): ").strip().upper()
    season = input("Enter the season (e.g., 2023-24): ").strip()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(country)

    # Tulostetaan taulukko Rich-kirjaston avulla
    console = Console()
    table = Table(title=f"Players from {country} - Season {season}")

    table.add_column("Name", style="cyan", justify="left")
    table.add_column("Team", style="magenta", justify="center")
    table.add_column("Goals", style="green", justify="center")
    table.add_column("Assists", style="yellow", justify="center")
    table.add_column("Points", style="bold red", justify="center")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points()))

    console.print(table)

if __name__ == "__main__":
    main()



