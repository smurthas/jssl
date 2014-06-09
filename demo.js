var gsl = require('./index.js');

gsl.randist.reseedRNG(Math.random()*10000000000000000);

console.error('gsl.randist.ranPoisson(25)', gsl.randist.ranPoisson(25));
console.error('gsl.randist.ranPoisson(25)', gsl.randist.ranPoisson(25));
console.error('gsl.randist.ranPoisson(25)', gsl.randist.ranPoisson(25));
console.error('gsl.randist.ranPoisson(25)', gsl.randist.ranPoisson(25));
console.error('gsl.randist.ranPoisson(25)', gsl.randist.ranPoisson(25));
