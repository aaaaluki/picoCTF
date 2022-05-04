#!/bin/sh

sudo losetup -o 184549376 /dev/loop0 disk_flag.img
sudo fsck -fv /dev/loop0
sudo mount /dev/loop0 /mnt
