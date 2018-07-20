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

---

## UCL users

### Beware: epcc-master branch

The `epcc-master` branch has not been tested on UCL systems. 

---

## Urika users

### Set up Python environment

Create `py27` environment:

```bash
module load anaconda3/4.1.1
conda create -n py27 python=2.7 anaconda

Proceed ([y]/n)? y
```

Activate environment:

```bash
source activate py27
```

Show active environment:

```bash
conda env list
```
```
# conda environments:
#
py27                  *  /home/users/<your-urika-username>/.conda/envs/py27
root                     /opt/cray/anaconda3/4.1.1
```

Install dependencies:

```bash
cd cluster-code
conda install -c anaconda --file requirements.txt
```

**Note**:  After creating the `py27` environment, for your subsequent Urika sessions you just need to type:

```bash
module load anaconda3/4.1.1
source activate py27
```

### Load additional modules

Load `mrun` module:

```bash
module load mrun
```

### Mount data using SSHFS

```bash
mkdir blpaper
sshfs -o intr,large_read,auto_cache,workaround=all -oPort=22222 <your-urika-username>@chss.datastore.ed.ac.uk:<path-in-uoe-datastore> dch
```

Create data directory on Lustre file system:

```bash
mkdir -p /mnt/lustre/<your-urika-username>/dch
```

Copy the complete data set to Lustre, by running in your home directory:

```bash
source deploy/bl_copy.sh ~/dch/BritishLibraryBooks/ /mnt/lustre/<your-urika-username>/dch/BritishLibraryBooks
```

**Important note:**

* Do **not** mount the DataStore directory directly onto Lustre. Urika compute nodes have no network access and so can't access DataStore via the mount. Also, for efficient processing, data movement needs to be minimised. Copy the data into Lustre as above.

### How data is processed

Data is processed as a background task using a combination of Mesos job submission to the compute nodes, and execution of MPI-enabled Python code on the compute nodes.

After you have set a query running, you can check if the processing has completed, by checking the running processes:

```bash
ps
```

If processing is still ongoing, this will show the following running processes:

```bash
   PID TTY          TIME CMD
...
105805 pts/2    00:00:00 urika.sh
105810 pts/2    00:00:00 mrun
105811 pts/2    00:00:00 mrun.py
...
```

### Update execution script to query a subset of books

Change `urika.sh` to only query all books in `1510_1699/`:

* Change:

```bash
for i in $remote_directory/*; do
```

* to:

```bash
for i in $remote_directory/1510*; do
```

## Run total books query

Run:

```bash
fab urika.setup:query=queries/total_books.py urika.run:query_name=total_books
```

When processing is complete, check the results:

```bash
cat production/bluclobber/harness/output_total_books/out_1510_1699_0.yml
```

You should get thje result `books` with value:

```bash
693
...
```

## Run total pages query

Run:

```bash
fab urika.setup:query=queries/total_pages.py urika.run:query_name=total_pages
```

When processing is complete, check the results:

```bash
cat production/bluclobber/harness/output_total_pages/out_1510_1699_0.yml
```

You should get the result `[books, pages]` with value:

```bash
[693, 62768]
```

## Run total words query

Run:

```bash
fab urika.setup:query=queries/total_words.py urika.run:query_name=total_words
```

When processing is complete, check the results:

```bash
cat production/bluclobber/harness/output_total_words/out_1510_1699_0.yml
```

You should get the result `[books, words]` with value:

```bash
[693, 17479341]
```

### Update execution script to query all books

Change `urika.sh` to only query all books:

* Change:

```bash
for i in $remote_directory/1510*; do
```

* to:

```bash
for i in $remote_directory/*; do
```

### Run total books, pages, words queries across all books

Run:

```bash
fab urika.setup:query=queries/<QUERY-NAME>.py urika.run:query_name=<QUERY-NAME>

where `<QUERY-NAME>` is one of `total_books`, `total_pages` or `total_words`. 

When processing is complete, there will be one data file in `production/bluclobber/harness/output_<QUERY-NAME>/` per period (e.g. for 1510-1699, etc). You can combine these into a single results file as follows:

```
python bluclobber/tools/<JOINER>.py production/bluclobber/harness/output_<QUERY-NAME>/ <QUERY-NAME>.txt.
```

For `total_books`, use `join_values.py` for `<JOINER>`.

For `total_pages` and `total_words`, use `join_lists.py` for `<JOINER>`.

The results should be as follows:

* `total_books.txt`: `63701`
* `total_pages.txt`: `[63701, 22044324]`
* `total_words.txt`: `[63701, 6866559285]`

### Run normaliser query

Run:

```bash
fab urika.setup:query=queries/normaliser.py urika.run:query_name=normaliser
```

When processing has completed, copy `data_normaliser/normaliser.yml`, and other outputs, before running another query:

```bash
mkdir ~/cluster-code-results
cp -r production/bluclobber/harness/data_normaliser/ ~/cluster-code-results/
cp -r production/bluclobber/harness/output_normaliser/ ~/cluster-code-results/
```

These file are needed for visualising results. `production/` will be deleted and recreated when running subsequent queries.

### Run diseases query

This is done in the same way as for a normaliser query above, only the commands and result file names differ.

Run:

```bash
fab urika.setup:query=queries/normaliser.py urika.run:query_name=diseases
```

When processing has completed, copy `data_diseases/*.yml`, and other outputs, before running another query:

```bash
cp -r production/bluclobber/harness/data_diseases/ ~/cluster-code-results/
cp -r production/bluclobber/harness/output_diseases/ ~/cluster-code-results/
```

These file are needed for visualising results. `production/` will be deleted and recreated when running subsequent queries.

### Check query results

To do a very quick and dirty check of the normaliser query results, run:

```bash
wc production/bluclobber/harness/data_normaliser/normaliser.yml
```

You should see:

```bash
287 1148 7780 production/bluclobber/harness/data_normaliser/normaliser.yml
```

To do a very quick and dirty check of the disease query results, run:

```bash
wc production/bluclobber/harness/data_diseases/*.yml
```

You should see:

```bash
   18   295  1497 production/bluclobber/harness/data_diseases/cancer.yml
   12   191  1036 production/bluclobber/harness/data_diseases/cholera.yml
   21   341  1804 production/bluclobber/harness/data_diseases/consumption.yml
    3    55   261 production/bluclobber/harness/data_diseases/diarrhoea.yml
    5    87   438 production/bluclobber/harness/data_diseases/diphtheria.yml
    6   103   480 production/bluclobber/harness/data_diseases/dysentry.yml
   13   211  1080 production/bluclobber/harness/data_diseases/measles.yml
  287  1148  7780 production/bluclobber/harness/data_diseases/normaliser.yml
   11   191   940 production/bluclobber/harness/data_diseases/phthisis.yml
   19   305  1582 production/bluclobber/harness/data_diseases/smallpox.yml
    5    79   381 production/bluclobber/harness/data_diseases/tuberculosis.yml
    9   151   767 production/bluclobber/harness/data_diseases/typhoid.yml
   13   207  1067 production/bluclobber/harness/data_diseases/typhus.yml
   13   223  1095 production/bluclobber/harness/data_diseases/whooping.yml
```

Query result data files with the expected results data can be found in the [epcc-master](https://github.com/alan-turing-institute/cluster-code-visualisations/tree/epcc-master) branch of [alan-turing-institute/cluster-code-visualisations](https://github.com/alan-turing-institute/cluster-code-visualisations) in the [diseases/data](https://github.com/alan-turing-institute/cluster-code-visualisations/tree/epcc-master/diseases/data) directory.

### Visualising query results

To visualise the query results, see the [epcc-master](https://github.com/alan-turing-institute/cluster-code-visualisations/tree/epcc-master) branch of [alan-turing-institute/cluster-code-visualisations](https://github.com/alan-turing-institute/cluster-code-visualisations).

### Number of processes

By default, 16 processes are used by MPI, as specified in `urika.sh`.


```
NP='2'
```

The number of processes must be <= the number of ZIP files. If not then the following exception will appear in the `production/bluclobber/harness/output_submission` log file:

```
0/16 INFO: 2018-07-18 17:20:08,146 Mapped
Traceback (most recent call last):
  File "query.py", line 70, in <module>
8/16 INFO: 2018-07-18 17:20:08,146 Analysing by archive
  File "query.py", line 57, in query
    local_result=reduce(self.reducer, quantities)
TypeError:     result = corpus.analyse(mapper, reducer, downsample, byboo
k, shuffler=shuffler)
  File "../model/corpus.py", line 41, in analyse
  File "../model/corpus.py", line 41, in analyse
    main()
  File "query.py", line 30, in main
```

### Notes

`bluclubber/harness/join_normaliser.py` merges the results from each process (held in `production/bluclobber/harness/output_normaliser`) into a `joined_normaliser.yml` file in the same directory. However, this is a simple script that can result in duplicated keys in the joined files. For example:

```bash
grep 1735 production/bluclobber/harness/output_normaliser/joined_normaliser.yml
```
```
1735: [12, 1226, 347355]
1735: [1, 330, 87592]
```
```
grep 1735 production/bluclobber/harness/data_normaliser/normaliser.yml
```
```
1735:  [13, 1556, 434947]
```

`bluclobber/harness/result_normaliser.py` processes `joined_normaliser.yml` into a single file with one key per year. It handles any duplicated keys in `joined_normaliser.yml` by summing the values of the duplicates.

`bluclubber/harness/join_diseases.py` merges the results from each process (held in `production/bluclobber/harness/output_diseases`) into a collection of files `joined_YYYY_YYYY.yml (e.g. `joined_1510_1699.yml`) for each set of years, in the same directory. However, as for `join_normaliser` this is a simple script and can also result in duplicated keys in the joined files.

`bluclobber/harness/result_diseases.py` creates a single file for each type of disease, with one key per year. It handles duplicated keys by summing the values of the duplicates.
