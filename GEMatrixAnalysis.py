"""
Gene Expression Matrix Analysis :

Analyzing how genes behave across multiple samples.This focuses on preparing gene expression data for downstream analysis 
(e.g., differential expression, ML models).

OBJECTIVE - Normalize expression data, Remove uninformative genes, Identify biologically relevant genes.

It helps to :
        -Identify important genes.
        -Remove noise/uninformative genes.

Prepare data for:
        -Machine Learning,
        -Biomarker discovery,
        -Drug target identification.

This step is used in:
        -Cancer biomarker discovery,
        -Disease vs control comparison,
        -Drug response studies.
Example:
        -Finding genes highly expressed in Parkinson’s disease vs control.

-------------------------------------USES------------------------------------------
Biomarker Discovery
   - What it means   
       Finding genes that indicate:
            Disease presence
            Disease progression
    - Example
            Overexpression of specific genes in cancer
            Parkinson’s disease markers.
    - Uses : Early diagnosis Prognosis prediction.
            
Differential Expression Analysis
     - What it means
           Compare: Control vs Disease.
           Output: Upregulated genes, Downregulated genes.
     - Use:
           Identify disease-causing genes Understand molecular mechanisms.
           
Drug Target Identification
      - What it means
            Find genes/proteins that can be targeted by drugs
      - Example : Highly expressed disease genes → potential targets
      - Uses : Drug discovery, Precision medicine

  Real-world usage
       You will use this file for:  
             Pathway analysis 
             Enrichment analysis
---------------------------------------------------------------------------------------
TYPE OF DATA REQUIRED ;
You need a gene expression matrix:
Feature	    Description
Rows     -  Genes (e.g., TP53, BRCA1).
Columns  -  Samples (Control / Disease).
Values   -  Expression levels.

How to download :
          -Go to GEO website -> Search:GSE54536(PD) -> Scroll → “Series Matrix File(s)” -> Download .txt file.
"""
------------------------------------------STEPS----------------------------------------

#Step 1 -> Load data 
import pandas as pd
df = pd.read_csv("dataset.txt", sep="\t", index_col=0)

#Step 2 -> Inspect Data [To detect outliers and understand distribution]
df.shape
df.head()
df.describe()

#Step 3 -> Remove Missing values 
df.isnull().sum()
df = df.dropna()

#Step 4 -> Distribution check 
df.hist(figsize=(10,6))

#Step 5 -> Normalization
#Method: Z-score normalization
df_norm = (df - df.mean()) / df.std()

#Step -> Variance Calculation
gene_variance = df_norm.var(axis=1)

#Step 7 -> Variance Filtering
threshold = gene_variance.mean()
df_filtered = df_norm[gene_variance > threshold]

#Step 8 -> Mean Expression
gene_mean = df_filtered.mean(axis=1)

#Step 9 -> Select Highly Expressed Genes
df_high = df_filtered[gene_mean > gene_mean.mean()]

#Step 10 -> Rank Genes
top_genes = gene_mean.sort_values(ascending=False).head(10)
print(top_genes)
top_genes.to_csv("top_genes.csv") # To download 
