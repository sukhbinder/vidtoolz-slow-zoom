# vidtoolz-slow-zoom

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-slow-zoom.svg)](https://pypi.org/project/vidtoolz-slow-zoom/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-slow-zoom?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-slow-zoom/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-slow-zoom/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-slow-zoom/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-slow-zoom/blob/main/LICENSE)

Slowzoom of text using ffmpeg

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-slow-zoom
```
## Usage

type ``vid slowzoom --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-slow-zoom
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
