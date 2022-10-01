#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <math.h>
#include "gsl/gsl_sf.h"
#include "gsl/gsl_errno.h"
#include "gslsfdr.h"

double gslfdr(double x,double y,double z,double p){
    gsl_set_error_handler_off ();
    gsl_sf_result result;
gsl_sf_ellint_RJ_e(x,y,z,p,0,&result);
//    struct_assign(&result,&res_status,stat);
    return result.val;
}

