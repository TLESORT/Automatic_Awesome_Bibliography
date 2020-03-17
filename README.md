# Generate automatically awesome continual learning lists from bibtex
Automatic script to parse bibtex to mardown to create manageable bibliography github repository. We take the example of continual learning to illustrate the script.


## Installation


```bash
pip install bibtexparser
```

## Run the classification

```
# python 2.x or 3.x
# it is assumed that you use the file "bibtex.bib"
python bibtex_to_md.py
```

## Modify the script

The script is only searching for keywords in bibtex attributs' entries. Then, to modify you can modify the keywords, the attributs to evaluate or the bibtex.
We use also simple functions to plot categories titles.
The code should be easy to modify. 

## Examples of mardown files created in the topic of continual learning

- [Conferences Classification](Mardown_Files/Conferences_Bibliography.md)
- [Chronological Classification](Mardown_Files/Chronological_Bibliography.md)
- [Keywords Classification](Mardown_Files/Classification_Bibliography.md) (I need to add keywords in bibtex for this one)
- [Specific Paper Selection by ID](Mardown_Files/Selection_Bibliography.md) (Almost ramdom selection)
- [Specific Paper Selection by Author](Mardown_Files/My_Bibliography.md) (my papers ... )


## How to contribute

- Add new entries in the bib files (yours if you want). Please be carefull to not add bibtex several times.
- Create new mardowns files by modifying/improving the script
