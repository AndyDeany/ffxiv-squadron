class Member:
    """Class for squadron members"""
    members = []

    def __init__(self, physical, mental, tactical):
        self.physical = physical
        self.mental = mental
        self.tactical = tactical

        self.members.append(self)

    def __str__(self):
        return str((self.physical, self.mental, self.tactical))
