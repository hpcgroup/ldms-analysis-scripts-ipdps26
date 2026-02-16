import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.pyplot import gca
import matplotlib as mpl
from cycler import cycler
import math

linestyle_tuple = [
    ("solid", "solid"),  # Same as (0, ()) or '-'
    ("dotted", "dotted"),  # Same as (0, (1, 1)) or '.'
    ("dashed", "dashed"),  # Same as '--'
    ("dashdot", "dashdot"),
    ("loosely dotted", (0, (1, 10))),
    ("dotted", (0, (1, 1))),
    ("densely dotted", (0, (1, 1))),
    ("loosely dashed", (0, (5, 10))),
    ("dashed", (0, (5, 5))),
    ("densely dashed", (0, (5, 1))),
    ("loosely dashdotted", (0, (3, 10, 1, 10))),
    ("dashdotted", (0, (3, 5, 1, 5))),
    ("densely dashdotted", (0, (3, 1, 1, 1))),
    ("dashdotdotted", (0, (3, 5, 1, 5, 1, 5))),
    ("loosely dashdotdotted", (0, (3, 10, 1, 10, 1, 10))),
    ("densely dashdotdotted", (0, (3, 1, 1, 1, 1, 1))),
]

linestyle_dict = {k: v for k, v in linestyle_tuple}


def setup_global():
    font_entry = fm.FontEntry(
        fname="/pscratch/sd/o/ocankur/dask/perlmutter-omni-analysis/sc24_scripts/ldms-analysis-scripts/dask_scripts/march_analysis/pssg-plots/gillsans.ttf",
        name="gill-sans",
    )

    # set font
    fm.fontManager.ttflist.insert(0, font_entry)
    mpl.rcParams["font.family"] = font_entry.name

    mpl.use("Agg")
    mpl.rcParams["axes.spines.right"] = False
    mpl.rcParams["axes.spines.top"] = False
    mpl.rcParams["font.size"] = 18
    # mpl.rcParams["font.size"] = 14
    mpl.rcParams["lines.linewidth"] = 2
    mpl.rcParams["lines.markersize"] = 8
    mpl.rcParams.update({"legend.labelspacing": 0.1})


def setup_local():
    plt.clf()
    gca().yaxis.grid(linestyle="dashed")
    gca().spines["left"].set_color("#606060")
    gca().spines["bottom"].set_color("#606060")
    global_cycler = cycler(color=get_colors()) + cycler(linestyle=get_linestyles())
    gca().set_prop_cycle(global_cycler)


def set_aspect_ratio(ratio=3 / 5, logx=None, logy=None):
    xleft, xright = gca().get_xlim()
    print("xleft: ", xleft)
    print("xright: ", xright)
    if logx is not None:
        xleft = math.log(xleft, logx)
        xright = math.log(xright, logx)
    ybottom, ytop = gca().get_ylim()
    print("ybottom: ", ybottom)
    print("ytop: ", ytop)
    if logy is not None:
        ytop = math.log(ytop, logy)
        ybottom = math.log(ybottom, logy)
    gca().set_aspect(abs((xright - xleft) / (ybottom - ytop)) * ratio)


def get_colors():
    return [
        "#D55E00",
        "#009E73",
        "#0072B2",
        "#CC79A7",
        "#000000",
        "#E03A3D",
        "#0072B2",
        "#CC79A7",
    ]


def get_hatches():
    return ["xxx", "xxxxxx", "\\\\\\\\", "-", "/", "+"]


def get_linestyles():
    return [
        linestyle_dict["solid"],
        linestyle_dict["dotted"],
        linestyle_dict["dashed"],
        linestyle_dict["dashdotted"],
        linestyle_dict["dashdotdotted"],
        linestyle_dict["solid"],
        linestyle_dict["dotted"],
        linestyle_dict["dashed"],
    ]


def get_markers():
    return [
        "^",
        "s",
        "o",
        "d",
        "x",
        "o",
        "d",
        "s",
    ]