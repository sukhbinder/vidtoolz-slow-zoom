import subprocess
from pathlib import Path
from argparse import ArgumentParser


def create_parser(subparser):
    parser = subparser.add_parser(
        "slowzoom", description="Slowzoom of text using ffmpeg"
    )

    parser.add_argument("input", type=str, help="Input video file")
    parser.add_argument("text", type=str, help="Text to display")

    parser.add_argument(
        "-d",
        "--duration",
        type=float,
        default=3,
        help="Text visible duration in seconds",
    )

    parser.add_argument(
        "-st", "--startat", type=float, default=0, help="Start time for text"
    )

    parser.add_argument("-fs", "--fontsize", type=int, default=80, help="Font size")

    parser.add_argument(
        "-o", "--output", type=str, required=True, help="Output video file"
    )

    return parser


class ViztoolzPlugin:
    """Slowzoom of text using ffmpeg"""

    __name__ = "slowzoom"

    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        input_file = Path(args.input)
        output_file = Path(args.output)

        start = args.startat
        duration = args.duration
        end = start + duration
        fade_start = end - 1  # last 1 second fade

        # Alpha expression:
        # invisible before start
        # fully visible until fade_start
        # fade out during last 1 sec
        alpha_expr = (
            f"if(lt(t,{start}),0,"
            f"if(lt(t,{fade_start}),1,"
            f"if(lt(t,{end}),({end}-t),0)))"
        )

        vf_filter = (
            "scale=iw*(1+0.01*t):ih*(1+0.01*t):eval=frame,"
            "crop=1920:1080,"
            f"drawtext=text='{args.text}':"
            "fontfile=/System/Library/Fonts/Supplemental/Arial.ttf:"
            f"fontsize={args.fontsize}:"
            "fontcolor=white:"
            "x=(w-text_w)/2:"
            "y=(h-text_h)/2:"
            "shadowcolor=black:shadowx=3:shadowy=3:"
            f"alpha='{alpha_expr}'"
        )

        cmd = [
            "ffmpeg",
            "-y",
            "-i",
            str(input_file),
            "-vf",
            vf_filter,
            "-c:a",
            "copy",
            "-preset",
            "slow",
            "-crf",
            "18",
            str(output_file),
        ]

        subprocess.run(cmd, check=True)


slowzoom_plugin = ViztoolzPlugin()
