import json
import os
import sys

i = open("tdconf.json")

config = json.load(i)

print(f"Loading Configurations.")

maxl = config["max.LINES"]


def execute():
    """
    Gives you All Of the TD.json File Configuration
    :return: 0
    """
    print(f"Configurations:\nMax Lines: {maxl}\nConfig Command: {config['INITCMD']}")


g = open("tdpackage.json")

package = json.load(g)

name = package['package_name']

repo = package['repo']

contr = package["contributors"] or package['contrib']


def get_package():
    """
    Package Returns The TD Pack Details
    :return: nil
    """
    print(f"Initial Package:\nPackage Name: {name}\nRepository Link: {repo}\nContributors: {contr}")

