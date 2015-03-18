#!/bin/bash

# change this to be right for your own setup
PYTHON_DIR=/home/pvh/Documents/python

BIN_DIR=$PYTHON_DIR/bin
LIB_DIR=$PYTHON_DIR/lib

if [ "$LOGNAME" != "pvh" -a "$PYTHON_DIR" == "/home/pvh/Documents/python" ] ; then
  echo "Please change the PYTHON_DIR variable setting so that it is correct for your own setup" >&2
else
  if [[ ":$PATH:" != *":$BIN_DIR:"* ]] ; then
    PATH=$PATH:$BIN_DIR
    export PATH
  fi

  if [ -z "$PYTHONPATH" ] ; then
    PYTHONPATH=$LIB_DIR
  elif [[ ":$PYTHONPATH:" != *":$LIB_DIR:"* ]] ; then
    PYTHONPATH=$PYTHONPATH:$LIB_DIR
  fi
  export PYTHONPATH
fi
