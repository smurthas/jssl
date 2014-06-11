# JSSL: JavaScript Scientific Library
(well, more like Node.js bindings for the [GNU Scientific
Library](http://www.gnu.org/software/gsl/)

This is still a WIP and only has a portion of the GSL Random Number
Distributions bound to JS functions.

```javascript

var jssl = require('./index.js'); // or require('jssl') from npm

console.log(jssl.randist.ranPoisson(mu));
console.log(jssl.randist.ranGaussian(sigma));
console.log(jssl.randist.ranGaussianPDF(x, sigma));
console.log(jssl.randist.ranGamma(a, b));
```

For, now see the bottom of `src/randist.cc` and the [GSL
Docs](http://www.gnu.org/software/gsl/manual/html_node/Random-Number-Distributions.html#Random-Number-Distributions)
for more info.

More to come soon!
