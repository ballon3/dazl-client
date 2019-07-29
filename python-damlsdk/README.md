damlsdk
=======

`damlsdk` is a Python library used to conveniently call methods on the
[DAML SDK](https://docs.daml.com/getting-started/installation.html).

Requirements
------------

`damlsdk` needs the `daml` executable to be installed and either available in
your path or installed in the standard location (`~/.daml`).

Sample Usage
------------

```py
import damlsdk as daml

with daml.sandbox():
    pass
```
