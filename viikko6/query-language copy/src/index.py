from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #og koodi
    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(20, "assists"),
    #     PlaysIn("PHI")
    # )

    #eka oma kysely  
    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    ) #vastauksena annettu lista 

      #toka oma kysely
    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR") #=sama kuin ekassa 
     )

    #kolmas oma kysely
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all)) # = 958


    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
