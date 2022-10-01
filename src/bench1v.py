from mpmath import *
import numpy as np
mp.prec = 128 

#f1
#gsl_sf_airy_Ai
rf1 = lambda x: airyai(x)

#f2
#gsl_sf_airy_Bi
rf2 = lambda x: airybi(x)

#f3
#gsl_sf_airy_Ai_scaled
rf3 = lambda x: fmul(exp(fmul(2.0/3.0,power(x,3.0/2.0),exact=True)),airyai(x),exact=True) if x>0 else airyai(x)

#f4
#gsl_sf_airy_Bi_scaled
rf4 = lambda x: fmul(exp(fmul(-2.0/3.0,power(x,3.0/2.0),exact=True)),airybi(x),exact=True) if x>0 else airybi(x)

#f5
#gsl_sf_airy_Ai_deriv
rf5 = lambda x: airyai(x,1)

#f6
#gsl_sf_airy_Bi_deriv 
rf6 = lambda x: airybi(x,1)

#f7
#gsl_sf_airy_Ai_deriv_scaled
rf7 = lambda x: fmul(exp(fmul(2.0/3.0,power(x,3.0/2.0),exact=True)),airyai(x,1),exact=True) if x>0 else airyai(x,1)

#f8
#gsl_sf_airy_Bi_deriv_scaled
rf8 = lambda x: fmul(exp(fmul(-2.0/3.0,power(x,3.0/2.0),exact=True)),airybi(x,1),exact=True) if x>0 else airybi(x,1)

#f9
#gsl_sf_bessel_J0
rf9 = lambda x: besselj(0,x)


#f10
#gsl_sf_bessel_J1
rf10 = lambda x: besselj(1,x)

#f11
#gsl_sf_bessel_Y0
rf11 = lambda x: bessely(0,x)

#f12
#gsl_sf_bessel_Y1 
rf12 = lambda x: bessely(1,x)

#f13
#gsl_sf_bessel_I0 
rf13 = lambda x: besseli(0,x)

#f14
#gsl_sf_bessel_I1
rf14 = lambda x: besseli(1,x)

#f15
#gsl_sf_bessel_I0_scaled
rf15 = lambda x: fmul(besseli(0,x),exp(-fabs(x)),exact=True)

#f16
#gsl_sf_bessel_I1_scaled
rf16 = lambda x: fmul(besseli(1,x),exp(-fabs(x)),exact=True)

#f17
#gsl_sf_bessel_K0
rf17 = lambda x: besselk(0,x)

#f18
#gsl_sf_bessel_K1
rf18 = lambda x: besselk(1,x)

#f19
#gsl_sf_bessel_K0_scaled
rf19 = lambda x: fmul(besselk(0,x),(exp(x)),exact=True) if (x>0) else besselk(0,x)

#f20
#gsl_sf_bessel_K1_scaled
rf20 = lambda x: fmul(besselk(1,x),(exp(x)),exact=True) if (x>0) else besselk(1,x)

#f21
#gsl_sf_bessel_j0
rf21 = lambda x: sin(x)/x

#f22
#gsl_sf_bessel_j1
rf22 = lambda x: (sin(x)/x - cos(x))/x

#f23
#gsl_sf_bessel_j2
rf23 = lambda x: fmul(sqrt(pi/(2*x)),besselj(2.5,x),exact=True)

#f24
#gsl_sf_bessel_y0
rf24 = lambda x: fmul(sqrt(pi/(2*x)),bessely(0.5,x),exact=True)

#f25
#gsl_sf_bessel_y1
rf25 = lambda x: fmul(sqrt(pi/(2*x)),bessely(1.5,x),exact=True)

#f26
#gsl_sf_bessel_y2
rf26 = lambda x: fmul(sqrt(pi/(2*x)),bessely(2.5,x),exact=True)

#f27
#gsl_sf_bessel_i0_scaled
rf27 = lambda x: re(fmul(exp(-fabs(x)),besseli(0.5,x)/sqrt(2.0*x/pi),exact=True))

#f28
#gsl_sf_bessel_i1_scaled 
rf28 = lambda x: re(fmul(exp(-fabs(x)),besseli(1.5,x)/sqrt(2.0*x/pi),exact=True))

#f29
#gsl_sf_bessel_i2_scaled
rf29 = lambda x: re(fmul(exp(-fabs(x)),besseli(2.5,x)/sqrt(2.0*x/pi),exact=True))

#f30
#gsl_sf_bessel_k0_scaled 
rf30 = lambda x: fmul(fmul(exp(x),besselk(0.5,x),exact=True),sqrt(pi/(2*x)),exact=True)

#f31
#gsl_sf_bessel_k1_scaled
rf31 = lambda x: fmul(fmul(exp(x),besselk(1.5,x),exact=True),sqrt(pi/(2*x)),exact=True)

#f32
#gsl_sf_bessel_k2_scaled 
rf32 = lambda x: fmul(fmul(exp(x),besselk(2.5,x),exact=True),sqrt(pi/(2*x)),exact=True)

#f33
#gsl_sf_clausen
rf33 = lambda x: clsin(2,x)

#f34
#gsl_sf_dawson
rf34 = lambda x: fmul(sqrt(pi),fmul(exp(-x*x),erfi(x),exact=True),exact=True)/2.0

#f35
#gsl_sf_debye_1
rf35 = lambda x: quad(lambda t: power(t,1)/(exp(t)-1),[0,x])/x

#f36
#gsl_sf_debye_2
rf36 = lambda x: 2.0 * quad(lambda t: power(t,2.0)/(exp(t)-1),[0,x])/power(x,2.0)

#f37
#gsl_sf_debye_3
rf37 = lambda x: 3.0 * quad(lambda t: power(t,3.0)/(exp(t)-1),[0,x])/power(x,3.0)

#f38
#gsl_sf_debye_4
rf38 = lambda x: 4.0 * quad(lambda t: power(t,4.0)/(exp(t)-1),[0,x])/power(x,4.0)

#f39
#gsl_sf_debye_5
rf39 = lambda x: 5.0 * quad(lambda t: power(t,5.0)/(exp(t)-1),[0,x])/power(x,5.0)

#f40
#gsl_sf_debye_6
rf40 = lambda x: 6.0 * quad(lambda t: power(t,6.0)/(exp(t)-1.0),[0,x])/power(x,6.0)

#f41
#gsl_sf_dilog
rf41 = lambda x:re(polylog(2,x))

#f42
#gsl_sf_ellint_Kcomp
rf42 = lambda x: ellipk(power(x,2.0))

#f43
#gsl_sf_ellint_Ecomp
rf43 = lambda x: ellipe(power(x,2.0))

#f44
#gsl_sf_erf 
rf44 = lambda x: erf(x)

#f45
#gsl_sf_erfc
rf45 = lambda x: erfc(x)

#f46
#gsl_sf_log_erfc
rf46 = lambda x: log(erfc(x))

#f47
#gsl_sf_erf_Z
rf47 = lambda x: exp(-power(x,2.0)/2)/sqrt(2*pi)

#f48
#gsl_sf_erf_Q
rf48 = lambda x: erfc(x/sqrt(2.0))/2.0

#f49
#gsl_sf_hazard 
rf49 = lambda x: npdf(x) / (1-ncdf(x))

#f50
#gsl_sf_exp
rf50 = lambda x: exp(x)

#f51
#gsl_sf_exp_e10_e 
rf51 = lambda x: exp(x)

#f52
#gsl_sf_expm1
rf52 = lambda x: expm1(x)

#f53
#gsl_sf_exprel
rf53 = lambda x: (fsub(exp(x),1,exact=True))/x if x > -1000 else -1.0/x

#f54
#gsl_sf_exprel_2
# rf54 = lambda x: 2.0*(fsub(exp(x),fsub(1.0,x,exact=True),exact=True))/(power(x,2.0)) if x > -1000 else 2.0*(fsub(0.0,fsub(1.0,x,exact=True),exact=True))/(power(x,2.0))
rf54 = lambda x: 2*(expm1(mpf(x))-mpf(x))/(fmul(x,x,exact=True))

#f55
#gsl_sf_expint_E1
rf55 = lambda x: re(expint(1,x))

#f56
#gsl_sf_expint_E2
rf56 = lambda x: re(expint(2,x))

#f57
#gsl_sf_expint_Ei
rf57 = lambda x: ei(x)

#f58
#gsl_sf_Shi
rf58 = lambda x: shi(x)

#f59
#gsl_sf_Chi
rf59 = lambda x: chi(x)

#f60
#gsl_sf_expint_3
rf60 = lambda x: quad(lambda t: exp(-power(t,3.0)),[0,x])

#f61
#gsl_sf_Si
rf61 = lambda x: si(x)

#f62
#gsl_sf_Ci
rf62 = lambda x: ci(x)

#f63
#gsl_sf_atanint 
rf63 = lambda x: quad(lambda t: atan(t)/t,[0,x])

#f64
#gsl_sf_fermi_dirac_m1
# rf64 = lambda x: exp(x)/(fadd(1,exp(x),exact=True))
rf64 = lambda x: -polylog(0, -exp(x))

#f65
#gsl_sf_fermi_dirac_0 
# rf65 = lambda x: -1.0*polylog(1.0,-exp(x)) if x > -50.0 else exp(x)
rf65 = lambda x: -polylog(1.0, -exp(x))

#f66
#gsl_sf_fermi_dirac_1 
# rf66 = lambda x: -1.0*polylog(2.0,-exp(x)) if x > -50.0 else exp(x)
rf66 = lambda x: -polylog(2.0, -exp(x))

#f67
#gsl_sf_fermi_dirac_2
# rf67 = lambda x: -1.0*polylog(3.0,-exp(x)) if x > -50.0 else exp(x)
rf67 = lambda x: -polylog(3.0, -exp(x))

#f68
#gsl_sf_fermi_dirac_mhalf
# rf68 = lambda x: quad(lambda t: 1/fmul(sqrt(t),(fadd(exp(fsub(t,x,exact=True)),1)),exact=True),[0,inf])/gamma(0.5) if x > -50.0 else exp(x)
rf68 = lambda x: re(-polylog(0.5, -exp(x)))

#f69
#gsl_sf_fermi_dirac_half
# rf69 = lambda x: quad(lambda t: sqrt(t)/(fadd(exp(fsub(t,x,exact=True)),1)),[0,inf])/gamma(1.5) if x > -50.0 else exp(x)
rf69 = lambda x: re(-polylog(1.5, -exp(x)))

#f70
#gsl_sf_fermi_dirac_3half
# rf70 = lambda x: quad(lambda t: fmul(t,sqrt(t),exact=True)/(fadd(exp(fsub(t,x,exact=True)),1)),[0,inf])/gamma(2.5) if x > -50.0 else exp(x)
rf70 = lambda x: re(-polylog(1.5, -exp(x)))

#f71
# gsl_sf_gamma
rf71 = lambda x: gamma(x)

#f72
#gsl_sf_lngamma
rf72 = lambda x: re(loggamma(x))

#f73
#gsl_sf_gammastar
rf73 = lambda x: gamma(x)/(fmul(sqrt(2*pi),fmul(power(x,(fsub(x,0.5,exact=True))),exp(-x),exact=True),exact=True))

#f74
#gsl_sf_gammainv 
rf74 = lambda x: rgamma(x)

#f75
#gsl_sf_lambert_W0
rf75 = lambda x: lambertw(x)


#f76
#gsl_sf_lambert_Wm1
rf76 = lambda x: re(lambertw(x,-1)) if (x<0.0) & (x>(-1.0/2.71828182845904523536028747135)) else lambertw(x)

#f77
#gsl_sf_legendre_P1
rf77 = lambda x: legendre(1,x)

#f78
#gsl_sf_legendre_P2
rf78 = lambda x: legendre(2,x)

#f79
#gsl_sf_legendre_P3
rf79 = lambda x: legendre(3,x)

#f80
#gsl_sf_legendre_Q0
rf80 = lambda x: legenq(0,0,x,type=3).real

#f81
#gsl_sf_legendre_Q1
rf81 = lambda x: legenq(1,0,x,type=3).real

#f82
#gsl_sf_log 
rf82 = lambda x: log(x)

#f83
#gsl_sf_log_abs
rf83 = lambda x: log(abs(x))

#f84
#gsl_sf_log_1plusx
rf84 = lambda x: log(fadd(1,x,exact=True))

#f85
#gsl_sf_log_1plusx_mx
rf85 = lambda x: fsub(log(fadd(1,x,exact=True)),x,exact=True)

#f86
#gsl_sf_psi
rf86 = lambda x: digamma(x)

#f87
#gsl_sf_psi_1piy
rf87 = lambda x: re(psi(0,1+x*j))

#f88
#gsl_sf_psi_1 
rf88 = lambda x: psi(1,x)

#f89
#gsl_sf_synchrotron_1
rf89 = lambda x: fmul(x,quad(lambda t: besselk(5.0/3.0,t),[x,inf]),exact=True) if x< 60 else fmul(x,quad(lambda t: besselk(5.0/3.0,t),linspace(x,x+21,5)+[inf]),exact=True)

#f90
#gsl_sf_synchrotron_2
rf90 = lambda x: fmul(x,besselk(2.0/3.0,x),exact=True)

#f91
#gsl_sf_transport_2
rf91 = lambda x: quad(lambda t: fmul(power(t,2.0),exp(t),exact=True)/power((fsub(exp(t),1.0)),2.0),[0,x])

#f92
#gsl_sf_transport_3
rf92 = lambda x: quad(lambda t: fmul(power(t,3.0),exp(t),exact=True)/power((fsub(exp(t),1.0)),2.0),[0,x])

#f93
#gsl_sf_transport_4
rf93 = lambda x: quad(lambda t: fmul(power(t,4.0),exp(t),exact=True)/power((fsub(exp(t),1.0)),2.0),[0,x])

#f94
#gsl_sf_transport_5
rf94 = lambda x: quad(lambda t: fmul(power(t,5.0),exp(t),exact=True)/power((fsub(exp(t),1.0)),2.0),[0,x])

#f95
#gsl_sf_sin
rf95 = lambda x: sin(x)

#f96
#gsl_sf_cos
rf96 = lambda x: cos(x)

#f97
#gsl_sf_sinc
rf97 = lambda x: sincpi(x)

#f98
#gsl_sf_lnsinh 
rf98 = lambda x: log(sinh(x))

#f99
#gsl_sf_lncosh
rf99 = lambda x: log(cosh(x))

#f100
#gsl_sf_angle_restrict_symm
rf100 = lambda x: fmod(x,2.0*pi) if fmod(x,2.0*pi)< pi else fmod(x,2.0*pi)-2.0*pi

#f101
#gsl_sf_angle_restrict_pos
rf101 = lambda x: fmod(x,2*pi)

#f102
#gsl_sf_zeta
rf102 = lambda x: zeta(x)

#f103
#gsl_sf_zetam1
rf103 = lambda x: fsub(zeta(x),1,exact=True) if x < 120 else fsub(zeta(x,dps=400),1.0,exact=True)

#f104
#gsl_sf_eta
rf104 = lambda x: altzeta(x)


#f105
#gsl_sf_expint_E1_scaled
rf105 = lambda x: re(expint(1,x) *exp(x))

#f106
#gsl_sf_expint_E2_scaled
rf106 = lambda x: re(expint(2, x)*exp(x))

#f107
#gsl_sf_expint_Ei_scaled
rf107 = lambda x: re(ei(x)*exp(-x))
input_domain = [[[-1000.0, 1000.0]], [[-1000.0, 100.0]], [[-1000.0, 1000.0]], [[-1000.0, 1000.0]], [[-1000.0, 1000.0]], [[-1000.0, 100.0]], [[-1000.0, 1000.0]], [[-1000.0, 100.0]], [[-1e+10, 1e+10]], [[-1e+10, 1e+10]], [[-10000000000.0, 10000000000.0]], [[-10000000000.0, 10000000000.0]], [[-709, 709]], [[-709, 709]], [[-1.7976931348623157e+308, 1.7976931348623157e+308]], [[-1.7976931348623157e+308, 1.7976931348623157e+308]], [[0, 1e+100]], [[0, 1e+100]], [[0, 17000000000.0]], [[0, 17000000000.0]], [[-1.7976931348623157e+100, 1.7976931348623157e+100]], [[-1.3407807929942596e+154, 1.3407807929942596e+154]], [[-823549.6645, 823549.6645]], [[0, 823549.6645]], [[0, 823549.6645]], [[0, 823549.6645]], [[-8.98846567431158e+107, 8.98846567431158e+107]], [[-1.3407807929942596e+154, 1.3407807929942596e+154]], [[-5.64380309412229e+102, 5.64380309412229e+102]], [[0, 8.988465674311579e+307]], [[0, 8.988465674311579e+307]], [[0, 8.988465674311579e+307]], [[-823549.6645, 823549.6645]], [[-709, 709]], [[0, 709]], [[0, 709]], [[0, 709]], [[0, 709]], [[0, 709]], [[0, 709]], [[-1e+100, 1]], [[-1, 1]], [[-1, 1]], [[-10, 10]], [[-40, 40]], [[-1.073315388749996e+51, 1.073315388749996e+51]], [[-40, 40]], [[-10, 40]], [[-40, 40]], [[-709.782712893384, 709.782712893384]], [[-709.782712893384, 709.782712893384]], [[-709.782712893384, 709.782712893384]], [[-709.782712893384, 709.782712893384]], [[-709.782712893384, 709.782712893384]], [[-701.8334146820821, 701.8334146820821]], [[-701.8334146820821, 701.8334146820821]], [[-701.8334146820821, 701.8334146820821]], [[-701.8334146820821, 701.8334146820821]], [[-701.8334146820821, 701.8334146820821]], [[0, 3]], [[-1e+100, 1e+100]], [[0, 823549.6645]], [[-17976931348.623158, 17976931348.623158]], [[-709, 709]], [[-709, 709]], [[-709, 30]], [[-709, 30]], [[-708, 30]], [[-708, 30]], [[-708, 30]], [[-168, 171.6243769563027]], [[0, 1000]], [[0, 17976931348.623158]], [[-168, 171.6243769563027]], [[-0.4678794411714423, 1e+100]], [[-0.4678794411714423, 1e+100]], [[-1e+100, 1e+100]], [[-1e+100, 1e+100]], [[-1e+100, 1e+100]], [[-1, 1e+100]], [[-1, 1e+100]], [[0, 1e+100]], [[-1e+100, 1e+100]], [[-1, 1e+100]], [[-1, 1e+100]], [[-262144.0, 262144.0]], [[0, 1.3407807929942596e+154]], [[-5, 10000000000.0]], [[0, 500]], [[0, 500]], [[0, 1351079888211.1487]], [[0, 1351079888211.1487]], [[0, 1351079888211.1487]], [[0, 1351079888211.1487]], [[-823549.6645, 823549.6645]], [[-823549.6645, 823549.6645]], [[-262143.99997369398, 262143.99997369398]], [[0, 1e+100]], [[-1e+100, 1e+100]], [[-823549.6645, 823549.6645]], [[-823549.6645, 823549.6645]], [[-170, 1000]], [[-170, 1000]], [[-168, 100]], [[100, 200]], [[-1, 1]], [[-1, 1]]]
rfl = [rf1, rf2, rf3, rf4, rf5, rf6, rf7, rf8, rf9, rf10, rf11, rf12, rf13, rf14, rf15, rf16, rf17, rf18, rf19, rf20, rf21, rf22, rf23, rf24, rf25, rf26, rf27, rf28, rf29, rf30, rf31, rf32, rf33, rf34, rf35, rf36, rf37, rf38, rf39, rf40, rf41, rf42, rf43, rf44, rf45, rf46, rf47, rf48, rf49, rf50, rf51, rf52, rf53, rf54, rf55, rf56, rf57, rf58, rf59, rf60, rf61, rf62, rf63, rf64, rf65, rf66, rf67, rf68, rf69, rf70, rf71, rf72, rf73, rf74, rf75, rf76, rf77, rf78, rf79, rf80, rf81, rf82, rf83, rf84, rf85, rf86, rf87, rf88, rf89, rf90, rf91, rf92, rf93, rf94, rf95, rf96, rf97, rf98, rf99, rf100, rf101, rf102, rf103, rf104, rf105, rf106, rf107]
nrfl_fname = ['gsl_sf_airy_Ai', 'gsl_sf_airy_Bi', 'gsl_sf_airy_Ai_scaled', 'gsl_sf_airy_Bi_scaled', 'gsl_sf_airy_Ai_deriv', 'gsl_sf_airy_Bi_deriv ', 'gsl_sf_airy_Ai_deriv_scaled', 'gsl_sf_airy_Bi_deriv_scaled', 'gsl_sf_bessel_J0', 'gsl_sf_bessel_J1', 'gsl_sf_bessel_Y0', 'gsl_sf_bessel_Y1 ', 'gsl_sf_bessel_I0 ', 'gsl_sf_bessel_I1', 'gsl_sf_bessel_I0_scaled', 'gsl_sf_bessel_I1_scaled', 'gsl_sf_bessel_K0', 'gsl_sf_bessel_K1', 'gsl_sf_bessel_K0_scaled', 'gsl_sf_bessel_K1_scaled', 'gsl_sf_bessel_j0', 'gsl_sf_bessel_j1', 'gsl_sf_bessel_j2', 'gsl_sf_bessel_y0', 'gsl_sf_bessel_y1', 'gsl_sf_bessel_y2', 'gsl_sf_bessel_i0_scaled', 'gsl_sf_bessel_i1_scaled ', 'gsl_sf_bessel_i2_scaled', 'gsl_sf_bessel_k0_scaled ', 'gsl_sf_bessel_k1_scaled', 'gsl_sf_bessel_k2_scaled ', 'gsl_sf_clausen', 'gsl_sf_dawson', 'gsl_sf_debye_1', 'gsl_sf_debye_2', 'gsl_sf_debye_3', 'gsl_sf_debye_4', 'gsl_sf_debye_5', 'gsl_sf_debye_6', 'gsl_sf_dilog', 'gsl_sf_ellint_Kcomp', 'gsl_sf_ellint_Ecomp', 'gsl_sf_erf ', 'gsl_sf_erfc', 'gsl_sf_log_erfc', 'gsl_sf_erf_Z', 'gsl_sf_erf_Q', 'gsl_sf_hazard ', 'gsl_sf_exp', 'gsl_sf_exp_e10_e ', 'gsl_sf_expm1', 'gsl_sf_exprel', 'gsl_sf_exprel_2', 'gsl_sf_expint_E1', 'gsl_sf_expint_E2', 'gsl_sf_expint_Ei', 'gsl_sf_Shi', 'gsl_sf_Chi', 'gsl_sf_expint_3', 'gsl_sf_Si', 'gsl_sf_Ci', 'gsl_sf_atanint ', 'gsl_sf_fermi_dirac_m1', 'gsl_sf_fermi_dirac_0 ', 'gsl_sf_fermi_dirac_1 ', 'gsl_sf_fermi_dirac_2', 'gsl_sf_fermi_dirac_mhalf', 'gsl_sf_fermi_dirac_half', 'gsl_sf_fermi_dirac_3half', ' gsl_sf_gamma', 'gsl_sf_lngamma', 'gsl_sf_gammastar', 'gsl_sf_gammainv ', 'gsl_sf_lambert_W0', 'gsl_sf_lambert_Wm1', 'gsl_sf_legendre_P1', 'gsl_sf_legendre_P2', 'gsl_sf_legendre_P3', 'gsl_sf_legendre_Q0', 'gsl_sf_legendre_Q1', 'gsl_sf_log ', 'gsl_sf_log_abs', 'gsl_sf_log_1plusx', 'gsl_sf_log_1plusx_mx', 'gsl_sf_psi', 'gsl_sf_psi_1piy', 'gsl_sf_psi_1 ', 'gsl_sf_synchrotron_1', 'gsl_sf_synchrotron_2', 'gsl_sf_transport_2', 'gsl_sf_transport_3', 'gsl_sf_transport_4', 'gsl_sf_transport_5', 'gsl_sf_sin', 'gsl_sf_cos', 'gsl_sf_sinc', 'gsl_sf_lnsinh ', 'gsl_sf_lncosh', 'gsl_sf_angle_restrict_symm', 'gsl_sf_angle_restrict_pos', 'gsl_sf_zeta', 'gsl_sf_zetam1', 'gsl_sf_eta', 'gsl_sf_expint_E1_scaled', 'gsl_sf_expint_E2_scaled', 'gsl_sf_expint_Ei_scaled']
ngfl_fname = ['gsl_sf_airy_Ai', 'gsl_sf_airy_Bi', 'gsl_sf_airy_Ai_scaled', 'gsl_sf_airy_Bi_scaled', 'gsl_sf_airy_Ai_deriv', 'gsl_sf_airy_Bi_deriv ', 'gsl_sf_airy_Ai_deriv_scaled', 'gsl_sf_airy_Bi_deriv_scaled', 'gsl_sf_bessel_J0', 'gsl_sf_bessel_J1', 'gsl_sf_bessel_Y0', 'gsl_sf_bessel_Y1 ', 'gsl_sf_bessel_I0 ', 'gsl_sf_bessel_I1', 'gsl_sf_bessel_I0_scaled', 'gsl_sf_bessel_I1_scaled', 'gsl_sf_bessel_K0', 'gsl_sf_bessel_K1', 'gsl_sf_bessel_K0_scaled', 'gsl_sf_bessel_K1_scaled', 'gsl_sf_bessel_j0', 'gsl_sf_bessel_j1', 'gsl_sf_bessel_j2', 'gsl_sf_bessel_y0', 'gsl_sf_bessel_y1', 'gsl_sf_bessel_y2', 'gsl_sf_bessel_i0_scaled', 'gsl_sf_bessel_i1_scaled ', 'gsl_sf_bessel_i2_scaled', 'gsl_sf_bessel_k0_scaled ', 'gsl_sf_bessel_k1_scaled', 'gsl_sf_bessel_k2_scaled ', 'gsl_sf_clausen', 'gsl_sf_dawson', 'gsl_sf_debye_1', 'gsl_sf_debye_2', 'gsl_sf_debye_3', 'gsl_sf_debye_4', 'gsl_sf_debye_5', 'gsl_sf_debye_6', 'gsl_sf_dilog', 'gsl_sf_ellint_Kcomp', 'gsl_sf_ellint_Ecomp', 'gsl_sf_erf ', 'gsl_sf_erfc', 'gsl_sf_log_erfc', 'gsl_sf_erf_Z', 'gsl_sf_erf_Q', 'gsl_sf_hazard ', 'gsl_sf_exp', 'gsl_sf_exp_e10_e ', 'gsl_sf_expm1', 'gsl_sf_exprel', 'gsl_sf_exprel_2', 'gsl_sf_expint_E1', 'gsl_sf_expint_E2', 'gsl_sf_expint_Ei', 'gsl_sf_Shi', 'gsl_sf_Chi', 'gsl_sf_expint_3', 'gsl_sf_Si', 'gsl_sf_Ci', 'gsl_sf_atanint ', 'gsl_sf_fermi_dirac_m1', 'gsl_sf_fermi_dirac_0 ', 'gsl_sf_fermi_dirac_1 ', 'gsl_sf_fermi_dirac_2', 'gsl_sf_fermi_dirac_mhalf', 'gsl_sf_fermi_dirac_half', 'gsl_sf_fermi_dirac_3half', ' gsl_sf_gamma', 'gsl_sf_lngamma', 'gsl_sf_gammastar', 'gsl_sf_gammainv ', 'gsl_sf_lambert_W0', 'gsl_sf_lambert_Wm1', 'gsl_sf_legendre_P1', 'gsl_sf_legendre_P2', 'gsl_sf_legendre_P3', 'gsl_sf_legendre_Q0', 'gsl_sf_legendre_Q1', 'gsl_sf_log ', 'gsl_sf_log_abs', 'gsl_sf_log_1plusx', 'gsl_sf_log_1plusx_mx', 'gsl_sf_psi', 'gsl_sf_psi_1piy', 'gsl_sf_psi_1 ', 'gsl_sf_synchrotron_1', 'gsl_sf_synchrotron_2', 'gsl_sf_transport_2', 'gsl_sf_transport_3', 'gsl_sf_transport_4', 'gsl_sf_transport_5', 'gsl_sf_sin', 'gsl_sf_cos', 'gsl_sf_sinc', 'gsl_sf_lnsinh ', 'gsl_sf_lncosh', 'gsl_sf_angle_restrict_symm', 'gsl_sf_angle_restrict_pos', 'gsl_sf_zeta', 'gsl_sf_zetam1', 'gsl_sf_eta', 'gsl_sf_expint_E1_scaled', 'gsl_sf_expint_E2_scaled', 'gsl_sf_expint_Ei_scaled']
