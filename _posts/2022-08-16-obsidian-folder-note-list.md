---
layout: post
title: Automatic notes list for each folder in Obsidian
date: 2022-08-16 13:06 +1000
---

If you prefer Notion's style of file navigation - all files are navigated through linkes, you will need two community plugins: 
1. [Folder Note](https://github.com/xpgo/obsidian-folder-note-plugin) 
2. [dataview](https://github.com/blacksmithgu/obsidian-dataview)

In Folder Note options, choose
- Note File Method: Folder Name Inside

In Initial Content, paste: 

<pre><code>
```dataview 
<span class="hljs-selector-tag">table</span> file<span class="hljs-selector-class">.ctime</span> AS <span class="hljs-string">"Created"</span> where endswith(file<span class="hljs-selector-class">.folder</span>, this<span class="hljs-selector-class">.file</span><span class="hljs-selector-class">.folder</span>) or (contains(file<span class="hljs-selector-class">.folder</span>, this<span class="hljs-selector-class">.file</span><span class="hljs-selector-class">.folder</span>) and contains(file<span class="hljs-selector-class">.folder</span>, file.name)) and file<span class="hljs-selector-class">.name</span> != this<span class="hljs-selector-class">.file</span><span class="hljs-selector-class">.name</span>
```
</code></pre>


Also check Hide Folder Note (recommended).

Then press cmd/ctrl + click on the folder to create the folder note with the list of notes in this folder. 

If there are subfolders, you also need to press cmd/ctrl + click on the subfolders to create the folder notes for them. Otherwise they will not appear in your parent's folder note's list.  

