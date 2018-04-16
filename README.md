# IRTools
IRTools is a computational toolset for detection and analysis of intron retention from RNA-Seq libraries.

## Installation



#### PIP

To install directly from PyPI:

```
pip install IRTools
```

If this fails, please install all dependencies first:

```
pip install HTSeq
pip install pysam
pip install pandas
pip install networkx
pip install bx-python==0.7.3
```


#### From source

To install from source:

1\. Install the dependencies with your favorite tools (`pip`, `conda`, etc.).

2\. Run:

```
python setup.py install
```


## Usage

```
IRTools [-h] [-v] {annotation,quant,diff} ...
```

There are three major functions available in IRTools serving as sub-commands.

| Command | Function |
| --- | --- |
| annotation | Generate annotation GTF file for intron retention analysis. |
| quant | Quantify intron retention in both gene and intron levels. |
| diff | Detection of differential intron retention from two samples with replicates in both gene and intron levels. |


### annotation

#### `Arguments`
**-g/--GTF-file GTFFILE**

Input annotation [GTF](http://mblab.wustl.edu/GTF22.html) File. GTF file for a specific species can be downloaded from [iGenome](https://support.illumina.com/sequencing/sequencing_software/igenome.html).

**-o/--annotation-file ANNOFILE**

Output annotation GTF file.

**--outdir**

If specified, all output files will be written to that directory. DEFAULT: the current working directory.

#### `Outputs`

`ANNOFILE` is the output GTF file that contains information for intron retention analysis, including the genomic coordinates of introns, exon-intron junctions, etc.

Sample lines are as follows.

```
chr1	IR_annotation	constitutive_intronic_region	3411983  3660632     .  	-	  .    downstream_constitutive_junction_number "002"; constitutive_intronic_region_number "001"; upstream_constitutive_junction_number "001"; gene_id "Xkr4"
chr1	IR_annotation	constitutive_junction	        3660632	 3660632	 . 	    -	  .	   constitutive_junction_type "5'_splice_junction"; constitutive_junction_number "001"; downstream "constitutive_intronic_region_number 001"; gene_id "Xkr4"; upstream "constitutive_exonic_region_number 001"
```

<br>
<br>

### quant

#### `Arguments`

**-q/--quant-type {IRI,IRC}**

IR quantifiation types: intron retention index (IRI), intron retention coefficient (IRC). DEFAULT: "IRI".

**-i/--alt-file ALTFILE**

Input RNA-Seq alignment file. If IR quantifiation type is "IRI", the input file can be BAM or BED file. If IR quantification type is "IRC", the input file can only be BAM file.

**-p/--read-type {paired,single}**

"paired" is for paired-end data and "single" is for single-end data. DEFAULT: "single".

**-f/--library-type {fr-unstranded,fr-firststrand,fr-secondstrand}**

Library type. DEFAULT: "fr-unstranded" (unstranded). Use "fr-firststrand" or "fr-secondstrand" for strand-specific data.

**-u/--map-file MAPFILE**

Mappability score bigWig file (depends on species,
                        sequence length of RNA-Seq library, etc). Or specify a
                        species (i.e. hg19 or mm9) for which a default
                        annotation file (default for 50 bps of single end RNA-
                        Seq library) can be downloaded and used. If specified,
                        mappability will take into account.
                        
**-e/--species {hg19,mm9}**

Specify a species for which integrated IR annotation
                        GTF file can be used.                    
<br>Note: -e and -g are mutually exclusive
                        and one is required.
                        

**-g/--annotation-file ANNOFILE**

IR annotation GTF file user-built by "IRTools
                        annotation" command. -e and -g are mutually exclusive
                        and one is required.
                        
**-n/--name NAME**

Sample name, which will be used to generate output
                        file names. REQUIRED.

**--outdir**

If specified, all output files will be written to that directory. DEFAULT: the current working directory.

**-f/--format {BAM,BED}**

Set when IR quantifiation type is "IRI". Specify input
                        RNA-Seq alignment file format: "BAM", "BED". DEFAULT:
                        "BAM".
                        
**-m/--min_overlap MINOVERLAP**

Set when IR quantifiation type is "IRC". Minimum
                        length of overlap between the reads and each of the
                        exons or introns involved in splicing. DEFAULT: 8.

#### `Outputs`

**-q IRI**

1\. `NAME.quant.IRI.genes.txt` is the quantification of intron retention index for all genes from RNA-Seq library ALTFILE.

The file format is as follows.

| gene_id |	gene_iv | gene_CIR_length | gene_CER_length | gene_CIR_read_count | gene_CER_read_count | gene_CIR_RPKM | gene_CER_RPKM | gene_IRI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1BG | chr19:58858171-58864865 | 4071 | 1766 | 80.13888888888889 | 93.86111111111111 | 0.7394798014780853 | 1.9965449549590883 | 0.37037974008115343 |
| A1CF | chr10:52559168-52645435 | 72712 | 9221 | 24.0 | 59.0 | 0.012399074027101793 | 0.2403577285944172 | 0.051585917788498296 |

2\. `NAME.quant.IRI.introns.txt` is the quantification of intron retention index for all introns from RNA-Seq library ALTFILE.

The file format is as follows.

| CIR_id |	CIR_iv |	CIR_length |	adjacent_CER_length |	CIR_read_count |	adjacent_CER_read_count |	CIR_RPKM |	adjacent_CER_RPKM |	intron_IRI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1BG:004 | chr19:58863053-58863648 | 474 | 570 | 7.138888888888889 | 17.02777777777778 | 0.5657653978142747 | 1.122192132703333 | 0.5041609019761704 |
| A1BG:005| chr19:58862017-58862756| 739 | 579 | 18.13888888888889 | 25.22222222222222 | 0.9220412349334726 | 1.636397795045001 | 0.5634578815281992 |

**-q IRC**

1\. `NAME.quant.IRC.genes.txt` is the quantification of intron retention coefficient for all genes from RNA-Seq library ALTFILE.

The file format is as follows.

| gene_id |	gene_iv |	gene_retained_reads |	gene_spliced_reads |	gene_IRC |
| --- | --- | --- | --- | --- |
| AAAS | chr12:53701239-53715412 | 2.5 | 64 | 0.0375939849624 |
| AAGAB | chr15:67493012-67547536 | 0.5 | 29 | 0.0169491525424 |

2\. `NAME.quant.IRC.introns.txt` is the quantification of intron retention coefficient for all introns from RNA-Seq library ALTFILE.

The file format is as follows.

| CIR_id | CIR_iv | CIR_5'retained_reads | CIR_3'retained_reads | CIR_spliced_reads | intron_IRC |
| --- | --- | --- | --- | --- | --- |
| AAAS:012 | chr12:53702133-53702218 | 1 | 0 | 4 | 0.111111111111 |
| AAGAB:007 | chr15:67496486-67500899 | 0 | 1 | 5 | 0.0909090909091 |

3\. `NAME.quant.IRC.junctions.txt` is the quantification of intron retention coefficient for all exon-intron junctions from RNA-Seq library ALTFILE.

The file format is as follows.

| CJ_id | CJ_iv | CJ_type | CJ_retained_reads | CJ_spliced_reads | junction_IRC |
| --- | --- | --- | --- | --- | --- |
| A1BG:012 | chr19:58859005-58859006 | 3'_splice_junction | 3 | 0 | 1.0 |
| AAAS:001 | chr12:53715125-53715126 | 5'_splice_junction | 0 | 12 | 0.0 |

<br>
<br>

### diff