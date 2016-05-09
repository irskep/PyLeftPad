PyLeftPad is a reimplementation of the popular JavaScript library
[left-pad](https://github.com/stevemao/left-pad).

<table-of-contents />

# Introduction

Sometimes you need to pad a string, on the left. PyLeftPad does this.

# Usage

```python
from leftpad import leftpad

leftpad('foo', 5)
# => "  foo"

leftpad('foobar', 6)
# => "foobar"

leftpad(1, 2, '0')
# => "01"
```

For more information, see <heading-link name="api" />.