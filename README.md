# siam_ms
install and setup pysot

add yolo5x6 under tools

download model.pth and dataset + json under experiments like the original pysot

you might have to add color folder changing add_color.py

change address

export PYTHONPATH=/home/atur/pysot-mot:$PYTHONPATHot

cd pysot-mot

python tools/demo_mot.py --config /home/atur/pysot-mot/experiments/siamrpn_r50_l234_dwxcorr/config.yaml --snapshot /home/atur/pysot-mot/experiments/siamrpn_r50_l234_dwxcorr/model.pth --video /home/atur/videos/basketball.avi
