#!/bin/bash
rm -rf ./root_folder
mkdir root_folder
for i in {1..5}
do
	mkdir ./root_folder/folder_$i
	for j in {1..3}
	do
		touch ./root_folder/folder_$i/file_$j
	done
	for k in {1..2}
	do
		touch ./root_folder/root_file_$k
	done
done

