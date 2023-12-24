success = False

try:
    import numpy
    import pandas
    import matplotlib.pyplot
    import sklearn
    import scipy
    import jupyter

    success = True

except Exception as e:
    print(e)
finally:
    print(f"Installation was{'' if success else ' not'} successful!")
