#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <math.h>
#include "gsl/gsl_sf.h"
#include "gsl/gsl_errno.h"
#include "gslsfdr.h"

double gslfdr(double aR,double aI,double c,double x){
    gsl_set_error_handler_off ();
    gsl_sf_result result;
gsl_sf_hyperg_2F1_conj_renorm_e(aR,aI,c,x,&result);
//    struct_assign(&result,&res_status,stat);
    return result.val;
}

