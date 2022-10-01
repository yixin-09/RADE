#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <math.h>
#include "gsl/gsl_sf.h"
#include "gsl/gsl_errno.h"
#include "gslsfdr.h"

double gslfdr(double a,double b){
    gsl_set_error_handler_off ();
    gsl_sf_result result;
gsl_sf_beta_e(a,b,&result);
//    struct_assign(&result,&res_status,stat);
    return result.val;
}

