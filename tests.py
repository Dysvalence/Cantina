from challenge import *

doc = getDocument(DOCUMENT_URL)
assert(doc is not None)

assert(len(multipleSelectorSearch("Input", doc)) == 26)
assert(len(multipleSelectorSearch("BFG9000", doc)) == 0)

#assert(len(multipleSelectorSearch("StackView.accessoryView",doc))==1) #todo: fix duplication bug
assert(len(multipleSelectorSearch(".accessoryView", doc)) == 1)
assert(len(multipleSelectorSearch(".BFG9000", doc)) == 0)
assert(len(multipleSelectorSearch(".", doc)) == 0)

assert(len(multipleSelectorSearch("CvarSelect#rate", doc)) == 1)         
assert(len(multipleSelectorSearch("CvarSelect#BFG9000", doc)) == 0)
assert(len(multipleSelectorSearch("#apply", doc)) == 1)
assert(len(multipleSelectorSearch("#BFG9000", doc)) == 0)
assert(len(multipleSelectorSearch("#", doc)) == 0)
                                  
print("ALL TESTS PASSED")
