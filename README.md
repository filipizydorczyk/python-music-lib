# 🎼 Python music lib

This project is my playground to provide library with types objects and utilities based on concepts in Western Theory (at lest for now only Western Theory).

[Documentation](./docs/README.md)

It is prototype even though I am trying to test everything and keep everything documentated. Models of this project will change in future surly and it wont be compatible with previous versions.

# 🏁 Getting started

Dependencies:

```
make init
```

Test:

```
make test
```

Install:

```
make install #probably with sudo
```

# 📘 Code conduct

## Factories

Factories are just functions that provides api for creating diffrent models. Their purpose is to make creation of certain models easier. All of factories should be places in `musiclib/utils` directory and its name should be `<model>factory.py`. Content of this file should be functions clled `create_<model>_<variation>` where variation is optional. See existing factories for reference

```py
def create_chord(pitch: Pitch) -> Chord:
    pass

def create_chord_major(pitch: Pitch) -> Chord:
    pass
```

## Tests

Thest are written in `pytest` and are stored in `tests` directory. I don't make any subdirectories in tests. Instead I name tests with pattern `test_subdirectory_subdirectory_pythonfile.py`. If in direcotry are many files with simillar goal u it can be just `test_subdirectory_subdirectory.py` like for example all exotic scales are tested in `tests/test_scales_exotic.py`. Otherwise it should contain python file name like `tests/test_collections_pitecheslist.py`.

Functions in these files should be named with pattern `test_description_what_it_does` so that pytest could detect them. For example `def test_should_add_pitches_after_adding_intervals_to_collection():`.
