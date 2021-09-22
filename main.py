# Fernando Da Silva
# SkoachCodeChallenge - Python
# version: 1.1

def justify(words, max_width):
    sentence_line = []
    justifiedText = []
    words_counter = 0

    for word in words:
        if words_counter + len(sentence_line) + len(word) > max_width:
            spaces = max_width - words_counter
            i = 0
            while spaces > 0:
                sentence_line[i] += ' '
                if len(sentence_line) > 1:
                    i = (i + 1) % (len(sentence_line) - 1)
                spaces -= 1
                if len(sentence_line[i])+spaces >= max_width:
                    sentence_line[i] = ' ' * (spaces + max_width - len(sentence_line[i])) + sentence_line[i]

            justifiedText.append(''.join(sentence_line))
            sentence_line, words_counter = [], 0
        sentence_line.append(word)
        words_counter += len(word)

    justifiedText.append(' '.join(sentence_line))
    spaces = max_width - words_counter - (len(sentence_line) - 1)
    justifiedText[-1] = ' ' * spaces + justifiedText[-1]
    return justifiedText

def alighLeft(words, max_width):
    sentence_line = []
    justifiedText = []
    words_counter = 0

    for word in words:
        if words_counter + len(sentence_line) + len(word) > max_width:
            justifiedText.append(''.join(sentence_line))
            sentence_line, words_counter = [], 0
        sentence_line.append(word)
        sentence_line.append(' ')
        words_counter += len(word)
    justifiedText.append(''.join(sentence_line))
    return justifiedText

def alighRight(words, max_width):
    sentence_line = []
    justifiedText = []
    words_counter = 0
    for word in words:
        if words_counter + len(sentence_line) + len(word) > max_width:
            spaces = max_width - words_counter
            justifiedText.append(' '.join(sentence_line))
            justifiedText[-1] = ' ' * (max_width - len(justifiedText[-1])) + justifiedText[-1]
            sentence_line, words_counter = [], 0
        sentence_line.append(word)
        words_counter += len(word)
    justifiedText.append(' '.join(sentence_line))
    spaces = max_width - words_counter
    justifiedText[-1] = ' ' * spaces + justifiedText[-1]

    return justifiedText


# TEST:
# mywords16 = ['This', 'is', 'an', 'example', 'of', 'text', 'justification']
# justify(mywords16, 16)

def testExample_1():
    print 'Running Test to the Example 1:'
    print '------------------------------'
    mywords_TEST_1 = ["This", "is", "an", "example", "of", "text", "justification."]

    sentences = justify(mywords_TEST_1, 16)
    for sentence in sentences:
        print(sentence)

def testExample_2():
    print 'Running Test to the Example 2:'
    print '------------------------------'
    mywords_TEST_2 = ["What","must","be","acknowledgment","shall","be"]

    sentences = justify(mywords_TEST_2, 16)
    for sentence in sentences:
        print(sentence)

def testExample_3():

    print 'Running Test to the Example 3:'
    print '------------------------------'
    mywords_TEST_3 = ['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.',
               'Art', 'is', 'everything', 'else', 'we', 'do']

    sentences = justify(mywords_TEST_3, 20)
    for sentence in sentences:
        print(sentence)

def testExample_4():
    print 'Running Test to the Example 4 EXTRA:'
    print '------------------------------------'

    mywords_TEST_4 = ['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.',
               'Art', 'is', 'everything', 'else', 'we', 'do']

    print '==========='
    print 'JUSTIFIED:'
    print '==========='
    sentences = justify(mywords_TEST_4, 20)
    for sentence in sentences:
        print(sentence)

    print 'Extra:'
    print '==========='
    print 'ALIGN LEFT:'
    print '==========='
    sentences = alighLeft(mywords_TEST_4, 20)
    for sentence in sentences:
        print(sentence)

    print '============'
    print 'ALIGH RIGHT:'
    print '============'
    sentences = alighRight(mywords_TEST_4, 20)
    for sentence in sentences:
        print(sentence)


# RUN THE TEST PROCESS:
testExample_1()

testExample_2()

testExample_3()

#this is an extra test if you decide to run just remove the (#) comment symbol.
#testExample_4()


