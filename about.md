---
layout: default
title: About Us
---

<style>
	.officer h3 {
		font-size: 20pt;
		margin-bottom: 0.75em;
		font-weight: bold;
		text-align: center;
		color: #199D72;
	}
</style>

<div markdown="1" class="text-center">

# The Way of the Geek

Geeks and Gadgets has three club values:  
Make it **fun!** Make it **cool!** Make it **open source!**

</div>

We hold these values dear as they are the very core of what the club is about;
having fun while make a cool open source project. We also highly value democracy
and cooperation, two things that are absolutely necessary for any project to
come to a successful end. The geeks are all about being open and transparent,
one of the reasons why we support open source. Don't believe us? Fine, we
encourage the question everything attitude! Here is our [Constitution](
{{ site.baseurl }}{% link static/constitution.pdf %})
so you can check it our for yourself!


## Meet the Geeks:

<div><ul class="list-group list-group-flush">
	{% for officer in site.officers %}
		<li class="list-group-item"><div class="officer row">
			<!-- Image-->
			<div class="col-12 col-md-4 mb-3">
				<img src="{{ officer.image | relative_url }}"
					class="float-left rounded img-fluid" alt="Image of {{ officer.name }}">
			</div>
			<!-- Body -->
			<div class="col-12 col-md-8">
				<h3>{{ officer.position }}: {{ officer.name }}</h3>
				{{ officer.content }}
				{% for contact in officer.contact %}
					<div class="text-center">{{ contact[0] }}: {{ contact[1] }}</div>
				{% endfor %}
			</div>
		</div></li>
	{% endfor %}
</ul></div>