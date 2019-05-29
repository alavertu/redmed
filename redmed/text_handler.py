import re
import string

punctuations = string.punctuation

class text_handler():

    def __init__(self):
        self.phrases = set()
        with open(
            "./data/redmed_phrases.txt"
        ) as inPhrases:
            for phrase in inPhrases:
                self.phrases.add(phrase.strip())
        inPhrases.close()

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
        orderedTokens = [x for x in testLine.split(" ")]
        return(orderedTokens)

    def preprocess_comment(self, line):
        testLine = self.get_ordered_tokens(line)
        orderedTokens = [x.strip(punctuations) for x in testLine]
        orderedTokens = [x.replace(",", "C").replace("|", " ") for x in orderedTokens]
        orderedTokens = [x for x in orderedTokens  if (x != "") and (x != " ") and ("www." not in x) and (".com" not in x) and ("wiki" not in x) and ("ref_=" not in x) and ("u/" not in x) and ("r/" not in x) and ("www" not in x) and ("http" not in x) and ("html" not in x) and ("message/compose" not in x)]
        orderedTokens = [re.split("\W+", x) if "_" not in x else [x] for x in orderedTokens]
        orderedTokens = [y for x in orderedTokens for y in x]
        tokensOut = orderedTokens
        return(tokensOut)
