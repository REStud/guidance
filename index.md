---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: page
title: Home
---
# How to share your research in a reproducible way
## Cite everything that the replication package relies on
> Citations in the manuscript and the README are the best way of directing readers to these resources and to give credit to the original authors.

{% capture example1 %}
Cite open data. 
{% endcapture %}
{% capture example2 %}
Cite confidential, but widely used data. 
{% endcapture %}
{% capture example3 %}
Cite proprietary data. 
{% endcapture %}
{% capture rules %}
All datasets, whether public or private, included or not, should be cited. It is good practice to cite software packages, but not required, unless the license terms specifically ask you to do so.
{% endcapture %}
{% include details.html %}

## Include all exhibits and the code to produce them ALL DATA THAT YOU ARE ABLE (drill down)
> The package should be self contained so that readers can verify that your analysis code produces the output you included.

{% capture example1 %}
This data is included. 
{% endcapture %}
{% capture example2 %}
Only exhibits are included. 
{% endcapture %}
{% capture example3 %}
Only exhibits are included.
{% endcapture %}
{% capture rules %}
Save all the output of the analysis in some standard format into the replication package. Tables can be saved as .csv, .xls or .tex files. It is also sufficient to save the Stata .log file. In this case, please report in the README the line numbers where the readers can find the table numbers. Figures can be saved in .eps, .pdf or .png.

Refer to confidential data questionnaire.
{% endcapture %}
{% include details.html %}
## For files not included, explain how to get them
> The goal is to describe clearly the steps that readers have to take if they want to access the data and software you could not included. 

{% capture example1 %}
This data is included. 
{% endcapture %}
{% capture example2 %}
Only exhibits are included. 
{% endcapture %}
{% capture example3 %}
Only exhibits are included.
{% endcapture %}
{% capture rules %}
Include a formal Data Availability Statement for each of the datasets you are using. List all software packages, libraries, toolboxes that you use in the README with instructions on how to install them.
{% endcapture %}
{% include details.html %}
## Guide the reader on how to get from the data to exhibits
> Readers are expert empirical economists but need specific instructions on how to reproduce your analysis.

{% capture example1 %}
This data is included. 
{% endcapture %}
{% capture example2 %}
Only exhibits are included. 
{% endcapture %}
{% capture example3 %}
Only exhibits are included.
{% endcapture %}
{% capture rules %}
Create a list of exhibits and state which one is produced by which script. If possible, include a master script executing all the necessary steps. Explain if your code requires special hardware or runs for particularly long.
{% endcapture %}
{% include details.html %}
