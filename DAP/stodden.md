# Compare Stodden's work with the RRS rules

## The Legal Framework for Reproducible Scientific Research - Licensing and Copyright
Source: http://stodden.net/papers/Legal-STODDEN2009.pdf
<br/> Summary: RRS is a framework to rescend the default copyright in computational scientific resarch. RRS is an amalgamation of commonly used existing licenses: attaching CC BY to the compendium’s media components, modified BSD to code components, and the Science Commons Database Protocol (http://commons.org/projects/publishing/open-access-data-protocol) to the data if scientists choose to release their data to the public domain.

<br/> Stodden's RRS is in line with REStud RRS, a recommended addition to REStud RRS could be: ask packages to use RRS license as default (Instead of the recommendation now: “Creative Commons Attribution 4.0 International” license). eg. in 14. Format (d): Place a notifiacation in the README that "the replication package falls under RRS." (but I don't know the pros and cons of RRS vs. CC BY 4.0 licenses, it might not be a relevant change)

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
-------------------------------
Stodden's RRS relates to the following part of REStud RRS: copyrightable parts of the computational research are the paper, documentation of data, code and instructions, results.

    1. Primary Data: - (Raw data aren’t copyrightable)

    2. Secondary Data: -

    3. Data extracts: -

    4. Format: a)- b) copyrightable: documentation, metadata

    5. Data transformation: copyrightable

    6. Analysis: copyrightable

    7. Format: a) - b) - c) copyrightable

    8. Instruments: copyrightable

    9. Exhibits: copyrightable

    10. Citation: required

    11. Dependencies: required

    12. Guidance: -

    13. Format: README is copyrightable

    14. Location: -
