This is a Doom source port regression testing system that uses the
thousands of demos in the
[Compet-N archive](https://doomwiki.org/wiki/Compet-n) to test demo
playback. It was developed for Chocolate Doom but it may be useful for
other source ports as well.

The demos have been played back in vanilla Doom running in
[statdump.exe](https://github.com/fragglet/vanilla-utilities)
to save statistics about the levels that were completed. The output
from statdump.exe (in the form of .txt files) gives a useful set of
expected outputs. A source port able to output the same statistics
data can then be tested by playing back the same demos and comparing
against this expected data set.

See [the Chocolate Doom
website](https://www.chocolate-doom.org/wiki/index.php/Statcheck) for
details about how to run the test suite.

