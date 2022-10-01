import bench1v as b1v
# from Onevbench import gfl
import load_driver as ldr
from RADE import RADE1v
import basic_function as bf
import numpy as np
import time
import sys

func_name = ["gsl_sf_airy_Ai", "gsl_sf_airy_Bi", "gsl_sf_airy_Ai_scaled", "gsl_sf_airy_Bi_scaled", "gsl_sf_airy_Ai_deriv", "gsl_sf_airy_Bi_deriv", "gsl_sf_airy_Ai_deriv_scaled", "gsl_sf_airy_Bi_deriv_scaled", "gsl_sf_bessel_J0", "gsl_sf_bessel_J1", "gsl_sf_bessel_Y0", "gsl_sf_bessel_Y1", "gsl_sf_bessel_j1", "gsl_sf_bessel_j2", "gsl_sf_bessel_y0", "gsl_sf_bessel_y1", "gsl_sf_bessel_y2", "gsl_sf_clausen", "gsl_sf_dilog", "gsl_sf_expint_E1", "gsl_sf_expint_E2", "gsl_sf_expint_E1_scaled", "gsl_sf_expint_E2_scaled", "gsl_sf_expint_Ei", "gsl_sf_expint_Ei_scaled", "gsl_sf_Chi", "gsl_sf_Ci", "gsl_sf_lngamma", "gsl_sf_lambert_W0", "gsl_sf_lambert_Wm1", "gsl_sf_legendre_P2", "gsl_sf_legendre_P3", "gsl_sf_legendre_Q1", "gsl_sf_psi", "gsl_sf_psi_1", "gsl_sf_sin", "gsl_sf_cos", "gsl_sf_sinc", "gsl_sf_lnsinh", "gsl_sf_zeta", "gsl_sf_zetam1", "gsl_sf_eta"]


Atomic_Input = [ -4.042852549222488e+11,  -7.237129918123468e+11, -3.073966210399579e+11,  -8.002750158072251e+11,  -1.018792971647468e+00,  -2.294439682614124e+00, -1.018792971647467e+00,  -2.294439682614120e+00, 2.404825557695774e+00, 3.831705970207514e+00, 3.957678419314854e+00, 2.197141326031017e+00,  -7.725251836937709e+00,  9.095011330476359e+00,  2.585919463588284e+17,  9.361876298934626e+16,  1.586407411088372e+17,  1.252935780352301e+14, 1.259517036984501e+01, -3.725074107813663e-01, -1.347155251069168e+00,  -3.725074107813663e-01, -2.709975303391678e+228,  3.725074107813668e-01, 3.725074107813666e-01, 5.238225713898647e-01, 2.311778262696607e+17, -2.457024738220797e+00, 1.666385643189201e-41, 1.287978304826439e-121,  -5.773502691896254e-01, 7.745966692414830e-01, 8.335565596009644e-01,  -6.678418213073426e+00,  -4.799999999999998e+01,  -5.037566598712291e+17, -1.511080519199221e+17, 3.050995817918706e+15,  8.813735870195427e-01,  -9.999999999999984e+00,  -1.699999999999999e+02,  -9.999999999999989e+00]

np.seterr(invalid='ignore')
np.seterr(all='ignore')
demc_fname = [u'gsl_sf_airy_Ai', u'gsl_sf_airy_Bi', u'gsl_sf_airy_Ai_deriv', u'gsl_sf_airy_Bi_deriv', u'gsl_sf_bessel_J0', u'gsl_sf_bessel_J1', u'gsl_sf_bessel_Y0', u'gsl_sf_bessel_Y1', u'gsl_sf_clausen', u'gsl_sf_expint_Ei', u'gsl_sf_legendre_P2', u'gsl_sf_legendre_P3', u'gsl_sf_legendre_Q1', u'gsl_sf_psi', u'gsl_sf_psi_1', u'gsl_sf_Chi', u'gsl_sf_Ci', u'gsl_sf_lnsinh', u'gsl_sf_zeta', u'gsl_sf_eta']
all_input = bf.gen_all_bounds()
inter_funcs = bf.load_pickle('fun_index.pkl')
atomic_idx_list = [0, 5, 6, 7, 8, 9, 12, 13, 15, 16, 17, 18, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 68, 69, 70, 71, 72, 76, 77, 78, 79, 80, 82, 83, 84, 85, 91, 94, 98, 101, 105, 107, 108, 109, 116, 118, 131, 133, 140, 142, 143, 146, 147, 148, 149, 152, 153, 154, 155, 156, 157]

def get_demc_count(fname):
  count = 0
  temp_count = 0
  for i in demc_fname:
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


def getFPEXP(x):
  # return x
  DBL_EXPOMASK = 0x7FF0000000000000;
  int_x = bf.floatToRawLongBits(x)
  exp_x = ((int_x & DBL_EXPOMASK) >> 52)
  return exp_x 

def generate_uniform(bound,n):
  fp_dis = bf.getUlpError(bound[0],bound[1])
  one_dis = float(fp_dis)/n
  inps = []
  if np.abs(bound[0])< np.abs(bound[1]):
    ulp_x = bf.getulp(bound[0])
  else:
    ulp_x = bf.getulp(bound[1])
  for i in range(n):
    inps.append(bound[0] + one_dis*i*ulp_x)
  return inps

# print(generate_uniform([1,2],10))
# print(generate_uniform([-2,-1],10))
    
    


def find_max_bound_test(test_fun,repeat):
    print(test_fun)
    fpx= ldr.load_gsl_pure(test_fun)
    try:
      fx,inpdm = load_1v_rf(test_fun[-1])
    except:
      fx = fpx
    record_res_l = []
    record_res_l2 = []
    break_tag=0
    st = time.time()
    for i in all_input:#依次处理所有区间
        res_l = []
        res_l2 = []
        x_l = list(np.random.uniform(i[0],i[1],28))#八个数的列表
        # x_l = generate_uniform(i,100)
        x_l.append(i[0])
        x_l.append(i[1])#包括区间边界在内的十个点
        for x0 in x_l:#依次处理区间内的十个点
            try:
                res = fpx(x0)
                exp_val =getFPEXP(res)
                err = 1.0/(exp_val+10)
                # err = 1.0/bf.fitness_fun1(fx,fpx,x0)
            except:
                print("You have triggered error")
                print(res)
                break_tag=1
                break
            if (np.isnan(res)|np.isinf(res)):
              break
            else:
              temp=[err,x0,i,res,exp_val]
              res_l.append(temp)
        if(break_tag==1):
          break    
        if len(res_l)!=0:
          arr = [0] * len(res_l)
          res_l = sorted(res_l,reverse=True)#按res_l每个temp[0]比较，由大到小，存了10个点里触发的最大误差
          for j in range(len(res_l)):
            res = res_l[j][3] #取每个temp的res值
            if res < 0:
              arr[j] = -res_l[j][-1]#负数
            else:
              arr[j] = res_l[j][-1]#正数
          variance_ten = np.max(arr) - np.min(arr)
          temp_max = 1.0 
          res_l[0][0] = variance_ten*temp_max
          record_res_l.append([res_l[0],variance_ten,arr,temp_max])#[[err,x0,区间,res,exp_val],方差,arr数组]
    record_res_l=sorted(record_res_l,reverse=True)
    dom_l = []
    for k in range(30):
      dom_l.append([record_res_l[k][0][2],record_res_l[k][0][1]])
    temp_dom_l = []
    for i in dom_l:
      flag = 0
      for j in temp_dom_l:
        if i[0]==j[0]:
          flag = 1
      if flag == 0:
        temp_dom_l.append(i)
    et_time = time.time()-st
    demc_res = RADE1v(fx,fpx,dom_l,test_fun[-1],repeat,7200,et_time)
    print(demc_res)
    x0 = float(demc_res[1])
    demc_res.append(et_time)
    demc_res.append(dom_l)
    try:
      y0 = float(np.abs((fpx(x0)-fx(x0))/(fx(x0)+bf.getulp(float(fx(x0))))))
    except:
      y0 = 0
    return y0,demc_res

  
  
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
  fpara_gen(para_test,atomic_idx_list,cpus) 
