import permutation
import copy

def getPriorProb(prior:dict, choose):
    return prior[choose] / sum(prior.values())

def calcExp(answers):
    exp = 0
    thisPrior = copy.copy(permutation.prior)

    for i in range(len(answers)):
        choose = answers[i]['choose']
        myProb = permutation.probMat[i][choose]
        priorProb = getPriorProb(thisPrior, choose)
        postProb = (myProb * priorProb) / ((myProb * priorProb) + ((1-myProb) * (1-priorProb)))
        exp += postProb
        thisPrior[choose] -= postProb  # 根据当前状态更新先验
    return exp

maxExp = None
maxExpAnswer = None
for answer in permutation.allAnswer:
    exp = calcExp(answer)
    print(exp, answer)
    if maxExp is None or exp > maxExp:
        maxExp = exp
        maxExpAnswer = answer
print('max:')
print(maxExp, maxExpAnswer)