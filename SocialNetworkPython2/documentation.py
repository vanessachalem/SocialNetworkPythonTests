'''
Created on Jun 4, 2013
module prints the doc string for the Network, Perosn, TestNetwork and TestPerson classes
@author: Vanessa
'''

from networkmodule import Network
from personmodule import Person
from testnetworkfixed import TestNetworkFixed
from testperson import TestPerson
from pydoc import help

help(Network())
print()
print()
help (Person())
print()
print()
help(TestNetworkFixed())
print()
print()
help(TestPerson())