import permutation

def calcAnswerAExp(answerA, maxTimes):
    # n次试验，事件发生的概率各为answerA中的元素，求成功次数期望
    # 注：最大成功maxTimes次，比这个大的不算
    global probSum, dist
    probSum = 0
    dist = {}
    for i in range(maxTimes + 1):
        dist[i] = 0

    def recu(sub, thisProb, successTimes):
        global probSum, dist
        if sub == len(answerA):
            if successTimes <= maxTimes:
                probSum += thisProb
                dist[successTimes] += thisProb
        else:
            recu(sub + 1, thisProb * (1 - answerA[sub]), successTimes)
            recu(sub + 1, thisProb * answerA[sub], successTimes + 1)
    recu(0, 1, 0)
    # 计算期望
    exp = 0
    for num, probNumerator in dist.items():
        prob = probNumerator / probSum
        exp += prob * num
    return exp

def calcExp(answer):
    def calcExpForChoose(choose):  # 计算选某个选项的题正确的期望
        answerA = []
        for i in answer:
            if i['choose'] == choose:
                answerA.append(i['prob'])
        # answerA.sort(reverse=True)
        answerAExp = calcAnswerAExp(answerA, permutation.prior[choose])
        print(choose, answerAExp)
        # 根据先验确定期望最小值
        expMin = len(answerA) - (len(permutation.probMat) - permutation.prior[choose])
        if answerAExp < expMin:
            return expMin
        else:
            return answerAExp

    exp = 0
    for choose in permutation.allChoose:
        exp += calcExpForChoose(choose)
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