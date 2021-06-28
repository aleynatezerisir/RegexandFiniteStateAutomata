from setOperations import *
import sys
class RegExtoNFA:
    def __init__(self, r):
        newObject = setOperations()
        self.str = '*'
        self.or_op = '|'
        self.oBracket = '('
        self.cBracket = ')'
        ln = set()
        self.s = []
        self.a = []
        p = "aleyna"
        self.flagStr = '.'
        self.ops = [self.or_op, self.flagStr]
        self.reg = r
        self.alp=[]
        for i in range(48,123):
            if (i>47 and i<58) or (i>64 and i<91) or (i>96 and i<123):
                self.alp.append(chr(i))
        for c in self.reg:
            if c in self.alp:
                ln.add(c)
                if p != self.flagStr and (p in self.alp or p in [self.cBracket,self.str]):
                    while(1):
                        if len(self.s) == 0:
                            break
                        top = self.s[len(self.s)-1]
                        if top == self.oBracket:
                            break
                        if top == self.flagStr or top == self.flagStr:
                            op = self.s.pop()
                            self.set_op(op)
                        else:
                            break
                    self.s.append(self.flagStr)
                self.a.append(setOperations().str_m(c))
            elif c  ==  self.oBracket:
                if p != self.flagStr and (p in self.alp or p in [self.cBracket,self.str]):
                    while(1):
                        if len(self.s) == 0:
                            break
                        top = self.s[len(self.s)-1]
                        if top == self.oBracket:
                            break
                        if top == self.flagStr or top == self.flagStr:
                            op = self.s.pop()
                            self.set_op(op)
                        else:
                            break
                    self.s.append(self.flagStr)
                self.s.append(c)
            elif c  ==  self.cBracket:
                if p in self.ops:
                    print "While operating %s,%s ERROR !!" % (c, p)
                    sys.exit()
                while(1):
                    if len(self.s) == 0:
                        print "While operating %s ERROR !!" % c
                        sys.exit()
                    o = self.s.pop()
                    if o == self.oBracket:
                        break
                    elif o in self.ops:
                        self.set_op(o)
            elif c == self.str:
                if p in self.ops or p  == self.oBracket or p == self.str:
                    print "While operating %s,%s ERROR !!" % (c, p)
                    sys.exit()
                self.set_op(c)
            elif c in self.ops:
                if p in self.ops or p  == self.oBracket:
                    print "While operating %s,%s ERROR !!" % (c, p)
                    sys.exit()
                else:
                    while(1):
                        if len(self.s) == 0:
                            break
                        top = self.s[len(self.s)-1]
                        if top == self.oBracket:
                            break
                        if top == c or top == self.flagStr:
                            op = self.s.pop()
                            self.set_op(op)
                        else:
                            break
                    self.s.append(c)
            else:
                print "%s symbol is not defined !!" % c
                sys.exit()
            p = c
        while len(self.s) != 0:
            op = self.s.pop()
            self.set_op(op)
        if len(self.a) > 1:
            print self.a
            print "While shredding regex ERROR !!"
            sys.exit()
        self.nfa = self.a.pop()
        self.nfa.lan = ln
        
    def set_op(self, op):
        if len(self.a) == 0:
            print "Memory is empty with processing %s" % op
            sys.exit()
        if op == self.str:
            a = self.a.pop()
            self.a.append(setOperations().str_str(a))
        elif op in self.ops:
            if len(self.a) < 2:
                print "While operating %s insufficiency error !" % op
                sys.exit()
            a = self.a.pop()
            b = self.a.pop()
            if op == self.or_op:
                self.a.append(setOperations().str_or(b,a))
            elif op == self.flagStr:
                self.a.append(setOperations().str_d(b,a))
