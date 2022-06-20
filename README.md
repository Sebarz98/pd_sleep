# Parkinson's Disease and Sleep

This study aims to study the correlation between chronotype, sleep quality and Parkinson's disease.

Sebastiano Vacca, Taha Binhuraib

## Dependencies
* **OS**: Linux or macOS
* **Language**: Python
* **Libraries**: scikit-learn, numpy, pandas

## Installation

### Git Clone
Git clone the repository by running the following commands:
```bash
# change directory to Documents
cd Documents
git clone https://github.com/TahaBinhuraib/pd_sleep.git
cd pd_sleep
```
### Anaconda
You need to install [Anaconda](https://www.anaconda.com/products/distribution), then run below:
```bash
conda create --name pd python=3.8
conda activate pd
pip install -r requirements.txt
```

## Usage
### Jupyter Notebook
* [Random Forest](./models/random_forest.ipynb)
* [Data Analysis](PCA&ICA.ipynb)

### Python :snake:
You can run our python deep and machine learning model by running the following:
```bash
cd model
# random_forest 
python random_forest.py
```
## Evaluation
### Voxel-Based-Morphometry(VBM)
VBM has been conducted on MATLAB, with SPM12 & CAT12 toolboxes. The results were visualized with xjview.
We used both Grey Matter and White Matter segmented images, after smoothing with a 8x8 Kernel, as inputs for our two-way t-test between Parkinson Patients and Healthy Controls. 
A p.value of < 0.001 and a Family Wise Error of 0.05 have been used. 
Regarding the GM analysis, the most significant differences have been found in the putamen, both left and right ones, with the HC having more GM. 
As far as the WM analysis, the most significant differences have been found in the sub-gyral parietal lobe, with the HC having slightly less WM.

<img width="779" alt="Screenshot 2022-06-13 at 11 46 15" src="https://user-images.githubusercontent.com/70062910/173335625-5b4c0941-3038-41bb-959e-2fd527585524.png">
<img width="782" alt="Screenshot 2022-06-13 at 11 47 57" src="https://user-images.githubusercontent.com/70062910/173335647-85e6e4c3-9fca-4ed9-ae2d-7bf3b56b827f.png">

### Source-Based-Morphometry(SBM)
SBM consists in applying PCA/ICA (through the infomax algorithm) to the smoothed images to have a better visualization and analysis of GM and WM densities.
SBM has been conducted on MATLAB, with the FUSION toolbox. The inputs are the same of the VBM.
Firstly, we ran the analysis with only one feature, the GM, and then with both GM and WM.
Only the components with a p.value of <0.001 have been reported here.
The regions have been identified based on the Talairach Coordinates, where the images have been converted to Z-scores with a threshold of 2.

### Source-Based-Morphometry(SBM) - Part 1
SBM consists in applying PCA/ICA (through the infomax algorithm) to the smoothed images to have a better visualization and analysis of GM and WM densities.
SBM has been conducted on MATLAB, with the FUSION toolbox. The inputs are the same of the VBM.
Firstly, we ran the analysis with only one feature, the GM, and then with both GM and WM.
Best component for each feature combination is deter- mined using two sample t-test on the mixing coefficients.
Only the components with a p.value of <0.001 have been reported here.
The regions have been identified based on the Talairach Coordinates, where the voxels above threshold |Z| > 1.5 were converted. 

#### GM ONLY
7th Independent Component(IC): The Lentiform Nucleus is the area where the HC show the highest GM density compared to PD, while the Precentral Gyrus the lowest.

<img width="760" alt="Screenshot 2022-06-13 at 09 24 32" src="https://user-images.githubusercontent.com/70062910/173338776-2c5fa667-42a2-42d2-89be-e49122e72746.png">

#### GM&WM

1st IC: The Lentiform Nucleus is the area where the HC show the highest GM density compared to PD, while the Middle Frontal Gyrus the lowest.

2nd IC: Same as the 1st as far as the two regions with the most differences go.

1st IC & Feature 1: The Lentiform Nucleus is the area where the HC show the highest GM density compared to PD, while the Middle Frontal Gyrus the lowest.

2nd IC & Feature 1: Same as the 1st as far as the two regions with the most differences go.

1st IC & Feature 2: The Lingual Gyrus is the area where the HC show the lowest WM density compared to PD, while the Middle Frontal Gyrus the highest.

2nd IC & Feature 2: Areas 20 and 21 is where the HC show the lowest WM density compared to PD, while the Fusiform Gyrus the highest.


<img width="760" alt="Screenshot 2022-06-13 at 10 35 16" src="https://user-images.githubusercontent.com/70062910/173338905-a1abf8c5-d019-4333-ace0-422ec7e9478f.png">
<img width="763" alt="Screenshot 2022-06-13 at 10 35 25" src="https://user-images.githubusercontent.com/70062910/173338918-5a7d48ba-dbbb-4add-b64d-2c38a1ba3d27.png">
<img width="754" alt="Screenshot 2022-06-13 at 10 35 46" src="https://user-images.githubusercontent.com/70062910/173338937-4db7766a-19a4-45c8-a815-f0c16e4cf341.png">
<img width="753" alt="Screenshot 2022-06-13 at 10 35 54" src="https://user-images.githubusercontent.com/70062910/173338961-3c5fb644-f62f-4f31-97be-bd5547816c08.png">


### Source-Based-Morphometry(SBM) - Part 2
The analysis consisted in comparing the Gray Matter of 11 PD patients (median age 39 years) vs 11 Healthy controls with an Early Chronotype (EC - median age 31 years) and other 11 with a Late Chronotype (LC - median age 31 years). 
Only the components with a p.value of <0.001 have been reported here. The regions have been identified based on the Talairach Coordinates, where the voxels above threshold |Z| > 1.5 were converted. The regions with the maximum t-value have been reported. 

#### PD vs EC
7th Independent Component(IC): The Middle and Inferior Temporal Gyrus are the areas where the EC show the highest GM density compared to PD, while the Uncus the lowest.

<img width="753" alt="Screenshot 2022-06-20 at 08 09 13" src="https://user-images.githubusercontent.com/70062910/174615281-c654d3b1-e335-4f67-bed8-7b297950e69b.png">

2nd Independent Component(IC): The Superior and Middle Frontal Gyri are the areas where the EC show the highest GM density compared to PD, while the Precentral Gyrus the lowest.

<img width="753" alt="Screenshot 2022-06-20 at 08 09 13" src="https://user-images.githubusercontent.com/70062910/174616466-dad90913-5292-407c-b33c-1b55e5852bbb.png">

#### PD vs LC
7th Independent Component(IC): The Middle and Inferior Temporal Gyrus are the areas where the LC show the highest GM density compared to PD, while the Uncus the lowest.

<img width="737" alt="Screenshot 2022-06-20 at 08 16 40" src="https://user-images.githubusercontent.com/70062910/174617951-fc7a12b8-19e0-4142-a563-0ad1fd050424.png">

5th Independent Component(IC): The Angula Gyrus and Parahippocampal Gyrus are the areas where the LC show the highest GM density compared to PD, while the Middle and Inferior Frontal Gyri the lowest.

<img width="743" alt="Screenshot 2022-06-20 at 08 16 52" src="https://user-images.githubusercontent.com/70062910/174618893-4d8e8665-f9ec-40e3-8081-e6dc0ae09c2b.png">
