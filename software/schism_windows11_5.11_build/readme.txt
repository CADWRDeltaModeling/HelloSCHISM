
1. copy all the exe and dll files to a local folder except folder ms-mpi-9.0, say schism511.
2. if you don't have ms mpi sdk and application, go to folder ms-mpi-9.0. run the sdk and application
   installation files.
3. you can run pschism in parallell like "mpiexec -np 32 ..\schism511\pschism_OLDIO_TVD-VL.exe", here 32 
   is the number of processors you want to use on your Windows system. "..\schism511\pschism_OLDIO_TVD-VL.exe" is 
   just an example, you need to change it to your pschism location.

