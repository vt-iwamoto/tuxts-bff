build:
	docker build -t tuxts-bff .

run:
	docker run --rm -it -v $(CURDIR):/tuxts-bff -p 5000:5000 tuxts-bff

sh:
	docker run --rm -it -v $(CURDIR):/tuxts-bff -p 5000:5000 tuxts-bff sh
