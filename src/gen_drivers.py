import ctypes
import os
import pickle
import sys

def found_funbyName(fun_name, inter_funcs):
    for i in inter_funcs:
        if i[0] == fun_name:
            return i
    return []
def write2file(new_lines,file_name):
    f = open(file_name, 'w')
    orig_stdout = sys.stdout
    sys.stdout = f
    for i in new_lines:
        print(i)
    sys.stdout = orig_stdout
    f.close()

def load_pickle(file_name):
    return pickle.load(open(file_name, "rb"))
def gen_gsl_pure_function(test_fun):
    ### generate driver_funcs
    driver_path = '../benchmark/gsl/driver_functions/'
    # os.system('rm -R ' + driver_path + test_fun[0])
    os.system('cp -R ' + driver_path + 'driver_template/. ' + driver_path + test_fun[0])
    test_driver_path = driver_path + test_fun[0]
    # change template of
    fp = open(test_driver_path + '/gslsfdr.c')
    lines = fp.read().split("\n")
    fp.close()
    new_lines = list(lines)
    var_str = " ".join(test_fun[1][0])
    var_name = test_fun[1][0][1]
    for i in test_fun[1][1:]:
        temp_str = " ".join(i)
        temp_var_name = i[1]
        var_str = var_str + ',' + temp_str
        var_name = var_name + ',' + temp_var_name
    var_str_lst = []
    var_name_lst = []
    for i in test_fun[1]:
        if i[0]=='double':
            var_str_lst.append(" ".join(i))
            var_name_lst.append(i[1])
        if i[0]=='int':
            var_str_lst.append(" ".join(i))
            var_name_lst.append(i[1])
        if i[0]=='gsl_mode_t':
            var_name_lst.append('0')
    var_str = ",".join(var_str_lst)
    var_name = ",".join(var_name_lst)
    str1 = 'double ' + 'gslfdr(' + var_str + '){'
    str11 = 'double ' + 'gslfdr(' + var_str + ');'
    # if test_fun[0].endswith('_e'):
    fun_name = test_fun[0]
    str2 = fun_name + '(' + var_name + ',&result);'
    new_lines[8] = str1
    new_lines[11] = str2
    fp = open(test_driver_path + '/gslsfdr.h')
    lines = fp.read().split("\n")
    fp.close()
    new_lines2 = list(lines)
    new_lines2[0] = str11
    write2file(new_lines, test_driver_path + '/gslsfdr.c')
    write2file(new_lines2, test_driver_path + '/gslsfdr.h')
    pwd = os.getcwd()
    os.chdir('../benchmark/gsl/driver_functions/' + test_fun[0])
    os.system('./test.sh')
    os.chdir(pwd)
import multiprocessing as mp
def fpara_gen(para_test_wrap,indx_funs):
    # Redefine, with only 1 mandatory argument.
    pool = mp.Pool(4)

    results = pool.map(para_test_wrap, [ i for i in indx_funs])

    pool.close()

    print(results[:10])
if __name__ == "__main__":
    inter_funcs = load_pickle('fun_index.pkl')
    fpara_gen(gen_gsl_pure_function,inter_funcs)



