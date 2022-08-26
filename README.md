# siam_multiple single object tracker
install and setup pysot

add yolo5x6 under tools

download model.pth and dataset + json under experiments like the original pysot, but directory name pysot-mot

you might have to add color folder by add_color.py, change the paths


for demo:

export PYTHONPATH=/path/to/pysot-mot:$PYTHONPATH

cd pysot-mot

similar to pysot

python tools/demo_mot.py --config /home/atur/pysot-mot/experiments/siamrpn_r50_l234_dwxcorr/config.yaml --snapshot /home/atur/pysot-mot/experiments/siamrpn_r50_l234_dwxcorr/model.pth --video /home/atur/videos/basketball.avi

It is still not stable enough, but this is the point I came to during the internship.

# siamtracker automatic

use pysot.zip + same with pysot -e.g. install the model- + install yolo5x6 under tools for automatic demo.

demo:

export PYTHONPATH=/path/to/pysot:$PYTHONPATH

python tools/demo_yolov5.py --config experiments/siamrpn_r50_l234_dwxcorr/config.yaml --snapshot experiments/siamrpn_r50_l234_dwxcorr/model.pth --video demo/bag.avi

# siam gradio

python ./pysot/tools/demo_gradio.py

this shows a black screen for the output because of the codecs. If you have the proper ones might work.

# pytracking

for comparisons sake, download tomp50.pth under networks.

demo:
conda activate pytrack

cd pytracking/pytracking

python run_video.py tomp tomp50 /home/atur/cheetah.mp4

test change the myexperiments and functions inside for your purpose check pytracking for more info:

python run_experiment.py myexperiments uav_test

use pysot-toolkit for evaluation since pytracking does not support vot2018 otherwise use as said in pytracking.
