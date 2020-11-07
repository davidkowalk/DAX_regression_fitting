# include <stdio.h>
# include "gradient_descent.c"
# include "data.h"
# include "io_utils.c"


double get_error(double *weights, uint weights_len, uint pos) {

  double summ = 0;
  //printf("Pos: %u\n", pos);

  for(uint i = 0; i<weights_len; i++) {
    //printf("\tPoint: %f\n", weights[i] * data[pos+i+1]);
    summ += weights[i] * data[pos+i+1];
  }

  double error = fabs(data[pos]-summ);

  return error;

}


double get_average_error(double *weights, uint len) {

  double average_error = 0;
  double error;

  for(uint i = 0; i<data_len-30; i++) {
    error = get_error(weights, len, i);

    //printf("\tError: %f\n", get_error(weights, len, i));

    average_error += error;

  }

  return average_error/(data_len-30);
}

void main() {

  //printf("Error at 8: %f\n", get_error(weights, 5, 8));
  //double avg_error = get_average_error(weights, 5);
  //printf("Avg. Error: %f", avg_error);

  //*function, input dimensions, *start position (Weights)
  //precision, gamma, max iters, dx
  //*output, *iterations

  double weights[] = {
    5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
    5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0
  };
  uint dimensions = 20;

  double precision = 0.02;
  double gamma = 0.002;
  double dx = 0.0001; //dx for derivative

  unsigned int max_iters = 1000;

  unsigned int iterations = 0;
  double out_precision = 0;
  double output[dimensions];

  printf("Running Gradient Descent\n");

  gradient_descent_double(
    &get_average_error, dimensions, weights,
    precision, gamma, max_iters, dx,
    output, &out_precision, &iterations
  );

  print_double_array(output, dimensions);

  printf("Iters:\t\t%u\n", iterations);
  printf("Precision:\t%f", out_precision);

}
