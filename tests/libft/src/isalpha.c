#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int ft_isalpha(int c);

int main(int argc, char **argv) {
  if (argc != 2)
    return 100;

  int test = atoi(argv[1]);
  int libft = ft_isalpha(test);
  int std = isalpha(test);

  // Since the std returns 1024 instead of 1 or 0 need to convert it to a
  // boolean. The same goes for the libft version
  if (!!std != !!libft)
    return 1;

  return 0;
}
