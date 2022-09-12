.. _module4:

MODULE 4: OVERVIEW
-------------------

This module’s directory (“./module_data/**m4_requestoutput**”) contains a sample of model input files that you will need to edit in order to change what outputs are produced in Hello SCHISM.

Adding Flow Observation Transects
``````````````````````````````````

As seen in "FIGURE" there are X transects already specified in the model with the **flowlines.yaml** file, which creates the **fluxflag.prop** file. You will add a X+1-nth transect to capture flow through A LOCATION as shown below:

"FIGURE N"

The coordinates for the transect you will add will be one line straight down the center of the grid.

.. code-block:: text

    [ Some coordinates here ] 

1.	Open ‘flow_station_xsects.yaml’ in an editor, and note the contents. 

2.	Add one line or remove one for the location to calculate flows if you want.

3.	Run the preprocessor to create a new fluxflag.prop.

.. code-block:: console

   prepare_pschism.py input.yaml

This creates all the neceesarry files for SCHISM to run, and your edit to the **flowlines.yaml** file is what modifies the **fluxflag.prop** file.

.. note::

   More prepreprocessing documentation may be found here:
   http://baydeltaoffice.water.ca.gov/modeling/deltamodeling/models/tools/ 

Adding Observation Point Locations
````````````````````````````````````

The station input file “**station.in**” used to launch *SCHISM* is how the x-,y-, and z- coordinates are associated with the station name. The z-coordinate in this example uses -1.0 m as the “default” observation depth, other depths are classified as “upper” or “lower” depending on where they are in the water column.

In the Hello SCHISM example model, there are 6 stations that have been designated prior to running the model in the “station.in” file which are distributed in the model domain:

.. _obs_sta_req:

.. figure:: /img/schism_obs_stations.png
   :alt: Hello SCHISM Input Stations
   :align: center

   *Hello SCHISM observation stations as specified by the station.in file*
