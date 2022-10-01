import bench1v as b1v
import load_driver as ldr
from DEMC import DEMC1v 
from RADE import RADE1v
import basic_function as bf
import numpy as np
import sys

func_name = ["gsl_sf_airy_Ai", "gsl_sf_airy_Bi", "gsl_sf_airy_Ai_scaled", "gsl_sf_airy_Bi_scaled", "gsl_sf_airy_Ai_deriv", "gsl_sf_airy_Bi_deriv", "gsl_sf_airy_Ai_deriv_scaled", "gsl_sf_airy_Bi_deriv_scaled", "gsl_sf_bessel_J0", "gsl_sf_bessel_J1", "gsl_sf_bessel_Y0", "gsl_sf_bessel_Y1", "gsl_sf_bessel_j1", "gsl_sf_bessel_j2", "gsl_sf_bessel_y0", "gsl_sf_bessel_y1", "gsl_sf_bessel_y2", "gsl_sf_clausen", "gsl_sf_dilog", "gsl_sf_expint_E1", "gsl_sf_expint_E2", "gsl_sf_expint_E1_scaled", "gsl_sf_expint_E2_scaled", "gsl_sf_expint_Ei", "gsl_sf_expint_Ei_scaled", "gsl_sf_Chi", "gsl_sf_Ci", "gsl_sf_lngamma", "gsl_sf_lambert_W0", "gsl_sf_lambert_Wm1", "gsl_sf_legendre_P2", "gsl_sf_legendre_P3", "gsl_sf_legendre_Q1", "gsl_sf_psi", "gsl_sf_psi_1", "gsl_sf_sin", "gsl_sf_cos", "gsl_sf_sinc", "gsl_sf_lnsinh", "gsl_sf_zeta", "gsl_sf_zetam1", "gsl_sf_eta"]
demc_fname = [u'gsl_sf_airy_Ai', u'gsl_sf_airy_Bi', u'gsl_sf_airy_Ai_deriv', u'gsl_sf_airy_Bi_deriv', u'gsl_sf_bessel_J0', u'gsl_sf_bessel_J1', u'gsl_sf_bessel_Y0', u'gsl_sf_bessel_Y1', u'gsl_sf_clausen', u'gsl_sf_expint_Ei', u'gsl_sf_legendre_P2', u'gsl_sf_legendre_P3', u'gsl_sf_legendre_Q1', u'gsl_sf_psi', u'gsl_sf_psi_1', u'gsl_sf_Chi', u'gsl_sf_Ci', u'gsl_sf_lnsinh', u'gsl_sf_zeta', u'gsl_sf_eta']

demc_inpdm = [[[-1000.0, 1000.0]], [[-1000.0, 1000.0]], [[-1000.0, 1000.0]], [[-1000.0, 1000.0]], [[-1e+10, 1e+10]], [[-1e+10, 1e+10]], [[-1e+10, 1e+10]], [[-1e+10, 1e+10]], [[-823549.6645, 823549.6645]], [[-701.8334146820821, 701.8334146820821]], [[-1e+100, 1e+100]], [[-1e+100, 1e+100]], [[-1, 1e+100]], [[-262144.0, 1e10]], [[-10, 10000000000.0]], [[-701.8334146820821, 701.8334146820821]], [[0, 823549.6645]], [[0, 1e+100]], [[-170, 1000]], [[-168, 100]]]

Atomic_Input = [ -4.042852549222488e+11,  -7.237129918123468e+11, -3.073966210399579e+11,  -8.002750158072251e+11,  -1.018792971647468e+00,  -2.294439682614124e+00, -1.018792971647467e+00,  -2.294439682614120e+00, 2.404825557695774e+00, 3.831705970207514e+00, 3.957678419314854e+00, 2.197141326031017e+00,  -7.725251836937709e+00,  9.095011330476359e+00,  2.585919463588284e+17,  9.361876298934626e+16,  1.586407411088372e+17,  1.252935780352301e+14, 1.259517036984501e+01, -3.725074107813663e-01, -1.347155251069168e+00,  -3.725074107813663e-01, -2.709975303391678e+228,  3.725074107813668e-01, 3.725074107813666e-01, 5.238225713898647e-01, 2.311778262696607e+17, -2.457024738220797e+00, 1.666385643189201e-41, 1.287978304826439e-121,  -5.773502691896254e-01, 7.745966692414830e-01, 8.335565596009644e-01,  -6.678418213073426e+00,  -4.799999999999998e+01,  -5.037566598712291e+17, -1.511080519199221e+17, 3.050995817918706e+15,  8.813735870195427e-01,  -9.999999999999984e+00,  -1.699999999999999e+02,  -9.999999999999989e+00]

np.seterr(invalid='ignore')
np.seterr(all='ignore')

all_input = bf.gen_all_bounds()
inter_funcs = bf.load_pickle('fun_index.pkl')
# atomic_idx = [48, 52, 49, 53, 46, 50, 47, 51, 12, 13, 21, 22, 28, 29, 34, 35, 36, 0, 5, 152, 154, 153, 155, 156, 157, 146, 147, 101, 43, 44, 69, 70, 72, 118, 116, 84, 80, 85, 83, 142, 143, 140]
# demc_idx =[48, 52, 46, 50, 12, 13, 21, 22, 0, 156, 69, 70, 72, 118, 116, 146, 147, 83, 142, 140]
demc_idx = [0, 5, 6, 8, 12, 13, 15, 17, 21, 22, 39, 40, 42, 43, 46, 48, 50, 52, 68, 69, 70, 71, 72, 76, 77, 78, 79, 80, 82, 83, 84, 85, 94, 98, 101, 105, 107, 116, 118, 133, 140, 142, 146, 147, 148, 149, 152, 154, 156]
def get_demc_inpdm(fname):
  count = 0
  inpdm = []
  for i in demc_fname:
    if i == fname:
      inpdm = demc_inpdm[count]
    count = count + 1
  return inpdm
  
def get_demc_count(fname):
  count = 0
  temp_count = 0
  for i in b1v.nrfl_fname:
    if i == fname:
      temp_count = count
      break
    count = count + 1
  return temp_count

def load_1v_rf(fun_name):
  for i,j,k in zip(b1v.ngfl_fname,b1v.rfl,b1v.input_domain):
    if i.strip() == fun_name:#去除fp(x)名字首尾空格
      # print(i)
      return j,k #返回j=f(x)，k=输入域


#[0,2-1022):0 [2-1022,2-1021):1 依次类推 为偶函数
def getFPEXP(x):
  # return x
  DBL_EXPOMASK = 0x7FF0000000000000;
  int_x = bf.floatToRawLongBits(x)
  return ((int_x & DBL_EXPOMASK) >> 52)

def find_max_bound_test(test_fun,repeat):
  temp_count = get_demc_count(test_fun[-1])
  fpx= ldr.load_gsl_pure(test_fun)
  print(test_fun)
  try:
    fx,inpdm = load_1v_rf(test_fun[-1])
  except:
    fx = fpx
  inpdm = get_demc_inpdm(test_fun[-1])
  inpdm = b1v.input_domain[temp_count]
  DEMC1v(fx,fpx,inpdm[0],test_fun[-1],repeat,72000)

  
  
def getlen(test_fun):
    vartyp_len = 0
    for i in test_fun[1]:
        if i[0] == 'double':
            vartyp_len = vartyp_len + 1
        if i[0] == 'int':
            vartyp_len = vartyp_len + 1
    return vartyp_len
  
import multiprocessing as mp
def fpara_gen(para_test_wrap,indx_funs,cpus):
    # Redefine, with only 1 mandatory argument.
    pool = mp.Pool(cpus)

    pool.map(para_test_wrap, [ i for i in indx_funs])

    pool.close()

def para_test(idx):
  find_max_bound_test(inter_funcs[idx],repeat)

if __name__ == "__main__":
  cpus = int(sys.argv[1])
  repeat = int(sys.argv[2])
  # para_test_wrap = lambda x: para_test(x,repeat)
  fpara_gen(para_test,demc_idx,cpus) 
