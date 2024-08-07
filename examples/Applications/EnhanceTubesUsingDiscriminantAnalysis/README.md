TubeTK Enhance Tubes Using Discriminant Analysis Application
============================================================

Purpose: This application uses tube-geometry related measures applied to
one or more images to generate a single image in which the pixels associated
with tubes are bright and all other pixels are darker.

Details: This method forms a Parzen window density estimate of the
distribution of tube pixels within a features space.  The feature space is
defined by multi-scale measurements of tube-related geometries (e.g.,
ridgeness, intensity, intensity curvature) made on the images passed
as input.

The program has two modes of operation: training and testing.  In training,
tube pixels are identified by the label map (required for training).
The values in the label map are interpreted via the ObjectId
parameter arguments.  The first parameter argument must be the label map
value associated with tubes in the image.  The remaining values passed as
ObjectIds are associated with non-tube pixels in the image.  Linear
discriminant analysis is applied to find the three orthogonal feature space
directions that best separate the classes.  Density function
estimates are formed for each class using parzen windowing in the three
dimension projective feature space.  The output is the probability of
each pixel in the input image(s) having been generated by the tube class.

In testing, a label map is not provided and instead the class descriptions
must be read from a parameter file.   The output is the probability of
each pixel in the input image(s) having been generated by the tube class.


---
*This file is part of [TubeTK](http://www.tubetk.org). TubeTK is developed by [Kitware, Inc.](https://www.kitware.com) and licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).*
