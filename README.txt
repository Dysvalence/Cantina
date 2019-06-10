This was written for a coding challenge as part of a hiring process, where I was expressly told to post to a public github repo.

Requires python 3 (written and tested on 3.6), and an active internet connection- the code grabs the json directly from the internet.

To run the program as specced, execute challenge.py

To run tests, execute tests.py

Assumptions:
    -prettyprint is sufficient
    -the input json file isn't going to change
    -Multiple selectors will always begin with a class, and have up to one other identifier or className. Chaining more isn't too hard, but I don't want to scope creep.
    -Valid input, e.g. not #.#.#.
    -Support for multiple selectors was implemented through a wrapper function instead of a proper refactor

Known issues:
    -classNames are stored as lists, and the code for parsing them causes duplicate entries to be displayed when chaining. Corresponding line in tests.py is commented out. I'd fix this but frankly I have other things to do.