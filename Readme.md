# node-gsl

Node.js bindings for the [GNU Scientific
Library](http://www.gnu.org/software/gsl/). This is still a WIP and only has one
"hello GSL" binding for the `gsl_ran_poisson` function [GSL
docs](http://www.gnu.org/software/gsl/manual/html_node/The-Poisson-Distribution.html#The-Poisson-Distribution):

```javascript

var gsl = require('./index.js');

console.log(gsl.randist.ranPoisson(5));
```

More to come soon!
