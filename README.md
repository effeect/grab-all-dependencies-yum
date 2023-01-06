# grab-all-dependencies-yum
A problem that I've often come across with setting up CentOS VMs at home is that I don't like having any internet connectivity setup for everything.

I wanted an offline download of some of my favourite programs and tools, and what I found is unlike Windows which is mostly prepackaged so most of the time you can grab the install binaries and it "should" work. CentOS and linux in general is quite fiddly especially when it comes to programs with lots of install dependencies. And what makes matters worst, downloading deps on a machine that already has the deps may bring out some odd results.

What I found is that funnily enough, using Docker and yumdownloader in combination allowed me to grab all the deps retaviely quickly without having to resort to creating a new VM entirely. What this repo is basically a quick way to get those packages through a Python package.