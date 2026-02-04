cd /usr/share/tiles/16
export count=0

export total=3990
for y in {27141..27350}; do
  mkdir $y
	for x in {46177..46195}; do
	wget https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/16/$y/$x -O /usr/share/tiles/16/$y/$x &
	sleep 0.08
		count=$((count + 1))
		echo "\n $y/$x.png    --------------- $count/$total\n"
	done
done

