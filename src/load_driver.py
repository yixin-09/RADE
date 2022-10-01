import ctypes
import difflib
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

def load_gsl(test_fun):
    print(test_fun)
    ### [fun_name, [[var_typ,var_name]..]]
    # print os.path.dirname(__file__)
    lib_ld = ctypes.CDLL('../benchmark/gsl/fpids_drivers/' + test_fun[0] + '/libgslbc.so')
    lib_fun = lib_ld.gslfdr
    # lib_stat = lib_ld.get_status
    lib_ini = lib_ld.ini_idx
    lib_ini()
    class gsl_sf_result(ctypes.Structure):
        _fields_ = [('val', ctypes.c_double),
                    ('err', ctypes.c_double)]
    # lib_idx = ctypes.POINTER(ctypes.c_int).in_dll(lib_ld, "idx")
    lib_ld.gslfdr.restype = ctypes.c_double
    # lib_ld.get_status.restype = ctypes.c_int
    vartyp_lst = []
    for i in test_fun[1]:
        if i[0] == 'double':
            vartyp_lst.append(ctypes.c_double)
        if i[0] == 'int':
            vartyp_lst.append(ctypes.c_int)
    lib_ld.gslfdr.argtypes = vartyp_lst
    lib_idx_arr = ctypes.POINTER(ctypes.c_int).in_dll(lib_ld, "idx_arr")
    lib_idx = ctypes.c_int.in_dll(lib_ld, "idx")
    return lib_fun,lib_idx,lib_idx_arr
def load_gsl_pure(test_fun):#加载gsl中的fp(x)
    ### [fun_name, [[var_typ,var_name]..]]
    # print os.path.dirname(__file__)
    lib_ld = ctypes.CDLL('../benchmark/gsl/driver_functions/' + test_fun[0] + '/libgslbc.so')
    lib_fun = lib_ld.gslfdr
    lib_ld.gslfdr.restype = ctypes.c_double
    vartyp_lst = []
    for i in test_fun[1]:
        if i[0] == 'double':
            vartyp_lst.append(ctypes.c_double)
        if i[0] == 'int':
            vartyp_lst.append(ctypes.c_int)
    lib_ld.gslfdr.argtypes = vartyp_lst
    return lib_fun
def load_gsl_flow(test_fun):
    print(test_fun)
    ### [fun_name, [[var_typ,var_name]..]]
    # print os.path.dirname(__file__)
    lib_ld = ctypes.CDLL('../benchmark/gsl/fpflow_drivers/' + test_fun[0] + '/libgslbcO2.so',mode=os.RTLD_DEEPBIND)
    lib_fun = lib_ld.gslfdr
    # lib_stat = lib_ld.get_status
    lib_ini = lib_ld.ini_idx
    lib_ini()
    class gsl_sf_result(ctypes.Structure):
        _fields_ = [('val', ctypes.c_double),
                    ('err', ctypes.c_double)]
    # lib_idx = ctypes.POINTER(ctypes.c_int).in_dll(lib_ld, "idx")
    lib_ld.gslfdr.restype = ctypes.c_double
    # lib_ld.get_status.restype = ctypes.c_int
    vartyp_lst = []
    for i in test_fun[1]:
        if i[0] == 'double':
            vartyp_lst.append(ctypes.c_double)
        if i[0] == 'int':
            vartyp_lst.append(ctypes.c_int)
    lib_ld.gslfdr.argtypes = vartyp_lst
    lib_idx_arr = ctypes.POINTER(ctypes.c_double).in_dll(lib_ld, "idx_arr")
    lib_idx = ctypes.c_int.in_dll(lib_ld, "idx")
    return lib_fun,lib_idx,lib_idx_arr
        

