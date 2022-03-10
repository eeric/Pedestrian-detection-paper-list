#https://github.com/RangiLyu/nanodet
#1.path:./nanodet/trainer/
#file:trainer.py  dist_trainer.py
#2.model arch
#path:./nanodet/model/arch
#file:__init__.py  gfl.py
#3.need to modify input size of model
#path:./nanodet/data/dataset/
#file: coco.py
#4.FGD
#Focal and Global Knowledge Distillation for Detectors
#https://github.com/yzd-v/FGD
#https://github.com/yzd-v/FGD/blob/master/mmdet/distillation/losses/fgd.py
