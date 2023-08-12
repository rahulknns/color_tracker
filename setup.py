from setuptools import setup
  
setup(
    name='color_tracker',
    version='1.0',
    description='track a single color in a frame or video',
    author='Rahulkannan S',
    author_email='rahulknns@gmail.com',
    packages=['color_tracker'],
    package_dir={'color_tracker': 'src/color_tracker'},

    install_requires=[
        'opencv-python',
        'numpy',

    ],
)