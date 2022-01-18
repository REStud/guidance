# Compare Stodden's work with the RRS rules

## Learning from reproducing computational results: introducing three principles and the Reproduction Package
<br/> *Summary: Authors tried to reproduce 7 articles, based on that they identify three principles with 12 specific guidelines for their implementation in practice. Reproduction Package: a formalism that specifies a structured way to share computational research artifact.*
<br/> *Stodden's Guidelines and the Reproduction Package is in line with REStud practice (eg. Zenodo, license, README, use main script).*
*A recommended addition to REStud RRS could be:
- Use Dockerfile G4. (I think it would be too much to ask, RRS 10b and 11e is enough)
- **Include a Rule about pathing G6. (eg. RRS, Format 7d)**
- **Include a Rule about set seed G7. (eg. RRS, Format 7e)**
- For complex softwares: use Make and containerized environment G10. (I think it might not be often/necessary in Economics research)
- **Provide scripts to reproduce visualizations of results. G11. (eg. RRS, edit Analysis 6 "Include programs used to run the final models, and to create exhibits")***

-------------------------------------

### Principles
(i) Provide transparency regarding how computational results are produced;
(ii) When writing and releasing research software, aim for ease of (re-)executability; (eg. parameters, labels, hardware requirement)
(iii) Make any code upon which the results rely as deterministic as possible. (eg. software dependencies, versions, seeds if random numbers are generated)
### Guidelines
- G1. Make all artifacts that support published results available, up to legal and ethical barriers. (eg. Github, Zenodo with DOI, license such as RRS)
- G2. Connect published scientific claims to the underlying computational steps and data. (provide a master script)
- G3. Specify versions and unique persistent identifiers for all artifacts. -> I think it does not relate to REStud, because they should submit the final version
- G4. Declare software dependencies and their versions.  (Provide exact info on version of dependencies. Package the code into a Docker image or other container solution such as Vagrant or Singularity) -> I think Docker would be too much to ask.
- G5. Refrain from using hard coded parameters in code.
- G6. Avoid using absolute or hard-coded filepaths in code. (use relative paths)
- G7. Provide clear mechanisms to set and report random seed values.
- G8. Report expected errors and tolerances with any published result that include any uncertainty from software or computational environments. -> I think it might not be often/necessary in Economics research
- G9. Give implementations for any competing approaches or methods relied upon in the article. -> I think it might not be often/necessary in Economics research  -> I think it might not be often/necessary in Economics research
- G10. Use build systems for complex software. (Use a build system, such as GNU Make, build a containerized environment)-> I think it might not be often/necessary in Economics research
- G11. Provide scripts to reproduce visualizations of results. (Provide a clearly identifiable script that creates each figure or table)
- G12. Disclose resource requirements for computational experiments. (hardware, runtime, RAM)

### Reproduction Package

<br/> Stodden's replication package includes (on top of what REStud requires in a pack):
- in main folder: License (I think it is covered in Zenodo?)
- in main folder: Dockerfile: This file helps to make clear how to build the code and any dependencies needed.
- in main folder: .travis.yml: This script integrates the code with Travis CI. This step shows the reader how to run the experiments.

-----------------------

## The Legal Framework for Reproducible Scientific Research - Licensing and Copyright
Source: http://stodden.net/papers/Legal-STODDEN2009.pdf
<br/> *Summary: RRS is a framework to rescend the default copyright in computational scientific resarch. RRS is an amalgamation of commonly used existing licenses: attaching CC BY to the compendium’s media components, modified BSD to code components, and the Science Commons Database Protocol (http://commons.org/projects/publishing/open-access-data-protocol) to the data if scientists choose to release their data to the public domain.*

<br/> *Stodden's RRS is in line with REStud RRS, a recommended addition to REStud RRS could be: ask packages to use RRS license as default (Instead of the recommendation now: “Creative Commons Attribution 4.0 International” license). eg. in 14. Format (d): Place a notifiacation in the README that "the replication package falls under RRS." (but I don't know the pros and cons of RRS vs. CC BY 4.0 licenses, it might not be a relevant change)*

---------------------------------------------
<br/> In the US, when scientists put their original research on the Web, it automatically falls under copyright. However, it is against open sharing, dissemination, using, reproducing and building on others’ research. This paper presents a methodology for scientists to **rescind copyright**. To rescind copyright on scientific research, you must actively choose to do so, and this is typically done with a **license**. Licenses offer an option to override default copyright law.

<br/>Two of the most common types of open licenses that rescind copyright are:
- those designed for code (for example, the GNU Public License or GPL and the Berkeley Software Distribution or BSD license)
- or media (for example, the family of Creative Commons licenses).
<br/> The **Share Alike concept is inappropriate in the scientific context** because it can impose limits on the use and reuse of others’ work:
- it renders the research unavailable for reuse by people who don’t want to use the same license as the original research for their own resulting research output.
- expanding the license to cover the entire derivative work product makes attempts at attribution more difficult.
- The **Science Commons Open Access Data Protocol** (sciencecommons.org/projects/publishing/open-access-data-protocol/) embodies many of these arguments.
<br/>  Two blocks exist to truly reproducible research:
- the **lack of reward for producing reproducible work** (norms in the scientific community)
- the **legal obstacle to the full sharing of methodologies**, writing, code, papers, and data (copyright law). I propose the **Reproducible Research Standard (RRS) to address this second block**

<br/> **Computational research compedium comprises:**
- **Research paper** - including all the source files from which the manuscript was built (for example, LaTex, Word, or WordPerfect files);
- **Data** - including documentation completely describing the data (sources, components, and interpretation); a description of how the data was brought into the form used in the research; the code and instructions used to bring the data into the form used in the research; and documentation of any code used for data processing. Raw data aren’t copyrightable, and thus it’s meaningless to apply a copyright rescinding license to them. However, original selection and arrangement of the data are copyrightable, as are the original metadata associated with dataset production such as documentation, arrangement, explanations, or data cleaning.
- **Experiment** - the code and instructions used in the experiment, including all source code; documentation of any code used, including pseudocode; a clear listing of the parameters, settings, and operating system dependencies used to achieve the results described in the paper; and a clear description of the experimental methodology;
- **Results of the Experiment** - any figures, data, or the like produced from the experiment; any illustration source files; and documentation and explanation of the processing of the experimental results; and
- **Any Auxiliary material** - materials used for presentation on the Web or an interface to the data or results; and documentation of any auxiliary code.
<br/> Encouraging the release of the entire research compendium is the purpose of the RRS. I argue this is best done through ensuring attribution. The RRS requires attribution for any part of the upstream compendium used in derivative research and those (US) components of the downstream research carry the license. **RRS is an amalgamation of commonly used existing licenses: attaching CC BY to the compendium’s media components, modified BSD to code components, and the Science Commons Database Protocol (http://commons.org/projects/publishing/open-access-data-protocol) to the data if scientists choose to release their data to the public domain.**

<br/> Stodden's RRS relates to the following part of REStud RRS: copyrightable parts of the computational research are the paper which is documentation of data, code and instructions, results. Raw data aren’t copyrightable.
