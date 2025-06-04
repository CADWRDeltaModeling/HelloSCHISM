.. _module2:

Module 2: Overview
--------------------

The transport flag *iupwind_t=0* signals the Eulerian-Lagrangian method of transport. Because it is not conservative for salt, this numerical method is not common in practice. Instead, we want to use the hybrid second order (TVD, *iupwind_t=2*) finite volume scheme with upwind being preferred in water shallower than 6m total depth. In the simplified grid example, which has a sea level of about a meter above the bathymetric datum, a total depth of 6m will occur at about 5m nominal bathymetric depth. 

.. warning::

   The information on **iupwind_t** variable needs to be updated

Setting *iupwind_t=2* is a single flag change in **param.nml**. However, because it is a hybrid scheme, SCHISM expects a property file called **tvd.prop** of 0 and 1 values describing where TVD can be used potentially. Keep in mind, even with this file TVD will only be used if *H > 6m*. 

The .prop file format just pairs element numbers and values. We are controlling TVD entirely with depth, so we just need a prop file full of ones. There are 4636 elements in the domain (you can get this number from first number on the second line of **hgrid.gr3**). So this file will be two columns, the first of which will be the numbers 1 to 4636 and the second of which will be the number 1:

.. grid:: 2

   .. grid-item::
      | 1     1
      | 2     1
      | 3     1
      | ...   ...
      | 4636  1

   .. grid-item-card:: TIP:
     :img-background: /img/blue_background.png

      One way to do this on a quick one-off basis if you are willing to put up with some cutting and pasting is to write a quick python script or do it in your favorite tool such as Excel. It should be space delineated rather than comma-delineated, which may require a search and replace if you save it in csv format.

The task is also a soft introduction to the preprocessor:

1.	Navigate to the m2_preprocessor folder  (./Module_Data/**m2_preprocessor**”)
2.	Inspect the directory. The launch file for the preprocessor is called **input.yaml** in all our examples. There are two variants of the simple bay mesh, which differ only in depth. We will use the 16m version this time. Go to the **“mesh”** section of **input.yaml** and following the amount of indentation in the file (preferably using spaces), set the mesh input file to hgrid_16m.gr3.

.. code:: yaml

   mesh_inputfile: hgrid_16.gr3
 
3.	We want to tell the preprocessor to build a .prop file based on a polygon. So at the outer level of indentation add:

.. code:: yaml

   prop:
     tvd.prop: !include tvd.yaml
 
4.	Now we need to create a trivial **tvd.yaml**, which will contain a default and one polygon. Because the default will assign 1.0 to anything we miss, the actual specification of the polygon doesn’t matter. However, we will add one that amply contains the whole domain (the “All” part is just a label). Here are the contents of **tvd.yaml**

.. code:: yaml

   default: 1
   polygons:
   - attribute: '1'
     name: All
     vertices:
     - [0.0, -100000.0]
     - [100000.0, -100000.0]
     - [100000.0, 100000.0]
     - [0.0, 100000.0]

5.	Now you should be able to run the preprocessor. You will either need to be in the **schism** conda environment created in the :ref:`Getting Started  section <pystart>` or you’ll need to specify the script location.

**With conda (Preferred):**

.. code-block:: console

   conda activate schism
   cd <PATH TO M2_PREPROCESSOR FOLDER>
   prepare_schism input.yaml

**Without conda:**

Navigate to the m2_preprocessor folder in your file explorer. Type “cmd” in the navigation bar to open a command prompt terminal in this directory. If you downloaded schimpy and placed it in the scripts folder (see the Python section of Getting Started) you should be able to do the following command:
.. code-block:: console
   
   python ../../scripts/schimpy-master/schimpy/prepare_schism.py input.yaml

6.	At this point, you have recreated the Hello SCHISM tutorial with an added prop file. Only a few more changes are needed. Locate and open the files **param.barotropic.nml**. Set *iupwind_t = 2* and *rnday=5* in **param.barotropic.nml**. This changes the transport method to TVD2 and the runtime in days to 5.

Then save the **param.barotropic.nml** file as **param.nml** and the **bctides.in.barotropic** file as **bctides.in**. SCHISM is looking for a specific files called param.nml and bctidess.in, so depending on wether you're running 2D or 3D you'll want to save the barotropic/baroclinic param file out as those file names, or use symbolic links. 

7.	Launch the run (note, you’ll need the windows build of SCHISM to be set in your system Path):

For Windows 10:
.. code-block:: console

   mpiexec -np 8 pschism_PREC_EVAP_GOTM_TVD-VL.exe 4

For Windows 11:
.. code-block:: console

   mpiexec -np 8 pschism_OLDIO_PREC_EVAP_TVD-VL.exe 4
