Guide: 

https://sphinx-intro-tutorial.readthedocs.io/en/latest/sphinx_first_steps.html

https://www.youtube.com/watch?v=gWrc4xzm45Y
# Documentation guide
## Start (terminal) venv:
```
[../docs]$ activate
```
## Stop (terminal) venv:
```
[../docs]$ deactivate
```
## Open the ducumentation:
Open Google Chrome and paste in the path to the index.html file:
C:/Other/Github/Rammeverk/Augmentio/docs/_build/html/index.html

or 
on autobuild use this in your Google Chrome http://127.0.0.1:8000
## Start autobuild (terminal):
```
[../docs]$ sphinx-autobuild . ./_build/html
```
Then use this in your Google Chrome http://127.0.0.1:8000
# Manually build (terminal):
```
[../docs]$ ./make html
```
