deps:
	pip3 install -r requirements.txt
pyflakes:
	pyflakes
test:
	PYTHONPATH=. py.test tests/* 
pep8:
	pep8 -r --ignore=E202,E501,E221,W291,W391,E302,E251,E203,W293,E231,E303,E201,E225,E261,E241 warpseq/ 
