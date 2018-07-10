class Invite:

    _all = []

    def __init__(self, dinner_party, guest, accepted = False):
        self._dinner_party = dinner_party
        self._guest = guest
        self._accepted = accepted
        Invite._all.append(self)

    @property
    def dinner_party(self):
        return self._dinner_party

    @property
    def guest(self):
        return self._guest

    @property
    def accepted(self):
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        self._accepted = accepted

    @classmethod
    def all(cls):
        return cls._all
