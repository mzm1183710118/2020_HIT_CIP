def createDict(dictFile):
    """
    构建词典
    :param dictFile: 词典文本路径
    :return: 包含所有词语的集合
    """
    lexicon = set()
    f = open(dictFile, 'r', encoding='utf-8')
    for line in f.readlines():
        lexicon.add(line.strip('\n'))
    f.close()
    return lexicon


def FMM(dictionary, inPath, outPath, max_length=7):
    """
    FMM算法进行中文分词
    :param dictionary: 词典
    :param inPath: 预料文件路径
    :param outPath: 输出文件路径
    :param max_length: 词典中最长词的长度
    :return: 分词后的结果，写入输出文件中
    """
    # 读取语料txt文件
    with open(inPath, 'r', encoding='utf-8', ) as f:
        lines = f.readlines()
    # 选定输出结果的txt文件
    result = open(outPath, 'w', encoding='utf-8', )
    # 分别对每行进行正向最大匹配处理
    for line in lines:
        my_list = []
        rowLength = len(line)
        while rowLength > 0:
            # 从最大词语长度开始截取字符并在词典中查找
            tryWord = line[0:max_length]
            while tryWord not in dictionary:
                if len(tryWord) == 1:
                    break
                tryWord = tryWord[0:len(tryWord) - 1]
            my_list.append(tryWord)
            line = line[len(tryWord):]
            rowLength = len(line)
        # 将分词结果写入生成文件
        for word in my_list:
            if word == '\n':
                result.write('\n')
            else:
                result.write(word + " ")

    result.close()


def simpleFMM(dictionary, input, max_length = 7):
    output = ''
    my_list = []
    rowLength = len(input)

    while rowLength > 0:
    # 从最大词语长度开始截取字符并在词典中查找
        tryWord = input[0:max_length]
        while tryWord not in dictionary:
            if len(tryWord) == 1:
                break
            tryWord = tryWord[0:len(tryWord) - 1]
        my_list.append(tryWord)
        input = input[len(tryWord):]
        rowLength = len(input)
    # 将分词结果写入生成文件
    for word in my_list:
        output = output + word + "\\"

    print(output)

