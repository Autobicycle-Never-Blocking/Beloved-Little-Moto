import jieba


def stopwordslist(filepath):  # 定义函数创建停用词列表
    stopword = [line.strip() for line in open(filepath, 'r').readlines()]  # 以行的形式读取停用词表，同时转换为列表
    return stopword


def cutsentences(sentences):  # 定义函数实现分词
    print('原句子为：' + sentences)
    cutsentence = jieba.lcut(sentences.strip())  # 精确模式
    print('\n' + '分词后：' + "/ ".join(cutsentence))
    stopwords = stopwordslist(filepath)  # 这里加载停用词的路径
    lastsentences = ''
    for word in cutsentence:  # for循环遍历分词后的每个词语
        if word not in stopwords:  # 判断分词后的词语是否在停用词表内
            if word != '\t':
                lastsentences += word
                lastsentences += "/ "
    print('\n' + '去除停用词后：' + lastsentences)
    return lastsentences


def fenci(sentences):
    lastsentences = cutsentences(sentences)
    # 词语数组
    wordList = []
    # 用于统计词频
    wordCount = {}

    # 从分词后的源文件中读取数据
    # 利用空格分割成数组
    wordsList = lastsentences.split('/ ')[:-1]
    # 遍历数组进行词频统计，这里使用wordCount 对象，出发点是对象下标方便查询
    for item in wordsList:
        if item not in wordCount:
            wordCount[item] = 1
        else:
            wordCount[item] += 1
    print(wordCount)


if __name__ == '__main__':
    filepath = 'stop_words.txt'

    sentences = '万里长城是中国古代劳动人民血汗的结晶和中国古代文化的象征和中华民族的骄傲'
    stopwordslist(filepath)
    cutsentences(sentences)

    fenci(sentences)

