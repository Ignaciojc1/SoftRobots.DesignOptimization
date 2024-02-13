# -*- coding: utf-8 -*-
"""Reduced config for the Tripod Finger.
This is a scene with object for calibration purpose.
"""

__authors__ = "tnavez"
__contact__ = "tanguy.navez@inria.fr"
__version__ = "1.0.0"
__copyright__ = "(c) 2020, Inria"
__date__ = "Feb 09 2023"


import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.absolute())+"/../")
sys.path.insert(0, str(pathlib.Path(__file__).parent.absolute()))

from Config import Config

import numpy as np 

class OptimizationConfig(Config):

    def __init__(self):
        super().__init__()

    def get_design_variables(self):   
        return {"youngModulus": [self.youngModulus, 5.0e-4, 0.5],
                "poissonRatio": [self.poissonRatio, 0.4, 0.49]}


    def get_objective_data(self):
        t = 50
        return {"TorqueCalibration": ["minimize", t]}

    def get_assessed_together_objectives(self):
        return [["TorqueCalibration"]]
    
    