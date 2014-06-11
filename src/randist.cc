
#include <node.h>
#include <v8.h>
#include <stdio.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>

using namespace v8;

gsl_rng * randist_rng;

Handle<Value> ReseedRNG(const Arguments& args) {
  HandleScope scope;
  unsigned long int seed = (unsigned long int)args[0]->NumberValue();

  gsl_rng_set(randist_rng, seed);

  return scope.Close(Undefined());
}

// gaussian
Handle<Value> ran_gaussian(const Arguments& args) {
  HandleScope scope;
  double sigma = (double)args[0]->NumberValue();

  double x = gsl_ran_gaussian(randist_rng, sigma);

  return scope.Close(Number::New(x));
}

Handle<Value> ran_gaussian_pdf(const Arguments& args) {
  HandleScope scope;
  double x = (double)args[0]->NumberValue();
  double sigma = (double)args[1]->NumberValue();

  double p = gsl_ran_gaussian_pdf(x, sigma);

  return scope.Close(Number::New(p));
}


// poisson
Handle<Value> ran_poisson(const Arguments& args) {
  HandleScope scope;
  double mu = (double)args[0]->NumberValue();

  unsigned int k = gsl_ran_poisson(randist_rng, mu);

  return scope.Close(Number::New(k));
}

Handle<Value> ran_poisson_pdf(const Arguments& args) {
  HandleScope scope;
  unsigned int k = (unsigned int)args[0]->NumberValue();
  double mu = (double)args[1]->NumberValue();

  double p = gsl_ran_poisson_pdf(k, mu);

  return scope.Close(Number::New(p));
}


// gamma
Handle<Value> ran_gamma(const Arguments& args) {
  HandleScope scope;
  double a = (double)args[0]->NumberValue();
  double b = (double)args[1]->NumberValue();

  double k = gsl_ran_gamma(randist_rng, a, b);

  return scope.Close(Number::New(k));
}

Handle<Value> ran_gamma_knuth(const Arguments& args) {
  HandleScope scope;
  double a = (double)args[0]->NumberValue();
  double b = (double)args[1]->NumberValue();

  double k = gsl_ran_gamma_knuth(randist_rng, a, b);

  return scope.Close(Number::New(k));
}

Handle<Value> ran_gamma_pdf(const Arguments& args) {
  HandleScope scope;
  double x = (double)args[0]->NumberValue();
  double a = (double)args[1]->NumberValue();
  double b = (double)args[2]->NumberValue();

  double k = gsl_ran_gamma_pdf(x, a, b);

  return scope.Close(Number::New(k));
}


void init(Handle<Object> target) {
  gsl_rng_env_setup();
  randist_rng = gsl_rng_alloc (gsl_rng_default);

  NODE_SET_METHOD(target, "reseedRNG", ReseedRNG);

  NODE_SET_METHOD(target, "ranGaussian", ran_gaussian);
  NODE_SET_METHOD(target, "ranGaussianPDF", ran_gaussian_pdf);

  NODE_SET_METHOD(target, "ranPoisson", ran_poisson);
  NODE_SET_METHOD(target, "ranPoissonPDF", ran_poisson_pdf);

  NODE_SET_METHOD(target, "ranGamma", ran_gamma);
  NODE_SET_METHOD(target, "ranGammaKnuth", ran_gamma_knuth);
  NODE_SET_METHOD(target, "ranGammaPDF", ran_gamma_pdf);
}
NODE_MODULE(randist, init)
