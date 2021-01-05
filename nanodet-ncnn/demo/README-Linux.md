## Linux

### Step1.
Build and install OpenCV from https://github.com/opencv/opencv

### Step2(Optional).
Download Vulkan SDK from https://vulkan.lunarg.com/sdk/home

### Step3.
Clone NCNN repository

``` shell script
git clone --recursive https://github.com/Tencent/ncnn.git 
```

Build NCNN following this tutorial: [Build for Linux / NVIDIA Jetson / Raspberry Pi](https://github.com/Tencent/ncnn/wiki/how-to-build#build-for-linux)

### Step4.

Set environment variables. Run:

``` shell script
export ncnn_DIR=YOUR_NCNN_PATH/build/install/lib/cmake/ncnn
```

Build project

``` shell script
cd <this-folder>
mkdir build
cd build
cmake ..
make
```

# Run demo

Download NanoDet ncnn model.
* [NanoDet ncnn model download link](https://github.com/RangiLyu/nanodet/releases/download/v0.0.1/nanodet_ncnn_model.zip)

Copy nanodet_m.param and nanodet_m.bin to demo program folder.

## Webcam

```shell script
nanodet_demo 0 0
```

## Inference images

```shell script
nanodet_demo 1 IMAGE_FOLDER/*.jpg
```

## Inference video

```shell script
nanodet_demo 2 VIDEO_PATH
```

## Benchmark

```shell script
nanodet_demo 3 0
```
![bench_mark](benchmark.jpg)
****

Notice:

If benchmark speed is slow, try to limit omp thread num.

Linux:

```shell script
export OMP_THREAD_LIMIT=4
