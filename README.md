# redmed

The redmed annotator tool is designed to annotate text data in accordance with the mappings from "RedMed: Extending drug lexicons for social media applications". 

The creation of this lexicon was automated and may contain errors. If you'd like to ensure complete accuracy, you can manually curate the `redmed_drug_lexicon.tsv` file inside of the data directory. Simply remove or add tokens to the relevant list of comma separated entites. Make sure that any tokens you add are all lowercase and spaces within phrases are replaced with underscores. Additionally, phrases need to be added to the `redmed_phrases.txt` file in the data directory.

**If you use this tool, please cite:**
> **A. Lavertu and RB Altman. "RedMed: Extending drug lexicons for social media applications"** **INSERT ACTUAL CITATION**


## Example usage:

First let's import the tool and create a redmed tagger object:
```python
import redmedTagger as rmt
tagger = rmt.redmedTagger()
```
Now let's create a string to annotate:
```python
testSent = "I went to the drug store the other day and bought some oxycotin, oxy 10s to be specific. Planning to mix these with some xannax."
```

### General annotation:
If we want to just annotate parts of the sentence that are generally related to drugs in the redmed lexicon, we can do that with the `general_drug_flagging` tool:
```python
tagger.general_drug_flagging(testSent, preserve_case=True)
```
Which returns the following string,
> 'I went to the drug store the other day and bought some <drug_related> oxycotin <drug_related> , <drug_related> oxy 10s <drug_related> to be specific . Planning to mix these with some <drug_related> xannax <drug_related> .'

### Specific annotation:
If we want to annotate parts of the sentence with a flag that indicates what redmed lexicon drug they were mapped to we can do that with the `specific_drug_flagging` tool:
```python
tagger.specific_drug_flagging(testSent, preserve_case=True)
```
Which returns the following string,
> 'I went to the drug store the other day and bought some <oxycodone> oxycotin <oxycodone> , <oxycodone> oxy 10s <oxycodone> to be specific . Planning to mix these with some <alprazolam> xannax <alprazolam> .'

### Entity counting:
If we'd rather just get a count of drug mentions, we can do that with `get_mention_counts`, which returns a dictionary objects with the generic drug names and their associated counts. 
```python
tagger.get_mention_counts(testSent)
```
> '{'oxycodone': 2, 'alprazolam': 1}'
