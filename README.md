# Soccer 3D — a Claude Fable 5.2 test

A seven-a-side 3D soccer game for phones and tablets, in a single self-contained HTML file.

This repository is a **test of Claude Fable 5.2**: the game was written by the model in one conversation.
Sound effects and commentary were generated with **ElevenLabs**.

## Play

Open `index.html` in a mobile or desktop browser, or use GitHub Pages:
<https://shaunprice.github.io/soccer-3d/>

## Features

- 3D stadium with jointed, animated players, real-time shadows and a big-screen scoreboard
- Animated introduction, followed by the Hall of Fame scoreboard
- Two halves, throw-ins, corners and goal kicks
- Slow-motion goal replays
- Eight levels of rising difficulty; win one to unlock the next
- Player profiles, automatic progress saving, save-and-resume of a match in progress
- Points for every match and a local high-score table
- In-game help

## Controls

| Input | With the ball | Without the ball |
|---|---|---|
| Left thumb (or arrows / WASD) | Move | Move |
| Red button (or Space) | Shoot: tap for a low drive, hold for power | Sliding tackle |
| Blue button (or Shift) | Pass to the ringed team-mate | Switch player |

Landscape gives a broadcast side view; portrait gives a view from behind the team.

## Notes

- Rendering uses three.js r128 from cdnjs. Everything else, including audio, is embedded in `index.html`.
- `src-index.html` is the source without audio; `python3 build.py` embeds the clips in `sounds/` and writes `index.html`.
- Profiles, saves and scores are stored in the browser's local storage on the device.
