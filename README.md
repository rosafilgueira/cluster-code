# Enabling Complex Analysis of Large Scale Digital Collections

This repository contains code from the first phase of '[Enabling Complex Analysis of Large Scale Digital Collections](http://figshare.com/articles/Enabling_Complex_Analysis_of_Large_Scale_Digital_Collections/1319482)', a project funded by the [Jisc Research Data Spring](http://opensource.org/licenses/MIT).

The core project team are:

- PI Melissa Terras (UCL)
- CI James Baker (British Library)
- CI David Beavan (UCL)
- CI James Hetherington (UCL)
- CI Martin Zaltz Austwick (UCL)

Associated researchers (without who research questions none of this could have happened!) are:
- Oliver Duke-Williams (UCL)
- Will Finley (Sheffield)
- Helen O'Neill (UCL)
- Anne Welsh (UCL)

All code is available for use and reuse under a [MIT Licence](http://opensource.org/licenses/MIT)

For more info on the project see the [UCL DH](http://blogs.ucl.ac.uk/dh/2015/05/07/bluclobber-or-enabling-complex-analysis-of-large-scale-digital-collections/) and [British Library Digital Scholarship](http://britishlibrary.typepad.co.uk/digital-scholarship/) blogs.


Note1: Unzip Users/rosafilgueira/EPCC/ATI-SE/Humanities/Rosa_Versions/cluster-code/bluclobber/test/fixtures/zips
      Install Spark- Mac os x: brew install apache-spark


Note2-Testing: fab standalone.setup:query=queries/diseases.py standalone.test:query_name=diseases
       fab standalone.setup:query=queries/normaliser.py standalone.test:query_name=normaliser
       
Note3-Running: fab urika.setup:query=queries/normaliser.py urika.run:query_name=normaliser
       fab urika.setup:query=queries/diseases.py urika.run:query_name=diseases


Dependencies:
- PyYAML
- mpi4py

