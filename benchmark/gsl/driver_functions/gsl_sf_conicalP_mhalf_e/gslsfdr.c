#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <math.h>
#include "gsl/gsl_sf.h"
#include "gsl/gsl_errno.h"
#include "gslsfdr.h"

double gslfdr(double lambda,double x){
    gsl_set_error_handler_off ();
    gsl_sf_result result;
gsl_sf_conicalP_mhalf_e(lambda,x,&result);
//    struct_assign(&result,&res_status,stat);
    return result.val;
}

