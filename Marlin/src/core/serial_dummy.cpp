#if ENABLE_DUMMY_SERIAL

#include "serial_dummy.h"

#include "serial_hook.h"

Serial1Class<DummySerial> MSerial1Dummy;
#if Serial2Class
  Serial2Class<DummySerial> MSerial2Dummy;
#endif
#if Serial3Class
  Serial3Class<DummySerial> MSerial3Dummy;
#endif

#endif
