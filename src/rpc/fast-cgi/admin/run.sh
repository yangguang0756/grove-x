#!/bin/bash
killall -QUIT admin_module
killall -QUIT nginx
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

mkdir -p /data/deploy/etc/fast-cgi/html/
mkdir -p /data/deploy/logs/
mkdir -p /data/deploy/tools/fast-cgi/

cp ../../../depends/bin/admin_module /data/deploy/etc/fast-cgi/admin_module
cp ./html/*.html /data/deploy/etc/fast-cgi/html/

cp ./nginx.conf /usr/local/nginx/conf/
/usr/local/nginx/sbin/nginx
../../../depends/bin/spawn-fcgi -a 127.0.0.1 -p 17001 -F 2 -f /data/deploy/etc/fast-cgi/admin_module


