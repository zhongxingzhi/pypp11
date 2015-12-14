# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import math
import unittest
import fundamental_tester_base
from pygccxml import declarations
from pyplusplus import function_transformers as ft
from pyplusplus.module_builder import call_policies

class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'ft_inout_static_matrix'

    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__(
            self
            , tester_t.EXTENSION_NAME
            , *args )

    def customize( self, mb ):
        mb.global_ns.calldefs().create_with_signature = True
        
        sum_and_fill = mb.free_fun( 'sum_and_fill' )
        sum_and_fill.add_transformation( ft.inout_static_matrix('m', rows=2, columns=3) )
        
        #calculate = mb.mem_fun( 'calculate' )
        #calculate.add_transformation( ft.input_static_matrix('m', rows=3, columns=5) )
               
    def run_tests(self, module):
        """Run the actual unit tests"""
        m = [ [1, 2, 3], [4,5,6] ]
        result = module.sum_and_fill( m, -1 )
        self.failUnless( 21 == result[0] )
        self.failUnless( [ [-1, -2, -3], [-4,-5,-6] ] == result[1])

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
