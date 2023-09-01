########### SVN repository information ###################
# $Date: 2023-05-11 18:08:12 -0500 (Thu, 11 May 2023) $
# $Author: toby $
# $Revision: 5577 $
# $URL: https://subversion.xray.aps.anl.gov/pyGSAS/trunk/unit_tests.py $
# $Id: unit_tests.py 5577 2023-05-11 23:08:12Z toby $
########### SVN repository information ###################
'''At present,
only modules :mod:`GSASIIspc` and :mod:`GSASIIlattice` have self-tests
and these have not been tested or updated in many, many years. 
'''

import GSASIIspc
import GSASIIlattice
def test_GSASIIspc():
    '''Test registered self-tests in ``GSASIIspc``.
    Takes no input and returns nothing. Throws an Exception if a test fails.
    '''
    #GSASIIspc.selftestquiet = False
    for test in GSASIIspc.selftestlist:
        test()
def test_GSASIIlattice():
    '''Test registered self-tests in ``GSASIIlattice``.
    Takes no input and returns nothing. Throws an Exception if a test fails.
    '''
    #GSASIIlattice.selftestquiet = False
    for test in GSASIIlattice.selftestlist:
        test()

if __name__ == '__main__':
    test_GSASIIspc()
    test_GSASIIlattice()
    print("OK")
