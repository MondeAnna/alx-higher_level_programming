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
    * How to run a JavaScript script
    * How to create variables and constants
    * What are differences between `var`, `const` and `let`
    * What are all the data types available in JavaScript
    * How to use the `if`, `if ... else` statements
    * How to use comments
    * How to affect values to variables
    * How to use `while` and `for` loops
    * How to use `break` and `continue` statements
    * What is a function and how do you use functions
    * What does a function that does not use any `return` statement return
    * Scope of variables
    * What are the arithmetic operators and how to use them
    * How to manipulate dictionary
    * How to import a file

<br />

#### Resources

* _[Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)_
* _[Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)_
* _[Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)_
* _[Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)_
* _[Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)_
* _[Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)_
* _[Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)_
* _[Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)_
* _[Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)_
* _[Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/)_
* _[var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)_
* _[JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)_
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
