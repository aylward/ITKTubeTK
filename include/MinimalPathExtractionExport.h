#pragma once

#include "itkConfigure.h"
// Workaround for ITKTubeTK Python package builds
#if !defined(MinimalPathExtraction_EXPORT)
#  define MinimalPathExtraction_EXPORT
#  define MinimalPathExtraction_HIDDEN
#else
#include "MinimalPathExtractionExport.h"
#endif
