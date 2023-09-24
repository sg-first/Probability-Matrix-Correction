import permutation
import copy

def getPriorProb(prior:dict, choose):
    return prior[choose] / sum(prior.values())

def calcExp(answers):
    expDict = {}
    answerNum = {}
    for choose in permutation.allChoose:
        expDict[choose] = 0
        answerNum[choose] = 0
    thisPrior = copy.copy(permutation.prior)

    for i in range(len(answers)):
        choose = answers[i]['choose']
        myProb = permutation.probMat[i][choose]
        priorProb = getPriorProb(thisPrior, choose)
        postProb = (myProb * priorProb) / ((myProb * priorProb) + ((1-myProb) * (1-priorProb)))
        # print(priorProb, postProb)
        expDict[choose] += postProb
        answerNum[choose] += 1
        thisPrior[choose] -= postProb  # 根据当前状态更新先验

    exp = 0
    for choose, answerAExp in expDict.items():
        expMin = answerNum[choose] - (len(permutation.probMat) - permutation.prior[choose])
        if answerAExp < expMin:
            exp += expMin
        else:
            exp += answerAExp
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