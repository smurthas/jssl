{
  'variables': { 'target_arch%': 'x64' },
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },
    'include_dirs': [
      # platform and arch-specific headers
      'config/<(OS)/<(target_arch)',
      'gsl',
      '.'
    ],
    'direct_dependent_settings': {
      'include_dirs': [
        '.',
      ],
    },
  },

  'targets': [
    {
      'target_name': 'utils',
      'product_prefix': 'lib',
      'type': 'static_library',
      'sources': [
        'utils/memcpy.c',
        'utils/memmove.c',
        'utils/placeholder.c',
        'utils/strdup.c',
        'utils/strtol.c',
        'utils/strtoul.c',
      ],
      'include_dirs': [
        'utils'
      ],
    },

    {
      'target_name': 'sys',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'sys/coerce.c',
        'sys/expm1.c',
        'sys/fcmp.c',
        'sys/fdiv.c',
        'sys/hypot.c',
        'sys/infnan.c',
        'sys/invhyp.c',
        'sys/ldfrexp.c',
        'sys/log1p.c',
        'sys/minmax.c',
        'sys/pow_int.c',
        'sys/prec.c',
        'sys/test.c',
      ],
      'include_dirs': [
        'sys'
      ],
    },

    {
      'target_name': 'test',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'test/results.c',
      ],
      'include_dirs': [
        'test'
      ],
    },

    {
      'target_name': 'err',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'err/error.c',
        'err/message.c',
        'err/stream.c',
        'err/strerror.c',
        'err/test.c',
      ],
      'include_dirs': [
        'err',
      ],
    },

    #{
    #  'target_name': 'const',
    #  'product_prefix': 'lib',
    #  'type': 'static_library',
    #  'sources': [
    #    'const/test.c',
    #  ],
    #  'include_dirs': [
    #    'const'
    #  ],
    #},

    {
      'target_name': 'complex',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'complex/inline.c',
        'complex/math.c',
        'complex/test.c',
      ],
      'include_dirs': [
        'complex'
      ],
    },

    {
      'target_name': 'cheb',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'cheb/deriv.c',
        'cheb/eval.c',
        'cheb/init.c',
        'cheb/integ.c',
        'cheb/test.c',
      ],
      'include_dirs': [
        'cheb'
      ],
    },

    {
      'target_name': 'block',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'block/init.c',
        'block/file.c',
        'block/block.c',
        #'block/block_source.c',
        #'block/fprintf_source.c',
        #'block/fwrite_source.c',
        #'block/init_source.c',
        #'block/test.c',
        #'block/test_complex_io.c',
        #'block/test_complex_source.c',
        #'block/test_io.c',
        #'block/test_source.c',
      ],
      'include_dirs': [
        'block'
      ],
    },

    {
      'target_name': 'vector',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'vector/init.c',
        'vector/file.c',
        'vector/vector.c',
        'vector/copy.c',
        'vector/swap.c',
        'vector/prop.c',
        'vector/minmax.c',
        'vector/oper.c',
        'vector/reim.c',
        'vector/subvector.c',
        'vector/view.c',

        #'vector/copy_source.c',
        #'vector/file_source.c',
        #'vector/init_source.c',
        #'vector/minmax_source.c',
        #'vector/oper_complex_source.c',
        #'vector/oper_source.c',
        #'vector/prop_source.c',
        #'vector/reim_source.c',
        #'vector/subvector_source.c',
        #'vector/swap_source.c',
        #'vector/test.c',
        #'vector/test_complex_source.c',
        #'vector/test_source.c',
        #'vector/test_static.c',
        #'vector/view_source.c',
      ],
      'include_dirs': [
        'vector'
      ],
    },

    {
      'target_name': 'matrix',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'matrix/init.c',
        'matrix/matrix.c',
        'matrix/file.c',
        'matrix/rowcol.c',
        'matrix/swap.c',
        'matrix/copy.c',
        'matrix/minmax.c',
        'matrix/prop.c',
        'matrix/oper.c',
        'matrix/getset.c',
        'matrix/view.c',
        'matrix/submatrix.c',
      ],
      'include_dirs': [
        'matrix'
      ],
    },

    {
      'target_name': 'permutation',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'permutation/init.c',
        'permutation/file.c',
        'permutation/permutation.c',
        'permutation/permute.c',
        'permutation/canonical.c',
        'permutation/inline.c',

      ],
      'include_dirs': [
        'permutation'
      ],
    },

    {
      'target_name': 'combination',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'combination/init.c',
        'combination/file.c',
        'combination/combination.c',
        'combination/inline.c',

      ],
      'dependencies': [
        'err',
      ],
      'include_dirs': [
        'combination'
      ],
    },

    {
      'target_name': 'multiset',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'multiset/init.c',
        'multiset/file.c',
        'multiset/multiset.c',
        'multiset/inline.c',

      ],
      'include_dirs': [
        'multiset'
      ],
    },

    {
      'target_name': 'sort',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'sort/sort.c',
        'sort/sortind.c',
        'sort/sortvec.c',
        'sort/sortvecind.c',
        'sort/subset.c',
        'sort/subsetind.c',

      ],
      'include_dirs': [
        'sort'
      ],
    },

    {
      'target_name': 'ieeeutils',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'ieee-utils/print.c',
        'ieee-utils/make_rep.c',
        'ieee-utils/env.c',
        'ieee-utils/fp.c',
        'ieee-utils/read.c',

        'ieee-utils/standardize.c',

      ],
      'include_dirs': [
        'ieee-utils'
      ],
    },

    #{
    #  'target_name': 'cblas',
    #  'product_prefix': 'libgsl',
    #  'type': 'static_library',
    #  'sources': [
    #    'cblas/caxpy.c',
    #    'cblas/ccopy.c',
    #    'cblas/cdotc_sub.c',
    #    'cblas/cdotu_sub.c',
    #    'cblas/cgbmv.c',
    #    'cblas/cgemm.c',
    #    'cblas/cgemv.c',
    #    'cblas/cgerc.c',
    #    'cblas/cgeru.c',
    #    'cblas/chbmv.c',
    #    'cblas/chemm.c',
    #    'cblas/chemv.c',
    #    'cblas/cher.c',
    #    'cblas/cher2.c',
    #    'cblas/cher2k.c',
    #    'cblas/cherk.c',
    #    'cblas/chpmv.c',
    #    'cblas/chpr.c',
    #    'cblas/chpr2.c',
    #    'cblas/cscal.c',
    #    'cblas/csscal.c',
    #    'cblas/cswap.c',
    #    'cblas/csymm.c',
    #    'cblas/csyr2k.c',
    #    'cblas/csyrk.c',
    #    'cblas/ctbmv.c',
    #    'cblas/ctbsv.c',
    #    'cblas/ctpmv.c',
    #    'cblas/ctpsv.c',
    #    'cblas/ctrmm.c',
    #    'cblas/ctrmv.c',
    #    'cblas/ctrsm.c',
    #    'cblas/ctrsv.c',
    #    'cblas/dasum.c',
    #    'cblas/daxpy.c',
    #    'cblas/dcopy.c',
    #    'cblas/ddot.c',
    #    'cblas/dgbmv.c',
    #    'cblas/dgemm.c',
    #    'cblas/dgemv.c',
    #    'cblas/dger.c',
    #    'cblas/dnrm2.c',
    #    'cblas/drot.c',
    #    'cblas/drotg.c',
    #    'cblas/drotm.c',
    #    'cblas/drotmg.c',
    #    'cblas/dsbmv.c',
    #    'cblas/dscal.c',
    #    'cblas/dsdot.c',
    #    'cblas/dspmv.c',
    #    'cblas/dspr.c',
    #    'cblas/dspr2.c',
    #    'cblas/dswap.c',
    #    'cblas/dsymm.c',
    #    'cblas/dsymv.c',
    #    'cblas/dsyr.c',
    #    'cblas/dsyr2.c',
    #    'cblas/dsyr2k.c',
    #    'cblas/dsyrk.c',
    #    'cblas/dtbmv.c',
    #    'cblas/dtbsv.c',
    #    'cblas/dtpmv.c',
    #    'cblas/dtpsv.c',
    #    'cblas/dtrmm.c',
    #    'cblas/dtrmv.c',
    #    'cblas/dtrsm.c',
    #    'cblas/dtrsv.c',
    #    'cblas/dzasum.c',
    #    'cblas/dznrm2.c',
    #    'cblas/hypot.c',
    #    'cblas/icamax.c',
    #    'cblas/idamax.c',
    #    'cblas/isamax.c',
    #    'cblas/izamax.c',
    #    'cblas/sasum.c',
    #    'cblas/saxpy.c',
    #    'cblas/scasum.c',
    #    'cblas/scnrm2.c',
    #    'cblas/scopy.c',
    #    'cblas/sdot.c',
    #    'cblas/sdsdot.c',
    #    'cblas/sgbmv.c',
    #    'cblas/sgemm.c',
    #    'cblas/sgemv.c',
    #    'cblas/sger.c',
    #    'cblas/snrm2.c',
    #    'cblas/srot.c',
    #    'cblas/srotg.c',
    #    'cblas/srotm.c',
    #    'cblas/srotmg.c',
    #    'cblas/ssbmv.c',
    #    'cblas/sscal.c',
    #    'cblas/sspmv.c',
    #    'cblas/sspr.c',
    #    'cblas/sspr2.c',
    #    'cblas/sswap.c',
    #    'cblas/ssymm.c',
    #    'cblas/ssymv.c',
    #    'cblas/ssyr.c',
    #    'cblas/ssyr2.c',
    #    'cblas/ssyr2k.c',
    #    'cblas/ssyrk.c',
    #    'cblas/stbmv.c',
    #    'cblas/stbsv.c',
    #    'cblas/stpmv.c',
    #    'cblas/stpsv.c',
    #    'cblas/strmm.c',
    #    'cblas/strmv.c',
    #    'cblas/strsm.c',
    #    'cblas/strsv.c',
    #    'cblas/tests.c',
    #    'cblas/xerbla.c',
    #    'cblas/zaxpy.c',
    #    'cblas/zcopy.c',
    #    'cblas/zdotc_sub.c',
    #    'cblas/zdotu_sub.c',
    #    'cblas/zdscal.c',
    #    'cblas/zgbmv.c',
    #    'cblas/zgemm.c',
    #    'cblas/zgemv.c',
    #    'cblas/zgerc.c',
    #    'cblas/zgeru.c',
    #    'cblas/zhbmv.c',
    #    'cblas/zhemm.c',
    #    'cblas/zhemv.c',
    #    'cblas/zher.c',
    #    'cblas/zher2.c',
    #    'cblas/zher2k.c',
    #    'cblas/zherk.c',
    #    'cblas/zhpmv.c',
    #    'cblas/zhpr.c',
    #    'cblas/zhpr2.c',
    #    'cblas/zscal.c',
    #    'cblas/zswap.c',
    #    'cblas/zsymm.c',
    #    'cblas/zsyr2k.c',
    #    'cblas/zsyrk.c',
    #    'cblas/ztbmv.c',
    #    'cblas/ztbsv.c',
    #    'cblas/ztpmv.c',
    #    'cblas/ztpsv.c',
    #    'cblas/ztrmm.c',
    #    'cblas/ztrmv.c',
    #    'cblas/ztrsm.c',
    #    'cblas/ztrsv.c',

    #  ],
    #  'include_dirs': [
    #    'cblas'
    #  ],
    #},

    {
      'target_name': 'blas',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'blas/blas.c',
      ],
      'include_dirs': [
        'blas',
      ],
    },

    {
      'target_name': 'specfunc',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'specfunc/airy.c',
        'specfunc/airy_der.c',
        'specfunc/airy_zero.c',
        'specfunc/atanint.c',
        'specfunc/bessel.c',
        'specfunc/bessel_I0.c',
        'specfunc/bessel_I1.c',
        'specfunc/bessel_In.c',
        'specfunc/bessel_Inu.c',
        'specfunc/bessel_J0.c',
        'specfunc/bessel_J1.c',
        'specfunc/bessel_Jn.c',
        'specfunc/bessel_Jnu.c',
        'specfunc/bessel_K0.c',
        'specfunc/bessel_K1.c',
        'specfunc/bessel_Kn.c',
        'specfunc/bessel_Knu.c',
        'specfunc/bessel_Y0.c',
        'specfunc/bessel_Y1.c',
        'specfunc/bessel_Yn.c',
        'specfunc/bessel_Ynu.c',
        'specfunc/bessel_amp_phase.c',
        'specfunc/bessel_i.c',
        'specfunc/bessel_j.c',
        'specfunc/bessel_k.c',
        'specfunc/bessel_olver.c',
        'specfunc/bessel_sequence.c',
        'specfunc/bessel_temme.c',
        'specfunc/bessel_y.c',
        'specfunc/bessel_zero.c',
        'specfunc/beta.c',
        'specfunc/beta_inc.c',
        #'specfunc/cheb_eval.c',
        #'specfunc/cheb_eval_mode.c',
        'specfunc/clausen.c',
        'specfunc/coulomb.c',
        'specfunc/coulomb_bound.c',
        'specfunc/coupling.c',
        'specfunc/dawson.c',
        'specfunc/debye.c',
        'specfunc/dilog.c',
        'specfunc/elementary.c',
        'specfunc/ellint.c',
        'specfunc/elljac.c',
        'specfunc/erfc.c',
        'specfunc/exp.c',
        'specfunc/expint.c',
        'specfunc/expint3.c',
        'specfunc/fermi_dirac.c',
        'specfunc/gamma.c',
        'specfunc/gamma_inc.c',
        'specfunc/gegenbauer.c',
        'specfunc/hyperg.c',
        'specfunc/hyperg_0F1.c',
        'specfunc/hyperg_1F1.c',
        'specfunc/hyperg_2F0.c',
        'specfunc/hyperg_2F1.c',
        'specfunc/hyperg_U.c',
        'specfunc/laguerre.c',
        'specfunc/lambert.c',
        'specfunc/legendre_H3d.c',
        'specfunc/legendre_Qn.c',
        'specfunc/legendre_con.c',
        'specfunc/legendre_poly.c',
        'specfunc/log.c',
        'specfunc/mathieu_angfunc.c',
        'specfunc/mathieu_charv.c',
        'specfunc/mathieu_coeff.c',
        'specfunc/mathieu_radfunc.c',
        'specfunc/mathieu_workspace.c',
        'specfunc/poch.c',
        'specfunc/pow_int.c',
        'specfunc/psi.c',
        'specfunc/result.c',
        'specfunc/shint.c',
        'specfunc/sinint.c',
        'specfunc/synchrotron.c',
        #'specfunc/test_airy.c',
        #'specfunc/test_bessel.c',
        #'specfunc/test_coulomb.c',
        #'specfunc/test_dilog.c',
        #'specfunc/test_gamma.c',
        #'specfunc/test_hyperg.c',
        #'specfunc/test_legendre.c',
        #'specfunc/test_mathieu.c',
        #'specfunc/test_sf.c',
        'specfunc/transport.c',
        'specfunc/trig.c',
        'specfunc/zeta.c',

      ],
      'dependencies': [
        #'cheb',
        'complex',
      ],
      'include_dirs': [
        'specfunc',
      ],
    },

    {
      'target_name': 'rng',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'rng/borosh13.c',
        'rng/cmrg.c',
        'rng/coveyou.c',
        'rng/default.c',
        'rng/file.c',
        'rng/fishman18.c',
        'rng/fishman20.c',
        'rng/fishman2x.c',
        'rng/gfsr4.c',
        'rng/inline.c',
        'rng/knuthran.c',
        'rng/knuthran2.c',
        'rng/knuthran2002.c',
        'rng/lecuyer21.c',
        'rng/minstd.c',
        'rng/mrg.c',
        'rng/mt.c',
        'rng/r250.c',
        'rng/ran0.c',
        'rng/ran1.c',
        'rng/ran2.c',
        'rng/ran3.c',
        'rng/rand.c',
        'rng/rand48.c',
        'rng/random.c',
        'rng/randu.c',
        'rng/ranf.c',
        'rng/ranlux.c',
        'rng/ranlxd.c',
        'rng/ranlxs.c',
        'rng/ranmar.c',
        'rng/rng.c',
        'rng/schrage.c',
        'rng/slatec.c',
        'rng/taus.c',
        'rng/taus113.c',
        #'rng/test.c',
        'rng/transputer.c',
        'rng/tt.c',
        'rng/types.c',
        'rng/uni.c',
        'rng/uni32.c',
        'rng/vax.c',
        'rng/waterman14.c',
        'rng/zuf.c',

      ],
      'dependencies': [
        'err',
      ],
      'include_dirs': [
        'rng',
      ],
    },

    {
      'target_name': 'randist',
      'product_prefix': 'libgsl',
      'type': 'static_library',
      'sources': [
        'randist/bernoulli.c',
        'randist/beta.c',
        'randist/bigauss.c',
        'randist/binomial.c',
        'randist/binomial_tpe.c',
        'randist/cauchy.c',
        'randist/chisq.c',
        'randist/dirichlet.c',
        'randist/discrete.c',
        'randist/erlang.c',
        'randist/exponential.c',
        'randist/exppow.c',
        'randist/fdist.c',
        'randist/flat.c',
        'randist/gamma.c',
        'randist/gauss.c',
        'randist/gausstail.c',
        'randist/gausszig.c',
        'randist/geometric.c',
        'randist/gumbel.c',
        'randist/hyperg.c',
        'randist/landau.c',
        'randist/laplace.c',
        'randist/levy.c',
        'randist/logarithmic.c',
        'randist/logistic.c',
        'randist/lognormal.c',
        'randist/multinomial.c',
        'randist/nbinomial.c',
        'randist/pareto.c',
        'randist/pascal.c',
        'randist/poisson.c',
        'randist/rayleigh.c',
        'randist/shuffle.c',
        'randist/sphere.c',
        'randist/tdist.c',
        #'randist/test.c',
        'randist/weibull.c',

      ],
      'dependencies': [
        'err',
        'sys',
        'rng',
        'specfunc',
      ],
      'include_dirs': [
        'randist',
      ],
    },

    {
      'target_name': 'gsl',
      'type': 'static_library',
      'sources': [
        'version.c'
      ],
      'dependencies': [
        'combination',
        'randist',
      ],
    },


    ## test program that prints the version number
    #{
    #  'target_name': 'randistdemo',
    #  'type': 'executable',
    #  'dependencies': [
    #    'randist'
    #  ],
    #  'sources': [
    #    'randist/demo.c'
    #  ]
    #},

    ## test program that prints the version number
    #{
    #  'target_name': 'demo',
    #  'type': 'executable',
    #  'dependencies': [
    #    'combination'
    #  ],
    #  'sources': [
    #    'combination/demo.c'
    #  ]
    #},
  ]
}
