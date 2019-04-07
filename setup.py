#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
from os import path
from glob import glob

name = "streamglob"
setup(name=name,
      version="0.0.11.dev0",
      description="Streaming video browser and player frontend",
      author="Tony Cebzanov",
      author_email="tonycpsu@gmail.com",
      url="https://github.com/tonycpsu/streamglob",
      python_requires='>=3.6',
      classifiers=[
          "Environment :: Console",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Intended Audience :: End Users/Desktop"
      ],
      license = "GPLv2",
      packages=find_packages(),# + ["streamglob.providers.contrib.foo"],
      data_files=[
          ('share/doc/%s' % name, ["docs/config.yaml.sample"]),
      ],
      include_package_data=True,
      install_requires = [
          "urwid @ git+https://github.com/tonycpsu/urwid",
          "urwid_utils==0.1.3.dev0",
          "panwid>=0.3.0.dev13",
          "requests",
          "lxml",
          "pytz",
          "tzlocal",
          "pymemoize",
          "orderedattrdict",
          "pyyaml",
          "py-dateutil",
          "streamlink>=0.11.0",
          "youtube_dl",
          "bitmath",
          "pony",
          "stevedore",
          "atoma",
          "python-twitch-client",
          "mistune",
          "html2text",
          "dataclasses_json",
          "tonyc_utils==1.0.1",
          "instagram_private_api @ git+https://github.com/ping/instagram_private_api",
          "PyPeri @ git+https://github.com/tonycpsu/PyPeri",
      ],
      test_suite="test",
      entry_points = {
          "console_scripts": [
              "streamglob=streamglob.__main__:main"
          ],
          "streamglob.providers": [
              "instagram = streamglob.providers.instagram:InstagramProvider",
              "mlb = streamglob.providers.mlb:MLBProvider",
              "nhl = streamglob.providers.nhl:NHLProvider",
              "periscope = streamglob.providers.periscope:PeriscopeProvider",
              "rss = streamglob.providers.rss:RSSProvider",
              "twitch = streamglob.providers.twitch:TwitchProvider",
              "youtube = streamglob.providers.youtube:YouTubeProvider",
          ]
      },
      zip_safe=False
     )
