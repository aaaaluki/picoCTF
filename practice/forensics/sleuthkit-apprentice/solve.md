# Sleuthkit Apprentice

We are given the following file:
```sh
$ file disk_flag.img
disk_flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0xc,223,19), startsector 2048, 204800 sectors; partition 2 : ID=0x82, start-CHS (0xc,223,20), end-CHS (0x16,111,25), startsector 206848, 153600 sectors; partition 3 : ID=0x83, start-CHS (0x16,111,26), end-CHS (0x26,62,24), startsector 360448, 253952 sectors
```

It has the following partitions:
```
$ fdisk -lu disk_flag.img
Disk disk_flag.img: 300 MiB, 314572800 bytes, 614400 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x7389e82d

Device         Boot  Start    End Sectors  Size Id Type
disk_flag.img1 *      2048 206847  204800  100M 83 Linux
disk_flag.img2      206848 360447  153600   75M 82 Linux swap / Solaris
disk_flag.img3      360448 614399  253952  124M 83 Linux
```

And each partition has the following file system type:
```
$ sudo parted -m disk_flag.img print
BYT;
/home/luki/CTF/picoCTF/practice/forensics/sleuthkit-apprentice/disk_flag.img:315MB:file:512:512:msdos::;
1:1049kB:106MB:105MB:ext4::boot;
2:106MB:185MB:78.6MB:linux-swap(v1)::;
3:185MB:315MB:130MB:ext4::;
```

Let's just mount the 3rd partition:
```bash
sudo losetup -o 184549376 /dev/loop0 disk_flag.img
sudo fsck -fv /dev/loop0
sudo mount /dev/loop0 /mnt
```
Note:
The `-o` option in `losetup` is the offset, which is (start\*sectorSize): `360448*512 = 184549376`

The flag is found on the root directory `/mnt/root/my_folder/flag.uni.txt`

<details>
    <summary>SPOILER! (Flag)</summary>

	picoCTF{by73_5urf3r_42028120}

</details>

Finally unmount the partition:
```bash
sudo umount /mnt
sudo losetup -d /dev/loop0
```

# Resources
- [Mounting single partition](https://askubuntu.com/a/69447)
- [Check disk image file system type](https://unix.stackexchange.com/a/438308)
