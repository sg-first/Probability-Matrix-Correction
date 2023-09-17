import copy

prior = { 'A':1, 'B':1, 'C':1 }
allChoose = prior.keys()

col1 = { 'A':0.9, 'B':0.05, 'C':0.05, 'ID':0 }
col2 = { 'A':0.8, 'B':0.1, 'C':0.1, 'ID':1 }
col3 = { 'A':0.7, 'B':0.15, 'C':0.15, 'ID':2 }
probMat = [col1, col2, col3]

def getChooseMaxNum(probMat:list, choose, choosedList):
    num = 0
    for col in probMat:
        maxValue = None
        maxChoose = None
        for _choose in allChoose:
            if _choose not in choosedList:
                if maxValue is None or col[_choose] > maxValue:
                    maxValue = col[_choose]
                    maxChoose = _choose
        if maxChoose == choose:
            num += 1
    return num

def getMaxNumChoose(probMat:list, choosedList):
    maxValue = None
    maxChoose = None
    for choose in allChoose:
        if choose not in choosedList:
            value = getChooseMaxNum(probMat, choose, choosedList)
            if maxValue is None or value > maxValue:
                maxValue = value
                maxChoose = choose
    return maxChoose

# 全选A=1

# 选两个A
def calcExp(answer):
    def calcExpForChoose(choose): # 计算选某个选项的题正确的期望
        answerA = []
        for i in answer.values():
            if i['choose'] == choose:
                answerA.append(i['prob'])
        answerAExp = 0
        answerA.sort(reverse=True)
        for i in range(prior[choose]):
            answerAExp += answerA[i]
        return answerAExp

    exp = 0
    for choose in allChoose:
        exp += calcExpForChoose(choose)
    return exp

# 按选项顺序选题
def addAnswerByChoose(answer:dict, choose:str, chooseTimes:int):
    probMatSortByA = copy.copy(probMat)
    probMatSortByA.sort(key=lambda i: i[choose], reverse=True)
    # 在probMatSortByA中选择未回答的前chooseTimes个问题，选择choose选项
    allAnsweredID = list(answer.keys())
    i = 0 # 当前已选数量
    for col in probMat:
        if col['ID'] not in allAnsweredID and i < chooseTimes:
            answer[col['ID']] = {'choose': choose, 'prob': col[choose]}
            i += 1
    return answer

def getMaxProbAnswer(chooseTimes):
    choosedList = []
    answer = {}
    for _ in allChoose:
        maxChoose = getMaxNumChoose(probMat, choosedList)
        choosedList.append(maxChoose)
        answer = addAnswerByChoose(answer, maxChoose, chooseTimes)
    return answer
    
