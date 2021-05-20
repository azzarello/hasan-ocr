twitch-dl download -q source $1
for video in ./*.mkv
do
	mkdir $(echo $video | cut -d '_' -f 1)
	ffmpeg -i $video -filter:v "crop=825:25:125:45,fps=5" $(echo $video | cut -d '_' -f 1)/$filename%12d.bmp
	rm $video
	tar -zcf $(echo $video | cut -d '_' -f 1).tar.gz $(echo $video | cut -d '_' -f 1)/
	rm -r $(echo $video | cut -d '_' -f 1)
done
