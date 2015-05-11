supplementary analysis
======================

Here are some details we noticed in the analysis.

{% set vars = d["supplementary_results.json"] %}
The data shows Foo std is {{ vars.foo_std }} and bar is {{ vars["bar_std"] }}.
