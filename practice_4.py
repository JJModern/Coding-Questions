class Professor:
    def __init__(self, name, tenured, fields):
        self.name = name
        self.tenured = tenured
        self.fields = fields


class Committee:
    def __init__(self, name, professors):
        self.name = name
        self.professors = professors

    def size(self):
        return len(self.professors)

    def num_tenured(self):
        count = 0
        for prof in self.professors:
            if prof.tenured:
                count += 1
        return count

    def unique_fields(self):
        return_set = set()
        for prof in self.professors:
            return_set = return_set.union(prof.fields)
        return list(return_set)


def get_bad_committees(committees):
    naughty_lst = []
    for committee in committees:
        count_set = set()
        num_tenured = 0
        for prof in committee.professors:
            count_set = count_set.union(prof.fields)
            if prof.tenured:
                num_tenured += 1
        if (
            1 <= len(count_set) <= 2
            and num_tenured < len(committee.professors) // 2 + 1
        ):
            naughty_lst.append(committee)
    return naughty_lst


p1 = Professor("p1", True, ["A", "B"])
p2 = Professor("p2", True, ["B"])
p3 = Professor("p3", True, ["C"])
p4 = Professor("p4", False, ["A"])
p5 = Professor("p5", False, ["A"])
p6 = Professor("p6", False, ["A", "C"])
p7 = Professor("p7", False, ["B"])
c1 = Committee(
    "c1", [p1, p2, p3]
)  # Good: Has enough tenured and enough fields >>> c2 = Committee("c2", [p1, p2, p4, p5, p7]) # Bad
c2 = Committee("c2", [p1, p2, p4, p5, p7])
c3 = Committee("c3", [p1, p4, p6, p7])  # Good: Has enough fields
c4 = Committee("c4", [p1, p2, p4])  # Good: Has enough tenured
c5 = Committee("c5", [p3, p4, p5, p6])  # Bad
c6 = Committee("c6", [p1, p2, p4, p5])  # Bad
committees = [c1, c2, c3, c4, c5, c6]
for c in committees:
    print("{}, {}, {}, {}".format(c.name, c.size(), c.num_tenured(), c.unique_fields()))

bad = get_bad_committees(committees)
for c in bad:
    print(c.name)
