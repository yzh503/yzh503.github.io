---
layout: post
title: Obsidian Tricks 
date: 2022-04-07 15:41 +1000
---

I have recently transferred my notes from Notion to Obsidian for various reasons: 

1. Obsidian supports local files, which can be synchronised in many ways. 
2. Full data ownership leads to better privacy. 
3. Notion is slow on very lage pages, easically with a lot of $$\LaTeX$$ equations.
4. Most of the Notion functionalities are supported in Obsidian with plugins.

How do you use Obsidian to manage research articles and references? 
---
Refer to my next post: [Use Obsidian to manage your research](/2022/04/08/use-obsidian-to-manage-your-research.html)

Can I see a list of notes as links for each folder?
---

Refer to my next post: [Automatic notes list for each folder](/2022/08/16/obsidian-folder-note-list.html)

Notion has database. What does Obsidian have? 
---

Use markdown tables with [Advanced Tables](https://github.com/tgrosinger/advanced-tables-obsidian) plugin, or use [dataview](https://github.com/blacksmithgu/obsidian-dataview) plugin to query the notes in any folder. For example, I query all my journal article notes as a table in the Folder Note page: 

![](/img/Pasted%20image%2020220407201415.png)

With code: 

<pre>
<code>
```dataview
table tags as Tags, year as Year from "Journal Articles/" sort file.name asc
```
</code>
</pre>

To filter or sort, just add `where` and `sort` clause in the query. See more examples in [Use Obsidian to manage your research](/2022/04/08/use-obsidian-to-manage-your-research.html).

How do you install plugins?
---
Browse core and community plugins in settings, or visit their github repositories. 

Is there a easier way to use Latex?
---

Create your own shortcut. For example, replace `\boldsymbol` with `\b`


<pre><code>
```
$$\newcommand{\b}[1]{\boldsymbol{#1}}$$
```
</code></pre>


Put this into any page and visit it once when launching Obsidian, the command will work in all notes until Obsidian is closed. 

Use [Quick Latex](https://github.com/joeyuping/quick_latex_obsidian) plugin for autocomplete. 



Can I modify the theme/fonts/colours?
---

Open the css snippets folder from settings - appearance, create a css to set variables or override the theme. For example, I want a minimum width for tables so that short words are not wrapped: 

```
th {
  white-space: nowrap !important; 
}
td {
  min-width: 5em !important;
}
```

How do you link to blocks?
---

- type `[[` and the note title, followed by a `#` to select the heading. 
- Put tags around locations that you want to link, so you can click the tag and get a list of locations in the search panel. 
- Use [Copy Block Link](https://github.com/mgmeyers/obsidian-copy-block-link).

How do you insert a web link as a bookmark like in Notion?
---

Install [Rich Link](https://github.com/dhamaniasad/obsidian-rich-links) plugin. Select a link you want to convert to a book mark, then `cmd/ctrl + P` will open the command palette, and type `rich link`. 

Install [Paste URL to Selection](https://github.com/denolehov/obsidian-url-into-selection) so you can select a word and paste url to make a named link. 


Can I create a dynamic/interactive note? 
---

Checkout the plugins like [Templater](https://github.com/SilentVoid13/Templater) [Custom JS](https://github.com/samlewis0602/obsidian-custom-js)  [Buttons](https://github.com/shabegom/buttons) and [React Components](https://github.com/elias-sundqvist/obsidian-react-components).  For example, I use Templater with JavaScript so I can create a Journal Article note with automatic yaml attributes extracted from BibTex. These attributes can be used in query. 

Why does my light theme look so grey and unclear?
---

You might have turned on translucent window. Turn it off in settings - appearance. 

How are files and attachments managed?
---

If you copy or drag images/files into the eidtor, it will place the file into a default folder for attachment, which is configurable in the settings. Do not use Wikilinks in case you want to migrate notes to other software. 

How do you sync across devices?
---

Save the vault in OneDrive/Google Drive/iCloud/Dropbox or use the paid add-on service from Obsidian. 