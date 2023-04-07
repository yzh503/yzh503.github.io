---
layout: post
title: Use Tensorflow and PyTorch on WSL 2 
date: 2023-04-07 21:06 +1000
---

Tensorflow 2.10 has been the last version that supports CUDA on Windows, so where should the Wnidows users go with Tensorflow GPU? The answer is WSL 2. You may have heard the performance issues of WSL 2 but that would not be much of an issue for CUDA. By Apr 2023, PyTorch 2.0 (without compile) and Tensorflow 2.12 can run perfectly well on Ubuntu WSL 2 without losing much performance. Here are the installation steps: 

1. Install Conda
2. Install [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)
3. Install CUDA following the [CUDA on WSL User Guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl) 
4. Install Tensorflow following the [official guide](https://www.tensorflow.org/install/pip#windows-wsl2). Do not install `tensorflow-gpu`, which does not support WSL. 
5. (Optional) Install [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing)

DirectML is a different way of using CUDA from Windows native. By Apr 2023, DirectML has about 10-20% performance loss. Better use CUDA directly in WSL. 

If you install TensorRT via pip, update your `$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh` as follows: 

```shell
TENSORRT_PATH=$(dirname $(python -c "import tensorrt;print(tensorrt.__file__)"))
CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib:$TENSORRT_PATH
```

Test GPU: 

```shell
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

**Important Note**: In WSL reading files from Windows drives can seriously affect IO performance. I strongly suggest you move your code and data file into the WSL drive. In WSL, copy files from C drive by `cp /mnt/c/...`. 

To move WSL virtual disk to another drive, follow [this blog](https://dev.to/mefaba/installing-wsl-on-another-drive-in-windows-5c4a#:~:text=Installing%20WSL%20on%20another%20drive%20in%20Windows%201,from%20the%20wsl2%20list%20that%20we%20saw%20earlier.)

After you export and import WSL, you might need to update the default user in WSL. Follow [this link](https://askubuntu.com/questions/816732/how-to-change-default-user-in-wsl-ubuntu-bash-on-windows-10).