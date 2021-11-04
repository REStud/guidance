---
papersize: a4
geometry:
- top=20mm
- left=20mm
- right=20mm
- bottom=20mm
- heightrounded
---
# Reproducible Research Standard v1.0
## What to include in the replication package and in the README document


| | Item No | Rule | Policy |
|---|-|-------|-|
| **Data** |
| Primary data | 1 | For papers collecting original data through surveys or experiments, include the original data unchanged, with the exception of anonymization and other privacy protection. | | 
| Secondary data | 2 | (a) Whenever usage terms permit, include raw secondary data. 
| | |(b) If secondary data cannot be published as part of a replication package or in an openly accessible trusted data repository, the rest of the policy still applies. | | 
| Data extracts | 3 | Include the data extract used for analysis, especially if source data cannot be published and when the data transformation codes are computationally demanding. | | 
| Format | 4 | (a) The data files may be provided in any format compatible with any commonly used statistical package or software. You are encouraged to provide data files in open, non-proprietary formats. 
| | |(b) Ensure that a meaningful name or description (label) is available for every variable in the provided datasets. Codebooks or similar metadata should describe the allowed values and their meaning for each variable. It is acceptable to reference publicly available documentation for these items. | | 
| **Code** |
| Data transformation | 5 | Include programs used to create any final and analysis data sets from raw data. | | 
| Analysis | 6 | Include programs used to run the final models. | | 
| Format | 7 | (a) The programs may be provided in any format compatible with commonly used statistical package or software. 
| | |(b) Should unusual or costly software be required, notify the responsible Editor. 
| | |(c) Include a main script running all the code in proper order. | | 
| **Supporting materials** |
| Instruments | 8 | (a) For papers collecting original data through surveys or experiments, include survey instruments or experiment instructions, 
| | |(b) computer code for experiment or survey collection mechanisms, 
| | |(c) and original instructions and details on subject selection. | | 
| Exhibits | 9 | Save all the output of the analysis in some standard, non-proprietary format into the replication package. | | 
| **README document** |
| Citation | 10 | (a) Cite all source data used in the paper, following journal guidelines. 
| | |(b) Cite all software packages used, following journal guidelines. | | 
| Dependencies | 11 | (a) For econometric, simulation, and experimental papers, include description sufficient to access all data at their original source location. 
| | |(b) Provide a data availability statement covering both the source data and any derivative data. It may additionally be provided as part of online appendices. 
| | |(c) The data availability statement shall provide detailed information on how, where, and under what conditions an independent researcher can access the original source data, as well as author-generated derivative data, and must be explicit and accurate about any restrictions, requirements, payments, and processing delays. 
| | |(d) The data availability statement shall provide information to assure the reader that the data are available for a sufficiently long period of time. 
| | |(e) List all software packages, libraries, toolboxes that you use with instructions on how to install them. 
| | |(f) Describe the hardware and operating system on which the code was last run. 
| | |(g) Explain if your code requires special hardware or runs for particularly long. | | 
| Guidance | 12 | (a) Provide description sufficient to allow all programs to be run. 
| | |(b) List all the data sets used with their bibliographic citation, referring to their specific file names if included. 
| | |(c) Create a list of exhibits and state which one is produced by which script. 
| | |(d) If a script creates multiple exhibits, point to the exact line number. | | 
| Format | 13 | (a) The README document should list the title and authors of the replication package, its preparation date, and clear reference to the journal article to which it belongs. 
| | |(b) Follow the schema provided by the Social Science Data Editors template README (https://social-science-data-editors.github.io/template_README/) 
| | |(c) Common formats are txt, PDF, and Markdown. The README file should not require proprietary software to view. | | 
| **Repository** |
| Location | 14 | Archive data and programs in the code and data repository designated by the journal. | | 

All participating journals value all rules, but the levels of enforcement may vary. For each rule, journal policy may be "Verified", "Required" or "Recommended."