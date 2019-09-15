---
layout: default
title: Library
books:
  feedbooks:
    - title: H. P. Lovecraft The Call of Cthulhu
      image: img/books/HPLovecraft_CallOfCthulhu.jpg
      url: http://www.feedbooks.com/book/18/the-call-of-cthulhu
    - title: Lawrence Lessig Free Culture
      image: img/books/LawrenceLessig_FreeCulture.png
      url: http://www.feedbooks.com/book/2750/free-culture
    - title: F. Scott Fitzgerald The Great Gatsby
      image: img/books/FScottFitzgerald_GreatGatsby.jpg
      url: http://www.feedbooks.com/book/5543/the-great-gatsby
    - title: The Lost World
      image: img/books/ArthurConanDoyle_LostWorld.jpg
      url: http://www.feedbooks.com/book/67/the-lost-world
  goalkicker:
    - title: Algorithms
      image: img/books/AlgorithmsGrow.png
      url: https://goalkicker.com/AlgorithmsBook/
    - title: C Plus Plus
      image: img/books/CPlusPlusGrow.png
      url: https://goalkicker.com/CPlusPlusBook/
    - title: JavaScript
      image: img/books/JavaScriptGrow.png
      url: https://goalkicker.com/JavaScriptBook/
    - title: Python
      image: img/books/PythonGrow.png
      url: https://goalkicker.com/PythonBook/
  gutenberg:
    - title: H. Beam Piper The Cosmic Computer
      image: img/books/HBeamPiper_CosmicComputer.jpg
      url: https://www.gutenberg.org/ebooks/20727
    - title: H. G. Wells The Time Machine
      image: img/books/HGWells_TimeMachine.jpg
      url: https://www.gutenberg.org/ebooks/35
    - title: H. G. Wells The War of the Worlds
      image: img/books/HGWells_WarOfTheWorlds.jpg
      url: https://www.gutenberg.org/ebooks/36
    - title: Homer The Iliad
      image: img/books/Homer_Iliad.jpg
      url: https://www.gutenberg.org/ebooks/6130
    - title: Jules Verne 20,000 Leagues Under the Sea
      image: img/books/JulesVerne_20000Leagues.jpg
      url: https://www.gutenberg.org/ebooks/2488
    - title: Jules Verne The Mysterious Island
      image: img/books/JulesVerne_MysteriousIsland.jpg
      url: https://www.gutenberg.org/ebooks/8993
    - title: Mary Shelley Frankenstein
      image: img/books/MaryShelley_Frankenstein.jpg
      url: https://www.gutenberg.org/ebooks/42324
    - title: Plato Symposium
      image: img/books/Plato_Symposium.jpg
      url: https://www.gutenberg.org/ebooks/1600

---

# G&G Library

Geeks and Gadgets lends its support to others in compiling a comprehensive,
free, and open library for ebooks on programming, technology, and beyond.


## The Free Ebook Foundation

> The Free Ebook Foundation envisions a world where ebooks will be funded,
> distributed and maintained for the benefit of all, by coordinating the efforts
> and resources of many.

The Foundation hosts a crowd-sourced list of free programming related learning
resources on their GitHub page. As of September 2019, this list contained over
1500 links to free resources covering an astonishing range of topics.

These topics include:

* Dozens of programming languages
* Text editors like Vim and Emacs
* Language agnostic topics like Regular Expressions, algorithms, and machine
  learning
* Software security and reverse engineering
* Text formatting languages like LaTeX and Markdown
* Other curated lists
* And so much more!

[Check it out on GitHub!](https://github.com/EbookFoundation/free-programming-books/blob/master/free-programming-books.md)

<div class="d-flex flex-wrap mb-4">
<span class="mr-1 mr-md-3 mb-1">{% include gh-pill.html left='<i class="fas fa-eye"></i>' right='8,291' %}</span>
<span class="mr-1 mr-md-3 mb-1">{% include gh-pill.html left='<i class="fas fa-star"></i>' right='128,509' %}</span>
<span class="mr-1 mr-md-3 mb-1">{% include gh-pill.html left='<i class="fas fa-code-branch"></i>' right='32,046' %}</span>
</div>


## Goalkicker

Found at [books.goalkicker.com](https://books.goalkicker.com/), this project has
archived the data from Stack Overflow's now defunct Documentation project. It
has PDF books on roughly 50 topics, averaging several hundred pages each.

Here are a few of the highlights from their catalog:

<div class="row mb-4">
  {% for book in page.books.goalkicker %}
    <a class="col-6 col-sm-6 col-md-3 mx-auto" href="{{ book.url }}" target="_blank">
      <img src="{{ book.image | relative_url }}" alt="{{ book.title }}"
        class="shadow rounded img-fluid mb-3">
    </a>
  {% endfor %}
</div>


## Project Gutenberg

Looking for some lighter reading? Project Gutenberg
[(gutenberg.org)](https://www.gutenberg.org/) offers books on hundreds of
non-tech topics, including children's books, classics, science, philosophy,
history, music, and more!

> Project Gutenberg is a library of over 60,000 free eBooks. Choose among free
> epub and Kindle eBooks, download them or read them online. You will find the
> world's great literature here, with focus on older works for which U.S.
> copyright has expired. Thousands of volunteers digitized and diligently
> proofread the eBooks, for enjoyment and education.

Here are a few of the highlights from their catalog:

<div class="row mb-4">
  {% for book in page.books.gutenberg %}
    <a class="col-6 col-sm-6 col-md-3 mx-auto" href="{{ book.url }}" target="_blank">
      <img src="{{ book.image | relative_url }}" alt="{{ book.title }}"
        class="shadow rounded img-fluid mb-3">
    </a>
  {% endfor %}
</div>


## Feedbooks

Although it's not a completely free and open platform, the French company
Feedbooks offers a wide selection of high quality free and public domain ebooks.
They were an early adopter of EPUB, and work others such as the Internet Archive
to develop the Open Publication Distribution System (OPDS) protocol implemented
by dozens of (some quite popular) software products like the open-source ebook
giant [Calibre](https://en.wikipedia.org/wiki/Calibre_(software)).

From their about page:

> We were the first service to support the [EPUB format](http://www.idpf.org/),
> now widely considered to be the standard for e-book formats.
>
> Through Stanza we were also the first service to distribute e-books on the iOS
> platform.
>
> Our continued efforts in the development of the [OPDS
> Protocol](http://opds-spec.org/), also means that we participate in the
> creation of an Open Web for Books, where a wide diversity of sources and
> devices can connect together.

Here are a few of the highlights from their catalog:

<div class="row mb-4">
  {% for book in page.books.feedbooks %}
    <a class="col-6 col-sm-6 col-md-3 mx-auto" href="{{ book.url }}" target="_blank">
      <img src="{{ book.image | relative_url }}" alt="{{ book.title }}"
        class="shadow rounded img-fluid mb-3">
    </a>
  {% endfor %}
</div>