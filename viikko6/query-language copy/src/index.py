from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from query_builder import QueryBuilder


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

    # #eka oma kysely  
    # matcher = And(
    #     Not(HasAtLeast(2, "goals")),
    #     PlaysIn("NYR")
    # ) #vastauksena annettu lista 

    #   #toka oma kysely
    # matcher = And(
    #     HasFewerThan(2, "goals"),
    #     PlaysIn("NYR") #=sama kuin ekassa 
    #  )

    # #kolmas oma kysely
    # filtered_with_all = stats.matches(All())
    # print(len(filtered_with_all)) # = 958

    # matcher = Or(
    #     HasAtLeast(45, "goals"),
    #     HasAtLeast(70, "assists")
    # )

    # for player in stats.matches(matcher):
    #     print(player)
    
    # matcher = And(
    #     HasAtLeast(70, "points"),
    #     Or(
    #         PlaysIn("NYR"),
    #         PlaysIn("FLA"),
    #         PlaysIn("BOS")
    #     )
    # )

    # for player in stats.matches(matcher):
    #     print(player)

    query = QueryBuilder()

    m1 = (query.plays_in("PHI").has_at_least(10, "assists").has_fewer_than(10, "goals"))

    m2 = (query.plays_in("EDM").has_at_least(50, "points"))

    matcher = query.one_of(m1, m2).build()

    for player in stats.matches(matcher):
        print(player)


    matcher = (query.one_of(query.plays_in("PHI").has_at_least(10, "assists").has_fewer_than(10, "goals"),query.plays_in("EDM").has_at_least(50, "points")).build())

    for player in stats.matches(matcher):
        print(player)





if __name__ == "__main__":
    main()
