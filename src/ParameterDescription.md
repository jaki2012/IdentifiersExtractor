# ParameterDescription

> An parameter specification of the identifier extractor.



### lang

* usage: specify the identifier language(file type) 
* options include:
  * `java`
  * `c`
  * `cpp`
  * `cs`
  * `js`
  * `go`
  * `py`
  * `php`
  * `pl`
  * `swift`
  * `m`  objective C

### type

* usage:  specify the identifier type
* options include:
  * `singlecase` which contains only lower case, like *identifiersextractor.*
  * `camelcase`  which may contain lower case and upper case, like *identifiersExtractor.*
  * `separator` which may contain lower case and separators, like *identifiers_extractor.*
  * `containdigits` which is like 'camelcase' with digits or 'separator' with digits, like *identifiersExtractor2* and *identifiers_extractor2*.
  * `mixed` default option, which may contain lower case, upper case, separators and digits.

###URL

* usage: specify the txt file containing the repository urls

### minlength

* usage: specify the min length of an identifier, default to **2**

### maxlength

* usage: specify the min length of an identifier, default to **25**

### number

* usage: specify the number of identifiers to extracted

### mode

* usage: only be valid when the parameter *number* is set.
* options include: 
  *  `greedy` which means it would extracted identifiers as many as you set.
  *  `random` default option, which means that it would randomly select them after all the identifiers are extracted.



