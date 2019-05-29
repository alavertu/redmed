import re
import string

punctuations = string.punctuation

class textHandler():

    def __init__(self, phrasePath="./data/redmed_phrases.txt"):
        self.phrases = set()
        with open(
            phrasePath
        ) as inPhrases:
            for phrase in inPhrases:
                self.phrases.add(phrase.strip())
        inPhrases.close()

    def tokenize(self, sentence):
        tokens = re.sub("([^\w\s])", r' \1', sentence).split(" ")
        return(tokens)

    def bigramize(self, tokenList):
        if len(tokenList) > 1:
            tempSet = set(
                [
                    "_".join([tokenList[i], tokenList[i + 1]])
                    for i in range(len(tokenList) - 1)
                ]
            )
            return(tempSet)
        else:
            return(None)


    def trigramize(self, tokenList):
        if len(tokenList) > 2:
            tempSet = set(
                [
                    "_".join([tokenList[i], tokenList[i + 1], tokenList[i + 2]])
                    for i in range(len(tokenList) - 2)
                ]
            )
            return(tempSet)
        else:
            return(None)


    def quadgramize(self, tokenList):
        if len(tokenList) > 3:
            tempSet = set(
                [
                    "_".join(
                        [
                            tokenList[i],
                            tokenList[i + 1],
                            tokenList[i + 2],
                            tokenList[i + 3],
                        ]
                    )
                    for i in range(len(tokenList) - 3)
                ]
            )
            return(tempSet)
        else:
            return(None)


    def quingramize(self, tokenList):
        if len(tokenList) > 4:
            tempSet = set(
                [
                    "_".join(
                        [
                            tokenList[i],
                            tokenList[i + 1],
                            tokenList[i + 2],
                            tokenList[i + 3],
                            tokenList[i + 4],
                        ]
                    )
                    for i in range(len(tokenList) - 4)
                ]
            )
            return(tempSet)
        else:
            return(None)


    def find_and_sub(self, tokenizer, textLine):
        tokens = textLine.split()
        grams = tokenizer(tokens)
        grams = {x.strip(punctuations) for x in grams}
        if grams is None:
            return(textLine)
        hits = grams.intersection(self.phrases)
        if len(hits) > 0:
            newLine = textLine
            for hit in hits:
                pat = hit.replace("_", " ")
                newLine = newLine.replace(pat, hit)
            return(newLine)
        else:
            return(textLine)


    def get_ordered_tokens(self, line):
        testLine = line.strip().lower().replace("\n", " ")
        testLine = self.find_and_sub(self.quingramize, testLine)
        testLine = self.find_and_sub(self.quadgramize, testLine)
        testLine = self.find_and_sub(self.trigramize, testLine)
        testLine = self.find_and_sub(self.bigramize, testLine)
        orderedTokens = self.tokenize(testLine)
        return(orderedTokens)
