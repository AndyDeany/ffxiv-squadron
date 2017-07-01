import json
from itertools import combinations

from lib.member import Member
from lib.group import Group


with open("assets/data.json") as data_json:
    data = json.load(data_json)

    base_physical = data["base"]["physical"]
    base_mental = data["base"]["mental"]
    base_tactical = data["base"]["tactical"]

    for member in data["members"]:
        Member(**member)


def mission(required_physical, required_mental, required_tactical):
    for members in combinations(Member.members, 4):
        (Group(members, base_physical, base_mental, base_tactical)
         .calculate_missing(required_physical, required_mental, required_tactical))

    Group.sort_groups()

    print("Stat:     | PHY | MEN | TAC | Members")
    print("----------|-----|-----|-----|--------")
    print(" | ".join(("required:", str(required_physical), str(required_mental), str(required_tactical))) + " |")
    print("----------|-----|-----|-----|--------")
    for group in Group.groups[:10]:
        print(" | ".join((" " * 9, str(group.physical), str(group.mental), str(group.tactical), str(group))))
