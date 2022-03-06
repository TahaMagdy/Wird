for file in $(ls *tex)
do
    xelatex $file

done
