---
layout: post
title: Use Obsidian to manage your research
date: 2022-04-08 15:41 +1000
---

Obsidian can be used as a simple database for resaerch articles, notes and references. Here is my configuration: 

Plugins needed: 
- [Templater](https://github.com/SilentVoid13/Templater)
- [dataview](https://github.com/blacksmithgu/obsidian-dataview)

Database Table
---

Firstly create a folder `/Journal Articles` to stoer all notes for reasearch articles, with one note per article. Then create a note outside the article, with the following dataview code: 

<pre>
<code>
```dataview
table tags as Tags, year as Year from "Journal Articles/" sort file.name asc
```
</code>
</pre>

Note Template
---

Use the following template file with Templater. This template will read BibTex from your clipboard and automatically fill in frontmatter and title. Note that `:` cannot be in the title so it is replaced by `-`. 

<pre><code>---
creation <span class="hljs-keyword">date</span>: &lt;% tp.<span class="hljs-keyword">file</span>.creation_date(<span class="hljs-string">"YYYY-MM-DD"</span>) %&gt; 
modification <span class="hljs-keyword">date</span>: &lt;% tp.<span class="hljs-keyword">file</span>.last_modified_date(<span class="hljs-string">"YYYY-MM-DD"</span>) %&gt;
tags: [] 
year: &lt;% await tp.<span class="hljs-keyword">system</span>.clipboard().then(<span class="hljs-keyword">text</span> =&gt; { <span class="hljs-keyword">return</span> <span class="hljs-keyword">text</span>.<span class="hljs-keyword">match</span>(/(?&lt;=year=\{)(.*)(?=\})/g) }) %&gt; 
title: &lt;% await tp.<span class="hljs-keyword">system</span>.clipboard().then(<span class="hljs-keyword">text</span> =&gt; { <span class="hljs-keyword">return</span> <span class="hljs-keyword">text</span>.<span class="hljs-keyword">match</span>(/(?&lt;=title=\{)(.*)(?=\})/g)[<span class="hljs-number">0</span>].replace(<span class="hljs-string">":"</span>, <span class="hljs-string">" -"</span>) }) %&gt; 
author: [&lt;% await tp.<span class="hljs-keyword">system</span>.clipboard().then(<span class="hljs-keyword">text</span> =&gt; { <span class="hljs-keyword">return</span> <span class="hljs-keyword">text</span>.<span class="hljs-keyword">match</span>(/(?&lt;=author=\{)(.*)(?=\})/g) }) %&gt;] 
---

# BibTex

```
&lt;% tp.system.clipboard() %&gt;
```

# Notes



# Attachment


&lt;% 
tp.<span class="hljs-keyword">file</span>.<span class="hljs-keyword">rename</span>(await tp.<span class="hljs-keyword">system</span>.clipboard().then(<span class="hljs-keyword">text</span> =&gt; {
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">text</span>.<span class="hljs-keyword">match</span>(/(?&lt;=title=\{)(.*)(?=\})/g)[<span class="hljs-number">0</span>].replace(<span class="hljs-string">":"</span>, <span class="hljs-string">" -"</span>);
}))
%&gt;
</code></pre>

Workflow
---

1. Find a journal article or paper
2. Copy the BibTex
3. Create a note from the template.
4. Drag or paste the attachment into the new note. 

Example
---

BibTex copied: 

```
@article{kalgutkar2019code,
  title={Code authorship attribution: Methods and challenges},
  author={Kalgutkar, Vaibhavi and Kaur, Ratinder and Gonzalez, Hugo and Stakhanova, Natalia and Matyukhina, Alina},
  journal={ACM Computing Surveys (CSUR)},
  volume={52},
  number={1},
  pages={1--36},
  year={2019},
  publisher={ACM New York, NY, USA}
}
```

The note: 

<pre>
<code>
---
creation date: 2022-04-08 
modification date: 2022-04-08
tags: [] 
year: 2019 
title: Code authorship attribution - Methods and challenges 
author: [Kalgutkar, Vaibhavi and Kaur, Ratinder and Gonzalez, Hugo and Stakhanova, Natalia and Matyukhina, Alina] 
---

# BibTex
```
@article{kalgutkar2019code,
  title={Code authorship attribution: Methods and challenges},
  author={Kalgutkar, Vaibhavi and Kaur, Ratinder and Gonzalez, Hugo and Stakhanova, Natalia and Matyukhina, Alina},
  journal={ACM Computing Surveys (CSUR)},
  volume={52},
  number={1},
  pages={1--36},
  year={2019},
  publisher={ACM New York, NY, USA}
}
```

# Notes



# Attachment
</code>
</pre>

Dataview table: 

<pre><code>
```
table tags as Tags, year as Year, author as Author from "Journal Articles" sort file.name asc
```
</code></pre>

![](/img/2022-04-08.png)