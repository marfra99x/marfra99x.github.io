---
layout: page
permalink: /research/
title: Research
nav: false
nav_order: 2
description: Research themes in string algorithms, data compression, indexing, uncertain strings, and quantum algorithms.
---

My work is centered on the design and analysis of algorithms for strings and sequences. A recurring theme is to exploit structure—sampling, repetitiveness, uncertainty, or computational models—to make searching and indexing more efficient.

<div class="research-grid research-page-grid">
  <section class="research-card research-card-static" id="string-algorithms-and-sampling">
    <span class="research-icon"><i class="fa-solid fa-magnifying-glass"></i></span>
    <h2>String algorithms &amp; sampling</h2>
    <p>
      I study exact and approximate pattern matching, with particular emphasis on text-sampling techniques that reduce the amount of text inspected during search. This line includes character-distance sampling, character-context sampling, fake sampled positions, and sampling-based approaches to periods and covers.
    </p>
    <p class="research-links">
      Representative work:
      <a href="{{ '/publications/#FaroMP20' | relative_url }}">Algorithmica 2020</a> ·
      <a href="{{ '/publications/#FaroMP23' | relative_url }}">TCS 2023</a> ·
      <a href="{{ '/publications/#FaroLM26' | relative_url }}">IEEE Access 2026</a>
    </p>
  </section>

  <section class="research-card research-card-static" id="compression-and-indexing">
    <span class="research-icon"><i class="fa-solid fa-layer-group"></i></span>
    <h2>Compression &amp; indexing</h2>
    <p>
      I work on compressed and structural representations of strings, including recompression, string attractors, and full-text indexing. Recent work investigates structural string comparison through attractors and compact indexing techniques based on the BWT and FM-index.
    </p>
    <p class="research-links">
      Representative work:
      <a href="{{ '/publications/#FKM26' | relative_url }}">DCC 2026 — Attractor Matching</a> ·
      <a href="{{ '/publications/#KopplM26' | relative_url }}">ICTCS 2026 — Recompression</a>
    </p>
  </section>

  <section class="research-card research-card-static" id="indeterminate-and-elastic-degenerate-strings">
    <span class="research-icon"><i class="fa-solid fa-diagram-project"></i></span>
    <h2>Indeterminate &amp; elastic-degenerate strings</h2>
    <p>
      Another research direction concerns strings whose positions or segments encode uncertainty. I study matching and indexing problems on indeterminate and elastic-degenerate strings, including SCER matching and FM-index construction through specialized wavelet-tree structures.
    </p>
    <p class="research-links">
      Representative work:
      <a href="{{ '/publications/#FKLM26CPM' | relative_url }}">CPM 2026 — SCER Matching</a> ·
      <a href="{{ '/publications/#FKLM26' | relative_url }}">DCC 2026 — ED FM-index</a>
    </p>
  </section>

  <section class="research-card research-card-static" id="quantum-algorithms">
    <span class="research-icon"><i class="fa-solid fa-atom"></i></span>
    <h2>Quantum algorithms</h2>
    <p>
      My quantum-computing work covers quantum string matching, Grover-style search, high-level programming abstractions, reversible and shallow circuits, and quantum shuffling. This includes the Qutes language and algorithmic work presented at HPDC, FUN, and ICTCS.
    </p>
    <p class="research-links">
      Representative work:
      <a href="{{ '/publications/#FMM25' | relative_url }}">HPDC 2025 — Qutes</a> ·
      <a href="{{ '/publications/#FMM26' | relative_url }}">FUN 2026</a> ·
      <a href="{{ '/publications/#FaroMPSV26' | relative_url }}">HPDC 2026 — Swap Matching</a>
    </p>
  </section>
</div>

## Collaboration

My research has been developed through collaborations with researchers in Italy, France, Japan and Brazil. I have carried out visiting research periods at the University of Yamanashi and at UNICAMP.
