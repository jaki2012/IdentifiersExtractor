# IdentifiersExtractor

An identifiers extractor supported by *web crawler* on *Github/SourceForge*.
> Giving a set of repository urls, it returns certains identifiers qualify your custom requirements.
<br > Maintained by [X-Lab](http://www.x-lab.ac/), SSE, Tongji University

### Supported language:
1. Java
2. C/C++/C#
3. JavaScript
4. Go
5. Python
6. PHP
7. Perl
8. Swift/Objective-C

### Prerequisites:
```Python version >= 3.5```

### Usage:
```python identifier_extractor.py [options]```

```options``` include:
* --*lang*: specify the identifier language
* --*type*: specify the identifier type from one of the ```singlecase```,```camelcase```,```seperator```,```containdigits```,```mixed```
* --*urls*: specify the txt file containing the repository urls
* --*minlength*: specify the min length of an identifier, default to **2**
* --*maxlength*: specify the min length of an identifier, default to **25**
* --*number*: specify the number of identifiers to extracted
* --*mode*: only be valid when the parameter *number* is set. Be one of the ```greedy``` or ```random```, default to be **random**, which means that it would randomly select them after all the identifiers are extracted.

### Task:
##### To manually establish a oracle dataset for software engineering subtopic - *Identifier Splitting*
---
composed of equal propotion of ```singlecase```,```camelcase```,```seperator```,```containdigits```,```mixed```
1. Java (500)
2. C/C++/C# (100/200/200)
3. JavaScript (500)
4. Go (500)
5. Python (500)
6. PHP (500)
7. Perl (500)
8. Swift/Objective-C (250/250)

with split type, sequence-labeling result.

We randomly choose different software projects written in different programming language including Java, C++, Python, etc. 4000 identifiers are randomly selected by script in certain percentage among these projects. Then, to lower the risk of wrongly split these identifiers, almost 10 experienced students together split them. We try our best to keep it accurate from two aspects: On the one hand, we take the context information context in aid in addition to the general programming and english knowledge. On the other hand, we take the criteria that a split is considered to be a accurate split until at least 7 people make a common consensus on it. After the construction of the manual, we make the analysis on the distribution of these identifiers based on their lengths.
\subsubsection{CodeNet}
We actually find that more or less mistakes are inside those oracles and that dictionaries that most techniques use are not custom enough. For example, there lacks special reserved words dictionary of different programing languages, conventional terms or unknown words that common in a specific programming languages.Hence we are going to start up a CodeNet Project with the purpose of addressing the problems listed before.
\begin{itemize}
	\item An \emph{Identifiers Extractor} that can automatically extract identifiers from different kinds language. After extracting enough identifiers, we strictly define its correct splitting results to construct an oracle.
	\item Lists of custom dictionary. We are going to collect several different custom dictionaries designed for identifier splitting and make them publicly available. For example, \emph{C stdin library functional names}, \emph{Common abbreviations for Medical/Military software development} etc.
\end{itemize}

