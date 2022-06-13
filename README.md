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
conda create --name energy python=3.8
conda activate energy
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

GM ONLY
7th Independt Component(IC): The Lentiform Nucleus is the area where the HC show the highest GM density compared to PD, while the Precentral Gyrus the lowest.

<img width="760" alt="Screenshot 2022-06-13 at 09 24 32" src="https://user-images.githubusercontent.com/70062910/173338776-2c5fa667-42a2-42d2-89be-e49122e72746.png">

GM&WM
1st IC: The Lentiform Nucleus is the area where the HC show the highest GM density compared to PD, while the Middle Frontal Gyrus the lowest.

2nd IC: Same as the 1st as far as the two regions with the most differences go.

<img width="760" alt="Screenshot 2022-06-13 at 10 35 16" src="https://user-images.githubusercontent.com/70062910/173338905-a1abf8c5-d019-4333-ace0-422ec7e9478f.png">
<img width="763" alt="Screenshot 2022-06-13 at 10 35 25" src="https://user-images.githubusercontent.com/70062910/173338918-5a7d48ba-dbbb-4add-b64d-2c38a1ba3d27.png">
<img width="754" alt="Screenshot 2022-06-13 at 10 35 46" src="https://user-images.githubusercontent.com/70062910/173338937-4db7766a-19a4-45c8-a815-f0c16e4cf341.png">
<img width="753" alt="Screenshot 2022-06-13 at 10 35 54" src="https://user-images.githubusercontent.com/70062910/173338961-3c5fb644-f62f-4f31-97be-bd5547816c08.png">
