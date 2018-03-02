class PositiveList(list):
    def append(self, x):
        if x > 0:
            list.append(self, x)
        else:
            raise NonPositiveError()


class NonPositiveError(Exception):
    pass
