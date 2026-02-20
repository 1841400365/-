#!/bin/bash

# 该指令表示任意指令执行失败，立即终止脚本
set -e

echo -e "\n=== 构建 build目录 ==="
cmake -B output

pushd output
make -j$(nproc)

if [ -f main ]; then
	echo -e "\n===== 编译成功 ====="
	#这里可以改成scp传输到我们的板卡上
	scp -O main root@192.168.0.16:/home/root/workspace
fi
popd
