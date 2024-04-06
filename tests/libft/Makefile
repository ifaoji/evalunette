CC = clang-12
CFLAGS = -Wall -Wextra -Werror -I. -L.
LFLAGS = -lft
BIN = bin

RAW_OBJS = isalpha

OBJS = $(RAW_OBJS:%=$(BIN)/%)

all: $(OBJS) 

$(BIN)/%: src/%.c | $(BIN)
	$(CC) $(CFLAGS) -o $@ $< $(LFLAGS)

isalpha: $(BIN)/isalpha

clean:
	rm -f $(BIN)/*

$(BIN):
	mkdir -p $(BIN)
