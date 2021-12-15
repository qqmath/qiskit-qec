# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2020
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Part of the QEC framework

import numpy as np

def asarray(*args, **kargs):
    return np.asarray(*args, **kargs)

def atleast_2d(*args, **kargs):
    return np.atleast_2d(*args, **kargs)

def concatenate(*args, **kargs):
    return np.concatenate(*args, **kargs)

def sum(*args, **kargs):
    return np.sum(*args, **kargs)

def zeros(*args, **kargs):
    return np.zeros(*args, **kargs)





