import myFMM
import myEvaluate as eva

dictionary = myFMM.createDict('text/dict.txt')
myFMM.FMM(dictionary, 'text/testSource.txt', 'text/myAnswer.txt')
eva.getTrueAnswer('text/testSource.txt', 'text/trueAnswer.txt')

rate = eva.accuracy('text/myAnswer.txt', 'text/trueAnswer.txt')
print('分词准确率为：'+str(rate))
myFMM.simpleFMM(dictionary, '将军任命了一名中将')