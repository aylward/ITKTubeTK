##############################################################################
#
# Library:   TubeTK
#
# Copyright 2010 Kitware Inc. 28 Corporate Drive,
# Clifton Park, NY, 12065, USA.
#
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
##############################################################################

include_regular_expression( "^.*$" )

set( PROJ_EXE
 ${TubeTK_LAUNCHER} $<TARGET_FILE:${MODULE_NAME}> )

# Test1
itk_add_test(
  NAME ${MODULE_NAME}-Test1
  COMMAND ${PROJ_EXE}
    DATA{${TubeTK_DATA_ROOT}/${MODULE_NAME}-CVT50-Branch-truth.cvt.mha}
    DATA{${TubeTK_DATA_ROOT}/${MODULE_NAME}-CVT50-Branch-truth.grp,${MODULE_NAME}-CVT50-Branch-truth.grp,${MODULE_NAME}-CVT50-Branch-truth.grp.mat,${MODULE_NAME}-CVT50-Branch-truth.grp.brc,${MODULE_NAME}-CVT50-Branch-truth.grp.rot}
    ${ITK_TEST_OUTPUT_DIR}/${MODULE_NAME}-CVT50-Branch-truth.grp.Image )

# Test1-Compare
itk_add_test(
  NAME ${MODULE_NAME}-Test1-Compare-00
  COMMAND ${TubeTK_CompareImages_EXE}
    CompareImages
    -t ${ITK_TEST_OUTPUT_DIR}/${MODULE_NAME}-CVT50-Branch-truth.grp.Image.mat.mha
    -b DATA{${TubeTK_DATA_ROOT}/${MODULE_NAME}-CVT50-Branch-truth.grp.Image.mat.mha} )

set_tests_properties( ${MODULE_NAME}-Test1-Compare-00 PROPERTIES DEPENDS
  ${MODULE_NAME}-Test1 )
