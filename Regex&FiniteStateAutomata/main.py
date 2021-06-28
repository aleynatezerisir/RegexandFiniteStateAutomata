from RegExtoNFA import *
from NFAtoDFA import*

def display(a):
    print "\n"
    print "States ==> ", list(a.states)
    print "Start States ==> ", a.initialStates
    print "Final States ==> ", a.acceptStates
    print ""
    print "FromWhere => ToWhere with 'WhichInput'\n\n"
    for fromstate, tostates in a.trans.items():
        for state in tostates:
            for char in tostates[state]:
                print "  ",
                print fromstate,
                print " ==> ",
                print state,
                print " with ",
                print "(", char , ")",
            print
def checkInput(regex):
    for i in regex:
        if (96<ord(i)) and (123>ord(i)):
            return 0
    if (regex == ""):
        return 0
    return 1

def main():
    regex = "aleyna"

    while(checkInput(regex)==0):
        regex = raw_input("\nPlease Enter Regex (accepting UPPERCASE) : \n\n --> ")

    print "Regular Expression: ", regex

    NewNfa = RegExtoNFA(regex)
    NewDfa = NFAtoDFA(NewNfa.nfa)

    while 1:

        print "\n\n1 -> Display NFA"
        print "2 -> Display DFA"
        print "3 -> Check String"
        print "4 -> Change Regex"
        print "5 -> Exit\n"
        choice = input("Choice: ")
        if (choice == 1):
            print "\n\n\n\tNFA - NFA - NFA"
            display(NewNfa.nfa)
        elif (choice == 2):
            print "\n\n\n\tDFA - DFA-DFA"
            display(NewDfa.dfa)
        elif (choice == 3):
            check_str = "aleyna"
            while(checkInput(check_str)==0):
                check_str = raw_input("Please Enter String (accepting UPPERCASE) : ")
            if(NewDfa.Check_Str(check_str)):
                print "\nAccepted String !" , check_str,
            else:
                print "\nRejected String !" , check_str,
        elif (choice == 4):
            regex = "aleyna"
            while(checkInput(regex)==0):
                regex = raw_input("Please Enter Regex (accepting UPPERCASE) : ")
            NewNfa = RegExtoNFA(regex)
            NewDfa = NFAtoDFA(NewNfa.nfa)
            print "Regular Expression: ", regex
        elif (choice == 5):
            print "\n>>> Closing program...\n"
            break

main()
