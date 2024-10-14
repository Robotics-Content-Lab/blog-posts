from setuptools import find_packages, setup

package_name = 'pub_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Robotics Content Lab',
    maintainer_email='office@roboticscontentlab.com',
    description='Basic example of publisher and subscriber in one node' 
        'as seen at https://www.roboticscontentlab.com/blog/publish-and-subscribe-mechanism-with-ros-2-rclpy/, on September 29, 2024',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_sub = pub_sub.pub_sub:main'
        ],
    },
)
