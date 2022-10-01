#The implementation of DEMC algorithm
import basic_function as bf
import time,signal
from scipy.optimize import differential_evolution
from scipy.optimize import basinhopping
from scipy.optimize import minimize
import warnings
import math
import numpy as np
import os
import mpmath

class TimeoutError (RuntimeError):
    pass

def handler (signum, frame):
    raise TimeoutError()

#在收到SIGALRM信号后，信号处理函数handler开始执行，随后返回主进程
signal.signal (signal.SIGALRM, handler)


warnings.filterwarnings('error')
def relative_error(fx,fpx,x0):
    try:
        fx_res = fx(x0)
        if type(fx_res) == 'mpc':
            print(fx_res)
        fx_res = mpmath.mpf(fx(x0))
        fp_res = mpmath.mpf(fpx(x0))
        if fx_res == 0.0:
            if fp_res == 0.0:
                y0 = 0.0
            else:
                y0 = np.abs((fp_res-fx_res)/fp_res)
        else:
            y0 = np.abs((fp_res-fx_res)/fx_res)
        return float(y0)
    except:
        return 0.0 
def produce_interval(x,k):
    a = bf.getulp(x)*1e10
    return [np.max([x-a,k[0]]),np.min([x+a,k[1]])]
def reduce_x(a,b,x):
    x = float(x)
    return (a+b+(b-a)*math.sin(x))/2.0
def RADE1v(rf,pf,dom_l,fnm,limit_n,limit_time,et_time):
    st = time.time() #当前时间
    file_name = "../experiments/detecting_results/RADE/" + fnm #创建xls文件
    if not os.path.exists("../experiments/detecting_results/RADE/"):
        os.makedirs("../experiments/detecting_results/RADE/")
    count = 0 #总执行次数
    final_max = 0.0 #最终触发的最大误差
    final_x = 0.0 #最终触发最大误差的点
    final_count1 = 0
    final_count2 = 0
    final_bound = [] #最终找到点所在区间
    record_res_l = []
    glob_fitness_real = np.frompyfunc(lambda x: bf.fitness_fun(rf, pf, x), 1, 1)
    """
        fun: 1.1125369292536007e-308 x对应的输出函数值
        message: 'Optimization terminated successfully.'
        nfev: 542 函数求值计数器数量
        nit: 50 
        success: True 指示优化器是否成功退出及描述终止原因的信息
        x: array([3.14159265]) 解决方案数组
    """
    try:
        print("Detecting possible maximum error by RADE algorithm")
        # signal.alarm(limit_time) #limit_time后，向进程自身发送SIGALRM信号
        while(count<limit_n): #执行次数
            temp_st=time.time() #当前时间
            count1 = 0
            count2 = 0
            rand_seed = bf.rd_seed[count] #一个bf中给定的数，随着每次循环的count不同不一样
            np.random.seed(rand_seed) #给定种子后确保每次生成的随机数都是一样的
            res_l = [] #存[temp_max, temp_x, k]
            temp_count = 0
            temp_y0 = 0.0
            minimizer_kwargs = {"method":"Powell"}
            temp_time = time.time()
            for k in dom_l:
                gen_l = k[0]
                glob_fitness_con_temp = lambda x: bf.fitness_fun1(rf, pf, reduce_x(gen_l[0],gen_l[1],x))
                n_x = np.random.uniform(0,3.14,1)
                x = k[1]
                err = 0.0
                for xi in n_x:
                    res = basinhopping(glob_fitness_con_temp,xi,minimizer_kwargs=minimizer_kwargs,niter_success=20,niter=300)
                    temp_x = reduce_x(gen_l[0],gen_l[1],res.x[0]) #差分进化找到触发条件数倒数最小输入的点
                    count1 = count1+res.nfev #函数评估次数
                    temp_err = 1.0/glob_fitness_real(temp_x)
                    if temp_err> err:
                        err=temp_err
                        x = temp_x
                        if (err > 4294967296.0):
                            break
                res_l.append([err,x,k[0]])
                if (err > 4294967296.0)&(temp_count>=10):
                    break
                temp_count = temp_count + 1
            t1 = time.time() - temp_st
            print
            temp_res_ct = 0
            res_l = sorted(res_l, reverse=True)
            for res_i in res_l[0:10]:
                loc_res = minimize(glob_fitness_real,res_i[1],bounds=[res_i[2]],method="Nelder-Mead")
                err = 1.0/loc_res.fun
                if (err > 1099511627776.0)&(temp_res_ct>=5):
                    break
                res_l[temp_res_ct][1] = loc_res.x[0]
                res_l[temp_res_ct][0] = 1.0/loc_res.fun
                temp_res_ct = temp_res_ct + 1
            res_l = sorted(res_l, reverse=True)#按temp_max由大到小排序
            temp_max = res_l[0][0]
            temp_x = res_l[0][1]
            bound = res_l[0][2]
            t2 = 0
            temp_l = [temp_max,temp_x,bound,t1,count1,count2,rand_seed,count,t2,res_l,et_time]
            final_count1 = final_count1+count1
            final_count2 = final_count2+count2
            record_res_l.append(temp_l)
            count = count + 1 #程序执行次数+1
            if temp_max>final_max:
                final_max=temp_max
                final_x = temp_x
                final_bound = bound
        final_time = time.time()-st #最终时间 - 起始时间 = 总执行时间
        bf.output_err(record_res_l, file_name, fnm)
        bf.save_line_list("picklelst/"+fnm+".pkl",record_res_l)
        return [final_max, final_x, final_bound, final_time+et_time,count,final_count1,final_count2,fnm]
    except TimeoutError:
        final_time = time.time() - st
        bf.output_err(record_res_l,file_name,fnm)
        bf.save_line_list("picklelst/"+fnm+".pkl",record_res_l)
        return [final_max, final_x, final_bound, final_time+et_time,count,final_count1,final_count2,fnm]