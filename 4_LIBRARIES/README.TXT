Hints
Note that the emoji module comes with two functions, per pypi.org/project/emoji, one of which is emojize, which takes an optional, 
named parameter called language. You can install it with:
  pip install emoji

You can install pyfiglet with:
  pip install pyfiglet
The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
  from pyfiglet import Figlet

  figlet = Figlet()
You can then get a list of available fonts with code like this:
  figlet.getFonts()
You can set the font with code like this, wherein f is the font’s name as a str:
  figlet.setFont(font=f)
And you can output text in that font with code like this, wherein s is that text as a str:
  print(figlet.renderText(s))
Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.

Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:
pip install inflect

Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.

Note that you can raise an exception like ValueError with code like:
raise ValueError
