<h1>JavaScript - Web scraping</h1>
<h2>Learning Objectives</h2>
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

<ul><h3>General</h3>
<li>Why JavaScript programming is amazing</li>
<li>How to manipulate JSON data</li>
<li>How to use request and fetch API</li>
<li>How to read and write a file using fs module</li>
<li>Copyright - Plagiarism</li>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.</li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly #!/usr/bin/node</li>
<li>A README.md file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using wc</li>
<li>You are not allowed to use var</li>
<h2>More Info</h2>
#Install Node 14
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

#Install semi-standard
$ sudo npm install semistandard --global

#Install request module and use it
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

#Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).
