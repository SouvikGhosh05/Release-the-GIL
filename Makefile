build:
	chmod +x ./build.sh
	./build.sh

test:
	pip3 install -U -r requirements.txt
	pytest -v .
clean:
	chmod +x ./clean.sh
	./clean.sh
