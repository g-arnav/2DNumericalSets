# 2DNumericalSets
Provides python classes to build a tree containing all the 2D numerical semigroups up to a given genus.

## Usage
The following code fragment gives an overview of how to use the `NumericalSemigroup` class from within Sage, and more complete documentation will be added in the near future.

	load('/PATH_TO_FILE/NumericalSemigroup.sage')
	McNuggets = NumericalSemigroup([6,9,20])
	print McNuggets.FrobeniusNumber()
	print McNuggets.LengthSet(400)
	print McNuggets.DeltaSet(400)
	print McNuggets.OmegaPrimality(400)
	print McNuggets.CatenaryDegree(400)
