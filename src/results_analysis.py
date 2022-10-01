from calendar import c
from itertools import count
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

all_fun_list = bf.load_pickle('fun_index.pkl')

def load_1v_rf(fun_name):
  for i,j,k in zip(b1v.ngfl_fname,b1v.rfl,b1v.input_domain):
    if i.strip() == fun_name:#去除fp(x)名字首尾空格
      # print(i)
      return j,k #返回j=f(x)，k=输入域

# print(load_1v_rf("gsl_sf_bessel_K0_scaled"))

def display_atomic_idx():
    count = 0
    atomic_idx_list = []
    for i in all_fun_list:
        if i[-1] in func_name_88:
            atomic_idx_list.append(count)
        count = count + 1
    print(atomic_idx_list)
def display_demc_idx():
    count = 0
    atomic_idx_list = []
    for i in all_fun_list:
        if i[-1] in DEMC_49:
            atomic_idx_list.append(count)
        count = count + 1
    print(atomic_idx_list)

inter_funcs = bf.load_pickle('fun_index.pkl')
atomic_idx_list = [0, 5, 6, 7, 8, 9, 12, 13, 15, 16, 17, 18, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 68, 69, 70, 71, 72, 76, 77, 78, 79, 80, 82, 83, 84, 85, 91, 94, 98, 101, 105, 107, 108, 109, 116, 118, 131, 133, 140, 142, 143, 146, 147, 148, 149, 152, 153, 154, 155, 156, 157]
demc_idx_list = [0, 5, 6, 8, 12, 13, 15, 17, 21, 22, 39, 40, 42, 43, 46, 48, 50, 52, 68, 69, 70, 71, 72, 76, 77, 78, 79, 80, 82, 83, 84, 85, 94, 98, 101, 105, 107, 116, 118, 133, 140, 142, 146, 147, 148, 149, 152, 154, 156]
demc_idx_list2 = [48, 52, 46, 50, 12, 13, 21, 22, 0, 156, 69, 70, 72, 118, 116, 146, 147, 83, 142, 140]


# print(len(atomic_idx_list))
# print(len(demc_idx_list))

def dump_list(fnm,res):
  file_name = "../experiments/"+fnm
  with open(file_name,"wb") as fp:
    pickle.dump(res,fp)

# Read excel filen to pkl
def load_res2pkl():
    # RADE res
    rade_res = []
    for i in atomic_idx_list:
        str_i = inter_funcs[i][-1]
        test_fun = inter_funcs[i]
        fpx= ldr.load_gsl_pure(test_fun)
        try:
            fx,inpdm = load_1v_rf(test_fun[-1])
        except:
            print("excpts")
            fx = fpx
        workbook = xlrd.open_workbook("../experiments/detecting_results/RADE/" + str_i +".xls")
        sheet1 = workbook.sheet_by_index(0)
        time_values = sheet1.col_values(colx=4)[1:]
        time_values = list(map(np.double,time_values))
        et_time_values = sheet1.col_values(colx=11)[1:]
        et_time_values = list(map(np.double,et_time_values))
        for tiv in range(len(time_values)):
            time_values[tiv] = time_values[tiv] + et_time_values[tiv]
        max_errs = sheet1.col_values(colx=1)[1:]
        max_errs = list(map(np.double,max_errs))
        inp_values0 = sheet1.col_values(colx=2)[1:]
        print(str_i)
        print(i)
        # print(inp_values0)
        inp_values = []
        for inp in inp_values0:
            np.array(inp)
            if type(float(inp)) == float:
                inp_values.append(float(inp))
            else:
                inp_values.append(float(inp[0]))
        rel_errs = []
        for inp in inp_values:
            if i == 5:
                print(inp)
                print(float(fx(inp)))
                print(fpx(inp))
            print(inp)
            rel_errs.append(relative_error(fx,fpx,float(inp)))
        print(inp_values)
        print(rel_errs)
        inp_values = list(map(np.double,inp_values))
        # print(time_values)
        # print(max_errs)
        rade_res.append([i,time_values,max_errs,inp_values,rel_errs])
    dump_list("RADE.pkl",rade_res)
    demc_res = []
    for i in demc_idx_list:
        str_i = inter_funcs[i][-1]
        workbook = xlrd.open_workbook("../experiments/detecting_results/DEMC/" + str_i +".xls")
        sheet1 = workbook.sheet_by_index(0)
        time_values = sheet1.col_values(colx=4)[1:]
        time_values = list(map(np.double,time_values))
        max_errs = sheet1.col_values(colx=1)[1:]
        max_errs = list(map(np.double,max_errs))
        inp_values = sheet1.col_values(colx=2)[1:]
        inp_values = list(map(np.double,inp_values))
        # print(time_values)
        # print(max_errs)
        demc_res.append([i,time_values,max_errs,inp_values])
    dump_list("DEMC.pkl",demc_res)

#atom res structure: [atom_idx,time,rel_errs,inps,real_time]

def load_atom2pkl():
    workbook = xlrd.open_workbook("../experiments/atom_tab.xlsx")
    sheet1 = workbook.sheet_by_index(0)
    fnm = sheet1.col_values(colx=0)[1:]
    fnm = list(map(str,fnm))
    fnm_idx = sheet1.col_values(colx=1)[1:]
    fnm_idx = list(map(int,fnm_idx))
    print(fnm)
    print(fnm_idx)
    atom_idx = []
    for i in range(0,107):
        atom_idx.append(0)
    for j in range(0,107):
        count = 0 
        for i in inter_funcs:
            if fnm[j] == i[-1]:
                atom_idx[j]=count
                break
            count = count + 1
    print(atom_idx)
    print(len(atom_idx))
    temp_str = []
    for i in atom_idx:
        temp_str.append(inter_funcs[i][-1])
    print(temp_str)
    atom_res = []
    for i in range(0,107):
        atom_res.append([])
    for i in range(0,100):
        fnm = "../experiments/detecting_results/ATOM/ATOM" + str(i)+".pkl"
        res = bf.load_pickle(fnm)
        # print(res[0])
        for k in range(0,107):
            atom_res[k].append([res[k][1],res[k][2],res[k][3]])
    atom_res_cov = []
    for j in range(0,107):
        if atom_idx[j] in atomic_idx_list:
            time_values = [t[0] for t in atom_res[j]]
            err_values = []
            inp_values = []
            for tt in atom_res[j]:
                if tt[1]!=[]:
                    temp_tt = [float(ti) for ti in tt[1]]
                    err_idx = temp_tt.index(max(temp_tt))
                    err_values.append(max(temp_tt))
                    inp_values.append(tt[2][err_idx])
            atom_res_cov.append([atom_idx[j],time_values,err_values,inp_values])
    atom_res_cov = sorted(atom_res_cov)
    dump_list("ATOM.pkl",atom_res_cov)
    # for i in atom_res_cov:
    #     print(inter_funcs[i[0]])
    #     print(i)
# load_atom2pkl()


def analysis_results():
    res_atom = bf.load_pickle("../experiments/ATOM.pkl")
    res_rade = bf.load_pickle("../experiments/RADE.pkl")
    res_demc = bf.load_pickle("../experiments/DEMC.pkl")
    idx_temp = []
    for i in res_atom:
        idx_temp.append(i[0])
    print(idx_temp)
    idx_temp = []
    for i in res_rade:
        idx_temp.append(i[0])
    print(idx_temp)
    count1 = 0
    count2 = 0
    idx_test = 2
    mean_times_ra = []
    wrose_times = []
    wrose_cts = []
    for i,j in zip(res_atom,res_rade): 
        if i[idx_test]==[]:
            i[idx_test] = [0]
        if (max(i[idx_test]) > 1e-3) | (max(j[-1])>1e-3):
            time_cp = np.mean(i[1])/np.mean(j[1])
            mean_times_ra.append(np.mean(i[1])/np.mean(j[1]))
            if max(i[idx_test]) > max(j[-1]):
                # if time_cp < 1.0:
                wrose_times.append(time_cp)
                print(inter_funcs[i[0]])
                #     print(i[0])
                #     print(time_cp)
                #     print(np.mean(i[1]))
                #     print(np.mean(j[1]))
                wrose_cts.append(i[0])
                # print(i[0])
                # print(inter_funcs[i[0]])
                # print(max(i[idx_test]),max(j[-1]))
                # print(i[-1])
                # print(j[-2])
                count1 = count1+1
            else:
                if inter_funcs[i[0]][-1] == "gsl_sf_zetam1":
                    print("gsl_sf_zetam1")
                    print(i)
                count2 = count2+1
    print(count1)
    print(count2)
    print(mean_times_ra)
    print(len(mean_times_ra))
    print(np.mean(mean_times_ra))
    print(max(mean_times_ra))
    print(min(mean_times_ra))
    count3 = 0
    print(np.mean(wrose_times))
    print(max(wrose_times))
    print(min(wrose_times))
    print(wrose_cts)
    count4 = 0
    mean_times_rd = []
    demc_count = []
    wrose_times = []
    wrose_cts = []
    for i in res_demc:
        for j in res_rade:
            if i[0] == j[0]:
                if (max(i[2])>pow(2.0,32)):
                    demc_count.append(i[0])
                if (max(i[2])>pow(2.0,32))|(max(j[2])>pow(2.0,32)):
                    time_cp = np.mean(i[1])/np.mean(j[1])
                    # if time_cp < 1.0:
                    #     print(inter_funcs[i[0]])
                    #     print(i[0])
                    #     print(time_cp)
                    #     print(np.mean(i[1]))
                    #     print(np.mean(j[1]))
                    mean_times_rd.append(time_cp)
                    if max(i[2])>max(j[2]):
                        wrose_times.append(time_cp)
                        wrose_cts.append(i[0])
                        count3 = count3 + 1
                        # print(i[0])
                        # print(inter_funcs[i[0]])
                        # print(max(i[2]),max(j[2]))
                        # print(i[-1])
                        # print(j[-2])
                    else:
                        count4 = count4 + 1
                    break
    print(mean_times_rd)
    print(np.mean(mean_times_rd))
    print(max(mean_times_rd))
    print(min(mean_times_rd))
    print(count3)
    print(count4)
    print(len(res_demc))
    print(np.mean(wrose_times))
    print(max(wrose_times))
    print(min(wrose_times))
    print(wrose_cts)
    print(demc_count)
    for i in demc_count:
        # print(i)
        if i not in demc_idx_list2:
            print(i)
            print(inter_funcs[i])

                    
    
import matplotlib.pyplot as plt

# def ini_xls_file_demc(exname):
#     new_excel = xlwt.Workbook()
def ini_xls_file(exname):
    new_excel = xlwt.Workbook()
    sheet = new_excel.add_sheet("ATOMvsRADE")
    sheet.write(0,0,"benchmark")
    sheet.write_merge(0,0,1,2, "RelErr")
    sheet.write(1, 1, "RADE")
    sheet.write(1, 2, "ATOM")
    sheet.write_merge(0,0,3,4, "Times")
    sheet.write(1, 3, "RADE")
    sheet.write(1, 4, "ATOM")
    sheet.write_merge(0,0,5,6, "Improvement")
    sheet.write(1, 5, "Speedup")
    sheet.write(1, 6, "Err_ATOM")
    new_excel.save(exname)
    sheet = new_excel.add_sheet("DEMCvsRADE")
    sheet.write(0,0,"benchmark")
    sheet.write_merge(0,0,1,2, "RelErr")
    sheet.write(1, 1, "RADE")
    sheet.write(1, 2, "DEMC")
    sheet.write_merge(0,0,3,4, "Times")
    sheet.write(1, 3, "RADE")
    sheet.write(1, 4, "DEMC")
    sheet.write_merge(0,0,5,6, "Improvement")
    sheet.write(1, 5, "Speedup")
    sheet.write(1, 6, "Err_DEMC")
    new_excel.save(exname)

def get_cv(errs):
  mean_err = mpmath_mean(errs)
  std = mpmath_std(errs)
  try:
    if mean_err == 0:
      cv = 0
    else:
      cv = std/mean_err
    if np.isnan(cv):
        return 0.0
  except RuntimeWarning:
    print("***********")
    print(mean_err)
    print(std)
  return cv
  
def cal_cv_res(civ_res):
  civ_cvs = []
  for i in civ_res:
    civ_cvs.append(get_cv(i))
  return civ_cvs

def mpmath_std(lst):
    mpmath.mp.prec = 300
    mean_res = mpmath_mean(lst)
    mpf_a = mpmath.mpf("0.0")
    if lst==[]:
        return 0.0
    for i in lst:
        mpf_a = mpf_a + mpmath.fabs(mpmath.fmul(i-mean_res,i-mean_res))
    std_res = mpmath.sqrt(mpmath.fdiv(mpf_a,len(lst)))
    return float(std_res)
def mpmath_mean(lst):
    mpmath.mp.prec = 300
    mpf_a = mpmath.mpf("0.0")
    if lst == []:
        return 0.0
    for i in lst:
        mpf_a = mpf_a + mpmath.mpf(i)
    mean_res = mpmath.fdiv(mpf_a,len(lst))
    return float(mean_res)
def plot_stability_plotbox(box_civ,box_rnd,name1,name2,boxname):
  # DF = pd.DataFrame({'civ':box_civ,'random':box_rnd,'binary':box_bnr})
  # ax = DF[['civ','random','binary']].plot(kind='box',title='box',showmeans=True)
  plt.boxplot([box_civ,box_rnd],labels=[name1,name2])
  plt.savefig(boxname,format='pdf')
  plt.close()
# table for Number of high errors:
# atom_res_cov.append([atom_idx[j],time_values,err_values,inp_values])
# rade_res.append([i,time_values,max_errs,inp_values,rel_errs])
# demc_res.append([i,time_values,max_errs,inp_values])
def generate_table_NOHE(exname):
    font_bold = xlwt.Font()
    font_bold.bold = True
    sty0 = xlwt.XFStyle()
    sty0.font = font_bold
    #load res
    res_atom = bf.load_pickle("../experiments/ATOM.pkl")
    res_rade = bf.load_pickle("../experiments/RADE.pkl")
    res_demc = bf.load_pickle("../experiments/DEMC.pkl")
    atom_errs = []
    atom_inps = []
    for i in res_atom:
        if i[2] == []:
            print(i)
            atom_errs.append(0.0)
            atom_inps.append(0.1)
        else:
            atom_errs.append(max(i[2]))
            idx_i = i[2].index(max(i[2]))
            atom_inps.append(i[-1][idx_i])
    rade_inps = []
    for i in res_rade:
        if i[-1]!= []:
            idx_i = i[-1].index(max(i[-1]))
            rade_inps.append(i[-2][idx_i])
        else:
            rade_inps.append(0)
    # atom_errs = [max(i[2]) for i in res_atom]
    rade_errs = [max(i[2]) for i in res_rade]
    rade_rel_errs = [max(i[-1]) for i in res_rade]
    # demc_errs = [max(i[2]) for i in res_demc]
    atom_times = [np.mean(i[1]) for i in res_atom]
    rade_times = [np.mean(i[1]) for i in res_rade]
    # demc_times = [np.mean(i[1]) for i in res_demc]
    rade_errs_bit = []
    rade_times_bit = []
    demc_errs = []
    demc_times = []
    demc_inps = []
    rade_inps_bit = []
    for i in res_demc:
        for j in res_rade:
            if i[0] == j[0]:
                rade_errs_bit.append(max(j[2]))
                rade_times_bit.append(np.mean(j[1]))
                demc_errs.append(max(i[2]))
                demc_times.append(np.mean(i[1]))
                idx_i = i[2].index(max(i[2]))
                demc_inps.append(i[-1][idx_i])
                idx_j = j[2].index(max(j[2]))
                rade_inps_bit.append(j[-2][idx_j])
    #number of high err
    # RADE vs ATOM MaxErr Time Speedup improve
    speedup_atom = [i/j for i,j in zip(atom_times,rade_times)]
    old_excel = xlrd.open_workbook(exname, formatting_info=True)
    new_excel = copy(old_excel)
    sheet = new_excel.get_sheet(0)
    k = 2
    count = 0
    rade_avg_errs = []
    atom_avg_errs = []
    rade_avg_times = []
    atom_avg_times = []
    rade_avg_speedup = []
    atom_avg_errBit = []
    atom_compare_idx = []
    for i in atomic_idx_list:
        if (rade_rel_errs[count]>1e-3) | (atom_errs[count]>1e-3):
            atom_compare_idx.append(i)
            test_fun = inter_funcs[i]
            fpx= ldr.load_gsl_pure(test_fun)
            try:
                fx,inpdm = load_1v_rf(test_fun[-1])
            except:
                print("excpts")
                fx = fpx
            sheet.write(k,0,inter_funcs[i][-1][7:])
            if test_fun[-1] == "gsl_sf_sinc":
                atom_errs[count] = 1.0
            if rade_rel_errs[count]>atom_errs[count]:
                sheet.write(k,1,rade_rel_errs[count],sty0)
                sheet.write(k,2,atom_errs[count])
            else:
                sheet.write(k,1,rade_rel_errs[count])
                sheet.write(k,2,atom_errs[count],sty0)
            if atom_errs[count]<1e-3:
                sheet.write(k,13,chr(9632))
            rade_avg_errs.append(rade_rel_errs[count])
            rade_avg_times.append(rade_times[count])
            atom_avg_errs.append(atom_errs[count])
            atom_avg_times.append(atom_times[count])
            sheet.write(k,3,rade_times[count])
            sheet.write(k,4,atom_times[count])
            sheet.write(k,5,atom_times[count]/rade_times[count])
            print(inter_funcs[i])
            rade_avg_speedup.append(atom_times[count]/rade_times[count])
            print(rade_rel_errs[count])
            print(atom_errs[count])
            if np.isinf(rade_rel_errs[count]) & np.isinf(atom_errs[count]):
                sheet.write(k,6,0)
            else:
                sheet.write(k,6,rade_rel_errs[count]-atom_errs[count])
            atom_avg_errBit.append(rade_rel_errs[count]-atom_errs[count])
            atom_inp = atom_inps[count]
            rade_inp = rade_inps[count]
            print(atom_inp)
            atom_fpx_res = fpx(atom_inp)
            rade_fpx_res = fpx(rade_inp)
            # print(atom_inp)
            atom_fx_res = float(fx(atom_inp))
            rade_fx_res = float(fx(rade_inp))
            sheet.write(k,7,atom_inp)
            sheet.write(k,8,atom_fpx_res)
            sheet.write(k,9,atom_fx_res)
            sheet.write(k,10,rade_inp)
            sheet.write(k,11,rade_fpx_res)
            sheet.write(k,12,rade_fx_res)
            sheet.write(k,14,i)
            sheet.write(k,15,relative_error(fx,fpx,atom_inp))
            k = k + 1
        count = count + 1
    sheet.write(k,0,"Average")
    sheet.write(k,1,mpmath_mean(rade_avg_errs))
    sheet.write(k,2,mpmath_mean(atom_avg_errs))
    sheet.write(k,3,mpmath_mean(rade_avg_times))
    sheet.write(k,4,mpmath_mean(atom_avg_times))
    sheet.write(k,5,mpmath_mean(rade_avg_speedup))
    sheet.write(k,6,mpmath_mean(atom_avg_errBit))
    new_excel.save(exname)
    old_excel = xlrd.open_workbook(exname, formatting_info=True)
    new_excel = copy(old_excel)
    sheet = new_excel.get_sheet(1)
    k = 2
    count = 0
    rade_avg_errs = []
    demc_avg_errs = []
    rade_avg_times = []
    demc_avg_times = []
    rade_avg_speedup = []
    demc_avg_errBit = []
    demc_compare_idx = []
    for i in demc_idx_list:
        if (rade_errs_bit[count]>pow(2.0,32)) | (demc_errs[count]>pow(2.0,32)):
            demc_compare_idx.append(i)
            test_fun = inter_funcs[i]
            fpx= ldr.load_gsl_pure(test_fun)
            try:
                fx,inpdm = load_1v_rf(test_fun[-1])
            except:
                print("excpts")
                fx = fpx
            sheet.write(k,0,inter_funcs[i][-1][7:])
            rade_avg_errs.append(np.log2(rade_errs_bit[count]))
            demc_avg_errs.append(np.log2(demc_errs[count]))
            demc_avg_times.append(demc_times[count])
            rade_avg_times.append(rade_times[count])
            sheet.write(k,3,rade_times[count])
            sheet.write(k,4,demc_times[count])
            sheet.write(k,5,demc_times[count]/rade_times[count])
            rade_avg_speedup.append(demc_times[count]/rade_times[count])
            print(inter_funcs[i])
            print(rade_errs_bit[count])
            print(demc_errs[count])
            if demc_errs[count]<pow(2.0,32):
                sheet.write(k,13,chr(9632))
            if rade_errs_bit[count]>demc_errs[count]:
                sheet.write(k,1,np.log2(rade_errs_bit[count]),sty0)
                sheet.write(k,2,np.log2(demc_errs[count]))
            else:
                sheet.write(k,1,np.log2(rade_errs_bit[count]))
                sheet.write(k,2,np.log2(demc_errs[count]),sty0)
            if np.isinf(rade_errs_bit[count]) & np.isinf(demc_errs[count]):
                sheet.write(k,6,0)
            else:
                sheet.write(k,6,np.log2(rade_errs_bit[count])-np.log2(demc_errs[count]))
            demc_avg_errBit.append(np.log2(rade_errs_bit[count])-np.log2(demc_errs[count]))
            demc_inp = demc_inps[count]
            rade_inp = rade_inps_bit[count]
            demc_fpx_res = fpx(demc_inp)
            rade_fpx_res = fpx(rade_inp)
            demc_fx_res = float(fx(demc_inp))
            rade_fx_res = float(fx(rade_inp))
            sheet.write(k,7,demc_inp)
            sheet.write(k,8,demc_fpx_res)
            sheet.write(k,9,demc_fx_res)
            sheet.write(k,10,rade_inp)
            sheet.write(k,11,rade_fpx_res)
            sheet.write(k,12,rade_fx_res)
            k = k + 1
        count = count + 1
    sheet.write(k,0,"Average")
    sheet.write(k,1,np.mean(rade_avg_errs))
    sheet.write(k,2,np.mean(demc_avg_errs))
    sheet.write(k,3,np.mean(rade_avg_times))
    sheet.write(k,4,np.mean(demc_avg_times))
    sheet.write(k,5,np.mean(rade_avg_speedup))
    sheet.write(k,6,np.mean(demc_avg_errBit))
    new_excel.save(exname)
    new_rade_res = []
    new_atom_res = []
    new_demc_res = []
    load_idx = []
    for i in atom_compare_idx:
        count = 0
        for j in res_rade:
            if j[0] == i:
                load_idx.append(i)
                test_fun = inter_funcs[res_atom[count][0]]
                if test_fun[-1] == "gsl_sf_sinc":
                    new_atom_res.append([1.0 for a in res_atom[count][2]])
                else:
                    new_atom_res.append(res_atom[count][2])
                new_rade_res.append([np.log2(ra) for ra in res_rade[count][2]])
                break
            count = count + 1
    rade_cvs = cal_cv_res(new_rade_res)
    atom_cvs = cal_cv_res(new_atom_res)
    print(rade_cvs)
    print(atom_cvs)
    plot_stability_plotbox(rade_cvs,atom_cvs,"RADE","ATOM","ATOMBOX.pdf")
    count = 0
    for i in load_idx:
        if rade_cvs[count]>0.5:
            print(i)
            print(inter_funcs[i])
            print(rade_cvs[count])
        count = count + 1
    print("**************")
    new_rade_res = []
    new_demc_res = []
    load_idx = []
    for i in demc_compare_idx:
        count = 0
        for j in res_rade:
            if j[0]==i:
                load_idx.append(i)
                new_rade_res.append([np.log2(r) for r in res_rade[count][2]])
                break
            count = count + 1
        count = 0
        for k in res_demc:
            if k[0]==i:
                new_demc_res.append([np.log2(d) for d in res_demc[count][2]])
                break
            count = count + 1
    rade_cvs = cal_cv_res(new_rade_res)
    demc_cvs = cal_cv_res(new_demc_res)
    plot_stability_plotbox(rade_cvs,demc_cvs,"RADE","DEMC","DEMCBOX.pdf")
    count = 0
    for i in load_idx:
        if rade_cvs[count]>0.5:
            print(i)
            print(inter_funcs[i])
            print(rade_cvs[count])
        count = count + 1
    print(rade_cvs)
    print(demc_cvs)
    
    

    
    

    
    #large err
    
    #avage time
# load_atom2pkl()
# load_res2pkl()
if __name__ == "__main__":
    exname = "../experiments/res_table.xls"
    load_res2pkl()
    load_atom2pkl()
    ini_xls_file(exname)
    generate_table_NOHE(exname)
# import os

# for i in demc_idx_list:
#     fnm = inter_funcs[i][-1] + ".xls"
#     file_name = "../experiments/detecting_results/DEMC/" + fnm
#     os.system("cp " + file_name + " ../experiments/detecting_results/DEMC_718/")


    
 
 
# analysis_results()