APP=mediamachine
JS_FILES=media/js/index.js
MAX_COMPLEXITY=2

all: eslint jenkins

include *.mk

eslint: $(JS_SENTINAL)
	$(NODE_MODULES)/.bin/eslint $(JS_FILES)

.PHONY: eslint
