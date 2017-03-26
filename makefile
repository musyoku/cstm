CC = g++
CFLAGS = -I`python -c 'from distutils.sysconfig import *; print get_python_inc()'` -std=c++11 -L/usr/local/lib -lboost_serialization -lboost_python -lpython2.7 -O3 -fomit-frame-pointer -DNDEBUG -fno-operator-names -msse2 -mfpmath=sse -march=native
CFLAGS_SO = -I`python -c 'from distutils.sysconfig import *; print get_python_inc()'` -shared -fPIC -std=c++11 -L/usr/local/lib -lboost_serialization -lboost_python -lpython2.7 -O3 -fomit-frame-pointer -DNDEBUG -fno-operator-names -msse2 -mfpmath=sse -march=native

install: ## Python用ライブラリをビルドします.
	$(CC) model.cpp -o model.so $(CFLAGS_SO)

test: ## LLDB用.
	$(CC) test.cpp $(CFLAGS)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help