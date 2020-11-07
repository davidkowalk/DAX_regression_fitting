# ifndef uint
# define uint unsigned int
# endif

# ifndef arrayprint
# define arrayprint

void print_double_array(double *array, unsigned int len) {
  printf("[\n");
  for(unsigned int i = 0; i<len; i++) {
    printf("\t%f", array[i]);

    if(i != len-1) {
      printf(",\n");
    }
  }

  printf("\n]\n");
}

# endif
