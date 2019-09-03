# hatespeech-ml
A classifier detecting hate speech. This repo holds the whole development process. 

All the steps are described under the following link (German): [projekte.lbssr.ch/der-hass-im-netz/methodology.html](https://projekte.lbssr.ch/der-hass-im-netz/methodology.html). This classifier is part of an article discussing the difficulty of combatting hate speech with artifical intelligence (German): [projekte.lbssr.ch/der-hass-im-netz/](https://projekte.lbssr.ch/der-hass-im-netz/).

## [`0_common`](../blob/master/0_common)

Contains helper functions used in various scripts. 

## `1_Data_Cleaning`

Cleaning and preparing text samples from various sources. All the data sources if suitable for publication.
Datasets used in the final model:
* dataset of the research training group "User-Centred Social Media", University Duisburg-Essen: [Link](https://github.com/UCSM-DUE/IWG_hatespeech_public)
* dataset from Uwe Bretschneider and Ralf Peters, Martin-Luther-University Halle-Wittenberg: [Link](http://www.ub-web.de/research/)
* Polly-Korpus by Tom De Smedt (Universität Antwerpen) and Sylvia Jaki (Universität Hildesheim): [Link](https://docs.google.com/spreadsheets/d/1c5peNMjt24U0FcEMSj8gD_JjzumqXTWbPWa_yb2nNt0/edit#gid=2031183870)

## `2_Feature_Engineering`

Experimenting with various features and combining datasets.

## `3_Model_Development`

Development of the machine learning model comparing different algorithms and parameters on different datasets. The final model is found here: [Jupyter Notebook](https://github.com/pscllbssr/hatespeech-ml/blob/master/3_Model_Development/7_Version%20Deployment/4%20RF%20with%20char-vec.ipynb).





