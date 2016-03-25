# bstar13-treemaker

This is the collection of [Treemaker](https://github.com/TC01/Treemaker) plugins,
configs, and scripts, for a CMS B2G ```b* -> tW``` semileptonic analysis.

## Usage

After setting up the CMS framework (and running ```cmsenv```), run the following commands:

```
cd $CMSSW_BASE/src
git clone https://github.com/TC01/Treemaker.git
git clone https://github.com/TC01/bstar13-treemaker.git
scram build
cd bstar13-treemaker/
make plugins configs
```

That should be it. Then to make a collection of samples (read the Makefile to see
what I mean by that), you can do e.g. ```make bstar``` or ```make singletop``` or
```make data```. Alternatively, just running ```make``` will schedule all the jobs
to run.

## Documentation

If you're writing a new plugin, land it in the ```plugins/``` directory. The Makefile
automatically copies plugins here into the right place when running. Then edit bstar.list
and add your plugin to the list.

To add a new sample, edit the Makefile. Under the ```config``` section add a new
line for each sample you want to generate Treemaker configuration for. The following
form should work, as an example:

```
treemaker-config -t tree -p bstar.list --param weight=$WEIGHT -n Bstar13Tev_1200_25ns -o Bstar13TeV_1200_25ns das://prod/phys03:/Bstar13TeV_1200_25ns/lcorcodi-BStar13TeV_B2GAnaFW_M1200-fe7510ccfc25ce06cca570ad43d5872d/USER
```

```$WEIGHT``` is the intended "weight" of the sample. If you don't know it, omit the
```param weight=``` option and weight will default to 1. ```bstar.list``` is the list of
analysis plugins to actually use (without the ".py" suffix).

```-n Bstar13Tev_1200_25ns``` is the name of the output ROOT file that will be created
when ran.

```-o Bstar13Tev_1200_25ns``` is the name of the output *configuration* file that will
be created. This can be omitted; it should default to either the name of the parent directory
(if not running in DAS query mode) or the first part of the dataset name.

If the sample is data, add a ```-d``` to the end.

For (a lot) more documentation on Treemaker, consult the Treemaker github repository
and github wiki.

