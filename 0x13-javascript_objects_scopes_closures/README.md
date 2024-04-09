### [ALX](https://www.alxafrica.com/) System Engineering Plus

Studies carried out in the **[ALX Software Engineering Plus](https://www.alxafrica.com/software-engineering-plus/)** course

<br />

#### Technologies

* Bash:     5.1-6ubuntu1
* Docker:   24.0.5
* Node:     14.21.3
* Ubuntu:   20.04 LTS

<br />

#### Learning Objectives

* At the end of this project, you are expected to be able to `explain to anyone`, **without the help of Google**:
    * Why JavaScript programming is amazing
    * How to create an object in JavaScript
    * What `this` means
    * What `undefined` means
    * Why the variable type and scope is important
    * What is a closure
    * What is a prototype
    * How to inherit an object from another

<br />

#### Resources

* _[JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)_
* _[Object-oriented JavaScript (read all examples!)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)_
* _[Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)_
* _[super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)_
* _[extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)_
* _[Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)_
* _[Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)_
* _[Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)_
* _[this/self](https://alistapart.com/article/getoutbindingsituations/)_
* _[Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)_

<br />

#### Requirements

* Allowed editors:
    * _[vi](https://www.geeksforgeeks.org/vi-editor-unix/)_
    * _[vim](https://www.geeksforgeeks.org/getting-started-with-vim-editor-in-linux/)_
    * _[emacs](https://www.geeksforgeeks.org/emacs-command-in-linux-with-examples/)_

* All source code:
    * Will be compiled on `Ubuntu 20.04 LTS` using `node` version `14.x.x`, with the options
    * The first line of all your files should be exactly #!/usr/bin/node
    * The second line to be a comment describing the task
    * Not to make use of `var`
    * To be semistandard compliant (version 16.x.x). Rules of [Standard](https://standardjs.com/rules.html) + [semicolons](https://github.com/standard/semistandard) on top
    * To end with a new line
    * All your files must be executable
    * The length of your files will be tested using `wc`

* A `README.md` file at the root of:
    * The repo, containing a description of the repository
    * The folder of each project, containing a description of the project

<br />

#### Install Node 14

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
source ~/.bashrc
nvm install 14
n=$(which node)
n=${n%/bin/node}
chmod -R 755 $n/bin/* 
sudo cp -r $n/{bin,lib,share} /usr/local
```

<br />

#### Install semi-standard

```
sudo npm install semistandard --global
```

<br />

#### Executable Scripts

* _[`Empty Class`](0-rectangle.js)_
* _[`Init Class Properties`](1-rectangle.js)_
* _[`Init using Natural Numbers`](2-rectangle.js)_
* _[`Add Print Feature`](3-rectangle.js)_
* _[`Augment Class Properties`](4-rectangle.js)_
* _[`Inheritance`](5-square.js)_
* _[`Inheritance II`](6-square.js)_

<br />
