from setuptools import setup, find_packages

setup(
    name='k8s-automation-script',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'connect-cluster=connect_cluster:main',
            'install-helm=install_tools:install_helm',
            'install-keda=install_tools:install_keda',
            'create-deployment=create_deployment:main',
            'get-health-status=get_health_status:main',
        ],
    },
)