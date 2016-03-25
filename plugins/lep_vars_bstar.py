# Implementation of the first part of the b* treemaker.
# Originally written by Marc Osherson, ported to Treemaker plugin form by Ben Rosser

import array

from Treemaker.Treemaker import cuts

# This dictionary is filled by the config file.
parameters = {}

# The input type; defaults to Ntuple if absent.
input_type = "Ntuple"

def setup(variables, isData):
	variables['lepType'] = array.array('f', [0.0])
	variables['lepPt'] = array.array('f', [-1.0])
	variables['lepPhi'] = array.array('f', [-100.0])
	variables['lepEta'] = array.array('f', [-100.0])
	variables['lepE'] = array.array('f', [-1.0])
	variables['lepIso'] = array.array('f', [100.0])
	variables['lepTight'] = array.array('f', [-1.0])
	return variables

def analyze(event, variables, labels, isData, cutDict):
	# Define some handles.

	# This produces a KeyError sometimes?
	# Uh...
	try:
		metPtHandle = labels['metFull']['metFullPt']
	except KeyError:
		metPtHandle = labels['met']['metPt']

	muPtHandle = labels['muons']['muPt']
	elPtHandle = labels['electrons']['elPt']

	# Figure out what lepton we are (use '0' as default value).
	if metPtHandle.isValid():
		if not muPtHandle.isValid() and (elPtHandle.isValid() and len(elPtHandle.product()) > 0):
			variables['lepType'][0] = -1.0
		if not elPtHandle.isValid() and (muPtHandle.isValid() and len(muPtHandle.product()) > 0):
			variables['lepType'][0] = 1.0
		if muPtHandle.isValid() and elPtHandle.isValid():
			if len(elPtHandle.product())>0 and len(muPtHandle.product())>0 and elPtHandle.product()[0] > muPtHandle.product()[0]:
				variables['lepType'][0] = -1.0
			if len(muPtHandle.product())>0 and len(elPtHandle.product())>0 and elPtHandle.product()[0] < muPtHandle.product()[0]:
				variables['lepType'][0] = 1.0

	# Now do things.
	if variables['lepType'][0] == -1:
		variables['lepPt'][0] = elPtHandle.product()[0]
		variables['lepPhi'][0] = labels['electrons']['elPhi'].product()[0]
		variables['lepEta'][0] = labels['electrons']['elEta'].product()[0]
		variables['lepE'][0] = labels['electrons']['elE'].product()[0]
		variables['lepIso'][0] = labels['electrons']['elIso03'].product()[0]
		variables['lepTight'][0] = labels['electrons']['elisTight'].product()[0]
	elif variables['lepType'][0] == 1:
		variables['lepPt'][0] = muPtHandle.product()[0]		
		variables['lepPhi'][0] = labels['muons']['muPhi'].product()[0]
		variables['lepEta'][0] = labels['muons']['muEta'].product()[0]
		variables['lepE'][0] = labels['muons']['muE'].product()[0]
		variables['lepIso'][0] = labels['muons']['muIso04'].product()[0]
		# Why does this have a different name :|
		variables['lepTight'][0] = labels['muons']['muIsTightMuon'].product()[0]

	return variables, cutDict

def drop(event, variables, cutArray, leaves, isData):
	# Drop hadronic events.
	if variables['lepType'][0] == 0:
		return True
	return False

def createCuts(cutDict):
	return cutDict
