#!/bin/bash
strings -n 1 -s "" network-dump.flag.pcap | sed "s/ //g" | grep -oE "picoCTF\{.*\}"
