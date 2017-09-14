#!/bin/bash
export ADMINUSER=$1
bash os_updates.sh
bash prepare_master_nodes.sh
