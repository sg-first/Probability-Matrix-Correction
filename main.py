import copy

prior = {'A': 1, 'B': 1, 'C': 1}
allChoose = prior.keys()

col1 = {'A': 0.9, 'B': 0.05, 'C': 0.05, 'ID': 0}
col2 = {'A': 0.8, 'B': 0.11, 'C': 0.09, 'ID': 1}
col3 = {'A': 0.7, 'B': 0.15, 'C': 0.15, 'ID': 2}
probMat = [col1, col2, col3]

def calcExp(answer):
    def calcExpForChoose(choose):  # 计算选某个选项的题正确的期望
        answerA = []
        for i in answer:
            if i['choose'] == choose:
                answerA.append(i['prob'])
        answerAExp = 0
        answerA.sort(reverse=True)
        i = 0
        while i < prior[choose] and i < len(answerA):
            answerAExp += answerA[i]
            i += 1
        # 根据先验确定期望最小值
        expMin = len(answerA) - (len(probMat) - prior[choose])
        if answerAExp < expMin:
            return expMin
        else:
            return answerAExp

    exp = 0
    for choose in allChoose:
        exp += calcExpForChoose(choose)
    return exp

def getChooseAndProbFromProbMat(sub, choose):
    col = probMat[sub]
    return {'choose':choose, 'prob':col[choose]}

def calcAllAnswer():
    allAnswer = []
    def recu(answer: list):
        if len(answer) == len(probMat):
            print(answer)
            allAnswer.append(answer)
        else:
            for choose in allChoose:
                nextAnswer = copy.copy(answer)
                nextAnswer.append(getChooseAndProbFromProbMat(len(answer), choose))
                recu(nextAnswer)
    recu([])
    return allAnswer

allAnswer = calcAllAnswer()
maxExp = None
maxExpAnswer = None
for answer in allAnswer:
    exp = calcExp(answer)
    if maxExp is None or exp > maxExp:
        maxExp = exp
        maxExpAnswer = answer
print(maxExp, maxExpAnswer)