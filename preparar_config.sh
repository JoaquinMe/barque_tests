marker=$1

git clone https://github.com/JoaquinMe/barque "$marker"/barque
cp "$marker"/barque/14_tests/"$marker"/"$marker"_barque_config.sh "$marker"/barque/02_info/barque_config.sh
cp "$marker"/barque/14_tests/"$marker"/"$marker"_primers.csv "$marker"/barque/02_info/primers.csv
