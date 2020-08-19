site_configuration = {
    'systems': [
        {
            'name':'alaska',
            'descr':'Default AlaSKA OpenHPC p3-appliances slurm cluster',
            'hostnames': ['openhpc-login-0', 'openhpc-compute'],
            'modules_system':'lmod',
            'partitions':[
                {
                    'name':'ib-gcc9-impi-verbs',
                    'descr': '100Gb Infiniband with gcc 9.3.0 and Intel MPI 2019.7.217',
                    'scheduler': 'slurm',
                    'launcher':'mpirun',
                    'max_jobs':8,
                    'environs': ['imb', 'omb', 'intel-hpl', 'intel-hpcg'],
                    'modules': ['gcc/9.3.0-5abm3xg', 'intel-mpi/2019.7.217-bzs5ocr'],
                    'variables': [
                        #['FI_PROVIDER', 'mlx'] # doesn't work, needs ucx
                        ['FI_VERBS_IFACE', 'ib'] # # Network interface to use - this is actually default
                        # these were (failed) attempts to make `srun` work:
                        #['I_MPI_PMI_LIBRARY', '/opt/ohpc/admin/pmix/lib/libpmi.so'], # see https://slurm.schedmd.com/mpi_guide.html#intel_mpi
                        #['SLURM_MPI_TYPE', 'pmi2'],
                    ],
                },
                {
                    'name':'roce-gcc9-impi-verbs',
                    'descr': '25Gb RoCE with gcc 9.3.0 and Intel MPI 2019.7.217 using verbs',
                    'scheduler': 'slurm',
                    'launcher':'mpirun',
                    'max_jobs':8,
                    'environs': ['imb', 'omb', 'intel-hpl', 'intel-hpcg'],
                    'modules': ['gcc/9.3.0-5abm3xg', 'intel-mpi/2019.7.217-bzs5ocr'],
                    'variables': [
                        ['FI_VERBS_IFACE', 'p3p2'] # Network interface to use.
                    ],
                },
                {
                    'name':'ib-gcc9-openmpi4-ucx',
                    'descr':'100Gb Infiniband with gcc 9.3.0 and openmpi 4.0.3 using UCX transport layer',
                    'scheduler': 'slurm',
                    'launcher':'srun',
                    'max_jobs':8,
                    'environs':['imb', 'omb', 'gromacs', 'openfoam', 'cp2k', 'hpl'],
                    'modules': ['gcc/9.3.0-5abm3xg', 'openmpi/4.0.3-qpsxmnc'],
                    'variables': [
                        ['SLURM_MPI_TYPE', 'pmix_v2'],
                    ]
                },
                {
                    'name':'roce-gcc9-openmpi4-ucx',
                    'descr':'25Gb RoCE with gcc 9.3.0 and openmpi 4.0.3 using UCX transport layer',
                    'scheduler': 'slurm',
                    'launcher':'srun',
                    'max_jobs':8,
                    'environs':['imb', 'omb', 'gromacs', 'openfoam', 'cp2k', 'hpl'],
                    'modules': ['gcc/9.3.0-5abm3xg', 'openmpi/4.0.3-qpsxmnc'],
                    'variables': [
                        ['SLURM_MPI_TYPE', 'pmix_v2'],
                        # use roce:
                        ['UCX_NET_DEVICES', 'mlx5_1:1'],
                    ]
                },
            ]
        }, # end alaska
        # < insert new systems here >
    ],
    'environments': [
        {
            'name': 'imb',      # a non-targeted environment seems to be necessary for reframe to load the config
        },
        {
            'name': 'imb', # OHPC-provided packages
            'target_systems': ['alaska:ib-gcc7-openmpi3-openib', 'alaska:roce-gcc7-openmpi3-openib'],
            'modules': ['imb'],
        },
        {
            'name': 'imb', # spack-provided packages
            'target_systems': ['alaska:ib-gcc7-openmpi4-ucx', 'alaska:roce-gcc7-openmpi4-ucx'],
            'modules': ['intel-mpi-benchmarks/2019.5-q5ujyli'],
        },
        {
            'name': 'imb', # spack-provided packages
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['intel-mpi-benchmarks/2019.5-dwg5q6j'],
        },
        {
            'name': 'imb', # spack-provided packages
            'target_systems': ['ib-gcc9-impi-verbs', 'roce-gcc9-impi-verbs'],
            'modules': ['intel-mpi-benchmarks/2019.5-w54huiw'],
        },
        {
            'name': 'gromacs',
        },
        {
            'name': 'gromacs',
            'target_systems': ['alaska:ib-gcc7-openmpi4-ucx', 'alaska:roce-gcc7-openmpi4-ucx'],
            'modules': ['gromacs/2016.4-xixmrii']
        },
        {
            'name': 'gromacs',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['gromacs/2016.4-y5sjbs4']
        },
        {
            'name': 'omb',
        },
        {
            'name': 'omb',
            'target_systems': ['alaska:ib-gcc7-openmpi4-ucx', 'alaska:roce-gcc7-openmpi4-ucx'],
            'modules': ['osu-micro-benchmarks/5.6.2-el6z55i']
        },
        {
            'name': 'omb',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['osu-micro-benchmarks/5.6.2-vx3wtzo']
        },
        {
            'name': 'omb',
            'target_systems': ['alaska:ib-gcc9-impi-verbs', 'alaska:roce-gcc9-impi-verbs'],
            'modules': ['osu-micro-benchmarks/5.6.2-ppxiddg']
        },
        {
            'name': 'hpl',
        },
        {
            'name': 'hpl',
            'target_systems': ['alaska:ib-gcc7-openmpi4-ucx', 'alaska:roce-gcc7-openmpi4-ucx'],
            'modules': ['hpl/2.3-tgk5uqq'],
        },
        {
            'name': 'hpl',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['hpl/2.3-iyor3px'],
        },
        {
            'name': 'intel-hpl',
        },
        {
            'name': 'intel-hpl',
            'target_systems': ['alaska:ib-gcc9-impi-verbs', 'alaska:roce-gcc9-impi-verbs'],
            'modules': ['intel-mkl/2020.1.217-5tpgp7b'],
            'variables':[
                ['PATH', '$PATH:$MKLROOT/benchmarks/mp_linpack/'], # MKLROOT provided by mkl module
            ],
        },
        {
            'name': 'intel-hpcg',
        },
        {
            'name': 'intel-hpcg',
            'target_systems': ['alaska:ib-gcc9-impi-verbs', 'alaska:roce-gcc9-impi-verbs'],
            'modules': ['intel-mkl/2020.1.217-5tpgp7b'],
            'variables':[
                ['PATH', '$PATH:$MKLROOT/benchmarks/hpcg/bin/'], # MKLROOT provided by mkl module
                ['XHPCG_BIN', 'xhpcg_avx2'],
                ['SLURM_CPU_BIND', 'verbose'], # doesn't work as task/affinity plugin not enabled
            ]
        },
        {
            'name':'openfoam'
        },
        {
            'name':'openfoam',
            'target_systems': ['alaska:ib-gcc7-openmpi4-ucx', 'alaska:roce-gcc7-openmpi4-ucx'],
            'modules': ['openfoam-org/7-2ceqb4l']
        },
        {
            'name':'openfoam',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['openfoam-org/7-4zgjbg2']
        },
        {
            'name':'cp2k',
        },
        {
            'name':'cp2k',
            'target_systems': ['alaska:ib-gcc7-openmpi4-ucx', 'alaska:roce-gcc7-openmpi4-ucx'],
            'modules': ['cp2k/7.1-spcqy4k']
        },
        {
            'name':'cp2k',
            'target_systems': ['alaska:ib-gcc9-openmpi4-ucx', 'alaska:roce-gcc9-openmpi4-ucx'],
            'modules': ['cp2k/7.1-akb54dx']
        }
    ],
    'logging': [
        {
            'level': 'debug',
            'handlers': [
                {
                    'type': 'file',
                    'name': 'reframe.log',
                    'level': 'debug',
                    'format': '[%(asctime)s] %(levelname)s: %(check_name)s: %(message)s',   # noqa: E501
                    'append': False
                },
                {
                    'type': 'stream',
                    'name': 'stdout',
                    'level': 'info',
                    'format': '%(message)s'
                },
                {
                    'type': 'file',
                    'name': 'reframe.out',
                    'level': 'info',
                    'format': '%(message)s',
                    'append': False
                }
            ],
            'handlers_perflog': [
                {
                    'type': 'filelog',
                    # make this the same as output filenames which are ('sysname', 'partition', 'environ', 'testname', 'filename')
                    'prefix': '%(check_system)s/%(check_partition)s/%(check_environ)s/%(check_name)s', # <testname>.log gets appended
                    'level': 'info',
                    # added units here - see Reference: https://reframe-hpc.readthedocs.io/en/latest/config_reference.html?highlight=perflog#logging-.handlers_perflog
                    'format': '%(check_job_completion_time)s|reframe %(version)s|%(check_info)s|jobid=%(check_jobid)s|%(check_perf_var)s=%(check_perf_value)s|%(check_perf_unit)s|ref=%(check_perf_ref)s (l=%(check_perf_lower_thres)s, u=%(check_perf_upper_thres)s)|%(check_tags)s',  # noqa: E501
                    'datefmt': '%FT%T%:z',
                    'append': True
                }
            ]
        }
    ],
    'general': [
        {
            'check_search_path': ['./'],
            'check_search_recursive': True
        }
    ]    
}
