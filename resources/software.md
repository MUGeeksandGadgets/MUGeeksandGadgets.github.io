---
layout: default
title: Software
blurbs:
  Integrated Development Environments: |
    An integrated development environment (IDE) is a software application that
    provides comprehensive facilities to computer programmers for software
    development. An IDE normally consists of a source code editor, build
    automation tools and a debugger. Most modern IDEs have an intelligent code
    completion.
  Computer Aided Design: |
    Computer-aided design (CAD) is the use of computer systems to aid in the
    creation, modification, analysis, or optimization of a design. CAD software
    is used to increase the productivity of the designer, improve the quality of
    design, improve communications through documentation, and to create a
    database for manufacturing. CAD output is often in the form of electronic
    files for print, machining, or other manufacturing operations.
  Text Editors: |
    Text editors are very handy for a variety of tasks. They do not take as much
    time to load when compared to a full on IDE, they are light weight, and
    there are a ton of them to choose from. The few listed here are the ones
    preferred by the club. Keep in mind that editors like text edit and notepad
    are not included because they are built in apps for OSX and Windows. The
    ones listed below are for download across all operating systems.
  Graphic Design: |
    This section contains information on programs used to create and or
    manipulate images for the purpose of graphic design.
---

# Software
{:.no_toc}

Welcome to the software page! All of the software listed is free to download for
all. This page is here as a resource when looking for programs to get stuff
done. The page contains excerpts from each program's respective wikipedia
article and a link to its official website. The software list is broken up into
several categories and has a brief explanation of what each piece of software
does. If you would like to see a software added to this page, please contact us
as by email.

* Table of Contents
{:toc}


{% assign groups = site.software | group_by: 'type' | sort: 'name' %}
{% for group in groups %}

----
## {{ group.name | default: 'General' }}

{{ page.blurbs[group.name] }}

{% for software in group.items %}

### {{ software.name }}

[Project Home Page]({{ software.homepage }})

{{ software.content }}

{% endfor %}
{% endfor %}