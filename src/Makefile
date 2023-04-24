NAME = xzhukd00_xlusky00_xterge00_xkinas00

.PHONY: all pack clean test doc run profile install initialization

all: initialization run
	chmod +x GUI.py

initialization:
	sudo apt-get install python3
	sudo apt-get install python3-tk
	sudo apt-get install doxygen
	pip install PyQt5

test: calc_tests.py
	python3 -m unittest -v $<

pack: clean doc install
	rm -rf ../../$(NAME).zip
	mkdir -p ../../$(NAME)/doc && cp -ar ../doc/. ../../$(NAME)/doc
	mkdir -p ../../$(NAME)/repo && cp -r ../ivs-project2/. ../../$(NAME)/repo #здесь я так и непоняла что за ivs-project2
	mkdir ../../$(NAME)/install && cp -r ../install/. ../../$(NAME)/install
	cd ../.. && zip -qr $(NAME).zip $(NAME)
	cd ../.. && rm -rf $(NAME)


run:
	python3 GUI.py

doc: Doxyfile
	rm -rf ../doc
	doxygen $<
	mv doc ../
	mv warning_doxygen.txt ../doc

profile: profiling.py
	python3 $<

install: GUI.py logic.py
	rm -rf ../install/*.deb
	bash installer.sh

clean:
	rm -r -f __pycache__ ../doc ../install warning_doxygen.txt ../../$(NAME)
