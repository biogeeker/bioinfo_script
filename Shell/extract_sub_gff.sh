echo "Command format: extract_sub_gff.sh read_id.txt input_file.gff output_flie.gff"
  
cat $1 | while read id; do read_id=`echo $id | cut -d "^" -f1`; grep -w $read_id $2 >> $3; done

echo "Extract Done!"
