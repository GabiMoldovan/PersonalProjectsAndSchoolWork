from Tests.TestDomain import testCarte
from Tests.testCRUD import testCrud
from Tests.testLogic import testAllLogicFunctions
from Tests.testUNDOandREDO import testUNDOREDO


def runTests():
    testCarte()
    testCrud()
    testAllLogicFunctions()
    testUNDOREDO()
