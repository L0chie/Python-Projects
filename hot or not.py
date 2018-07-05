Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> ariana_grande = ('24 | 1.53m | 9')
>>> ariana_grande
'24 | 1.53m | 9'
>>> age, height, sexiness = ariana_grande.split('|')
>>> age
'24 '
>>> split
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    split
NameError: name 'split' is not defined
>>> sexiness
' 9'
>>> ariana_age, ariana_height, ariana_sexiness = ariana_grande.split('|')
>>> ariana_age
'24 '
>>> jennifer_lawrence = ('27 | 1.75 | 8')
>>> jennifer_age, jennifer_height, jennifer_sexiness = jennifer_lawrence.split('|')
>>> jennifer_sexiness
' 8'
>>> gal_gadot = ('32 | 1.78m | 9')
>>> gal_age, gal_height, gal_sexiness = gal_gadot.split('|')
>>> gal_sexiness
' 9'
>>> alissa_violet = ('21 | unknown | 10')
>>> allisa_age, alissa_height, alissa_sexiness = alissa_violet.split('|')
>>> allissa_age
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    allissa_age
NameError: name 'allissa_age' is not defined
>>> alisa_age, alissa_height, alissa_sexiness = alissa_violet.split('|')
>>> alissa_age, alissa_height, alissa_sexiness = alissa_violet.split('|')
>>> alissa_sexiness
' 10'
>>> demi_lovato = ('25 | 1.61m | 8')
>>> demi_age, demi_height, demi_sexiness = demi_lovato.split("\")
							 
SyntaxError: EOL while scanning string literal
>>> demi_age, demi_height, demi_sexiness = demi_lovato.split('|')
>>> demi_sexiness
' 8'
>>> camila_cabello = ('20 | 1.57m | 8')
>>> camila_age, camila_height, camila_sexiness = camila_cabello.split('|')
>>> camila_sexiness
' 8'
>>> taylor_swift = ('27 | 1.8m | 8')
>>> taylor_age, taylor_height, taylor_sexiness = taylor_swift.split('|')
>>> taylor_sexiness
' 8'
>>> katy_perry = ('33 | 1.75 | 6')
>>> katy_age, katy_height, katy_sexiness = katy_perry.split('|')
>>> katy_perry.sexiness
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    katy_perry.sexiness
AttributeError: 'str' object has no attribute 'sexiness'
>>> katy-sexiness
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    katy-sexiness
NameError: name 'katy' is not defined
>>> katy_sexiness
' 6'
>>> selena_gomez = ('25 | 1.65m | 9')
>>> selena_age, selena_height, selena_sexiness = selena_gomez.split('|')
>>> selena_sexiness
' 9'
>>> gigi_hadid = ('22 | 1.79 | 9')
>>> gigi_age, gigi_height, gigi_sexiness = gigi_hadid.split('|')
>>> kate_upton = ('25 | 1.78m | 9')
>>> kate_age, kate_height, kate_sexiness = kate_upton.split('|')
>>> jessica_alba = ('36 | 1.69m | 8')
>>> jessica_age, jessica_height, jessica_sexiness = jessica_alba.split('|')
>>> 
