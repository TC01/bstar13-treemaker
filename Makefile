.PHONY: all plugins

TREEMAKER=cd working && treemaker -fl
TREEMAKER_CONDOR=cd working && treemaker-condor -fr

all:    clean plugins config run
run:    bstar

clean:
	rm -rf working/
	rm -rf configs/*

plugins:
	cp -rv plugins/* ${CMSSW_BASE}/src/Treemaker/Treemaker/python/plugins/

config:
	# bstar
	treemaker-config -t tree -p bstar.list -n Bstar13Tev_1200_25ns -o Bstar13TeV_1200_25ns das://prod/phys03:/Bstar13TeV_1200_25ns/lcorcodi-BStar13TeV_B2GAnaFW_M1200-fe7510ccfc25ce06cca570ad43d5872d/USER

	mv *.cfg configs/

bstar:
	mkdir -p working
	$(TREEMAKER) ../configs/Bstar13TeV_1200_25ns.cfg
