SRC      = src/Beyond-GIL/
TEST_SRC = src/Beyond-GIL/tests/

build:
	chmod +x ./build.sh
	./build.sh

test:
	python3 -m unittest discover -v --failfast  $(TEST_SRC) -t $(SRC) 
	@echo "Tests completed..."

lintcheck:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

clean:
	chmod +x ./clean.sh
	./clean.sh