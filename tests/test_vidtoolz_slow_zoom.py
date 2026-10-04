import pytest
import vidtoolz_slow_zoom as w
from pathlib import Path


from argparse import ArgumentParser

# IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"


def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    result = parser.parse_args(["hello.mp4", "Display text"])
    assert result.inputvideo == "hello.mp4"
    assert result.text == "Display text"


def test_plugin(capsys):
    w.slowzoom_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``vidtoolz`` plugin." in captured.out


def test_realcase_slowzoom(tmpdir):
    outfile = tmpdir / "test_slowzoom.mp4"
    testdata = Path(__file__).parent / "test_data"
    movefile = testdata / "IMG_4022.MOV"

    # -d or --duration 3 , -st or --startat 1
    # other options -fs --fontsize
    argv = [str(movefile), "Hello World", "-d", "3", "-st", "1", "-o", str(outfile)]
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)
    args = parser.parse_args(argv)
    args.func = None
    w.slowzoom_plugin.run(args)
    assert outfile.exists()
