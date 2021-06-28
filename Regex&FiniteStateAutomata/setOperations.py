from setGraph import *
class setOperations:
    lan=set()
    def str_str(self, x):
        a = setGraph(l=set())
        [x, i] = x.SetFromA(2)
        a.ChangeInitialState(1)
        a.AddAcceptState(i)
        a.AddTrans(a.initialStates, x.initialStates, "epsilon")
        a.AddTrans(a.initialStates, a.acceptStates[0], "epsilon")
        a.AddTrans(x.acceptStates[0], a.acceptStates[0], "epsilon")
        a.AddTrans(x.acceptStates[0], x.initialStates, "epsilon")
        a.AddTransitionToDict(x.trans)
        return a
    def str_or(self, x, y):
        a = setGraph(l=set())
        [x, i] = x.SetFromA(2)
        [y, j] = y.SetFromA(i)
        a.ChangeInitialState(1)
        a.AddAcceptState(j)
        a.AddTrans(a.initialStates, x.initialStates, "epsilon")
        a.AddTrans(a.initialStates, y.initialStates, "epsilon")
        a.AddTrans(x.acceptStates[0], a.acceptStates[0], "epsilon")
        a.AddTrans(y.acceptStates[0], a.acceptStates[0], "epsilon")
        a.AddTransitionToDict(x.trans)
        a.AddTransitionToDict(y.trans)
        return a
    def str_d(self, x, y):
        a = setGraph(l=set())
        [x, i] = x.SetFromA(1)
        [y, j] = y.SetFromA(i)
        a.ChangeInitialState(1)
        a.AddAcceptState(j-1)
        a.AddTrans(x.acceptStates[0], y.initialStates, "epsilon")
        a.AddTransitionToDict(x.trans)
        a.AddTransitionToDict(y.trans)
        return a
    def str_m(self, x):
        a = setGraph(l=set())
        a.ChangeInitialState(1)
        a.AddAcceptState(2)
        a.AddTrans(1,2,x)
        return a