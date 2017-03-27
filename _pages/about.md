---
layout: about
title: About Me!
description: "About me"
permalink: /about.html
---


---
> #### "The world is a book, and those who don't travel read only a page." -St. Augustine

---
<html>
    <head>
        <style>
            .round {
                border-radius: 5%;
                overflow: hidden;
                width: 380px;
                height: 380px;
            }
            .round img {
                display: block;
            min-width: 100%;
            min-height: 100%;
            }
        </style>
    </head>
    <body>
        <div style="float:top;">
            <div class="round">
                <img src="{{ site.url }}/images/me.jpg" />
            </div>
        </div>
    </body>
</html>
<!--
# Akash Suresh
### Traveler. Photographer. Coder. 
### Hey, welcome to my blog. 
 -->
---
### Hi! Welcome to my blog. These are stories about the **journeys** that mattered.The **people** I met on them. And the **places** they led me to.
---
<p style="text-indent: 1em;">

{% if site.twitter %}
    <a href="https://twitter.com/{{ site.twitter }}">
      <i class="fa fa-twitter"></i> Twitter  
    </a>
{% endif %}

{% if site.github %}
    <a href="https://github.com/{{ site.github }}">
      <i class="fa fa-github"></i> GitHub  
    </a>
{% endif %}

{% if site.instagram %}
    <a href="https://www.instagram.com/{{ site.instagram }}">
      <i class="fa fa-instagram"></i> Instagram
    </a>
{% endif %}
</p>