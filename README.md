# Python simple argument interpreter
A simple argument interpreter for python scripts.
# Usage
Pysai.option(arglist, argtofind):
Parses through given arglist and finds the argument argtofind. Then, it returns the next argument.
Example:
```python
import pysai
arglist = ["-h", "-k", "foo.bar", "-m"]
print pysai.option(arglist, "-k")
print pysai.option(arglist, "-j")
```
Output:
```
foo.bar
None
```
Pysai.flag(arglist, argtofind):
Parses through given arglist and finds the argument argtofind. If it's there, it returns True. If not, it returns False.
Example:
```python
import pysai
arglist = ["-h", "-k", "foo.bar", "-m"]
print pysai.flag(arglist, "-h")
print pysai.flag(arglist, "-j")
```
Output:
```
True
False
```
# More examples
```python
import pysai

arglist = ["cat", "dog", "--append", "end.dne", "-k", "-mlk", "/K", "cot", "+=+"]

print pysai.option(arglist, "cat")
print pysai.option(arglist, "--append")
print pysai.option(arglist, "-k")
print pysai.option(arglist, "/K")

print pysai.flag(arglist, "dog")
print pysai.flag(arglist, "end")
print pysai.flag(arglist, -K)
print pysai.flag(arglist, "-mlk")
print pysai.flag(arglist, "+=+")
```
```
dog
end.dne
-mlk
cot
True
False
False
True
True
```
