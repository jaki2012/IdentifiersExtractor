# IdentifiersExtractor

An identifiers extractor supported by *web crawler* on *Github/SourceForge*.
> Giving a set of repository urls, it returns certains identifiers qualify your custom requirements.

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

