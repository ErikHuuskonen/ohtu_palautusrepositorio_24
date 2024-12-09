from matchers import All, And, Or, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, matchers=None):
        if matchers is None:
            matchers = []
        self._matchers = matchers

    def plays_in(self, team):
        return QueryBuilder(self._matchers + [PlaysIn(team)])

    def has_at_least(self, value, attr):
        return QueryBuilder(self._matchers + [HasAtLeast(value, attr)])

    def has_fewer_than(self, value, attr):
        return QueryBuilder(self._matchers + [HasFewerThan(value, attr)])

    def one_of(self, *queries):
        matchers = [query.build() if isinstance(query, QueryBuilder) else query for query in queries]
        return QueryBuilder(self._matchers + [Or(*matchers)])

    def build(self):
        if not self._matchers:
            return All()
        if len(self._matchers) == 1:
            return self._matchers[0]
        return And(*self._matchers)