var randist = require('../index.js').randist;
var assert = require('assert');

function shouldPass(fn, args, expectedResult) {
  it('should pass', function() {
    if (!(args instanceof Array)) args = [args];
    assert.equal(fn.apply(null, args), expectedResult);
  });
}

describe('randist', function() {
  beforeEach(function() {
    randist.reseedRNG(0);
  });

  describe('gaussian', function() {
    shouldPass(randist.ranGaussian, 10, 1.3391860811867589);
    shouldPass(randist.ranGaussianPDF, [0, 1], 0.3989422804014327);
  });

  describe('poisson', function() {
    shouldPass(randist.ranPoisson, 10, 15);
    shouldPass(randist.ranPoissonPDF, [0, 1], 0.36787944117144233);
  });

  describe('gamma', function() {
    shouldPass(randist.ranGammaKnuth, [1, 1], 0.00025828444588394794);
    shouldPass(randist.ranGamma, [1, 1], 1.506491531884399);
    shouldPass(randist.ranGammaPDF, [3, 1, 1], 0.049787068367863944);
  });

});
