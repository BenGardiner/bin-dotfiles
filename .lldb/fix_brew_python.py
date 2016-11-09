import sys
sys.path = [p for p in sys.path if 'Cellar' not in p]

new_path = ['/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
'/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
'/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
'/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
'/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
'/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python',
'/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
'/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
'/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload']

for p in new_path:
    if p not in sys.path:
        sys.path.append(p)