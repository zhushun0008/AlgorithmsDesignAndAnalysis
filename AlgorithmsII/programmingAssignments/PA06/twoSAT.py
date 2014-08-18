__author__ = 'zhushun0008'

"""TwoSatisfiability.py

Algorithms for solving 2-satisfiability problems.
For theory and references, see http://en.wikipedia.org/wiki/2-satisfiability

All instances should be represented as a directed implication graph in which
the vertices represent variables and (via Not.py) their negations. A variable
may be represented by any hashable Python object, and its negation should
be represented by the object Not(x). For instance, the implication graph
    {1:[2,3], 2:[Not(1),3]}
from the unit tests of this module represents the system of implications
among three logical variables v1, v2, and v3:
    v1 => v2, v1 => v3;  v2 => ~v1, v2 => v3.
An instance is satisfiable if it is possible to assign the Boolean values
True and False to these variables in order to make all implications become
logically correct. These problems have many applications involving problems
in which variables may take on either of two values and pairs of variables
are subject to arbitrary constraints; see the Wikipedia article for details.

If G is a graph of this type,
- Symmetrize(G) extends G by adding the contrapositive of each implication
- Satisfiable(G) returns True or False according to whether the
  2SAT instance can be satisfied. It takes linear time in the size of G.
- Forced(G) returns a dictionary mapping a subset of variables of G to
  values that they are forced to hold in any satisfying assignment.
  The empty dictionary is returned if all variables are free to take either
  truth value, and None is returned if the instance is unsatisfiable.
  Because this uses a reachability algorithm in directed acyclic graphs,
  it is not truly linear time but is still polynomial.

D. Eppstein, April 2009.
"""




def getData(fileName):
    data = open(fileName).readlines()
    formatedData = [tuple(map(int, r.split())) for r in data[1:]]

    return formatedData

def proProcessData(satPairList):
    default = None
    varDic = {}
    varInitDic = {}
    for i in range(len(satPairList)):
        varInitDic[1 + 1] = False

    tempSatPairList = satPairList[:]
    for i in range(len(satPairList)):
        temp = satPairList[i]
        a = temp[0]
        b = temp[1]
        if temp[0] > 0 and temp[1] > 0 :
            if None == varDic.get(temp[0], default):
                varDic[temp[0]] = True
            else:
                if True != varDic[temp[0]]:
                    return False
            if None == varDic.get(temp[1], default):
                varDic[temp[1]] = True
            else:
                if True != varDic[temp[1]]:
                    return False
        if a < 0 and b < 0 :
            a = abs(a)
            if None == varDic.get(a, default):
                 varDic[a] = False
            else:
                if False != varDic[a]:
                    return False
            if None == varDic.get(b, default):
                varDic[b] = False
            else:
                if False != varDic[b]:
                    return False
        if a in varInitDic:
            varInitDic.pop(temp[0], None)
        if b in varInitDic:
            varInitDic.pop(temp[1], None)

        tempSatPairList.remove(temp)

    return varDic, varInitDic, True, tempSatPairList



def papadiSATalgorithm(satPairList):
    result = False



    return result






import math
import random
import gc

def papadimitrou(clauses):

    n = len(clauses)

    for j in xrange(int(math.log(n, 2))):
        assignment = random_assignment(n)
        i = 2*n*n
        while i > 0:
            i -= 1
            clause_index = unsatisfied_clause(clauses, assignment)
            if clause_index is None:
                return 'satisfiable'
            else:
                var_index = abs(clauses[clause_index][random.randint(0, 1)]) - 1
                assignment[var_index] = 1 - assignment[var_index]

    return 'unsatisfiable'


def random_assignment(n):
    return [random.randint(0, 1) for _ in xrange(n)]


def unsatisfied_clause(clauses, assignment):
    for i in xrange(len(clauses)):
        if ((clauses[i][0] < 0 and assignment[abs(clauses[i][0])-1] == 1) or     \
            (clauses[i][0] > 0 and assignment[abs(clauses[i][0])-1] == 0)) and   \
            ((clauses[i][1] < 0 and assignment[abs(clauses[i][1])-1] == 1) or    \
            (clauses[i][1] > 0 and assignment[abs(clauses[i][1])-1] == 0)):
            return i
    return None




def main():
    for i in xrange(1, 7):
        f = open('2sat%i.txt' % i)
        n = int(f.readline())
        clauses = [[int(x) for x in line.split()] for line in f]

        print 'result: %s\n' % papadimitrou(clauses)

        gc.collect()


def twoSATsolver():
    for i in xrange(1, 7):
        satPairList = getData('2sat%i.txt' % i)
        [varDic, result, reducedSatPairList] = proProcessData(satPairList)

        print "length of reducedSatPairList is : " + len(reducedSatPairList)
        if result == False:
            finalResult = 'unsatisfiable'
        else:
            finalResult = papadimitrou(reducedSatPairList)

        print 'result: %s\n' % finalResult
        gc.collect()


twoSATsolver()