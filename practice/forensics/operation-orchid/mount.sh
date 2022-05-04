#!/bin/sh

sudo losetup -o 210763776 /dev/loop0 disk.img
sudo fsck -fv /dev/loop0
sudo mount /dev/loop0 /mnt
