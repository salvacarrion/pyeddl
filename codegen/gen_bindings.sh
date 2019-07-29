#!/bin/bash

set -e

this="${BASH_SOURCE:-$0}"
this_dir=$(cd -P -- "$(dirname -- "${this}")" && pwd -P)

# this refers to the crs4/binder docker container
binder=${BINDER_EXE:-/binder/build/llvm-4.0.0/build_4.0.0*/bin/binder}

eddl_inc=${EDDL_INCLUDE:-"${this_dir}"/../third_party/eddl/src}
eigen_inc=${EIGEN_INCLUDE:-"${this_dir}"/../third_party/eddl/third_party/eigen}

rm -rf ./bindings/ && mkdir bindings/
${binder} \
  --root-module _core \
  --prefix $PWD/bindings/ \
  --bind "" \
  --config config.cfg \
  --single-file \
  all_bash_includes.hpp \
  -- -std=c++11 \
  -I"${eddl_inc}" \
  -I"${eigen_inc}" \
  -DNDEBUG

# Fix for pybind11 ImportError
# "overloading a method with both static and instance methods is not supported"
sed -i 's/def("sum"/def("sum_unary"/' bindings/_core.cpp

# add buffer_protocol annotation
sed -i -f add_annotation.sed bindings/_core.cpp
