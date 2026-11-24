# makefun-news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/chunzhiyi492-lab/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/chunzhiyi492-lab/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Sum up 24 November 2026's world news in one image: a 1024x1024 newspaper-style infographic. Nvidia's Jensen Huang returns as CEO and shares jump 31%; Ukraine says it sank a Russian warship off Libya; three tankers are hit by mines in the Strait of Hormuz; Israeli strikes kill a Hamas security chief in Gaza; a Russian strike hits flats in Zaporizhzhia; a factory fire in Indonesia kills 26.

## Run it

```sh
python3 draw.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` uses only the Python standard library, needs no network, and copies the bundled `entry.png` to `/output/entry.png` byte for byte on every run. `draw.py` is the build tool that drew `entry.png` with Pillow; it is not run by the grader.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1xkk96y5&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
