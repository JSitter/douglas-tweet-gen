def create_corpus(filename):
    input_string = getStringFromFile(filename)
    input_string = sanitizeText(input_string)
    return createWordList(input_string)

def getStringFromFile(filename):
    '''
        Get string of words from Text File
    '''
    with open(filename) as f:
        return f.read()

def sanitizeText(sourceText):
    '''
        Santize words
    '''
    acceptedChars = set("'\nabcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return ''.join(filter(acceptedChars.__contains__, sourceText)).replace("\n", " ").lower()


def createWordList(sourceText):
    '''
        Create list of words
    '''
    splitText = sourceText.split(" ")
    #Remove any empty values
    for item in splitText:
        if item == "":
            splitText.pop(splitText.index(item))
    return [token for token in splitText if token != '']

def create_sentence_list(filename):
    '''
        Split text into sentences
    '''
    input_string = getStringFromFile(filename)
    input_string = sanitizeText(input_string)

def split_sentences(input_string):
    pass    
