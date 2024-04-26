#!/bin/bash
#program will monitor cpu speed (ghz)

#watch grep \"cpu MHz\" /proc/cpuinfo
watch cat /sys/devices/system/cpu/cpu[0-9]*/cpufreq/scaling_cur_freq
