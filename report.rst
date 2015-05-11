***************
Research report
***************


In this report we cover the analysed data.

Introduction
============

Here is a figure that shows the trend:

.. figure:: result_plot.png
   :scale: 20 %
   :alt: trending line

   This is the caption of the figure (a simple paragraph).

{% set vars = d["results.json"] %}

The data shows Foo is {{ vars.foo }} and bar is {{ vars["bar"] }}.