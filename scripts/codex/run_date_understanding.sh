#!/bin/bash
set -x

# Specify your EXEHOME first. EXEHOME=/home/user-name/Model-Selection-Reasoning/src
cd ${EXEHOME}

# Specify your API key
APIKEY=''

python selection_date_codex.py --start 0 \
        --end -1 \
        --cot_temperature 0. \
        --pal_temperature 0. \
        --output_dir '../output/' \
        --key ${APIKEY}
