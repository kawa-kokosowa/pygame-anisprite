Animated sprites
================

.. py:module:: pygame_anisprite.anisprite

.. automodule:: pygame_anisprite.anisprite

AnimatedSprite overview
-----------------------

An :class:`AnimatedSprite` is typically loaded from GIF with
:meth:`AnimatedSprite.from_gif()`.

.. automethod:: AnimatedSprite.from_gif

So to create an :class:`AnimatedSprite` from a GIF, you'd
do something like this code sample below:

>>> sprite = AnimatedSprite.from_gif('somedir/walk.gif')
>>> sprite.image
<Surface(10x10x32 SW)>

The :meth:`AnimatedSprite.from_gif()` method will build
the respective :class:`Frame` objects and their
:class:`FrameAnchors`. These frames are sent to the
:class:`AnimatedSprite` constructor, as seen below.

.. automethod:: AnimatedSprite.__init__

Here's what an `AnimatedSprite` looks like:

.. autoclass:: AnimatedSprite

To update the animation, so that it progresses, you need
to pass the :class:`pygame.time.Clock` you
:meth:`pygame.time.Clock.tick()` in your main loop.
Here's another sample of how you'd use :class:`AnimatedSprite`::

    pygame.init()
    screen = pygame.display.set_mode([700, 500])
    clock = pygame.time.Clock()
    done = False

    while not done:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               done = True 

       screen.blit(animated_sprite.image)
       animated_sprite.update(clock)
       pygame.display.flip()
       clock.tick(60)

    pygame.quit()

