import copy

prior = {'A': 1, 'B': 1, 'C': 1}
allChoose = prior.keys()

col1 = {'A': 0.9, 'B': 0.05, 'C': 0.05, 'ID': 0}
col2 = {'A': 0.8, 'B': 0.11, 'C': 0.09, 'ID': 1}
col3 = {'A': 0.7, 'B': 0.15, 'C': 0.15, 'ID': 2}
probMat = [col1, col2, col3]

def getChooseAndProbFromProbMat(sub, choose):
    col = probMat[sub]
    return {'choose':choose, 'prob':col[choose]}

def calcAllAnswer():
    allAnswer = []
    def recu(answer: list):
        if len(answer) == len(probMat):
            allAnswer.append(answer)
        else:
            for choose in allChoose:
                nextAnswer = copy.copy(answer)
                nextAnswer.append(getChooseAndProbFromProbMat(len(answer), choose))
                recu(nextAnswer)
    recu([])
    return allAnswer

allAnswer = calcAllAnswer()