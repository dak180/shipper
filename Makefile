# Makefile for the shipper project

VERS=$(shell sed <shipper -n -e '/^version *= *\(.*\)/s//\1/p')

MANDIR=$(DESTDIR)/usr/share/man/man1
BINDIR=$(DESTDIR)/usr/bin

DOCS    = README COPYING shipper.xml shipper.1
SOURCES = shipper Makefile $(DOCS) control shipper-logo.png

all: shipper-$(VERS).tar.gz

install: shipper.1
	cp shipper $(BINDIR)
	gzip <shipper.1 >$(MANDIR)/shipper.1.gz

shipper.1: shipper.xml
	xmlto man shipper.xml
shipper.html: shipper.xml
	xmlto html-nochunks shipper.xml

shipper-$(VERS).tar.gz: $(SOURCES)
	@mkdir shipper-$(VERS)
	@cp $(SOURCES) shipper-$(VERS)
	@tar -czf shipper-$(VERS).tar.gz shipper-$(VERS)
	@rm -fr shipper-$(VERS)

shipper-$(VERS).md5: shipper-$(VERS).tar.gz
	md5sum shipper-$(VERS).tar.gz >shipper-$(VERS).md5

clean:
	rm -f *.1 *.tar.gz *.rpm *.tar.gz SHIPPER.* *.html *.md5 *.sha*

version:
	echo $(VERS)

PYLINTOPTS = --rcfile=/dev/null --reports=n --include-ids=y --disable=C0103,C0111,C0301,W0122,W0511,W0603,W0612,W0621,W0631,R0902,R0912,R0915
pylint:
	@pylint --output-format=parseable $(PYLINTOPTS) shipper

dist: shipper-$(VERS).tar.gz shipper-$(VERS).md5 

release: shipper-$(VERS).tar.gz shipper.html
	shipper -u -m -t; make clean

