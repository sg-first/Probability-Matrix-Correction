import permutation

def calcExp(answer):
    def calcExpForChoose(choose):  # 计算选某个选项的题正确的期望
        answerA = []
        for i in answer:
            if i['choose'] == choose:
                answerA.append(i['prob'])
        answerAExp = 0
        answerA.sort(reverse=True)
        i = 0
        while i < permutation.prior[choose] and i < len(answerA):
            answerAExp += answerA[i]
            i += 1
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