from setGraph import *
class NFAtoDFA:
    def __init__(self, nfa):
        d = nfa.GetFromE(nfa.initialStates)
        e = dict()
        e[nfa.initialStates] = d
        dfa = setGraph(nfa.lan)
        x = 1
        dfa.ChangeInitialState(x)
        y = [[d, x]]
        a = dict()
        a[x] = d
        x +=  1
        while len(y) != 0:
            [z, fr] = y.pop()
            for c in dfa.lan:
                tra_st = nfa.GetFromTra(z, c)
                for s in list(tra_st)[:]:
                    if s not in e:
                        e[s] = nfa.GetFromE(s)
                    tra_st = tra_st.union(e[s])
                if len(tra_st) != 0:
                    if tra_st not in a.values():
                        y.append([tra_st, x])
                        a[x] = tra_st
                        to = x
                        x +=  1
                    else:
                        to = [k for k, v in a.iteritems() if v  ==  tra_st][0]
                    dfa.AddTrans(fr, to, c)
        for num, z in a.iteritems():
            if nfa.acceptStates[0] in z:
                dfa.AddAcceptState(num)
        self.dfa = dfa
        
    def Check_Str(self, string):
        NewSt = self.dfa.initialStates
        for ch in string:
            if ch=="epsilon":
                continue
            arr = list(self.dfa.GetFromTra(NewSt, ch))
            if len(arr) == 0:
                return False
            NewSt = arr[0]
        if NewSt in self.dfa.acceptStates:
            return True
        return False