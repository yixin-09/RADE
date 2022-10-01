from calendar import c
from itertools import count
from math import fabs
from time import time
import xlrd
import numpy as np
import xlwt
from xlutils.copy import copy
from RADE import relative_error
from bench_name_list import func_name_88,DEMC_49 
import basic_function as bf
import pickle
import load_driver as ldr
import bench1v as b1v
import mpmath
import os

inter_funcs = bf.load_pickle('fun_index.pkl')

func_name = ["gsl_sf_airy_Ai", "gsl_sf_airy_Bi", "gsl_sf_airy_Ai_scaled", "gsl_sf_airy_Bi_scaled", "gsl_sf_airy_Ai_deriv", "gsl_sf_airy_Bi_deriv", "gsl_sf_airy_Ai_deriv_scaled", "gsl_sf_airy_Bi_deriv_scaled", "gsl_sf_bessel_J0", "gsl_sf_bessel_J1", "gsl_sf_bessel_Y0", "gsl_sf_bessel_Y1", "gsl_sf_bessel_j1", "gsl_sf_bessel_j2", "gsl_sf_bessel_y0", "gsl_sf_bessel_y1", "gsl_sf_bessel_y2", "gsl_sf_clausen", "gsl_sf_dilog", "gsl_sf_expint_E1", "gsl_sf_expint_E2", "gsl_sf_expint_E1_scaled", "gsl_sf_expint_E2_scaled", "gsl_sf_expint_Ei", "gsl_sf_expint_Ei_scaled", "gsl_sf_Chi", "gsl_sf_Ci", "gsl_sf_lngamma", "gsl_sf_lambert_W0", "gsl_sf_lambert_Wm1", "gsl_sf_legendre_P2", "gsl_sf_legendre_P3", "gsl_sf_legendre_Q1", "gsl_sf_psi", "gsl_sf_psi_1", "gsl_sf_sin", "gsl_sf_cos", "gsl_sf_sinc", "gsl_sf_lnsinh", "gsl_sf_zeta", "gsl_sf_zetam1", "gsl_sf_eta"]

Input = [ -4.042852549222488e+11,  -7.237129918123468e+11, -3.073966210399579e+11,  -8.002750158072251e+11,  -1.018792971647468e+00,  -2.294439682614124e+00, -1.018792971647467e+00,  -2.294439682614120e+00, 2.404825557695774e+00, 3.831705970207514e+00, 3.957678419314854e+00, 2.197141326031017e+00,  -7.725251836937709e+00,  9.095011330476359e+00,  2.585919463588284e+17,  9.361876298934626e+16,  1.586407411088372e+17,  1.252935780352301e+14, 1.259517036984501e+01, -3.725074107813663e-01, -1.347155251069168e+00,  -3.725074107813663e-01, -2.709975303391678e+228,  3.725074107813668e-01, 3.725074107813666e-01, 5.238225713898647e-01, 2.311778262696607e+17, -2.457024738220797e+00, 1.666385643189201e-41, 1.287978304826439e-121,  -5.773502691896254e-01, 7.745966692414830e-01, 8.335565596009644e-01,  -6.678418213073426e+00,  -4.799999999999998e+01,  -5.037566598712291e+17, -1.511080519199221e+17, 3.050995817918706e+15,  8.813735870195427e-01,  -9.999999999999984e+00,  -1.699999999999999e+02,  -9.999999999999989e+00]



def load_1v_rf(fun_name):
  for i,j,k in zip(b1v.ngfl_fname,b1v.rfl,b1v.input_domain):
    if i.strip() == fun_name:#去除fp(x)名字首尾空格
      # print(i)
      return j,k #返回j=f(x)，k=输入域
def search_around(fx,fpx,inp):
    inp_lst = []
    for i in range(0,100):
        inp_lst.append([i,inp+bf.getulp(inp)*i])
    for i in range(0,100):
        inp_lst.append([-i,inp+bf.getulp(inp)*(-i)])
    rel_errs = []
    for i in inp_lst:
        rel_errs.append([relative_error(fx,fpx,i[1]),i])
    return rel_errs

idx_lst = [48, 52, 49, 53, 46, 50, 47, 51, 12, 13, 21, 22, 28, 29, 34, 35, 36, 0, 5, 152, 154, 153, 155, 156, 157, 146, 147, 101, 43, 44, 69, 70, 72, 118, 116, 84, 80, 85, 83, 142, 143, 140]
count = 0
final_res = []
for i in idx_lst:
    test_fun = inter_funcs[i]
    fpx= ldr.load_gsl_pure(test_fun)
    try:
        fx,inpdm = load_1v_rf(test_fun[-1])
    except:
        print("excpts")
        fx = fpx
    inp = Input[count]
    ori_rel_err = relative_error(fx,fpx,Input[count])
    rel_errs = search_around(fx,fpx,inp)
    rel_errs = sorted(rel_errs,reverse=True)
    if rel_errs[0][0]>ori_rel_err:
        print(test_fun)
        inp = rel_errs[0][1][1]
        print(relative_error(fpx,fx,inp))
        print(ori_rel_err)
        print(rel_errs[0])
        final_res.append([test_fun[-1][7:],ori_rel_err,rel_errs[0][1][0],rel_errs[0][0],inp])
    count = count + 1
final_res = sorted(final_res,key=lambda x: fabs(x[2]),reverse=True)
new_excel = xlwt.Workbook()
sheet = new_excel.add_sheet("ATOMvsRADE")
sheet.write(0,0,"benchmark")
sheet.write(1, 1, "RelErr")
sheet.write(1, 2, "Ulp to x0")
sheet.write(1, 3, "After RelErr")
new_excel.save("search_around.xls")

old_excel = xlrd.open_workbook("search_around.xls", formatting_info=True)
new_excel = copy(old_excel)
sheet = new_excel.get_sheet(0)
k = 2
for i in final_res:
    sheet.write(k,0,i[0])
    sheet.write(k,1,("%.18e" % i[1]))
    sheet.write(k,2,str(i[2])+"ulp")
    sheet.write(k,3,("%.18e" % i[3]))
    sheet.write(k,4,("%.18e" % i[4]))
    k = k + 1
new_excel.save("search_around.xls")
os.system("cp search_around.xls ../experiments/")