#!/bin/bash
set -x

function main {

  init_params "$@"
  run_benchmark

}

# init params
function init_params {

  for var in "$@"
  do
    case $var in
      --input_model=*)
          input_model=$(echo $var |cut -f2 -d=)
      ;;
      --mode=*)
          mode=$(echo $var |cut -f2 -d=)
      ;;
      --dataset_location=*)
          dataset_location=$(echo $var |cut -f2 -d=)
      ;;
    esac
  done

}

# run_benchmark
function run_benchmark {

    python main.py \
            --model_path ${input_model} \
            --mode=${mode} \
            --data_path ${dataset_location} \
            --benchmark
            
}

main "$@"

