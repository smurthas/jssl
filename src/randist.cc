
#include <node.h>
#include <v8.h>
#include <stdio.h>
#include <gsl/gsl_combination.h>
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

Handle<Value> RanPoisson(const Arguments& args) {
  HandleScope scope;
  double mu = (double)args[0]->NumberValue();

  unsigned int k = gsl_ran_poisson(randist_rng, mu);

  return scope.Close(Number::New(k));
}

void init(Handle<Object> target) {
  gsl_rng_env_setup();
  randist_rng = gsl_rng_alloc (gsl_rng_default);

  NODE_SET_METHOD(target, "reseedRNG", ReseedRNG);
  NODE_SET_METHOD(target, "ranPoisson", RanPoisson);
}
NODE_MODULE(randist, init)
