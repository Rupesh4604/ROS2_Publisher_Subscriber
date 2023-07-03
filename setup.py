from setuptools import setup

package_name = 'pubsub_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rupesh',
    maintainer_email='rupesh@todo.todo',
    description='Basic Publisher and Subsriber Programme',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = pubsub_pkg.publisher:main',
            'listener = pubsub_pkg.subscriber:main'
        ],
    },
)