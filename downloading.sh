cd /usr/share/tiles/16
export count=0

export total=1290
for y in {26954..26958}; do
  mkdir $y
	for x in {45329..47331}; do
	wget https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/16/$y/$x -O /usr/share/tiles/16/$y/$x &
	sleep 0.08
		count=$((count + 1))
		echo "\n $y/$x.png    --------------- $count/$total\n"
	done
done

