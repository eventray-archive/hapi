.DEFAULT_GOAL = development
.PHONY = development clean
SHELL := /bin/bash

bootstrap.py :
	@ if [ ! -f "bootstrap.py" ]; then \
		wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py; \
		python bootstrap.py; \
	  fi

development : bootstrap.py
	bin/buildout

clean :
	rm -rf bin develop-eggs eggs parts .installed.cfg downloads bootstrap.py *.egg-info src
	find . -name "*~" -exec rm {} \;
	find . -name "*.pyc" -exec rm {} \;
