# MU Geeks & Gadgets Site

This README establishes rules & conventions to be used throughout the
website development.  These will make collaboration easier and keep
things organized.  If you have any questions or comments, please email
Brandon Duke at: 'duke23@marshall.edu'


## Site Organization

Each page gets its own folder, and its resources are held in the contents folder. 
The home page is an exception: it will always be in the root directory of the site.

Example: The "About" page gets its own folder. All of its contents, if any, are held in its 
own folder, or shared folder, in the contents folder.

A page to supplement an officer's description would not need its own
directory.  It would use the same resources as the "About" page, and
thus it would be in the same folder as the "About" page.


## Page Formating

All page formating will be done through CSS.  The general, site-wide
stylesheet is located at ROOT/css/wideScreen.css or ROOT/css/mobile.css. This is so that the CSS can be changed depending on the screen size.  All pages will be
styled the same with the exception of a key element that seperates that
page from the rest of the site.  **All** Images, and any other contents should be placed in the `ROOT/contents/` directory.

All css should be in the css file unless there is a good reason not to.


## Web Apps

There is no protocol for apps at the moment.  This will change in the
future when we can support them.

## Closing

This is a living document and will evolve with the site over time.
Please be sure to follow the directions entailed so that the site is
well organized and easy to develop for people who have never seen the
code before.  Commenting is heavily encouraged.
