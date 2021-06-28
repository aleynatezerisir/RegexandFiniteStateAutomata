class setGraph:
    def __init__(self, l):
        self.states = set()
        self.initialStates = None
        self.acceptStates = []
        self.trans = dict()
        self.lan = l
    def AddTrans(self, f, t, input):
        if isinstance(input, str):
            input = set([input])
        self.states.add(f)
        self.states.add(t)
        if f in self.trans:
            if t in self.trans[f]:
                self.trans[f][t] = self.trans[f][t].union(input)
            else:
                self.trans[f][t] = input
        else:
            self.trans[f] = {t : input}
    def ChangeInitialState(self, durum):
        self.initialStates = durum
        self.states.add(durum)
    def AddAcceptState(self, durum):
        if isinstance(durum, int):
            durum = [durum]
        for s in durum:
            if s not in self.acceptStates:
                self.acceptStates.append(s)
    def AddTransitionToDict(self, x):
        for from_where, to_where in x.items():
            for a in to_where:
                self.AddTrans(from_where, a, to_where[a])
    def GetFromTra(self, durum, k):
        if isinstance(durum, int):
            durum = [durum]
        a = set()
        for x in durum:
            if x in self.trans:
                for y in self.trans[x]:
                    if k in self.trans[x][y]:
                        a.add(y)
        return a
    def GetFromE(self, f):
        a = set()
        b = set([f])
        while len(b)!= 0:
            s = b.pop()
            a.add(s)
            if s in self.trans:
                for t in self.trans[s]:
                    if "epsilon" in self.trans[s][t] and t not in a:
                        b.add(t)
        return a
    def SetFromA(self, s):
        t = {}
        for i in list(self.states):
            t[i] = s
            s += 1
        r = setGraph(self.lan)
        r.ChangeInitialState(t[self.initialStates])
        r.AddAcceptState(t[self.acceptStates[0]])
        for fr, to in self.trans.items():
            for d in to:
                r.AddTrans(t[fr], t[d], to[d])
        return [r, s]