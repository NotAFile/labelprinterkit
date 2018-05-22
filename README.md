### Labelprinterkit

Labelprinterkit is a Python3 library for creating and printing labels. It was
developed for the Networking department of the KIT (Karlsruhe Institute of
Technology).

Labelprinterkit's simple layout engine can use it to declaratively create
Labels:

```python
>>> class MyLabel(Label):
...     items = [
...         Text(), Text()
...     ]
...
>>> l = MyLabel("text1", "text2")
>>> printer.print_label(l)
```

The Following printers are currently supported:

 * Brother P-Touch PT-700 (aka P700)

The following printers will probably work, but are not tested:

 * Brother H500
 * Brother E500

The official source of this repository is at https://git.scc.kit.edu/scc-net/labelprinterkit.
