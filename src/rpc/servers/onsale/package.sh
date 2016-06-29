#!/bin/bash

tmp_dir=onsale_`date +%Y%m%d_%H%M`

mkdir -p ./${tmp_dir}/

cp ../../../rpc/config/daemon/onsale_store_server.json	./${tmp_dir}/

cp ../../../depends/bin/onsale_* 			            ./${tmp_dir}/

md5sum ./${tmp_dir}/* > ./${tmp_dir}/checklist.txt
tar -czvf  ${tmp_dir}.tar.gz                            ./${tmp_dir}/
rm -rf ./${tmp_dir}/
