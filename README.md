# siam_ms
install and setup pysot

add yolo5x6 under tools

download model.pth and dataset + json under experiments like the original pysot, but directory name pysot-mot

you might have to add color folder by add_color.py, change the paths

for demo:

export PYTHONPATH=/path/to/pysot-mot:$PYTHONPATH

cd pysot-mot

similar to pysot
python tools/demo_mot.py --config /home/atur/pysot-mot/experiments/siamrpn_r50_l234_dwxcorr/config.yaml --snapshot /home/atur/pysot-mot/experiments/siamrpn_r50_l234_dwxcorr/model.pth --video /home/atur/videos/basketball.avi




