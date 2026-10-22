# Transcriptomics analysis: spermatozoal transcriptome of Frieswal bulls

Scripts used for the differential expression and annotation steps of an RNA-seq study of bull spermatozoa. The study compared semen from crossbred Frieswal (Holstein Friesian × Sahiwal) bulls with a good conception rate (> 55 %) and a poor one (< 40 %).

The work is described in:

Singh, R.<sup>†</sup>; Junghare, V.<sup>†</sup>; Hazra, S.; Singh, U.; Sengar, G. S.; Raja, T. V.; Kumar, S.; Tyagi, S.; Das, A. K.; Kumar, A.; Koringa, P.; Jakhesara, S.; Joshi, C. J.; Deb, R. Database on spermatozoa transcriptogram of categorised Frieswal crossbred (Holstein Friesian X Sahiwal) bulls. *Theriogenology* **2019**, 129, 130–145. https://doi.org/10.1016/j.theriogenology.2019.01.025

<sup>†</sup> These authors contributed equally.

## deg_filter/

`deseq1.py` is the Python program the paper describes for selecting DEGs. It reads the result table produced by the CLC Genomics Workbench "Differential Expression for RNA-Seq" tool.


## david_annotation/

`filter.py` keeps only the *Bos taurus* entries from the output of the DAVID Gene ID Conversion Tool. The converted list contained IDs from many species (18,634), and only 117 were *Bos taurus*. It reads the DAVID output file named at the top of the script and writes the matching lines to `list.txt`. The kept IDs were used for the DAVID functional annotation, with *Bos taurus* as the background. Python 2.
