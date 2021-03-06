"""
Set up file for the Python Madrigal Remote API

"""

from distutils.core import setup

setup(name="madrigalWeb", version="3.0.5", \
      description="Remote Madrigal Python API", \
      author="Ronald Ilma", author_email="rri5@cornell.edu", \
      url="http://cedar.openmadrigal.org", \
      packages=["madrigalWeb", "madrigalWebPlot"], keywords = ['Madrigal'], \
      scripts=['madrigalWeb/globalIsprint.py', 'madrigalWeb/globalDownload.py', \
      'madrigalWebPlot/scripts/madrigalPColor.py', 'madrigalWebPlot/scripts/madrigalScatter.py'])
      