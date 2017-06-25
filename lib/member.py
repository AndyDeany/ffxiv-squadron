class Member:
    """Class for squadron members"""
    members = []

    def __init__(self, name, physical, mental, tactical):
        self.name = name
        self.physical = physical
        self.mental = mental
        self.tactical = tactical

        self.members.append(self)

    def __str__(self):
        return self.name + " " + str((self.physical, self.mental, self.tactical))
