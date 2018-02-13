# IdentifiersExtractor

An identifiers extractor supported by *web crawler* on *Github/SourceForge*.
> Giving a repository, it returns the identifiers extracted from the code files which qualify your custom requirements.
> <br > Maintained by [X-Lab](http://www.x-lab.ac/), SSE, Tongji University

### Supported language:
1. C

2. C++

3. Java8

4. Python3

5. PHP

6. Objective-C

   ​

### Prerequisites:
1. Python version >= 3.5

2. antlr4 (http://www.antlr.org/)

   ##### Install

   `pip3 install antlr4-python3-runtime`

   ​

### Usage:
```python main.py [options]```

```options``` include:

* --*owner*: specify the owner of the repository on github
* --*repository*: specify the name of the repository
* --*branch*: specify the branch of the project in the repository
* --*file-type*: specify the code files' type from one of the `c`, `cpp`, `java`, `py`, `php`, `m`
* --*file-name*: specify the name of the file to print identifiers, which should end up with `.txt`


* --*identifier-type*: specify the identifier type from one of the `singlecase`, `camelcase`, `seperator`, `containdigits`, `mixed`
  * `singlecase` which contains only lower case, like *identifiersextractor.*
  * `camelcase`  which may contain lower case and upper case, like *identifiersExtractor.*
  * `separator` which may contain lower case and separators, like *identifiers_extractor.*
  * `containdigits` which is like 'camelcase' with digits or 'separator' with digits, like *identifiersExtractor2* and *identifiers_extractor2*.
  * `mixed` default option, which may contain lower case, upper case, separators and digits.
* --*minlength*: specify the min length of an identifier, default to **2**
* --*maxlength*: specify the min length of an identifier, default to **25**
* --*number*: specify the number of identifiers to extracted



### Examples

##### c

```
python main.py --owner=Mzzopublic --repository=C --branch=master --file-type=c --file-name=test_c.txt --identifier-type=mixed --minlength=2 --maxlength=25 --number=500
```

The identifiers are saved in *test_c.txt*

##### cpp

```
python main.py --owner=exercism --repository=cpp --branch=master --file-type=cpp --file-name=test_cpp.txt --identifier-type=mixed --minlength=2 --maxlength=25 --number=500
```

The identifiers are saved in *test_cpp.txt*

##### java

```
python main.py --owner=winterbe --repository=java8-tutorial --branch=master --file-type=java --file-name=test_java.txt --identifier-type=mixed --minlength=2 --maxlength=25 --number=500
```

The identifiers are saved  in *test_java.txt*

##### py

```
python main.py --owner=michaelliao --repository=learn-python3 --branch=master --file-type=py --file-name=test_py.txt --identifier-type=mixed --minlength=2 --maxlength=25 --number=500
```

The identifiers are saved  in *test_py.txt*

##### php

```
python main.py --owner=exercism --repository=php --branch=master --file-type=php --file-name=test_php.txt --identifier-type=mixed --minlength=2 --maxlength=25 --number=500
```

The identifiers are saved  in *test_php.txt*

##### m

```
python main.py --owner=exercism --repository=objective-c --branch=master --file-type=m --file-name=test_m.txt --identifier-type=mixed --minlength=2 --maxlength=25 --number=500
```

The identifiers are saved  in *test_m.txt*



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
