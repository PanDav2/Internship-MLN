YAPPS=yapps

all: parser.py

parser.py: parser_grammar.g
	${YAPPS} parser_grammar.g parser.py

clean:
	rm -f parser.py