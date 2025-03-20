class NaiveED:
    def __init__(self):
        self.trace = []
        self.cnt = 0

    def edit_dis_recursive(self, x, y):
        self.cnt += 1
        if y not in self.trace:
            self.trace.append(y)

        if len(x) == 0:
            return len(y)
        if len(y) == 0:
            return len(x)
        delt = 1 if x[-1] != y[-1] else 0
        diag = self.edit_dis_recursive(x[:-1], y[:-1]) + delt
        vert = self.edit_dis_recursive(x[:-1], y) + 1
        horz = self.edit_dis_recursive(x, y[:-1]) + 1

        return min(diag, vert, horz)
