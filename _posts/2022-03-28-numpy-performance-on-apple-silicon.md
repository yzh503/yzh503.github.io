---
layout: post
title: Numpy Performance on Apple Silicon
---

Although Apple Silicon has come out for more than a year, programming environment setup is still a hassle if you wish to avoid Rosetta 2. This post is probably the optimal setup for Apple Silicon chips up to March 2022. Please be aware that the instructions may be out of date. 

# Conda 
Install [miniforge](https://github.com/conda-forge/miniforge) with the Apple Silicon build. 

Let Conda recognise your pip packages if you wish to use pip in conda environments:  
```
conda config --set pip_interop_enabled true
```
The best practice is still to install packages via conda unless you need to build a wheel locally, such as PyTorch. 

# Numpy
We need a Numpy build with arm64 C-extensions and [vecLib](https://developer.apple.com/documentation/accelerate/veclib) (Apple's BLAS library) mounted. 

Install via Conda (recommended if in conda enviornments): 
```
conda install numpy "blas=*=*accelerate*"
```
Alternatively, build the wheel: 
```
pip install cython
pip install --no-binary :all: --no-use-pep517 numpy
```
`--no-binary :all: --no-use-pep517` options let you build the wheel from scratch. 

## Testing
```
python -c "import numpy; numpy.show_config()"
```
If successful, `show_config` should print some information this: 
```
accelerate_info:
    extra_compile_args = ['-I/System/Library/Frameworks/vecLib.framework/Headers']
    extra_link_args = ['-Wl,-framework', '-Wl,Accelerate']
    define_macros = [('NO_ATLAS_INFO', 3), ('HAVE_CBLAS', None)]
blas_opt_info:
    extra_compile_args = ['-I/System/Library/Frameworks/vecLib.framework/Headers']
    extra_link_args = ['-Wl,-framework', '-Wl,Accelerate']
    define_macros = [('NO_ATLAS_INFO', 3), ('HAVE_CBLAS', None)]
```
Test the performance,
```
import time
import numpy as np
np.random.seed(0)
a = np.random.uniform(size=(300, 300))
start = time.time()
for _ in range(100):
    a += 1
    np.linalg.svd(a)
t = time.time() - start
print(f'{t:.2f}s')
```
*Code provided by [graphitump](https://stackoverflow.com/a/70255105)*

As I tested, M1 Pro and M1 Max would finish in 1.04s on Monterey 12.2.1 with Python 3.9.10 packaged by conda-forge.


# MacOS Monterey 12.3 Performance Loss

With Monterey 12.3, Numpy performance could degrade by about 10%. In the aforementioned test, the execution time is about 1.11s, as likely the result of kernal upgrade from 21.3.0 to 21.4.0. 

If you wish to stay on Monterey 12.2.1 or below and would like to disable System Preference uprade notification red badge, use this command so it will forget once: 

```
defaults write com.apple.systempreferences AttentionPrefBundleIDs 0 && killall Dock
```

# Tensorflow 
Use Tensorflow optimised with ML Compute framework: [Tensorflow MacOS](https://developer.apple.com/metal/tensorflow-plugin/).

Note that the above instructions will reinstall Numpy in the wrong way. You need to uninstall reinstall Numpy again in the right way. 

# PyTorch
At the current stage, PyTorch official suggests that MacOS Conda binaries are for x86_64 only and use wheels for M1. Thus, we will install via pip, 

```
pip install torch torchvision torchaudio
```

# BLAS 
BLAS is a set of low level routines performing fast linear algebra operations. According to [danielchalef](https://github.com/danielchalef/openblas-benchmark-m1)'s benchmarks, vecLib significantly outperforms OpenBLAS, possibly due to hardware-based  acceleration. MKL is the intel's implementation so it's not available on Apple Silicon. 

# PyPy
Up until now there is no arm-64 build for PyPy according to [this post](https://www.pypy.org/posts/2020/12/mac-meets-arm64-940822335619099039.html). 
According to this [FAQ](https://doc.pypy.org/en/latest/faq.html#should-i-install-numpy-or-numpypy), it is not recommended to use Numpy with PyPy as the performance deteriorates with infamously slow cpyext. Moreover, the JIT friendly `numpypy` is no longer supported. 

Use Numpy vectorisation as much as possible so performance intensive snippets will run via C-extension. 

As mentioned in [this article](https://medium.com/codex/pypy-vs-python-49153daca65c) PyPy is also slower than CPython when using SQLite. However in any other cases, PyPy still has an extraodinary performance. 

