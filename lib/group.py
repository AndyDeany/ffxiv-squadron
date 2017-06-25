class Group:
    groups = []

    @classmethod
    def sort_groups(cls):
        cls.groups.sort(key=lambda g: g.missing)

    def __init__(self, members, base_physical, base_mental, base_tactical):
        self.members = members
        self.physical = base_physical
        self.mental = base_mental
        self.tactical = base_tactical
        for member in self.members:
            self.physical += member.physical
            self.mental += member.mental
            self.tactical += member.tactical

        self.groups.append(self)

    def calculate_missing(self, required_physical, required_mental, required_tactical):
        self.missing = 0
        missing_physical = required_physical - self.physical
        missing_mental = required_mental - self.mental
        missing_tactical = required_tactical - self.tactical
        for missing_stat in (missing_physical, missing_mental, missing_tactical):
            if missing_stat > 0:
                self.missing += missing_stat

    def __str__(self):
        return ", ".join((str(member) for member in self.members))
