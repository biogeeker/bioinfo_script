# Gene annotation file
GENE_ANNOT_FILE='FM4_synt_02.gtf'

# Extract genes
awk '$3 == "gene"' $GENE_ANNOT_FILE > genes_temp.gtf

# Use BEDops convert2bed
# convert2bed won't work if the "transcript_id" field is not there. This makes an empty "transcript_id" field so convert2bed is happy.
awk '{ if ($0 ~ "transcript_id") print $0; else print $0" transcript_id \"\";"; }' genes_temp.gtf > genes.gtf

#Extract exons (exons always have transcript_id field, no need to repeat above)
awk '$3 == "exon"' $GENE_ANNOT_FILE > exons.gtf

#Convert both to bed format so we can use bedtools
convert2bed -i gtf < exons.gtf > exons.bed
convert2bed -i gtf < genes.gtf > genes.bed

# Remove exons from the genes.bed file, enforce strand specificy (-s)
bedtools subtract -a genes.bed -b exons.bed -s > introns.bed

# Convert intron bed file to GTF file
awk '{print $1"\t"$7"\t""intron""\t"($2+1)"\t"$3"\t"$5"\t"$6"\t"$9"\t"(substr($0, index($0,$10)))}' introns.bed > introns.gtf

# combine with original annotations file
#cat gencode.v27.annotation.gtf inferred_introns.gtf > gencode.v27.w.introns.gtf

# remove generated temporary files
#rm genes.gtf exons.gtf exons.bed genes.bed introns.bed
