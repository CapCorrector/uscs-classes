#!/bin/bash
#Getting list ov volumes and deparsing df's output into variable
getvolinfo () {
	volumes=(`df -k | grep dev/ | awk '{print $1 "," $2 "," $4}'`)
	echo ${volumes[@]}
	volnum=${#volumes[@]}
	echo "We have $volnum volumes (including disk images):"
	echo "FS		Size		Free"
	for vol in "${volumes[@]}"
	do
		awk -v avol="$vol" 'BEGIN{split(avol,list,","); print list[1],"	",list[2]*1024,"	",list[3]*1024}'
	done
}

#Getting CPU info
getcpuinfo () {
	cpucount=`system_profiler SPHardwareDataType | grep "Number of Processors:" | awk '{print $4}'`
	cpudesc=`sysctl -n machdep.cpu.brand_string`
	corecount=`sysctl -n hw.physicalcpu`
	echo "We have $cpucount processor(s) and $corecount cores in sum."
	echo "Cpu model is $cpudesc"
}

#Getting RAM info
getraminfo () {
memgb=$(($(sysctl hw.memsize | awk '{print $2}')/1024/1024/1024))
echo "We have $memgb GB of RAM"
}

# Getting HW interfaces info
getifinfo () {
	i=1
	hwnetlist=`networksetup -listallhardwareports`
	iflist=(`echo $hwnetlist | awk '{for(i=1; i<=NF; i++) if($i~/Device/) print $(i+1)}'`)
	echo "Getting list of interfaces and their ip addresses in forman interface name \n mac-address \n ip-address"
	for if in "${iflist[@]}"
	do
		echo $if
		ifconfig $if | grep -E 'ether|inet' | awk '{print $2}'
	done
}

for param in "$@"
do
	case $param in
		-all)
		getvolinfo
		getcpuinfo
		getraminfo
		getifinfo
		;;
		-volumes)
		getvolinfo
		;;
		-cpu)
		getcpuinfo
		;;
		-ram)
		getraminfo
		;;
		-network)
		getifinfo
		;;
		*)
		echo $"Usage: $0 {-volumes|-cpu|-ram|-network|-all}"
		exit 1
	esac
done
if [[ $# -eq 0 ]] ; then
	echo $"Usage: $0 {-volumes|-cpu|-ram|-network|-all}"
	exit 1
fi
