# Bioinformatics scripts

A collection of light bioinformatics analysis pipelines for specific tasks.
- Print feature sequences given GFF file and FASTA file (e.g. extracting CDS sequences)
- Synonymous calculation
- Codon table calculation
- Extract introns sequence and GFF file
- Given gene ids, extract subsets from GFF file

Dive into specific folder to view more detailed usage on each application.

# Source
|Authors |GitHub| 
|---|---|
|Haibao Tang (tanghaibao)| **[bio-pipeline](https://github.com/tanghaibao/bio-pipeline)**|
|隐藏层数量   |依具体问题而定，一般1到5层   |
|每个隐藏层神经元数量   |依具体问题而定，一般10到100个    |
|输出神经元  |依输出维度而定，每个预测维度1个输出   |
|隐藏层激活函数  |ReLU (或 SELU, 见11章)  |
|输出层激活函数  |不加, 或 ReLU/softplus 正输出) 或 logistic/tanh (有界输出)  |
|损失函数  |MSE 或 MAE/Huber (如果存在离群值) |
