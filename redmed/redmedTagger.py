import textHandler as th


class redmedTagger():

    def __init__(self):

        self.parser = th.textHandler()

        self.known_entities = dict()
        self.ms_entities = dict()
        self.pillmark_entities = dict()
        self.synonym_entities = dict()

        self.backMap = dict()
        self.foundMappings = dict()
        self.redmed_terms = dict()
        with open("./data/redmed_drug_lexicon.tsv") as inFile:
            for i, line in enumerate(inFile):
                dbid, drug, known, misspellingPhon, edOne, edTwo, pillMark, google_ms, google_title, google_snipped, ud_slang, missed = line.strip().split(
                    "\t")
                self.backMap[drug] = (dbid, drug)
                self.backMap[dbid] = (dbid, drug)
                val = [x.split(",") for x in
                       [known, misspellingPhon, edOne, edTwo, pillMark, google_ms, google_title, google_snipped,
                        ud_slang]]
                self.foundMappings[(dbid, drug)] = val
                for cat in val:
                    for term in cat:
                        self.redmed_terms[term] = (dbid, drug)

                # known entities
                for token in val[0]:
                    self.known_entities[token] = (dbid, drug)

                # misspelled entites
                for token in val[1]:
                    self.ms_entities[token] = (dbid, drug)
                for token in val[2]:
                    self.ms_entities[token] = (dbid, drug)
                for token in val[3]:
                    self.ms_entities[token] = (dbid, drug)
                for token in val[5]:
                    self.ms_entities[token] = (dbid, drug)

                # pillmark entites
                for token in val[4]:
                    self.pillmark_entities[token] = (dbid, drug)

                # synonym entites
                for token in val[6]:
                    self.synonym_entities[token] = (dbid, drug)
                for token in val[7]:
                    self.synonym_entities[token] = (dbid, drug)
                for token in val[8]:
                    self.synonym_entities[token] = (dbid, drug)


    def get_redmed_drug_hits(self, temp_tokens):
        hit_indices = list()
        for i, tok in enumerate(temp_tokens):
            if tok in self.redmed_terms:
                hit_indices.append(i)

        return(hit_indices)

    def get_output(self, text, temp_tokens, hit_indices, flag):
        preserved_tokens = self.parser.tokenize(text)
        phrase_adjust = 0
        out_strs = list()
        for i, tok in enumerate(temp_tokens):
            if "_" in tok:

                if i in hit_indices:
                    out_strs.append(flag)
                    _ = [out_strs.append(x) for x in preserved_tokens[i + phrase_adjust:i + phrase_adjust + 2]]
                    out_strs.append(flag)
                else:
                    _ = [out_strs.append(x) for x in preserved_tokens[i + phrase_adjust:i + phrase_adjust + 2]]
                phrase_adjust += 1
            #             phrase_adjust += 1
            else:
                if tok in redmed_terms:
                    out_strs.append(flag)
                    out_strs.append(preserved_tokens[i + phrase_adjust])
                    out_strs.append(flag)
                else:
                    out_strs.append(preserved_tokens[i + phrase_adjust])
            if i + phrase_adjust > len(preserved_tokens) - 1:
                break
        return(" ".join(out_strs))

    def get_normalized_output(self, temp_tokens, hit_indices, flag):
        out_strs = list()
        for i, tok in enumerate(temp_tokens):
            if i in hit_indices:
                out_strs.append(flag)
                out_strs.append(tok)
                out_strs.append(flag)
            else:
                out_strs.append(tok)
        return(" ".join(out_strs))

    def general_drug_flagging(self, sentence, preserve_case=True):
        temp_tokens = self.parser.get_ordered_tokens(sentence)
        out_strs = list()
        hits = self.get_redmed_drug_hits(temp_tokens)
        if preserve_case:
            out_str = self.get_output(sentence, temp_tokens, hits, "<drug_related>")

        else:
            out_str = self.get_normalized_output(temp_tokens, hits, "<drug_related>")

        return(out_str)
    