# sashimi.py

[![PyPI version](https://badge.fury.io/py/sashimi-py.svg)](https://pypi.org/project/sashimi.py/)
[![PyPI download](https://img.shields.io/pypi/dm/sashimi-py.svg)](https://pypi.org/project/sashimi.py/)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/sashimi-py/README.html)
[![Documentation Status](https://readthedocs.org/projects/sashimi/badge/?version=latest)](https://sashimi.readthedocs.io/en/latest/)
[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%20v3-clause.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![DOI](https://img.shields.io/badge/DOI-10.1101%2F2022.11.02.514803%20-blue)](https://www.biorxiv.org/content/10.1101/2022.11.02.514803v1)

---

![](example/diagram.png)

[Tutorials](https://sashimi.readthedocs.io/en/latest/)

## what is sashimi.py

sashimi.py is a tool for visualizing various next-generation sequencing (NGS) data, including DNA-seq, RNA-seq, single-cell RNA-seq and full-length sequencing datasets. 

### Features of sashimi.py

1. Support various file formats as input
2. Support strand-aware coverage plot
3. Visualize coverage by heatmap, including HiC diagram 
4. Visualize protein domain based the given gene id
5. Demultiplex the single-cell RNA/ATAC-seq which used cell barcode into cell population 
6. Support visualizing individual full-length reads in read-by-read style
7. Support visualize circRNA sequencing data

## Input

sashimi.py supports almost NGS data format, including

- BAM
- Bed
- bigBed
- bigWig
- Depth file generated by `samtools depth`
- naive Hi-C format


## Output

The output will be a pdf and other image file formats which satisfy the requirement of the major journals, 
and each track on output corresponds these datasets from config file.

## Usage

The sashimi.py is written in Python, and user could install it in a variety of ways as follows

__Note:__ if `segment fault` with multiple processing, please try to use docker image, or just run with `-p 1`.

1. install from PiPy

    ```bash
    pip install sashimi.py
   # __Note:__ We noticed some pypi mirrors are not syncing some packages we depend on, 
   # therefore please try another pypi mirror once you encounter 
   # `No local packages or working download links found for xxx`
    ```

2. install from bioconda

    ```bash
    conda install -c bioconda -c conda-forge sashimi-py
   
    # or
    conda env create -n sashimi -f environment.yaml

    # or
    conda create -n sashimi -c bioconda -c conda-forge sashimi-py
    ```

3. using docker image

    ```bash
    docker pull ygidtu/sashimi
    docker run --rm ygidtu/sashimi --help

    # or 

    git clone from https://github.com/ygidtu/sashimi.py sashimi
    cd sashimi
    docker build -t ygidtu/docker .
    docker run --rm ygidtu/sashimi --help
    ```

4. install from source code

    ```bash
    git clone https://github.com/ygidtu/sashimi.py sashimi
    cd sashimi
    python setup.py install
    
    sashimipy --help
    # pr
    python main.py --help
    ```

5. running from a local webserver

   ```bash
    git clone https://github.com/ygidtu/sashimi.py sashimi
    cd sashimi/web

    # build the frontend static files
    npm install -g vue-cli vite && npm install
    vite build

    # prepare the backend server
    pip install fastapi pydantic jinja2 uvicorn

    python server.py --help
    ```

6. for `pipenv` users

    ```bash
    git clone https://github.com/ygidtu/sashimi.py
    cd sashimi.py
    pipenv install   # create virtualenv and install required packages
    pipenv shell   # switch to virtualenv
    
    sashimipy --help
    # pr
    python main.py --help
    ```



## Example

```bash
python main.py \
  -e chr1:1270656-1284730:+ \
  -r example/example.sorted.gtf.gz \
  --interval example/interval_list.tsv \
  --density example/density_list.tsv \
  --show-site \
  --show-junction-num \
  --igv example/igv.tsv \
  --heatmap example/heatmap_list.tsv \
  --focus 1272656-1272656:1275656-1277656 \
  --stroke 1275656-1277656:1277856-1278656@blue \
  --sites 1271656,1271656,1272656 \
  --line example/line_list.tsv \
  -o example/example.png \
  --dpi 300 \
  --width 10 \
  --height 1 \
  --barcode example/barcode_list.tsv \
  --domain --remove-duplicate-umi \
  -p 4
```
here is the [output file](https://raw.githubusercontent.com/ygidtu/sashimi.py/main/example/example.png).


## Questions

Visit [issues](https://github.com/ygidtu/sashimi.py/issues) or 
contact [Yiming Zhang](https://github.com/ygidtu) and 
[Ran Zhou](https://github.com/zhou-ran)

## Citation

If you use Sashimi.py in your publication, please cite Sashimi.py by

[Zhang et al. Sashimi.py: a flexible toolkit for combinatorial analysis of genomic data. bioRxiv 2022.11.02.514803.](https://www.biorxiv.org/content/10.1101/2022.11.02.514803v1)

