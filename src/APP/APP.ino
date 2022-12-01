#include <Arduino.h>
#include "lib_otto.h"

Otto Otto;

#define PIE_DER D4
#define PIE_IZQ D3
#define PIERNA_DER D2
#define PIERNA_IZQ D1

void setup()
{
  Otto.init(PIERNA_IZQ, PIERNA_DER, PIE_DER, PIE_IZQ);
  Otto.home();
}

void loop()
{
  Otto.shakeLeg(1,1000,RIGHT);
}
