## Bioinformatics scripts

A collection of light bioinformatics analysis pipelines for specific tasks.

### *Python*
---
- Print feature sequences given GFF file and FASTA file (e.g. extracting CDS sequences) - **gff_loader.py**
- Converting GenBank/EMBL to GFF (for QUAST) - **gb_embl2gff.py**
- Converting JCVI ##.simple file to Circos ##.links file - **simple2links.py**
- Filtering subsequences according to seq length - **fasta_len_filter.py**
- Sequencing data alignment results statistics - **alignment_stats.py**
- SNP annotation - **snp_annotate.py**
- 4DTV atx to one-line - **atx2oneline.py**
- use snpEff to annoate VCF file and ka/ks calculation - **snpEff_kaks_calculator.py**
- Codon table calculation 密码子优化, 计算密码子频率 - **codon_freq.py**
- Extract introns sequence and GFF file - **extract_intron_gff3_from_gff3.py**

###  *Perl*
---
- Calculate 4DTV 可用于构建 SNP 进化树 - **caculate_4DTV_correction.pl**


### *Shell*
---
- Extracting subset from GFF file according to ids - **extract_sub_gff.sh**
- Split bam to NFR (nucleosome free region) in ATAC-seq analysis - **splitBam.sh**
- Split bam to sense and antisense strand for strand-specific RNA-seq - **splitSense.sh**

Dive into specific folder to view more detailed usage on each script's function.

### Code source
---
|Authors| GitHub| 
|---|---|
|*[tanghaibao](https://github.com/tanghaibao)*| **[bio-pipeline](https://github.com/tanghaibao/bio-pipeline)**|
|*[jorvis](https://github.com/jorvis)*| **[biocode](https://github.com/biogeeker/biocode)**|
|*[mscook](https://github.com/mscook)*| **[to-gff](https://github.com/mscook/to-gff)**|
|*[xuzhougeng](https://github.com/xuzhougeng)*| **[myscripts](https://github.com/xuzhougeng/myscripts)**|
|*[JinfengChen / Scripts](https://github.com/JinfengChen/Scripts)*| **[Scripts](https://github.com/JinfengChen/Scripts/tree/master/FFgenome/03.evolution/distance_kaks_4dtv/bin)**|
|*scbgfengchao / 4DTv*| **[scbgfengchao / 4DTv](https://github.com/scbgfengchao/4DTv/blob/master/axt2one-line.py)**|
|*MerrimanLab/selectionTools*|**selectionTools/extrascripts/kaks.py/**|
