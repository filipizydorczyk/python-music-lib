# Documentation

## Building

```
cd docs
make clean
make html
```

## Updating docs

Every subdirectory in musiclib directory needs to have own `.rts` file in docs directory and each one needs to be included in `modules.rst`

```r
python-music-lib
================

.. toctree::
   :maxdepth: 4

   models
   types
```

In subdirectory file we have to inlude python file. For examlpe

`docs/types.rst`

```r
Note Durations
----------------------------

.. automodule:: musiclib.types.notedurations
   :members:
   :undoc-members:
   :show-inheritance:

```

where **Note Durations** is title that can be set as we want to `musiclib.types.notedurations` is patch tu directory.
