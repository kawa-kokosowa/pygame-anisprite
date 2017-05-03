# PyGame-AniSprite

[![GitHub
license](https://img.shields.io/github/license/lily-mayfield/pygame-anisprite.svg?style=flat-square)](https://raw.githubusercontent.com/lily-mayfield/pygame-anisprite/master/LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/pygame-anisprite.svg?style=flat-square)](https://pypi.python.org/pypi/pygame-anisprite/)
[![Code
Climate](https://img.shields.io/codeclimate/github/lily-mayfield/pygame-anisprite.svg?style=flat-square)](https://codeclimate.com/github/lily-mayfield/pygame-anisprite)
[![Travis](https://travis-ci.org/lily-mayfield/pygame-anisprite.svg)](https://travis-ci.org/lily-mayfield/pygame-anisprite)
[![Coverage
Status](https://img.shields.io/coveralls/lily-mayfield/pygame-anisprite.svg)](https://coveralls.io/github/lily-mayfield/pygame-anisprite)

PyGame-AniSprite is a 2D game engine for Python (2 *and* 3)/PyGame. What's
special about this project is how an `AnimatedSprite` is almost
indistinguishable from a normal
[`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite).

Written because I didn't like `pyganim`...

Split off from my [Sappho game engine](https://github.com/lily-mayfield/sappho).

Be sure to checkout the `AUTHORS.md`!

## Design Philosophy

  1. Don't interfere with the way people build their pygame games
  2. We are not automating game logic
  3. PyGame-AniSprite modules _may not_ import other PyGame-AniSprite modules
  4. Inherit from pygame objects when possible; use conventional
     pygame models/architecture.
  5. Consistency.
  6. Simplicity trumps all else.
  7. Well documented.
  8. Code is easy-to-test. We show that with our 100% test coverage.

For more check `CONTRIBUTING.md`.

## Getting Started

Install pygame:

  * You can try `pip install hg+http://bitbucket.org/pygame/pygame`
    but it may not work...
  * **Ubuntu**, Python 2.7: `sudo apt install python-pygame`
  * **FreeBSD**, Python 2.7: `sudo pkg install py27-game`
  * **OSX**, Python 2.7: available in homebrew (note that there is
    a caveat in El Capitan [see: #63])
  * For any other operating system, or more details, see:
    http://www.pygame.org/download.shtml

Install `pygame-anisprite`: `pip install -r requirements/main.txt .`

If you wanna contribute, please read `CONTRIBUTING.md`!
