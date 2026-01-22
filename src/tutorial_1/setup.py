from setuptools import find_packages, setup

package_name = 'tutorial_1'

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
    maintainer='Achutha Thyagaraju',
    maintainer_email='cathyagaraju2000@gmail.com',
    description='ROS 2 tutorial package demonstrating core concepts using turtlesim',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "test_node = tutorial_1.Node_0:main",
            "draw_circle = tutorial_1.Node_1__Draw_Circle:main",
            "pose_subscriber = tutorial_1.Node_2__Pose_Subscriber:main",
            "turtle_controller_cl = tutorial_1.Node_3__Closed_Loop_Turtle_Controller:main"
        ],
    },
)
