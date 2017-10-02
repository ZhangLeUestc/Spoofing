#!/usr/bin/env bash


LOG_FILE=Logs/train_val_spoofing.log



echo "logging to ${LOG_FILE}"

TOOLS=/home/m2a01/Work/caffe/build/tools

$TOOLS/caffe train --solver=ProtoFiles/solver.prototxt  -weights=VGG_ILSVRC_16_layers.caffemodel 2>&1 | tee ${LOG_FILE}


